# Runtime Install Matrix

[English](runtime_install.md) | [简体中文](runtime_install.zh-CN.md)

VibeHarness has two layers:

- **Agent skill:** a portable method guide installed into a local agent runtime.
- **Project runtime:** repository files installed by `vh init`, including
  `.vibeharness/` episode templates and native adapter files.

For day-to-day use, prefer installing the skill once and running `vh init` in
each project that should keep replayable episodes.

## Codex

Install the skill:

```sh
git clone https://github.com/AlexKaiqi/vibeharness.git
cd vibeharness
./install.sh --codex-only
```

This writes:

```text
${CODEX_HOME:-$HOME/.codex}/skills/vibeharness
```

Invoke it explicitly in Codex:

```text
Use $vibeharness to run this task as a checkpointed, replayable episode.
```

Enable VibeHarness inside a project:

```sh
python3 -m pip install .
cd /path/to/project
vh init .
```

This writes `AGENTS.md` and `.vibeharness/` so Codex can read the repository
instructions and create episodes with `vh start`.

## Claude Code

Install the skill:

```sh
git clone https://github.com/AlexKaiqi/vibeharness.git
cd vibeharness
./install.sh --claude-only
```

This writes:

```text
${CLAUDE_HOME:-$HOME/.claude}/skills/vibeharness
```

Enable VibeHarness inside a project:

```sh
python3 -m pip install .
cd /path/to/project
vh init .
```

This writes:

```text
CLAUDE.md
.claude/commands/vh-start.md
.claude/commands/vh-recovery.md
.claude/commands/vh-audit.md
.vibeharness/
```

Claude Code can then use `/vh-start`, `/vh-recovery`, and `/vh-audit`.

## Cursor

Cursor can use a custom skill directory if your local setup supports it:

```sh
./install.sh --cursor-only
```

Project-level setup is the more portable path:

```sh
python3 -m pip install .
cd /path/to/project
vh init .
```

This writes:

```text
.cursor/rules/vibeharness.mdc
.vibeharness/
```

The Cursor rule is marked `alwaysApply: true`.

## OpenHands

OpenHands uses repository-level microagents rather than the global skill install
path:

```sh
python3 -m pip install .
cd /path/to/project
vh init .
```

This writes:

```text
.openhands/microagents/vibeharness.md
.vibeharness/
```

When OpenHands opens the repository, the microagent file provides the
VibeHarness workflow.

## Custom Skill Directory

For any runtime that supports a skills folder:

```sh
./install.sh --target /path/to/skills/vibeharness
```

The target should be the final skill directory, not its parent.

## What Needs The CLI

The skill can explain the method without Python. The CLI is needed for:

- `vh init`: copy project runtime files into a target repository;
- `vh start`: create a structured episode;
- `vh score`: score an episode;
- `vh validate`: run repository health checks.

All CLI commands also work from a checkout:

```sh
python3 -m vibeharness.cli <command>
```
