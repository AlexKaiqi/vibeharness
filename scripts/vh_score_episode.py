#!/usr/bin/env python3
"""Compatibility wrapper for `vh score`."""

from __future__ import annotations

from vibeharness.cli import main


if __name__ == "__main__":
    raise SystemExit(main(["score", *(__import__("sys").argv[1:])]))
