# VibeHarness

[English](README.md) | 简体中文

VibeHarness 是一个面向 AI 辅助软件工程的实用 harness 恢复工作流。它针对一个常见的生产问题：coding agent 卡住之后，人类通常会介入并修复眼前问题，但底层 agent harness 没有被改进，最终结果也没有从干净状态重新回放验证。

核心假设：

> 很多看似是 coding agent 能力不足的问题，其实是可恢复的 harness 问题。supervisor agent 可以通过 checkpoint、指挥 worker agent、观察人类或工具介入、修复 harness、回滚并重新执行任务，提升整体可靠性。

本仓库包含：

- `AGENTS.md`、`CLAUDE.md`、`.cursor/rules/`、`.claude/commands/`、`.openhands/microagents/`：面向常见 coding agent 的薄适配层。
- `.vibeharness/`：可移植的运行时配置和 episode 模板。
- `docs/landing_architecture.md` / [中文](docs/landing_architecture.zh-CN.md)：生产落地架构和运行模式。
- `docs/evaluation.md` / [中文](docs/evaluation.zh-CN.md)：可靠性、干预减少、迁移和安全评估方案。
- `docs/i18n.md`：双语文档维护规范。
- `docs/agent_adapters.md` / [中文](docs/agent_adapters.zh-CN.md)：Codex、Claude Code、Cursor、OpenHands 的 adapter notes。
- `docs/prior_art.md` / [中文](docs/prior_art.zh-CN.md)：已有工作、思想 lineage 和致谢。
- `docs/open_source_readiness.md` / [中文](docs/open_source_readiness.zh-CN.md)：公开开源发布 checklist。
- `docs/release_process.md` / [中文](docs/release_process.zh-CN.md)：轻量 release 和 tag 流程。
- `docs/verification.md` / [中文](docs/verification.zh-CN.md)：`make validate` 检查什么、不证明什么。
- `docs/example_results.md` / [中文](docs/example_results.zh-CN.md)：当前内置 examples 的评估结果。
- `docs/episode_collection.md` / [中文](docs/episode_collection.zh-CN.md)：如何收集、脱敏、评分和划分 episodes。
- `docs/licensing.md` / [中文](docs/licensing.zh-CN.md)：license 选择、署名期待和复用边界。
- `docs/installation.md` / [中文](docs/installation.zh-CN.md)：本地 package 使用、editable development install 和 `vh init`。
- `CONTRIBUTING.md`、`SECURITY.md`、`.github/`：社区和贡献文件。
- `CHANGELOG.md` / [中文](CHANGELOG.zh-CN.md)：当前 release notes 和 known limits。
- `benchmark/` / [中文](benchmark/README.zh-CN.md)：VibeHarnessBench 的任务格式、指标和 seed task。
- `benchmark/metrics.md` / [中文](benchmark/metrics.zh-CN.md) 与 `benchmark/scoring_rubric.md` / [中文](benchmark/scoring_rubric.zh-CN.md)：primary score 和 diagnostic subscores。
- `docs/framework.md` / [中文](docs/framework.zh-CN.md)：当前 framework design 和 evaluation checks。
- `vibeharness/`、`vibeharness/assets/` 和 `pyproject.toml`：本地 CLI package 和 packaged `vh init` templates。
- `scripts/`：benchmark、episode、i18n 校验工具。

## 当前状态

VibeHarness 目前是一个早期 workflow preview。它包含可移植 runtime、面向不同 agent 的 adapters、可执行 examples、可本地安装的 CLI，以及能从 fresh checkout 运行的 validation checks。

当前版本聚焦可回放的工作流机制。更大的实证主张需要脱敏真实 episodes、baselines 和 transfer evaluation 支撑。

## 实用贡献

1. vibe coding 中由用户介入触发的 harness failure taxonomy。
2. 面向每次非平凡 agent run 的 repository-native episode package。
3. supervisor-worker 恢复协议：把 intervention evidence 转化为 versioned harness change，并从 clean checkpoint 回放。
4. Codex、Claude Code、Cursor、OpenHands 的薄适配层。
5. 超越最终 task pass 的评估指标：intervention absorption、replay、attribution、trajectory safety、人类干预减少和 transfer。

## 已有工作

相关工作与致谢见：[已有工作与致谢](docs/prior_art.zh-CN.md)。

## 开源

公开开源发布准备度详见：[开源准备度](docs/open_source_readiness.zh-CN.md)。当前仓库使用 Apache-2.0 license。

署名和复用期待详见：[License 与署名](docs/licensing.zh-CN.md)。引用元数据在 `CITATION.cff`，attribution notices 在 `NOTICE`。

## 示例

运行 executable fixture 和脱敏 episode：

```sh
make example
make report
make ablation
```

## 验证

运行完整仓库健康检查：

```sh
make validate
```

具体验证项见：[验证](docs/verification.zh-CN.md)。

当前内置 examples 的结果见：[示例结果](docs/example_results.zh-CN.md)。

## CLI

直接从 checkout 使用：

```sh
python3 -m vibeharness.cli validate
```

或安装本地 CLI：

```sh
python3 -m pip install .
vh version
vh validate
vh ablation
vh episodes examples/episodes
vh init /path/to/target/repo
```

详见：[安装](docs/installation.zh-CN.md)。

## 下一步里程碑

1. 用 VH-Lite 跑一周真实 Codex/Claude/Cursor/OpenHands 任务。
2. 收集用户必须介入的 episode。
3. 把重复出现的介入升级为 VH-Recovery harness 修复。
4. 按 transfer group 跑 held-out tasks，并与旧工作流对比。
5. 把可量化收益整理成公开 evaluation report 和 benchmark pack。

## 本地命令

```sh
make validate
make example
make report
make ablation
make episodes
make i18n-check
make episode REQUEST="implement the user request"
EPISODE=.vibeharness/episodes/<id> make score-episode
```
