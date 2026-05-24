#!/usr/bin/env python3
"""Visible smoke test for the todo fixture."""

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
    assert "ship harness recovery" in completed.stdout
    assert "write one-off patch" in completed.stdout
    print("visible test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
