"""Path helpers for VibeHarness."""

from __future__ import annotations

from pathlib import Path
from typing import Optional


def find_repo_root(start: Optional[Path] = None) -> Path:
    current = (start or Path.cwd()).resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".vibeharness").exists() or (candidate / ".git").exists():
            return candidate
    return current


def package_root() -> Path:
    return Path(__file__).resolve().parents[1]
