"""Validation for lightweight agent adapter surfaces."""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ADAPTER_FILES: Dict[str, List[str]] = {
    "codex": ["AGENTS.md"],
    "claude": [
        "CLAUDE.md",
        ".claude/commands/vh-start.md",
        ".claude/commands/vh-recovery.md",
        ".claude/commands/vh-audit.md",
    ],
    "cursor": [".cursor/rules/vibeharness.mdc"],
    "openhands": [".openhands/microagents/vibeharness.md"],
}


REQUIRED_PHRASES: Dict[str, List[str]] = {
    "AGENTS.md": [
        "vh start --request",
        "python3 -m vibeharness.cli start",
        "When the User Intervenes",
        "decision_contract.md",
        "vh score <episode>",
    ],
    "CLAUDE.md": [
        "vh start --request",
        "python3 -m vibeharness.cli start",
        "Recovery Trigger",
        "Recovery Protocol",
        "/vh-start",
        "/vh-recovery",
        "/vh-audit",
    ],
    ".claude/commands/vh-start.md": [
        "vh start --request",
        "python3 -m vibeharness.cli start",
    ],
    ".claude/commands/vh-recovery.md": [
        "intervention_log.md",
        "decision_contract.md",
        "Replay the original request",
        "scorecard.json",
    ],
    ".claude/commands/vh-audit.md": [
        "vh score",
        "python3 -m vibeharness.cli score",
        "scorecard.json",
    ],
    ".cursor/rules/vibeharness.mdc": [
        "alwaysApply: true",
        "vh start --request",
        "python3 -m vibeharness.cli start",
        "decision contract",
        "vh score <episode>",
    ],
    ".openhands/microagents/vibeharness.md": [
        "name: vibeharness",
        "type: general",
        "vh start --request",
        "python3 -m vibeharness.cli start",
        "vh score <episode>",
    ],
}


FORBIDDEN_PHRASES = [
    "python3 scripts/",
    "scripts/vh_",
    "vh_start.py",
    "vh_score_episode.py",
]


def _iter_adapter_paths(root: Path) -> Iterable[Path]:
    for files in ADAPTER_FILES.values():
        for rel in files:
            yield root / rel


def _module_env(root: Path) -> dict:
    env = os.environ.copy()
    existing = env.get("PYTHONPATH")
    env["PYTHONPATH"] = str(root) if not existing else f"{root}{os.pathsep}{existing}"
    return env


def _run_init(root: Path, target: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "vibeharness.cli", "init", str(target)],
        cwd=root,
        env=_module_env(root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )


def _check_file(root: Path, rel: str, errors: List[str]) -> int:
    checks = 1
    path = root / rel
    if not path.exists():
        errors.append(f"{rel}: missing")
        return checks

    text = path.read_text(encoding="utf-8")
    for phrase in REQUIRED_PHRASES.get(rel, []):
        checks += 1
        if phrase not in text:
            errors.append(f"{rel}: missing adapter phrase {phrase!r}")
    for phrase in FORBIDDEN_PHRASES:
        checks += 1
        if phrase in text:
            errors.append(f"{rel}: should not require repository-local helper {phrase!r}")
    return checks


def check_agent_adapters(root: Path) -> Tuple[List[str], int]:
    """Validate all lightweight agent adapters and their init output."""

    errors: List[str] = []
    checks = 0

    for rel in [path.relative_to(root).as_posix() for path in _iter_adapter_paths(root)]:
        checks += _check_file(root, rel, errors)

    with tempfile.TemporaryDirectory(prefix="vh-agent-adapters-") as tmp:
        target = Path(tmp) / "target"
        target.mkdir()
        init = _run_init(root, target)
        checks += 1
        if init.returncode != 0:
            errors.append("agent adapter init smoke failed: " + (init.stderr.strip() or init.stdout.strip()))
            return errors, checks

        for source in _iter_adapter_paths(root):
            rel = source.relative_to(root)
            target_file = target / rel
            checks += 1
            if not target_file.exists():
                errors.append(f"vh init target missing adapter file: {rel.as_posix()}")
                continue
            if source.read_text(encoding="utf-8") != target_file.read_text(encoding="utf-8"):
                errors.append(f"vh init target adapter differs from source: {rel.as_posix()}")
            checks += _check_file(target, rel.as_posix(), errors)

    return errors, checks
