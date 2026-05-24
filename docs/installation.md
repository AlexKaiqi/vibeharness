# Installation

[English](installation.md) | [简体中文](installation.zh-CN.md)

VibeHarness can be used directly from a checkout or installed as an editable
Python package.

## From Checkout

```sh
python3 -m vibeharness.cli validate
python3 -m vibeharness.cli report
```

This is what the Makefile uses, so contributors do not need to install anything
extra.

## Editable Install

```sh
python3 -m pip install -e .
vh validate
vh report
```

If your Python user script directory is not on `PATH`, use
`python3 -m vibeharness.cli ...` from the checkout, or add the directory shown
by `pip` to `PATH`.

## Initialize Another Repository

From this project checkout or an editable install:

```sh
vh init /path/to/target/repo
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
vh score .vibeharness/episodes/<id>
vh validate
vh report
vh i18n
vh links
vh benchmark
```

## Packaging Status

The current package is a local editable-install preview. It is not published to
PyPI yet, and normal wheel/sdist packaging is not the stable distribution path
yet.
