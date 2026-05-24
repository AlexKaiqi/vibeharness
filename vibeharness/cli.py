"""VibeHarness command-line interface."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path
from typing import List, Optional

from .benchmark import validate_manifests
from .episode import create_episode, score_episode
from .examples import run_examples
from .i18n import check_i18n
from .links import check_links
from .paths import find_repo_root, package_root
from .validate import validate_repo


INIT_PATHS = [
    ".vibeharness",
    "AGENTS.md",
    "CLAUDE.md",
    ".claude/commands",
    ".claude/settings.example.json",
    ".cursor/rules",
    ".openhands/microagents",
]


def copy_path(src: Path, dst: Path, force: bool) -> None:
    if dst.exists():
        if not force:
            print(f"skip existing {dst}")
            return
        if dst.is_dir():
            shutil.rmtree(dst)
        else:
            dst.unlink()
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
    print(f"wrote {dst}")


def cmd_init(args: argparse.Namespace) -> int:
    source_root = package_root()
    target = Path(args.path).resolve()
    target.mkdir(parents=True, exist_ok=True)
    for rel in INIT_PATHS:
        src = source_root / rel
        if src.exists():
            copy_path(src, target / rel, args.force)
    return 0


def cmd_start(args: argparse.Namespace) -> int:
    root = find_repo_root()
    episode = create_episode(root, args.request, args.mode)
    print(episode.relative_to(root))
    return 0


def cmd_score(args: argparse.Namespace) -> int:
    root = find_repo_root()
    report, passed = score_episode(root, Path(args.episode))
    print(json.dumps(report, indent=2))
    return 0 if passed else 2


def cmd_validate(args: argparse.Namespace) -> int:
    root = find_repo_root()
    return 0 if validate_repo(root) else 1


def cmd_report(args: argparse.Namespace) -> int:
    root = find_repo_root()
    report = run_examples(root)
    print(json.dumps(report["summary"], indent=2))
    summary = report["summary"]
    return 0 if summary["fixture_pass_rate"] == 1 and summary["episode_primary_pass_rate"] == 1 else 1


def cmd_links(args: argparse.Namespace) -> int:
    root = find_repo_root()
    errors, checked = check_links(root)
    if errors:
        print("Broken local links:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"Checked {checked} local Markdown link(s).")
    return 0


def cmd_i18n(args: argparse.Namespace) -> int:
    root = find_repo_root()
    errors, warnings, missing = check_i18n(root)
    if warnings:
        print("Warnings:")
        print("\n".join(f"- {warning}" for warning in warnings))
    if missing:
        print("Missing translations:")
        print("\n".join(f"- {item}" for item in missing))
    if errors:
        print("Errors:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("i18n manifest is valid.")
    return 0


def cmd_benchmark(args: argparse.Namespace) -> int:
    root = find_repo_root()
    errors, count = validate_manifests(root / args.path)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {count} manifest(s).")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="vh", description="VibeHarness CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init = subparsers.add_parser("init", help="Install VibeHarness files into a repository")
    init.add_argument("path", nargs="?", default=".")
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=cmd_init)

    start = subparsers.add_parser("start", help="Create an episode")
    start.add_argument("--request", required=True)
    start.add_argument("--mode", default=None)
    start.set_defaults(func=cmd_start)

    score = subparsers.add_parser("score", help="Score an episode")
    score.add_argument("episode")
    score.set_defaults(func=cmd_score)

    validate = subparsers.add_parser("validate", help="Run repository validation")
    validate.set_defaults(func=cmd_validate)

    report = subparsers.add_parser("report", help="Run bundled example evaluation")
    report.set_defaults(func=cmd_report)

    links = subparsers.add_parser("links", help="Check local Markdown links")
    links.set_defaults(func=cmd_links)

    i18n = subparsers.add_parser("i18n", help="Check i18n status")
    i18n.set_defaults(func=cmd_i18n)

    benchmark = subparsers.add_parser("benchmark", help="Validate benchmark manifests")
    benchmark.add_argument("path", nargs="?", default="benchmark/tasks")
    benchmark.set_defaults(func=cmd_benchmark)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
