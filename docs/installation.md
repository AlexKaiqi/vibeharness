# Installation

[English](installation.md) | [简体中文](installation.zh-CN.md)

VibeHarness can be used directly from a checkout or installed as a local Python
package.

## From Checkout

```sh
python3 -m vibeharness.cli validate
python3 -m vibeharness.cli report
```

This is what the Makefile uses, so contributors do not need to install anything
extra.

## Package Install

```sh
python3 -m pip install .
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

## Initialize Another Repository

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
assets before committing:

```sh
make sync-assets
make validate
```

## Packaging Status

The package can be installed locally from a checkout and includes the runtime
templates used by `vh init`. It is not published to PyPI yet.
