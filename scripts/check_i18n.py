#!/usr/bin/env python3
"""Compatibility wrapper for `vh i18n`."""

from __future__ import annotations

from vibeharness.cli import main


if __name__ == "__main__":
    raise SystemExit(main(["i18n"]))
