#!/usr/bin/env python3
"""Visible test that passes with an explicit database path."""

from __future__ import annotations

import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    completed = subprocess.run(
        [
            "python3",
            str(ROOT / "app" / "notes.py"),
            "--tag",
            "harness",
            "--db",
            str(ROOT / "data" / "notes.json"),
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    assert "Bootstrap local services" in completed.stdout
    print("visible test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
