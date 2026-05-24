"""i18n status validation."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional, Tuple


VALID_STATUSES = {"current", "stale", "missing", "not_required"}


def first_heading(path: Path) -> Optional[str]:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return None


def check_i18n(root: Path) -> Tuple[List[str], List[str], List[str]]:
    data = json.loads((root / ".vibeharness" / "i18n.json").read_text(encoding="utf-8"))
    errors: List[str] = []
    warnings: List[str] = []
    missing: List[str] = []

    for entry in data.get("files", []):
        source = root / entry["source"]
        target = root / entry["target"]
        status = entry.get("status")

        if status not in VALID_STATUSES:
            errors.append(f"{entry['source']}: invalid status {status!r}")
            continue

        if not source.exists():
            errors.append(f"{entry['source']}: source missing")

        if status == "not_required":
            continue

        if not target.exists():
            if status == "missing":
                missing.append(f"{entry['target']}: translation pending")
            else:
                errors.append(f"{entry['target']}: target missing but status is {status!r}")
            continue

        if status == "missing":
            errors.append(f"{entry['target']}: exists but status is missing")

        if status == "current" and not entry.get("reviewed_at"):
            source_mtime = source.stat().st_mtime
            target_mtime = target.stat().st_mtime
            if target_mtime + 1 < source_mtime:
                warnings.append(
                    f"{entry['target']}: target is older than source; confirm translation or set reviewed_at"
                )

        src_heading = first_heading(source)
        dst_heading = first_heading(target)
        if src_heading and dst_heading and not dst_heading:
            errors.append(f"{entry['target']}: missing first-level heading")

    return errors, warnings, missing
