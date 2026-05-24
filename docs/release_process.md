# Release Process

[English](release_process.md) | [简体中文](release_process.zh-CN.md)

This document defines the lightweight release process for VibeHarness.

## Release Types

- `workflow preview`: runnable open-source workflow with examples and validation,
  but no real-world intervention claims.
- `evaluation preview`: includes sanitized real episodes and baseline reports.
- `benchmark release`: includes a stable task set, held-out transfer groups, and
  published scoring rules.

Version `0.1.0` is a workflow preview.

## Pre-Release Checklist

Before tagging a release:

```sh
make sync-assets
make validate
python3 -m pip install .
vh version
vh validate
vh ablation
vh episodes examples/episodes
```

Also check:

- `CHANGELOG.md` and `CHANGELOG.zh-CN.md` are updated;
- `README.md` and `README.zh-CN.md` point to the current commands;
- `docs/open_source_readiness.md` reflects known limits;
- generated reports and build artifacts are not committed unless explicitly
  intended;
- no hidden checks, secrets, customer data, or private paths are present in
  committed episodes.

## Tagging

Use annotated tags:

```sh
git tag -a v0.1.0 -m "VibeHarness v0.1.0"
git push origin main
git push origin v0.1.0
```

Do not tag an evaluation preview until sanitized real episodes and baseline
reports are available.

## Release Notes Positioning

For `0.1.x`, describe VibeHarness as a workflow preview. Avoid claiming
intervention reduction or benchmark superiority until the evaluation plan has
real or realistic episodes.
