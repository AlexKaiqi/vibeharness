"""Validation suite for VibeHarness repositories."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import List

from .ablation import run_ablation
from .benchmark import validate_manifests
from .codex_adapter import check_codex_adapter
from .episode import score_episode_set
from .examples import run_examples
from .i18n import check_i18n
from .init_assets import check_asset_sync
from .links import check_links
from .skill_distribution import check_skill_distribution


def run_fixture(command: List[str], cwd: Path) -> bool:
    completed = subprocess.run(command, cwd=cwd)
    return completed.returncode == 0


def validate_repo(root: Path) -> bool:
    ok = True

    print("==> benchmark manifests", flush=True)
    errors, count = validate_manifests(root / "benchmark" / "tasks")
    if errors:
        print("\n".join(errors))
        ok = False
    else:
        print(f"Validated {count} manifest(s).")

    print("==> i18n manifest", flush=True)
    i18n_errors, warnings, missing = check_i18n(root)
    if warnings:
        print("Warnings:")
        print("\n".join(f"- {warning}" for warning in warnings))
    if missing:
        print("Missing translations:")
        print("\n".join(f"- {item}" for item in missing))
    if i18n_errors:
        print("Errors:")
        print("\n".join(f"- {error}" for error in i18n_errors))
        ok = False
    else:
        print("i18n manifest is valid.")

    print("==> local Markdown links", flush=True)
    link_errors, checked = check_links(root)
    if link_errors:
        print("Broken local links:")
        print("\n".join(f"- {error}" for error in link_errors))
        ok = False
    else:
        print(f"Checked {checked} local Markdown link(s).")

    print("==> packaged init assets", flush=True)
    asset_errors, asset_count = check_asset_sync(root)
    if asset_errors:
        print("Packaged init asset errors:")
        print("\n".join(f"- {error}" for error in asset_errors))
        ok = False
    else:
        print(f"Packaged {asset_count} init asset file(s) are in sync.")

    print("==> skill distribution", flush=True)
    skill_errors, skill_count = check_skill_distribution(root)
    if skill_errors:
        print("Skill distribution errors:")
        print("\n".join(f"- {error}" for error in skill_errors))
        ok = False
    else:
        print(f"Checked {skill_count} skill distribution invariant(s).")

    print("==> Codex adapter smoke", flush=True)
    codex_errors, codex_count = check_codex_adapter(root)
    if codex_errors:
        print("Codex adapter errors:")
        print("\n".join(f"- {error}" for error in codex_errors))
        ok = False
    else:
        print(f"Checked {codex_count} Codex adapter invariant(s).")

    print("==> todo fixture visible test", flush=True)
    if not run_fixture(["python3", "tests/test_visible.py"], root / "examples" / "fixtures" / "todo_cli"):
        ok = False

    print("==> todo fixture acceptance test", flush=True)
    if not run_fixture(["python3", "tests/test_acceptance.py"], root / "examples" / "fixtures" / "todo_cli"):
        ok = False

    print("==> bundled episode scores", flush=True)
    episode_report, episode_pass = score_episode_set(root, root / "examples" / "episodes")
    print(json.dumps(episode_report["summary"], indent=2))
    if not episode_pass:
        ok = False

    print("==> example evaluation report", flush=True)
    example_report = run_examples(root)
    print(json.dumps(example_report["summary"], indent=2))
    summary = example_report["summary"]
    if summary["fixture_pass_rate"] != 1 or summary["episode_primary_pass_rate"] != 1:
        ok = False

    print("==> ablation evaluation report", flush=True)
    ablation_report = run_ablation(root)
    print(json.dumps(ablation_report["summary"], indent=2))
    ablation_summary = ablation_report["summary"]
    if ablation_summary["recovered_gap_rate"] != 1:
        ok = False

    if ok:
        print("VibeHarness validation passed.")
    return ok
