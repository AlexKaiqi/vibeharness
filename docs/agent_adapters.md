# Agent Adapter Notes

[English](agent_adapters.md) | [简体中文](agent_adapters.zh-CN.md)

VibeHarness stays portable by using each tool's native instruction/config
surface instead of building a vendor-specific wrapper.

For user-facing installation commands by runtime, see
[Runtime Install Matrix](runtime_install.md).
For Codex-specific artifact mapping, see [Codex Install](codex_install.md).

## Codex

Use `AGENTS.md` for repository instructions and keep VibeHarness commands
explicit in prompts or task templates. Codex cloud tasks run in sandboxed
environments and can read, edit, and execute code in repositories. Treat network
access as a policy decision: Codex documentation describes internet access as
off by default in cloud tasks, with allowlists available when needed.

Install shape:

- local skill: `./install.sh --codex-only`;
- project runtime: `vh init /path/to/project`, which writes `AGENTS.md` and
  `.vibeharness/`.

Useful sources:

- https://platform.openai.com/docs/codex
- https://platform.openai.com/docs/codex/agent-network
- https://platform.openai.com/docs/docs-mcp

## Claude Code

Use:

- `CLAUDE.md` for project memory;
- `.claude/commands/*.md` for repeatable slash commands;
- `.claude/settings.example.json` as an opt-in hook example.

Be careful with hooks: Claude Code hook commands execute shell commands
automatically, so use them for logging or reminders first, and gate anything
destructive.

Install shape:

- local skill: `./install.sh --claude-only`;
- project runtime: `vh init /path/to/project`, which writes `CLAUDE.md`,
  `.claude/commands/`, and `.vibeharness/`.

Useful sources:

- https://docs.anthropic.com/en/docs/claude-code/memory
- https://docs.anthropic.com/en/docs/claude-code/slash-commands
- https://docs.anthropic.com/en/docs/claude-code/hooks

## Cursor

Use `.cursor/rules/*.mdc` project rules. Cursor also documents `AGENTS.md` as a
simple Markdown alternative, while `.cursorrules` is legacy. The VibeHarness rule
is marked `alwaysApply: true` so the recovery workflow is consistently visible.

Install shape:

- project runtime: `vh init /path/to/project`, which writes
  `.cursor/rules/vibeharness.mdc`;
- optional custom skill path: `./install.sh --target /path/to/skills/vibeharness`
  when your local runtime supports it.

Useful source:

- https://docs.cursor.com/context/rules

## OpenHands

Use `.openhands/microagents/*.md` for repository-specific guidance. For real
projects, add `.openhands/setup.sh` only when you need deterministic dependency
bootstrap; keep it minimal and idempotent.

Install shape:

- project runtime: `vh init /path/to/project`, which writes
  `.openhands/microagents/vibeharness.md`;
- no global skill install path is required.

Useful sources:

- https://docs.all-hands.dev/usage/prompting/microagents-overview
- https://docs.all-hands.dev/usage/prompting/repository

## Adapter Contract

Every adapter should expose the same five actions:

1. create episode;
2. record intervention;
3. write decision contract;
4. replay from checkpoint;
5. score and audit.

If an agent cannot support one action natively, keep the action as an explicit
command in the episode workflow rather than hiding it in prose.
