#!/usr/bin/env python3
"""Compatibility wrapper for `vh benchmark`."""

from __future__ import annotations

from vibeharness.cli import main


if __name__ == "__main__":
    import sys

    args = sys.argv[1:] or ["benchmark/tasks"]
    raise SystemExit(main(["benchmark", *args]))
