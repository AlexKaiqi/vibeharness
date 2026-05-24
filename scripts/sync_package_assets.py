#!/usr/bin/env python3
"""Synchronize packaged ``vh init`` assets from repository sources."""

from __future__ import annotations

import shutil
from pathlib import Path

from vibeharness.init_assets import INIT_PATHS, check_asset_sync


def copy_path(source: Path, target: Path) -> None:
    if source.is_dir():
        shutil.copytree(source, target)
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    asset_root = root / "vibeharness" / "assets"
    if asset_root.exists():
        shutil.rmtree(asset_root)
    asset_root.mkdir(parents=True, exist_ok=True)

    for rel in INIT_PATHS:
        source = root / rel
        if not source.exists():
            raise SystemExit(f"missing source asset: {rel}")
        copy_path(source, asset_root / rel)

    errors, count = check_asset_sync(root)
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Synchronized {count} packaged init asset file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
