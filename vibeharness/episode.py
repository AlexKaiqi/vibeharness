"""Episode creation and scoring."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


BASE_REQUIRED = [
    "manifest.json",
    "request.md",
    "intervention_log.md",
    "decision_contract.md",
    "audit.md",
    "scorecard.json",
]


def run_git(root: Path, args: List[str]) -> Optional[str]:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=root,
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return completed.stdout.strip()


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug[:48] or "episode"


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Missing file: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}")


def create_episode(root: Path, request: str, mode: Optional[str] = None) -> Path:
    vh_dir = root / ".vibeharness"
    templates = vh_dir / "templates"
    episodes = vh_dir / "episodes"
    config = load_json(vh_dir / "config.json")

    selected_mode = mode or config.get("default_mode", "vh_lite")
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    episode_dir = episodes / f"{timestamp}_{slugify(request)}"
    episode_dir.mkdir(parents=True, exist_ok=False)

    checkpoint = run_git(root, ["rev-parse", "--verify", "HEAD"]) or "NO_COMMIT"
    status = run_git(root, ["status", "--short"]) or ""

    manifest = {
        "version": 1,
        "mode": selected_mode,
        "created_at": timestamp,
        "checkpoint": checkpoint,
        "request": request,
        "git_status_at_start": status.splitlines(),
        "harness_version": config.get("version"),
    }

    (episode_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n",
        encoding="utf-8",
    )
    (episode_dir / "request.md").write_text(
        f"# Request\n\n{request}\n\n## Acceptance Criteria\n\n- TBD\n",
        encoding="utf-8",
    )

    for template in ("decision_contract.md", "intervention_log.md", "audit.md", "scorecard.json"):
        src = templates / template
        if src.exists():
            shutil.copyfile(src, episode_dir / template)

    return episode_dir


def score_episode(root: Path, episode: Path) -> Tuple[Dict[str, Any], bool]:
    if not episode.is_absolute():
        episode = root / episode
    if not episode.exists():
        raise SystemExit(f"Episode not found: {episode}")

    config = load_json(root / ".vibeharness" / "config.json")
    scorecard = load_json(episode / "scorecard.json")
    primary_fields = config["primary_score_fields"]

    missing = [name for name in BASE_REQUIRED if not (episode / name).exists()]
    field_values = {field: bool(scorecard.get(field)) for field in primary_fields}
    primary_pass = not missing and all(field_values.values())

    report = {
        "episode": str(episode.relative_to(root)),
        "primary_pass": primary_pass,
        "missing_artifacts": missing,
        "primary_fields": field_values,
        "diagnostics": {
            key: scorecard.get(key)
            for key in sorted(scorecard)
            if key not in primary_fields
        },
    }
    return report, primary_pass


def discover_episode_dirs(root: Path, path: Path) -> List[Path]:
    if not path.is_absolute():
        path = root / path
    if path.is_dir() and (path / "manifest.json").exists():
        return [path]
    if not path.exists():
        raise SystemExit(f"Episode path not found: {path}")
    return sorted(
        item
        for item in path.iterdir()
        if item.is_dir() and ((item / "manifest.json").exists() or (item / "scorecard.json").exists())
    )


def score_episode_set(root: Path, path: Path) -> Tuple[Dict[str, Any], bool]:
    episode_dirs = discover_episode_dirs(root, path)
    reports = []
    passed_count = 0

    for episode_dir in episode_dirs:
        try:
            report, passed = score_episode(root, episode_dir)
        except SystemExit as exc:
            report = {
                "episode": str(episode_dir.relative_to(root)),
                "primary_pass": False,
                "error": str(exc),
            }
            passed = False
        reports.append(report)
        if passed:
            passed_count += 1

    count = len(reports)
    summary = {
        "episodes": count,
        "primary_pass_rate": passed_count / count if count else 0,
        "primary_passed": passed_count,
        "primary_failed": count - passed_count,
    }
    result = {
        "path": str((root / path).relative_to(root) if not path.is_absolute() else path),
        "summary": summary,
        "episodes": reports,
    }
    return result, count > 0 and passed_count == count
