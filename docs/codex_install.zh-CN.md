# Codex 安装

[English](codex_install.md) | 简体中文

VibeHarness 通过三类 artifact 支持 Codex：

| 用途 | 仓库中的 artifact | 安装后位置 |
| --- | --- | --- |
| repo-scoped Codex skill | `.agents/skills/vibeharness/` | `vh init` 后的 `/path/to/project/.agents/skills/vibeharness` |
| user Codex skill | `skills/vibeharness/` | `${AGENTS_HOME:-$HOME/.agents}/skills/vibeharness` |
| Codex app compatibility skill | `skills/vibeharness/` | `${CODEX_HOME:-$HOME/.codex}/skills/vibeharness` |
| 项目级指令 | `AGENTS.md` | `vh init` 后的 `/path/to/project/AGENTS.md` |

仓库里不会直接提交 `.codex/` 目录。当前 Codex 文档描述的 repo-scoped skills
路径是 `.agents/skills`，而 `AGENTS.md` 仍然是项目级 instruction file。

## 安装 Codex Skill

```sh
git clone https://github.com/AlexKaiqi/vibeharness.git
cd vibeharness
./install.sh --codex-only
```

验证安装后的 artifact：

```sh
test -f "${AGENTS_HOME:-$HOME/.agents}/skills/vibeharness/SKILL.md"
test -f "${CODEX_HOME:-$HOME/.codex}/skills/vibeharness/SKILL.md"
test -f "${CODEX_HOME:-$HOME/.codex}/skills/vibeharness/agents/openai.yaml"
test -f "${CODEX_HOME:-$HOME/.codex}/skills/vibeharness/references/episode-format.md"
diff -qr skills/vibeharness "${AGENTS_HOME:-$HOME/.agents}/skills/vibeharness"
diff -qr skills/vibeharness "${CODEX_HOME:-$HOME/.codex}/skills/vibeharness"
```

在 Codex 中显式调用：

```text
Use $vibeharness to run this task as a checkpointed, replayable episode.
```

如果 Codex 在安装前已经启动，需要重启或 reload session，新的 skill 才能被发现。

## 在项目中启用 VibeHarness

从 VibeHarness checkout 安装可选 CLI：

```sh
python3 -m pip install .
```

然后初始化目标仓库：

```sh
cd /path/to/project
vh init .
```

这会写入 Codex 项目级 artifact：

```text
AGENTS.md
.agents/skills/vibeharness/
.vibeharness/
```

`.agents/skills/vibeharness/` 给 Codex 提供 repo-scoped `$vibeharness` skill。
`AGENTS.md` 会告诉 Codex 使用 `vh start --request ...` 创建 episode，记录
interventions，写 decision contracts，在需要时从 checkpoint replay，并使用
`vh score` 给 episode 评分。

## Smoke Test

在目标仓库中运行：

```sh
vh start --request "codex install verification"
vh score .vibeharness/episodes/<episode-id>
```

刚创建的 episode 在填写 `scorecard.json` 前不会通过，这是预期行为。这个 smoke
test 用来确认 Codex 可见文件和 VibeHarness 命令都已经就位。
