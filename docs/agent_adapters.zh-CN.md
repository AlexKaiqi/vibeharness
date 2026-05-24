# Agent Adapter Notes

[English](agent_adapters.md) | 简体中文

VibeHarness 通过使用各工具原生的 instruction/config surface 来保持可移植性，而不是构建特定厂商 wrapper。

各 runtime 面向用户的安装命令见：[Runtime 安装矩阵](runtime_install.zh-CN.md)。

## Codex

使用 `AGENTS.md` 放置仓库级指令，并在 prompt 或 task template 中显式保留 VibeHarness 命令。Codex cloud tasks 运行在 sandboxed environment 中，可以读取、编辑和执行仓库代码。网络访问应作为 policy decision 处理：Codex 文档描述 cloud tasks 的 internet access 默认关闭，需要时可以通过 allowlist 开启。

Install shape：

- local skill：`./install.sh --codex-only`；
- project runtime：`vh init /path/to/project`，写入 `AGENTS.md` 和 `.vibeharness/`。

Useful sources:

- https://platform.openai.com/docs/codex
- https://platform.openai.com/docs/codex/agent-network
- https://platform.openai.com/docs/docs-mcp

## Claude Code

使用：

- `CLAUDE.md` 作为 project memory；
- `.claude/commands/*.md` 作为可重复 slash commands；
- `.claude/settings.example.json` 作为 opt-in hook example。

谨慎使用 hooks：Claude Code hooks 会自动执行 shell commands，所以优先把它们用于 logging 或 reminders；任何 destructive action 都应设置明确 gate。

Install shape：

- local skill：`./install.sh --claude-only`；
- project runtime：`vh init /path/to/project`，写入 `CLAUDE.md`、`.claude/commands/` 和 `.vibeharness/`。

Useful sources:

- https://docs.anthropic.com/en/docs/claude-code/memory
- https://docs.anthropic.com/en/docs/claude-code/slash-commands
- https://docs.anthropic.com/en/docs/claude-code/hooks

## Cursor

使用 `.cursor/rules/*.mdc` project rules。Cursor 也把 `AGENTS.md` 作为简单 Markdown alternative 记录在文档中，而 `.cursorrules` 是 legacy。VibeHarness rule 设置了 `alwaysApply: true`，确保 recovery workflow 稳定可见。

Install shape：

- project runtime：`vh init /path/to/project`，写入 `.cursor/rules/vibeharness.mdc`；
- optional custom skill path：当你的本地 runtime 支持时，使用 `./install.sh --target /path/to/skills/vibeharness`。

Useful source:

- https://docs.cursor.com/context/rules

## OpenHands

使用 `.openhands/microagents/*.md` 放置仓库级指导。对于真实项目，只有在需要 deterministic dependency bootstrap 时才添加 `.openhands/setup.sh`；保持它最小、可重复、幂等。

Install shape：

- project runtime：`vh init /path/to/project`，写入 `.openhands/microagents/vibeharness.md`；
- 不需要全局 skill install 路径。

Useful sources:

- https://docs.all-hands.dev/usage/prompting/microagents-overview
- https://docs.all-hands.dev/usage/prompting/repository

## Adapter Contract

每个 adapter 都应暴露同一组五个动作：

1. create episode；
2. record intervention；
3. write decision contract；
4. replay from checkpoint；
5. score and audit。

如果某个 agent 无法原生支持其中一个动作，应把这个动作作为 episode workflow 中的显式命令保留下来，而不是藏在 prose 里。
