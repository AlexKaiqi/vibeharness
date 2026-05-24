#!/usr/bin/env python3
"""Render a tiny todo list as HTML."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List


def render(tasks: List[Dict[str, Any]]) -> str:
    items = "\n".join(f"<li>{task['title']}</li>" for task in tasks)
    empty_state = "" if tasks else '<p data-testid="empty-state">No tasks yet</p>'
    return f"""<!doctype html>
<html>
  <body>
    <main data-testid="todo-app">
      {empty_state}
      <ul data-testid="todo-list">
        {items}
      </ul>
    </main>
  </body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tasks", type=Path, required=True)
    args = parser.parse_args()
    tasks = json.loads(args.tasks.read_text(encoding="utf-8"))
    print(render(tasks))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
