#!/usr/bin/env python3
"""Small todo CLI fixture for VibeHarness examples."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List, Any


def load_tasks(path: Path) -> List[Dict[str, Any]]:
    return json.loads(path.read_text(encoding="utf-8"))


def format_tasks(tasks: List[Dict[str, Any]]) -> str:
    ordered = sorted(tasks, key=lambda task: bool(task.get("done")))
    lines = []
    for task in ordered:
        marker = "[x]" if task.get("done") else "[ ]"
        lines.append(f"{marker} {task['title']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", type=Path, required=True, help="JSON task file")
    args = parser.parse_args()
    print(format_tasks(load_tasks(args.list)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
