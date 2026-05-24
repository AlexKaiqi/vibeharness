"""Run bundled examples and produce reports."""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from .episode import score_episode


def bundled_examples(root: Path) -> List[Dict[str, Any]]:
    return [
        {
            "id": "todo_cli_spec_capture",
            "failure_class": "spec_capture",
            "fixture": root / "examples" / "fixtures" / "todo_cli",
            "episode": root / "examples" / "episodes" / "todo_cli_spec_capture",
            "commands": [
                ["python3", "tests/test_visible.py"],
                ["python3", "tests/test_acceptance.py"],
            ],
        },
        {
            "id": "env_bootstrap_notes",
            "failure_class": "environment_bootstrap",
            "fixture": root / "examples" / "fixtures" / "env_bootstrap_notes",
            "episode": root / "examples" / "episodes" / "env_bootstrap_notes",
            "commands": [
                ["python3", "tests/test_visible.py"],
                ["bash", "harness/bootstrap.sh"],
                ["python3", "tests/test_acceptance.py"],
            ],
        },
        {
            "id": "ui_snapshot_tasks",
            "failure_class": "tool_affordance",
            "fixture": root / "examples" / "fixtures" / "ui_snapshot_tasks",
            "episode": root / "examples" / "episodes" / "ui_snapshot_tasks",
            "commands": [
                ["python3", "tests/test_visible.py"],
                ["python3", "tests/test_acceptance.py"],
            ],
        },
    ]


def run_command(root: Path, command: List[str], cwd: Path) -> Dict[str, Any]:
    completed = subprocess.run(
        command,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout = completed.stdout.strip().replace(str(root), "<repo>")
    stderr = completed.stderr.strip().replace(str(root), "<repo>")
    return {
        "command": " ".join(command),
        "returncode": completed.returncode,
        "stdout": stdout,
        "stderr": stderr,
        "passed": completed.returncode == 0,
    }


def write_markdown(report: Dict[str, Any], path: Path) -> None:
    lines = [
        "# Example Evaluation Report",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        "## Summary",
        "",
        f"- examples: {report['summary']['examples']}",
        f"- fixture_pass_rate: {report['summary']['fixture_pass_rate']:.2f}",
        f"- episode_primary_pass_rate: {report['summary']['episode_primary_pass_rate']:.2f}",
        "",
        "## Results",
        "",
        "| Example | Failure class | Fixture | Episode |",
        "| --- | --- | --- | --- |",
    ]

    for item in report["examples"]:
        fixture_status = "pass" if item["fixture_pass"] else "fail"
        episode_status = "pass" if item["episode_score"].get("primary_pass") else "fail"
        lines.append(
            f"| `{item['id']}` | `{item['failure_class']}` | {fixture_status} | {episode_status} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "This report validates the executable examples bundled with the repository. It does not prove the research claim; that requires real or realistic intervention episodes and baseline comparisons.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def run_examples(root: Path, out_dir: Optional[Path] = None) -> Dict[str, Any]:
    output_dir = out_dir or root / "reports"
    output_dir.mkdir(exist_ok=True)
    results = []

    for example in bundled_examples(root):
        command_results = [
            run_command(root, command, example["fixture"]) for command in example["commands"]
        ]
        episode_report, _ = score_episode(root, example["episode"])
        results.append(
            {
                "id": example["id"],
                "failure_class": example["failure_class"],
                "fixture": str(example["fixture"].relative_to(root)),
                "episode": str(example["episode"].relative_to(root)),
                "commands": command_results,
                "fixture_pass": all(item["passed"] for item in command_results),
                "episode_score": episode_report,
            }
        )

    summary = {
        "examples": len(results),
        "fixture_pass_rate": sum(item["fixture_pass"] for item in results) / len(results),
        "episode_primary_pass_rate": sum(
            bool(item["episode_score"].get("primary_pass")) for item in results
        )
        / len(results),
    }
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": summary,
        "examples": results,
    }

    (output_dir / "example_evaluation.json").write_text(
        json.dumps(report, indent=2) + "\n",
        encoding="utf-8",
    )
    write_markdown(report, output_dir / "example_evaluation.md")
    return report
