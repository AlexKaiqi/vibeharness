# 开源准备度

[English](open_source_readiness.md) | 简体中文

本文档跟踪 VibeHarness 在公开 GitHub 发布前还需要补齐什么。

## 发布准备度

已经足够支撑早期开源发布的部分：

- Apache-2.0 license；
- 用于 attribution 的 NOTICE 和 CITATION.cff；
- 清晰的英文 README 和中文 README；
- prior-art 与致谢页面；
- VibeHarness runtime config 和 templates；
- Codex、Claude Code、Cursor、OpenHands adapters；
- episode 创建和评分脚本；
- benchmark manifest validator；
- i18n 状态检查脚本；
- 用 GitHub Actions 跑 `make validate`；
- contribution、security、conduct、issue、pull request templates；
- 一个 executable example fixture；
- 一个脱敏 example episode；
- examples 中已有三个 recovery classes：`spec_capture`、
  `environment_bootstrap` 和 `tool_affordance`；
- 本地 example evaluation report runner；
- 内置 harness-gap probes 的 executable ablation runner；
- 用于验证 collected episode directories 的 episode-set scorer；
- 可本地安装的 CLI package，并包含 packaged `vh init` templates；
- 高优先级 docs 和 benchmark pages 的中文翻译已补齐。

还不够支撑成熟发布的部分：

- 还没有真实世界 intervention dataset；
- 还没有外部 user study 或 multi-repository evaluation。

## 成熟公开发布前必须补齐

- 来自多个 agent tools 的真实脱敏 episodes；
- 至少一个 transfer group 的 multi-repository evaluation；
- release notes 和 version tag。

## License 建议

不要在没有 license 的情况下公开发布。GitHub 文档说明，即使仓库是公开的，如果没有 open-source license，默认版权法仍然适用。

推荐选项：

- 代码和脚本用 Apache-2.0：适合作为 tooling 默认选择，因为包含 patent grant。
- 代码和脚本用 MIT：更简单，社区熟悉。
- docs、benchmark specs、papers 用 CC BY 4.0：如果你希望别人复用并署名。

当前选择：整个仓库使用 Apache-2.0。NOTICE 和 CITATION.cff 用于明确 attribution 和 citation 期待。若后续 docs 或 datasets 使用不同 license，再额外注明。

## 公开定位

建议定位为：

> 一个可移植 recovery workflow，把 coding-agent session 中的人类介入转化为持久、可回放的 harness 改进。

避免：

- 声称发明了 harness engineering；
- 在没有数据前声称 benchmark 结果；
- 暗示 OpenAI、Anthropic、Cursor、OpenHands 官方背书。

## 第一个公开里程碑

第一个公开里程碑建议是 `v0.1`：

- VH-Lite 能端到端跑通；
- VH-Recovery 已文档化并可手动运行；
- 至少包含一个 example episode；
- 内置 ablations 能暴露 harness gaps，并通过 replay 恢复；
- CI 中 `make validate` 通过；
- issue templates 可用；
- Apache-2.0 license 已存在；
- i18n 状态在 CI 中检查。
