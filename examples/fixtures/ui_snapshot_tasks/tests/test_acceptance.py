#!/usr/bin/env python3
"""Acceptance test that uses the harness snapshot verifier."""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def render(tasks_file: Path, output_file: Path) -> None:
    completed = subprocess.run(
        [
            "python3",
            str(ROOT / "app" / "render.py"),
            "--tasks",
            str(tasks_file),
        ],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    )
    output_file.write_text(completed.stdout, encoding="utf-8")


def check_snapshot(html_file: Path, empty_state: str, list_items: int) -> None:
    subprocess.run(
        [
            "python3",
            str(ROOT / "harness" / "snapshot.py"),
            str(html_file),
            "--expect-empty-state",
            empty_state,
            "--expect-list-items",
            str(list_items),
        ],
        check=True,
        text=True,
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        empty_html = tmp_path / "empty.html"
        one_task_html = tmp_path / "one_task.html"

        render(ROOT / "data" / "empty.json", empty_html)
        render(ROOT / "data" / "one_task.json", one_task_html)

        check_snapshot(empty_html, "present", 0)
        check_snapshot(one_task_html, "absent", 1)

    print("acceptance test passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
