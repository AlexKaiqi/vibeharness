# Runtime 安装矩阵

[English](runtime_install.md) | 简体中文

VibeHarness 分成两层：

- **Agent skill：** 安装到本地 agent runtime 的可移植方法指南。
- **Project runtime：** 由 `vh init` 写入仓库的文件，包括 `.vibeharness/`
  episode templates 和各 agent 原生 adapter files。

日常使用建议：skill 安装一次；每个需要保留可回放 episodes 的项目再运行
`vh init`。

## Codex

Codex 详细说明见：[Codex 安装](codex_install.zh-CN.md)。

安装 skill：

```sh
git clone https://github.com/AlexKaiqi/vibeharness.git
cd vibeharness
./install.sh --codex-only
```

写入位置：

```text
${CODEX_HOME:-$HOME/.codex}/skills/vibeharness
${AGENTS_HOME:-$HOME/.agents}/skills/vibeharness
```

在 Codex 中显式调用：

```text
Use $vibeharness to run this task as a checkpointed, replayable episode.
```

在某个项目中启用 VibeHarness：

```sh
python3 -m pip install .
cd /path/to/project
vh init .
```

这会写入 `AGENTS.md`、`.agents/skills/vibeharness/` 和 `.vibeharness/`，让
Codex 能读取仓库级指令、发现 repo-scoped skill，并用 `vh start` 创建 episode。

## Claude Code

安装 skill：

```sh
git clone https://github.com/AlexKaiqi/vibeharness.git
cd vibeharness
./install.sh --claude-only
```

写入位置：

```text
${CLAUDE_HOME:-$HOME/.claude}/skills/vibeharness
```

在某个项目中启用 VibeHarness：

```sh
python3 -m pip install .
cd /path/to/project
vh init .
```

这会写入：

```text
CLAUDE.md
.claude/commands/vh-start.md
.claude/commands/vh-recovery.md
.claude/commands/vh-audit.md
.vibeharness/
```

Claude Code 之后可以使用 `/vh-start`、`/vh-recovery` 和 `/vh-audit`。

## Cursor

如果你的本地 Cursor setup 支持自定义 skills 目录，可以安装 skill：

```sh
./install.sh --cursor-only
```

更可移植的方式是项目级初始化：

```sh
python3 -m pip install .
cd /path/to/project
vh init .
```

这会写入：

```text
.cursor/rules/vibeharness.mdc
.vibeharness/
```

Cursor rule 设置了 `alwaysApply: true`。

## OpenHands

OpenHands 使用 repository-level microagents，而不是全局 skill install 路径：

```sh
python3 -m pip install .
cd /path/to/project
vh init .
```

这会写入：

```text
.openhands/microagents/vibeharness.md
.vibeharness/
```

OpenHands 打开仓库后会读取 microagent 文件中的 VibeHarness workflow。

## 自定义 Skill 目录

任何支持 skills folder 的 runtime 都可以使用：

```sh
./install.sh --target /path/to/skills/vibeharness
```

`--target` 应该指向最终 skill 目录，而不是它的父目录。

## 哪些能力需要 CLI

Skill 本身可以解释方法，不需要 Python。以下能力需要 CLI：

- `vh init`：把 project runtime files 复制到目标仓库；
- `vh start`：创建结构化 episode；
- `vh score`：给 episode 评分；
- `vh validate`：运行仓库健康检查。

所有 CLI 命令也可以直接从 checkout 运行：

```sh
python3 -m vibeharness.cli <command>
```
