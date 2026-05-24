#!/usr/bin/env python3
"""Compatibility wrapper for `python3 -m vibeharness.cli ablation`."""

from __future__ import annotations

import json
from pathlib import Path

from vibeharness.ablation import run_ablation


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    report = run_ablation(root)
    print(json.dumps(report["summary"], indent=2))
    summary = report["summary"]
    return 0 if summary["recovered_gap_rate"] == 1 else 1


if __name__ == "__main__":
    raise SystemExit(main())
