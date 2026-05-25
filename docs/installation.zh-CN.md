# 安装

[English](installation.md) | 简体中文

VibeHarness 有两条安装路径：

1. 面向 agent 工作流的 skill-first 安装，不需要 Python package。
2. 可选的 Python CLI 安装，用于 episode scaffolding、scoring 和 reports。

不同 runtime 的具体安装方式见：[Runtime 安装矩阵](runtime_install.zh-CN.md)。
Codex-specific artifacts 和验证方式见：[Codex 安装](codex_install.zh-CN.md)。

## Skill Install

从 checkout 安装：

```sh
git clone https://github.com/AlexKaiqi/vibeharness.git
cd vibeharness
./install.sh
```

默认会安装到：

- `${CODEX_HOME:-$HOME/.codex}/skills/vibeharness`
- `${CLAUDE_HOME:-$HOME/.claude}/skills/vibeharness`

也可以只安装到某个 runtime：

```sh
./install.sh --codex-only
./install.sh --claude-only
./install.sh --cursor-only
./install.sh --target /path/to/skills/vibeharness
./install.sh --force
```

安装后，在 coding agent 中显式调用：

```text
Use $vibeharness to run this task as a checkpointed, replayable episode.
```

兼容 skills 的安装器也可以直接指向 `skills/vibeharness` 目录。如果某个
runtime 的 skills 目录不同，可以用 `--target`。根目录 `SKILL.md` 会保持同步，以兼容期望 top-level skill entry 的工具。

Runtime notes：

- Codex：用 `./install.sh --codex-only` 安装本地 skill；每个需要启用的项目中再运行 `vh init`，写入 `AGENTS.md`、`.agents/skills/vibeharness/` 和 `.vibeharness/`。
- Claude Code：用 `./install.sh --claude-only` 安装本地 skill；项目中用 `vh init` 写入 `CLAUDE.md` 和 `.claude/commands/`。
- Cursor：更推荐用 `vh init` 写入 `.cursor/rules/vibeharness.mdc`；只有当你的本地 runtime 支持 skills 目录时，才使用 `--target` 或 `--cursor-only`。
- OpenHands：用 `vh init` 写入 `.openhands/microagents/vibeharness.md`；不需要全局 skill install 路径。

## 直接从 Checkout 使用

```sh
python3 -m vibeharness.cli validate
python3 -m vibeharness.cli report
```

Makefile 使用的就是这种方式，所以贡献者不需要全局安装 CLI。

## 可选 CLI Install

```sh
python3 -m pip install .
vh version
vh validate
vh report
```

如果你的 Python user script 目录不在 `PATH` 里，可以先从 checkout 使用
`python3 -m vibeharness.cli ...`，或把 `pip` 提示的脚本目录加入 `PATH`。

如果要做 active development，再使用 editable mode：

```sh
python3 -m pip install -e .
```

## 初始化另一个仓库的 Runtime Files

从当前项目 checkout 或本地 package install 运行：

```sh
vh init /path/to/target/repo
```

如果 `vh` 不在 `PATH` 中，可以从 checkout 使用 module form：

```sh
python3 -m vibeharness.cli init /path/to/target/repo
```

它会复制可移植的 VibeHarness runtime 和 agent adapter files：

- `.vibeharness/`
- `.agents/skills/vibeharness/`
- `AGENTS.md`
- `CLAUDE.md`
- `.claude/commands/`
- `.cursor/rules/`
- `.openhands/microagents/`

只有当你明确想覆盖已有文件时，才使用 `--force`：

```sh
vh init /path/to/target/repo --force
```

## 常用命令

```sh
vh start --request "implement the user request"
vh version
vh score .vibeharness/episodes/<id>
vh episodes .vibeharness/episodes
vh validate
vh report
vh ablation
vh i18n
vh links
vh benchmark
```

所有命令都可以在 checkout 中用 `python3 -m vibeharness.cli <command>` 运行。

## Maintainer Command

修改 runtime templates 或 agent adapters 后，提交前同步 packaged `vh init`
assets，并验证 skill distribution：

```sh
make sync-assets
make validate
```

## 打包状态

当前 package 可以从 checkout 本地安装，并包含 `vh init` 所需的 runtime templates。它还没有发布到 PyPI。目前更推荐把 skill install 作为公开入口。
