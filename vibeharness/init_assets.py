"""Packaged assets used by ``vh init``."""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple


INIT_PATHS = [
    ".vibeharness/README.md",
    ".vibeharness/config.json",
    ".vibeharness/templates",
    "AGENTS.md",
    "CLAUDE.md",
    ".claude/commands",
    ".claude/settings.example.json",
    ".cursor/rules",
    ".openhands/microagents",
]


def iter_files(root: Path, rel: str) -> List[Path]:
    path = root / rel
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(item for item in path.rglob("*") if item.is_file())
    return []


def expected_asset_files(root: Path) -> List[Path]:
    files = []
    for rel in INIT_PATHS:
        files.extend(iter_files(root, rel))
    return sorted(files)


def check_asset_sync(root: Path) -> Tuple[List[str], int]:
    asset_root = root / "vibeharness" / "assets"
    source_files = expected_asset_files(root)
    expected_rels = {path.relative_to(root) for path in source_files}
    asset_files = sorted(item for item in asset_root.rglob("*") if item.is_file())
    actual_rels = {
        path.relative_to(asset_root)
        for path in asset_files
    }

    errors: List[str] = []
    for rel in sorted(expected_rels - actual_rels):
        errors.append(f"missing packaged init asset: {rel}")
    for rel in sorted(actual_rels - expected_rels):
        errors.append(f"unexpected packaged init asset: {rel}")
    for rel in sorted(expected_rels & actual_rels):
        source = root / rel
        packaged = asset_root / rel
        if source.read_bytes() != packaged.read_bytes():
            errors.append(f"stale packaged init asset: {rel}")
    return errors, len(expected_rels)
