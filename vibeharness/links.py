"""Local Markdown link validation."""

from __future__ import annotations

import re
from pathlib import Path
from typing import List, Tuple
from urllib.parse import unquote


LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SKIP_DIRS = {".git", "dist", ".vibeharness/episodes", "reports"}
SKIP_SUFFIXES = {".aux", ".bbl", ".blg", ".log", ".out", ".pdf", ".xdv"}


def should_skip(root: Path, path: Path) -> bool:
    rel = path.relative_to(root).as_posix()
    if any(rel == skip or rel.startswith(f"{skip}/") for skip in SKIP_DIRS):
        return True
    return path.suffix in SKIP_SUFFIXES


def iter_markdown_files(root: Path) -> List[Path]:
    files: List[Path] = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".mdc"} and not should_skip(root, path):
            files.append(path)
    return sorted(files)


def is_external(target: str) -> bool:
    return (
        "://" in target
        or target.startswith("mailto:")
        or target.startswith("app://")
        or target.startswith("#")
    )


def strip_target(target: str) -> str:
    target = target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    return unquote(target.split("#", 1)[0])


def check_links(root: Path) -> Tuple[List[str], int]:
    errors: List[str] = []
    checked = 0

    for path in iter_markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            for match in LINK_RE.finditer(line):
                raw = match.group(1)
                if is_external(raw):
                    continue
                target = strip_target(raw)
                if not target:
                    continue
                checked += 1
                resolved = (path.parent / target).resolve()
                try:
                    resolved.relative_to(root)
                except ValueError:
                    errors.append(f"{path.relative_to(root)}:{lineno}: link escapes repo: {raw}")
                    continue
                if not resolved.exists():
                    errors.append(f"{path.relative_to(root)}:{lineno}: broken link: {raw}")

    return errors, checked
