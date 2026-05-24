# 安装

[English](installation.md) | 简体中文

VibeHarness 可以直接从 checkout 使用，也可以作为本地 Python package 安装。

## 直接从 Checkout 使用

```sh
python3 -m vibeharness.cli validate
python3 -m vibeharness.cli report
```

Makefile 使用的就是这种方式，所以贡献者不需要额外安装。

## Package Install

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

## 初始化另一个仓库

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
assets：

```sh
make sync-assets
make validate
```

## 打包状态

当前 package 可以从 checkout 本地安装，并包含 `vh init` 所需的 runtime templates。它还没有发布到 PyPI。
