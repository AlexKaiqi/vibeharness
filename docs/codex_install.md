# Codex Install

[English](codex_install.md) | [简体中文](codex_install.zh-CN.md)

VibeHarness supports Codex through three artifacts:

| Purpose | Repository artifact | Installed location |
| --- | --- | --- |
| Repo-scoped Codex skill | `.agents/skills/vibeharness/` | `/path/to/project/.agents/skills/vibeharness` after `vh init` |
| User Codex skill | `skills/vibeharness/` | `${AGENTS_HOME:-$HOME/.agents}/skills/vibeharness` |
| Codex app compatibility skill | `skills/vibeharness/` | `${CODEX_HOME:-$HOME/.codex}/skills/vibeharness` |
| Project instructions | `AGENTS.md` | `/path/to/project/AGENTS.md` after `vh init` |

The repository does not keep a checked-in `.codex/` directory. Current Codex
docs describe repo-scoped skills under `.agents/skills`, while `AGENTS.md`
remains the project instruction file.

## Install The Codex Skill

```sh
git clone https://github.com/AlexKaiqi/vibeharness.git
cd vibeharness
./install.sh --codex-only
```

Verify the installed artifact:

```sh
test -f "${AGENTS_HOME:-$HOME/.agents}/skills/vibeharness/SKILL.md"
test -f "${CODEX_HOME:-$HOME/.codex}/skills/vibeharness/SKILL.md"
test -f "${CODEX_HOME:-$HOME/.codex}/skills/vibeharness/agents/openai.yaml"
test -f "${CODEX_HOME:-$HOME/.codex}/skills/vibeharness/references/episode-format.md"
diff -qr skills/vibeharness "${AGENTS_HOME:-$HOME/.agents}/skills/vibeharness"
diff -qr skills/vibeharness "${CODEX_HOME:-$HOME/.codex}/skills/vibeharness"
```

Invoke it explicitly in Codex:

```text
Use $vibeharness to run this task as a checkpointed, replayable episode.
```

If Codex was already running before installation, restart or reload the session
so the new skill can be discovered.

## Enable VibeHarness In A Project

Install the optional CLI from the VibeHarness checkout:

```sh
python3 -m pip install .
```

Then initialize the target repository:

```sh
cd /path/to/project
vh init .
```

This writes the Codex project artifact:

```text
AGENTS.md
.agents/skills/vibeharness/
.vibeharness/
```

`.agents/skills/vibeharness/` gives Codex a repo-scoped `$vibeharness` skill.
`AGENTS.md` tells Codex to start episodes with `vh start --request ...`, record
interventions, write decision contracts, replay from checkpoints when needed,
and score episodes with `vh score`.

## Smoke Test

From the target repository:

```sh
vh start --request "codex install verification"
vh score .vibeharness/episodes/<episode-id>
```

A fresh episode will not pass until its `scorecard.json` is filled. That is
expected. The smoke test confirms that Codex-visible files and VibeHarness
commands are present.
