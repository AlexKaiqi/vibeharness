# 安装

[English](installation.md) | 简体中文

VibeHarness 可以直接从 checkout 使用，也可以作为 editable Python package 安装。

## 直接从 Checkout 使用

```sh
python3 -m vibeharness.cli validate
python3 -m vibeharness.cli report
```

Makefile 使用的就是这种方式，所以贡献者不需要额外安装。

## Editable Install

```sh
python3 -m pip install -e .
vh validate
vh report
```

如果你的 Python user script 目录不在 `PATH` 里，可以先从 checkout 使用
`python3 -m vibeharness.cli ...`，或把 `pip` 提示的脚本目录加入 `PATH`。

## 初始化另一个仓库

从当前项目 checkout 或 editable install 运行：

```sh
vh init /path/to/target/repo
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
vh score .vibeharness/episodes/<id>
vh validate
vh report
vh i18n
vh links
vh benchmark
```

## 打包状态

当前 package 是本地 editable-install preview，还没有发布到 PyPI，普通
wheel/sdist 也还不是稳定分发路径。
