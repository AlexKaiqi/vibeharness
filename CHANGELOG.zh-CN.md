# Changelog

[English](CHANGELOG.md) | 简体中文

这里记录 VibeHarness 的重要变更。

## 0.1.0 - 2026-05-24

首次公开 workflow preview。

### Added

- 可移植 `.vibeharness/` runtime templates，用于 episode creation、scoring、
  decision contracts、intervention logs 和 trajectory audits。
- 面向 Codex、Claude Code、Cursor、OpenHands 的 agent adapters。
- 本地 CLI package，包含 `vh init`、`vh start`、`vh score`、`vh episodes`、
  `vh report`、`vh ablation`、`vh validate` 和 `vh version`。
- `pip install .` 后仍可使用的 packaged `vh init` assets。
- 三个 executable example fixtures，覆盖 `spec_capture`、
  `environment_bootstrap` 和 `tool_affordance`。
- 内置 example evaluation 和 ablation reports。
- VibeHarnessBench seed task manifests、metrics 和 scoring rubric。
- 高优先级项目文档的英文和简体中文版本。
- Apache-2.0 license、NOTICE、citation metadata、contribution docs、issue
  templates 和 GitHub validation workflow。

### Validation

- `make validate` 检查 benchmark manifests、i18n status、本地 Markdown links、
  packaged init assets、fixture tests、bundled episode scores、example reports
  和 ablation recovery。
- 非 editable package smoke test 覆盖 `vh validate`、`vh ablation`、
  `vh episodes`、`vh init` 和 `vh start`。

### Known Limits

- 这个 release 是 workflow preview，不是成熟 empirical benchmark。
- 还没有包含真实世界 intervention dataset。
- 还没有发布 PyPI package。
- 论文草稿中的 empirical numbers 仍然标记为 `TODO`。
