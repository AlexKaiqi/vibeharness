#!/usr/bin/env python3
"""Acceptance test that requires bootstrap-provided NOTES_DB."""

from __future__ import annotations

import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    env = os.environ.copy()
    env_file = ROOT / ".env.vibeharness"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            if line.startswith("export NOTES_DB="):
                env["NOTES_DB"] = line.split("=", 1)[1].strip('"')

    completed = subprocess.run(
        ["python3", str(ROOT / "app" / "notes.py"), "--tag", "harness"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        env=env,
    )
    lines = completed.stdout.strip().splitlines()
    assert lines == [
        "Bootstrap local services",
        "Replay from checkpoint",
    ], completed.stdout
    print("acceptance test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
