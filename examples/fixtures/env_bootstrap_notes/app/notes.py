#!/usr/bin/env python3
"""Notes CLI fixture that requires harness bootstrap for acceptance testing."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List


def load_notes(path: Path) -> List[Dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def search_by_tag(notes: List[Dict[str, Any]], tag: str) -> List[str]:
    matches = []
    for note in notes:
        tags = note.get("tags", [])
        if tag in tags:
            matches.append(str(note["title"]))
    return matches


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--db", type=Path, default=None)
    args = parser.parse_args()

    db_path = args.db or (Path(os.environ["NOTES_DB"]) if "NOTES_DB" in os.environ else None)
    if db_path is None:
        print("NOTES_DB is not configured", file=sys.stderr)
        return 2

    for title in search_by_tag(load_notes(db_path), args.tag):
        print(title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
