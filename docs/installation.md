# Installation

[English](installation.md) | [简体中文](installation.zh-CN.md)

VibeHarness has two installation paths:

1. Skill-first install for agent workflows, with no Python package required.
2. Optional Python CLI install for episode scaffolding, scoring, and reports.

For runtime-specific setup, see
[Runtime Install Matrix](runtime_install.md).

## Skill Install

From a checkout:

```sh
git clone https://github.com/AlexKaiqi/vibeharness.git
cd vibeharness
./install.sh
```

By default this installs the skill into:

- `${CODEX_HOME:-$HOME/.codex}/skills/vibeharness`
- `${CLAUDE_HOME:-$HOME/.claude}/skills/vibeharness`

Use runtime-specific installs when needed:

```sh
./install.sh --codex-only
./install.sh --claude-only
./install.sh --cursor-only
./install.sh --target /path/to/skills/vibeharness
./install.sh --force
```

After installation, invoke the skill explicitly in your coding agent:

```text
Use $vibeharness to run this task as a checkpointed, replayable episode.
```

Skills-compatible installers can also target the `skills/vibeharness` folder
directly. Use `--target` when a runtime has a different skills directory. The
root `SKILL.md` is kept in sync for tools that expect a top-level skill entry.

Runtime notes:

- Codex: use `./install.sh --codex-only` for the local skill, and `vh init` in
  each project that should carry `AGENTS.md` and `.vibeharness/`.
- Claude Code: use `./install.sh --claude-only` for the local skill, and
  `vh init` for `CLAUDE.md` plus `.claude/commands/`.
- Cursor: prefer `vh init` for `.cursor/rules/vibeharness.mdc`; use
  `--target` or `--cursor-only` only when your local runtime supports a skills
  directory.
- OpenHands: use `vh init` for `.openhands/microagents/vibeharness.md`; there
  is no global skill install path required.

## From Checkout

```sh
python3 -m vibeharness.cli validate
python3 -m vibeharness.cli report
```

This is what the Makefile uses, so contributors do not need to install the CLI
globally.

## Optional CLI Install

```sh
python3 -m pip install .
vh version
vh validate
vh report
```

If your Python user script directory is not on `PATH`, use
`python3 -m vibeharness.cli ...` from the checkout, or add the directory shown
by `pip` to `PATH`.

For active development, use editable mode:

```sh
python3 -m pip install -e .
```

## Initialize Another Repository With Runtime Files

From this project checkout or a local package install:

```sh
vh init /path/to/target/repo
```

If `vh` is not on `PATH`, use the module form from the checkout:

```sh
python3 -m vibeharness.cli init /path/to/target/repo
```

This copies the portable VibeHarness runtime and agent adapter files:

- `.vibeharness/`
- `AGENTS.md`
- `CLAUDE.md`
- `.claude/commands/`
- `.cursor/rules/`
- `.openhands/microagents/`

Use `--force` only when you intentionally want to overwrite existing files:

```sh
vh init /path/to/target/repo --force
```

## Common Commands

```sh
vh start --request "implement the user request"
vh version
vh score .vibeharness/episodes/<id>
vh episodes .vibeharness/episodes
vh validate
vh report
vh ablation
vh i18n
vh links
vh benchmark
```

All commands also work as `python3 -m vibeharness.cli <command>` from a
checkout.

## Maintainer Command

When changing runtime templates or agent adapters, update packaged `vh init`
assets and validate the skill distribution before committing:

```sh
make sync-assets
make validate
```

## Packaging Status

The package can be installed locally from a checkout and includes the runtime
templates used by `vh init`. It is not published to PyPI yet. The skill install
is the preferred public entry point for now.
