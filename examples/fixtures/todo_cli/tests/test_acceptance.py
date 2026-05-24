#!/usr/bin/env python3
"""Acceptance test created from the user intervention."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    completed = subprocess.run(
        [
            "python3",
            str(ROOT / "app" / "todo.py"),
            "--list",
            str(ROOT / "examples" / "sample_tasks.json"),
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    lines = completed.stdout.strip().splitlines()
    assert lines == [
        "[ ] ship harness recovery",
        "[x] write one-off patch",
    ], completed.stdout
    print("acceptance test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
