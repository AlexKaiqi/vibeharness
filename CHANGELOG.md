# Changelog

[English](CHANGELOG.md) | [简体中文](CHANGELOG.zh-CN.md)

All notable changes to VibeHarness are documented here.

## Unreleased

### Added

- Skill-first distribution via root `SKILL.md`, `skills/vibeharness/`, and
  `install.sh`, so Codex, Claude Code, and custom skill-directory users can
  install the workflow without installing the Python package.

### Validation

- `make validate` now checks skill frontmatter, root and nested skill sync,
  installer executability, and a temporary Codex/Claude skill install smoke
  test.
- `make validate` now runs a Codex adapter smoke test that initializes a
  temporary target repository, verifies `AGENTS.md`, creates an episode, and
  scores it without relying on repository-local helper scripts.
- `make validate` now checks Codex, Claude Code, Cursor, and OpenHands adapter
  surfaces against the same lightweight method contract and verifies their
  `vh init` output.

## 0.1.0 - 2026-05-24

Initial public workflow preview.

### Added

- Portable `.vibeharness/` runtime templates for episode creation, scoring,
  decision contracts, intervention logs, and trajectory audits.
- Agent adapters for Codex, Claude Code, Cursor, and OpenHands.
- Local CLI package with `vh init`, `vh start`, `vh score`, `vh episodes`,
  `vh report`, `vh ablation`, `vh validate`, and `vh version`.
- Packaged `vh init` assets that work after ordinary `pip install .`.
- Three executable example fixtures covering `spec_capture`,
  `environment_bootstrap`, and `tool_affordance`.
- Bundled example evaluation and ablation reports.
- VibeHarnessBench seed task manifests, metrics, and scoring rubric.
- English and Simplified Chinese documentation for the high-priority project
  pages.
- Apache-2.0 license, NOTICE, citation metadata, contribution docs, issue
  templates, and GitHub validation workflow.

### Validation

- `make validate` checks benchmark manifests, i18n status, local Markdown links,
  packaged init assets, fixture tests, bundled episode scores, example reports,
  and ablation recovery.
- Non-editable package smoke testing covers `vh validate`, `vh ablation`,
  `vh episodes`, `vh init`, and `vh start`.

### Known Limits

- This release is a workflow preview, not a polished empirical benchmark.
- No real-world intervention dataset is included yet.
- No PyPI package is published yet.
- Empirical intervention-reduction claims are intentionally not made in this
  release.
