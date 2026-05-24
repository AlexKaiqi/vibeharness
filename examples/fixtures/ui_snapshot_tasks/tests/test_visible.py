#!/usr/bin/env python3
"""Visible render smoke test."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    completed = subprocess.run(
        [
            "python3",
            str(ROOT / "app" / "render.py"),
            "--tasks",
            str(ROOT / "data" / "one_task.json"),
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    assert "<html>" in completed.stdout
    assert "verify UI state" in completed.stdout
    print("visible test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
