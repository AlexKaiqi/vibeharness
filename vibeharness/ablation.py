"""Executable ablation probes for bundled VibeHarness examples."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


def run_command(
    command: List[str],
    cwd: Path,
    sanitize_roots: Iterable[Path],
    env_remove: Optional[List[str]] = None,
) -> Dict[str, Any]:
    env = os.environ.copy()
    for key in env_remove or []:
        env.pop(key, None)

    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    stdout = sanitize_text(completed.stdout.strip(), sanitize_roots)
    stderr = sanitize_text(completed.stderr.strip(), sanitize_roots)
    return {
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "passed": completed.returncode == 0,
    }


def sanitize_text(text: str, roots: Iterable[Path]) -> str:
    replacements = set()
    for root in roots:
        for value in (str(root), str(root.resolve())):
            replacements.add(value)
            if value.startswith("/var/"):
                replacements.add("/private" + value)
            if value.startswith("/private/var/"):
                replacements.add(value.removeprefix("/private"))
    for path in sorted(replacements, key=len, reverse=True):
        text = text.replace(path, "<path>")
    return text


def copy_fixture(root: Path, name: str, parent: Path) -> Path:
    source = root / "examples" / "fixtures" / name
    target = parent / name
    shutil.copytree(source, target)
    return target


def mutate_todo_to_visible_only_solution(fixture: Path) -> None:
    app = fixture / "app" / "todo.py"
    text = app.read_text(encoding="utf-8")
    old = (
        '        marker = "[x]" if task.get("done") else "[ ]"\n'
        '        lines.append(f"{marker} {task[\'title\']}")'
    )
    new = '        lines.append(task["title"])'
    if old not in text:
        raise RuntimeError(f"could not mutate visible-only todo solution in {app}")
    app.write_text(text.replace(old, new), encoding="utf-8")


def command_group(
    commands: List[List[str]],
    cwd: Path,
    sanitize_roots: Iterable[Path],
    env_remove: Optional[List[str]] = None,
) -> Dict[str, Any]:
    results = [
        run_command(command, cwd, sanitize_roots, env_remove=env_remove)
        for command in commands
    ]
    return {
        "commands": results,
        "passed": all(item["passed"] for item in results),
    }


def probe_todo(root: Path, tmp: Path) -> Dict[str, Any]:
    gap_fixture = copy_fixture(root, "todo_cli", tmp / "todo_gap")
    replay_fixture = copy_fixture(root, "todo_cli", tmp / "todo_replay")
    mutate_todo_to_visible_only_solution(gap_fixture)
    sanitize = [root, tmp, Path(tempfile.gettempdir())]
    return {
        "id": "todo_cli_spec_capture",
        "failure_class": "spec_capture",
        "probe": "visible-only task formatting hides missing acceptance criteria",
        "visible_only": run_command(["python3", "tests/test_visible.py"], gap_fixture, sanitize),
        "gap_probe": run_command(["python3", "tests/test_acceptance.py"], gap_fixture, sanitize),
        "replay": command_group(
            [["python3", "tests/test_acceptance.py"]],
            replay_fixture,
            sanitize,
        ),
    }


def probe_env_bootstrap(root: Path, tmp: Path) -> Dict[str, Any]:
    gap_fixture = copy_fixture(root, "env_bootstrap_notes", tmp / "env_gap")
    replay_fixture = copy_fixture(root, "env_bootstrap_notes", tmp / "env_replay")
    for fixture in (gap_fixture, replay_fixture):
        env_file = fixture / ".env.vibeharness"
        if env_file.exists():
            env_file.unlink()
    sanitize = [root, tmp, Path(tempfile.gettempdir())]
    return {
        "id": "env_bootstrap_notes",
        "failure_class": "environment_bootstrap",
        "probe": "acceptance validation fails when NOTES_DB is not bootstrapped",
        "visible_only": run_command(
            ["python3", "tests/test_visible.py"],
            gap_fixture,
            sanitize,
            env_remove=["NOTES_DB"],
        ),
        "gap_probe": run_command(
            ["python3", "tests/test_acceptance.py"],
            gap_fixture,
            sanitize,
            env_remove=["NOTES_DB"],
        ),
        "replay": command_group(
            [
                ["bash", "harness/bootstrap.sh"],
                ["python3", "tests/test_acceptance.py"],
            ],
            replay_fixture,
            sanitize,
            env_remove=["NOTES_DB"],
        ),
    }


def probe_ui_snapshot(root: Path, tmp: Path) -> Dict[str, Any]:
    gap_fixture = copy_fixture(root, "ui_snapshot_tasks", tmp / "ui_gap")
    replay_fixture = copy_fixture(root, "ui_snapshot_tasks", tmp / "ui_replay")
    (gap_fixture / "harness" / "snapshot.py").unlink()
    sanitize = [root, tmp, Path(tempfile.gettempdir())]
    return {
        "id": "ui_snapshot_tasks",
        "failure_class": "tool_affordance",
        "probe": "acceptance validation fails when machine-readable UI snapshot tool is absent",
        "visible_only": run_command(["python3", "tests/test_visible.py"], gap_fixture, sanitize),
        "gap_probe": run_command(["python3", "tests/test_acceptance.py"], gap_fixture, sanitize),
        "replay": command_group(
            [["python3", "tests/test_acceptance.py"]],
            replay_fixture,
            sanitize,
        ),
    }


def summarize(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    count = len(results)
    visible_pass = sum(item["visible_only"]["passed"] for item in results)
    gap_exposed = sum(not item["gap_probe"]["passed"] for item in results)
    replay_pass = sum(item["replay"]["passed"] for item in results)
    recovered = sum(
        item["visible_only"]["passed"]
        and not item["gap_probe"]["passed"]
        and item["replay"]["passed"]
        for item in results
    )
    return {
        "examples": count,
        "visible_only_pass_rate": visible_pass / count,
        "gap_probe_failure_rate": gap_exposed / count,
        "replay_pass_rate": replay_pass / count,
        "recovered_gap_rate": recovered / count,
    }


def status(passed: bool) -> str:
    return "pass" if passed else "fail"


def write_markdown(report: Dict[str, Any], path: Path) -> None:
    summary = report["summary"]
    lines = [
        "# Ablation Evaluation Report",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        "## Summary",
        "",
        f"- examples: {summary['examples']}",
        f"- visible_only_pass_rate: {summary['visible_only_pass_rate']:.2f}",
        f"- gap_probe_failure_rate: {summary['gap_probe_failure_rate']:.2f}",
        f"- replay_pass_rate: {summary['replay_pass_rate']:.2f}",
        f"- recovered_gap_rate: {summary['recovered_gap_rate']:.2f}",
        "",
        "## Results",
        "",
        "| Example | Failure class | Visible-only | Gap probe | Replay | Recovered |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for item in report["examples"]:
        recovered = (
            item["visible_only"]["passed"]
            and not item["gap_probe"]["passed"]
            and item["replay"]["passed"]
        )
        lines.append(
            f"| `{item['id']}` | `{item['failure_class']}` | "
            f"{status(item['visible_only']['passed'])} | "
            f"{'exposed' if not item['gap_probe']['passed'] else 'missed'} | "
            f"{status(item['replay']['passed'])} | "
            f"{status(recovered)} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This report is an executable ablation over bundled examples. It demonstrates that visible-only validation can pass while a harness-gap probe fails, and that the repaired VibeHarness path passes the replay check. It is not a real-world intervention study.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def run_ablation(root: Path, out_dir: Optional[Path] = None) -> Dict[str, Any]:
    output_dir = out_dir or root / "reports"
    output_dir.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp_name:
        tmp = Path(tmp_name)
        results = [
            probe_todo(root, tmp),
            probe_env_bootstrap(root, tmp),
            probe_ui_snapshot(root, tmp),
        ]

    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": summarize(results),
        "examples": results,
    }
    (output_dir / "ablation_evaluation.json").write_text(
        json.dumps(report, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(report, output_dir / "ablation_evaluation.md")
    return report
