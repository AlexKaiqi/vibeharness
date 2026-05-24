"""Validation suite for VibeHarness repositories."""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import List

from .benchmark import validate_manifests
from .episode import score_episode
from .examples import run_examples
from .i18n import check_i18n
from .links import check_links


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

    print("==> todo fixture visible test", flush=True)
    if not run_fixture(["python3", "tests/test_visible.py"], root / "examples" / "fixtures" / "todo_cli"):
        ok = False

    print("==> todo fixture acceptance test", flush=True)
    if not run_fixture(["python3", "tests/test_acceptance.py"], root / "examples" / "fixtures" / "todo_cli"):
        ok = False

    print("==> example episode score", flush=True)
    report, primary_pass = score_episode(root, root / "examples" / "episodes" / "todo_cli_spec_capture")
    import json

    print(json.dumps(report, indent=2))
    if not primary_pass:
        ok = False

    print("==> example evaluation report", flush=True)
    example_report = run_examples(root)
    print(json.dumps(example_report["summary"], indent=2))
    summary = example_report["summary"]
    if summary["fixture_pass_rate"] != 1 or summary["episode_primary_pass_rate"] != 1:
        ok = False

    if ok:
        print("VibeHarness validation passed.")
    return ok
