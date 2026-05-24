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
- `docs/prior_art.md` / [中文](docs/prior_art.zh-CN.md)：已有工作、思想 lineage 和致谢。
- `docs/publication_strategy.md` / [中文](docs/publication_strategy.zh-CN.md)：什么时候值得作为论文发表。
- `docs/open_source_readiness.md` / [中文](docs/open_source_readiness.zh-CN.md)：公开开源发布 checklist。
- `docs/verification.md` / [中文](docs/verification.zh-CN.md)：`make validate` 检查什么、不证明什么。
- `docs/example_results.md` / [中文](docs/example_results.zh-CN.md)：当前内置 examples 的评估结果。
- `docs/licensing.md` / [中文](docs/licensing.zh-CN.md)：license 选择、署名期待和复用边界。
- `docs/installation.md` / [中文](docs/installation.zh-CN.md)：本地使用、editable install 和 `vh init`。
- `CONTRIBUTING.md`、`SECURITY.md`、`.github/`：社区和贡献文件。
- `paper/`：论文草稿和引用。
- `benchmark/`：VibeHarnessBench 的任务格式、指标和 seed task。
- `vibeharness/` 和 `pyproject.toml`：本地 editable CLI package preview。
- `scripts/`：benchmark、episode、i18n 校验工具。

## 当前状态

这个项目现在优先作为落地工作流维护，其次才是论文 scaffold。真正有价值的产品主张不是“harness engineering 是新概念”，而是：

> 用户介入应该被吸收为持久、可回放、可迁移的 harness 改进。

## 实用贡献

1. vibe coding 中由用户介入触发的 harness failure taxonomy。
2. 面向每次非平凡 agent run 的 repository-native episode package。
3. supervisor-worker 恢复协议：把 intervention evidence 转化为 versioned harness change，并从 clean checkpoint 回放。
4. Codex、Claude Code、Cursor、OpenHands 的薄适配层。
5. 超越最终 task pass 的评估指标：intervention absorption、replay、attribution、trajectory safety、人类干预减少和 transfer。

## 已有工作

VibeHarness 建立在近期 harness engineering、agent recovery、benchmark 和 trajectory audit 工作之上。详见：[已有工作与致谢](docs/prior_art.zh-CN.md)。

## 发表与开源

只有当 workflow 已经基于真实或现实化 episodes 产生实证证据时，项目才值得作为论文发表。详见：[发表策略](docs/publication_strategy.zh-CN.md)。

公开开源发布准备度详见：[开源准备度](docs/open_source_readiness.zh-CN.md)。当前仓库使用 Apache-2.0 license。

署名和复用期待详见：[License 与署名](docs/licensing.zh-CN.md)。引用元数据在 `CITATION.cff`，attribution notices 在 `NOTICE`。

## 示例

运行 executable fixture 和脱敏 episode：

```sh
make example
make report
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
python3 -m pip install -e .
vh validate
vh init /path/to/target/repo
```

详见：[安装](docs/installation.zh-CN.md)。

## 下一步里程碑

1. 用 VH-Lite 跑一周真实 Codex/Claude/Cursor/OpenHands 任务。
2. 收集用户必须介入的 episode。
3. 把重复出现的介入升级为 VH-Recovery harness 修复。
4. 按 transfer group 跑 held-out tasks，并与旧工作流对比。
5. 在工作流产生可量化收益之后，再把数据整理成论文或公开 benchmark。

## 本地命令

```sh
make validate
make example
make report
make i18n-check
make episode REQUEST="implement the user request"
EPISODE=.vibeharness/episodes/<id> make score-episode
make paper
```
