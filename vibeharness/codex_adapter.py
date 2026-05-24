"""Codex adapter smoke validation."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import List, Tuple


AGENTS_REQUIRED_PHRASES = [
    "vh start --request",
    "python3 -m vibeharness.cli start",
    "When the User Intervenes",
    "vh score <episode>",
]


def _module_env(root: Path) -> dict:
    env = os.environ.copy()
    existing = env.get("PYTHONPATH")
    env["PYTHONPATH"] = str(root) if not existing else f"{root}{os.pathsep}{existing}"
    return env


def _run_cli(root: Path, cwd: Path, args: List[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "vibeharness.cli", *args],
        cwd=cwd,
        env=_module_env(root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def _set_scorecard_true(target: Path, episode_rel: str) -> None:
    config = json.loads((target / ".vibeharness" / "config.json").read_text(encoding="utf-8"))
    scorecard = json.loads((target / episode_rel / "scorecard.json").read_text(encoding="utf-8"))
    for field in config["primary_score_fields"]:
        scorecard[field] = True
    scorecard["notes"] = "Codex adapter smoke test."
    (target / episode_rel / "scorecard.json").write_text(
        json.dumps(scorecard, indent=2) + "\n",
        encoding="utf-8",
    )


def check_codex_adapter(root: Path) -> Tuple[List[str], int]:
    """Validate the Codex-facing adapter path in a temporary target repo."""

    errors: List[str] = []
    checks = 0

    agents = root / "AGENTS.md"
    checks += 1
    if not agents.exists():
        errors.append("AGENTS.md: missing")
        return errors, checks

    agents_text = agents.read_text(encoding="utf-8")
    for phrase in AGENTS_REQUIRED_PHRASES:
        checks += 1
        if phrase not in agents_text:
            errors.append(f"AGENTS.md: missing Codex adapter phrase {phrase!r}")

    checks += 1
    if "scripts/vh_" in agents_text:
        errors.append("AGENTS.md: should not require repository-local scripts after vh init")

    with tempfile.TemporaryDirectory(prefix="vh-codex-adapter-") as tmp:
        target = Path(tmp) / "target"
        target.mkdir()
        subprocess.run(["git", "init", "-q"], cwd=target, check=False)

        init = _run_cli(root, root, ["init", str(target)])
        checks += 1
        if init.returncode != 0:
            errors.append("Codex adapter smoke init failed: " + (init.stderr.strip() or init.stdout.strip()))
            return errors, checks

        target_agents = target / "AGENTS.md"
        checks += 2
        if not target_agents.exists():
            errors.append("Codex adapter smoke target missing AGENTS.md")
        elif "scripts/vh_" in target_agents.read_text(encoding="utf-8"):
            errors.append("Codex adapter smoke target AGENTS.md still references repository-local scripts")

        start = _run_cli(root, target, ["start", "--request", "codex adapter smoke"])
        checks += 1
        if start.returncode != 0:
            errors.append(
                "Codex adapter smoke episode start failed: "
                + (start.stderr.strip() or start.stdout.strip())
            )
            return errors, checks

        episode_rel = start.stdout.strip().splitlines()[-1]
        episode_dir = target / episode_rel
        checks += 1
        if not (episode_dir / "manifest.json").exists():
            errors.append(f"Codex adapter smoke missing episode manifest: {episode_rel}")
            return errors, checks

        _set_scorecard_true(target, episode_rel)
        score = _run_cli(root, target, ["score", episode_rel])
        checks += 1
        if score.returncode != 0:
            errors.append("Codex adapter smoke score failed: " + (score.stderr.strip() or score.stdout.strip()))

    return errors, checks
