#!/usr/bin/env python3
"""Machine-readable UI snapshot verifier for rendered HTML."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any


class SnapshotParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.testids: Set[str] = set()
        self.list_items = 0

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        attrs_map = dict(attrs)
        testid = attrs_map.get("data-testid")
        if testid:
            self.testids.add(testid)
        if tag == "li":
            self.list_items += 1


def snapshot(html: str) -> Dict[str, Any]:
    parser = SnapshotParser()
    parser.feed(html)
    return {
        "has_empty_state": "empty-state" in parser.testids,
        "list_items": parser.list_items,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("html", type=Path)
    parser.add_argument("--expect-empty-state", choices=["present", "absent"], required=True)
    parser.add_argument("--expect-list-items", type=int, required=True)
    args = parser.parse_args()

    state = snapshot(args.html.read_text(encoding="utf-8"))
    expected_empty = args.expect_empty_state == "present"
    assert state["has_empty_state"] is expected_empty, state
    assert state["list_items"] == args.expect_list_items, state
    print("snapshot check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
