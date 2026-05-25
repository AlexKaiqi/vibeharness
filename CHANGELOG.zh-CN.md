# Changelog

[English](CHANGELOG.md) | 简体中文

这里记录 VibeHarness 的重要变更。

## Unreleased

### Added

- 新增 skill-first 分发：根目录 `SKILL.md`、`skills/vibeharness/` 和
  `install.sh`，让 Codex、Claude Code 和自定义 skills 目录用户无需安装 Python package 也能使用工作流。
- 新增 runtime-specific 安装文档，覆盖 Codex、Claude Code、Cursor、
  OpenHands 和自定义 skill 目录。
- 新增 Codex-specific 安装文档，明确 skill 与 `AGENTS.md` artifacts，并提供验证命令。

### Validation

- `make validate` 现在会检查 skill frontmatter、根目录与嵌套 skill 同步、
  installer 可执行权限，以及临时 Codex/Claude skill 安装 smoke test。
- `make validate` 现在会运行 Codex adapter smoke test：初始化临时目标仓库、
  验证 `AGENTS.md`、创建 episode，并在不依赖 repository-local helper scripts
  的情况下完成 scoring。
- `make validate` 现在会按同一套轻量 method contract 检查 Codex、Claude
  Code、Cursor 和 OpenHands adapter surfaces，并验证它们的 `vh init` output。

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
- 本 release 暂不声称已经证明 intervention reduction。
