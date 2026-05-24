# VibeHarness

English | [简体中文](README.zh-CN.md)

VibeHarness is a practical harness-recovery workflow for AI-assisted software
engineering. It targets a common production failure mode: after a coding agent
gets stuck, a human often intervenes to fix the immediate problem, but the
underlying agent harness remains unchanged and the final outcome is not
replay-verified.

The core hypothesis is:

> Many apparent coding-agent failures are recoverable harness failures. A
> supervisor agent can improve reliability by checkpointing the repository,
> delegating implementation to worker agents, observing human or tool
> interventions, repairing the harness, rolling back, and replaying the task
> until both the user task and the harness fix are verified.

This repository contains:

- `AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.claude/commands/`, and
  `.openhands/microagents/`: thin adapters for common coding agents.
- `.vibeharness/`: the portable runtime config and episode templates.
- `docs/landing_architecture.md`: the production architecture and operating
  modes.
- `docs/evaluation.md`: practical evaluation plan for reliability, intervention
  reduction, transfer, and safety.
- `docs/i18n.md`: bilingual documentation maintenance policy.
- `docs/agent_adapters.md`: adapter notes for Codex, Claude Code, Cursor, and
  OpenHands.
- `docs/prior_art.md`: prior art, lineage, and acknowledgements.
- `docs/open_source_readiness.md`: checklist for public open-source release.
- `docs/release_process.md`: lightweight release and tagging process.
- `docs/verification.md`: what `make validate` checks and what it does not
  prove.
- `docs/example_results.md`: current bundled example evaluation results.
- `docs/episode_collection.md`: how to collect, sanitize, score, and split
  episodes.
- `docs/licensing.md`: license choice, attribution expectations, and reuse
  boundaries.
- `docs/installation.md`: local package usage, editable development install,
  and `vh init`.
- `CONTRIBUTING.md`, `SECURITY.md`, `.github/`: community and contribution
  files.
- `CHANGELOG.md`: current release notes and known limits.
- `benchmark/`: the proposed VibeHarnessBench task format, metrics, and seed
  task cards.
- `benchmark/metrics.md` and `benchmark/scoring_rubric.md`: binary primary
  score and diagnostic subscore definitions.
- `docs/framework.md`: the current framework design, including the parts
  absorbed from recent harness-engineering papers.
- `vibeharness/`, `vibeharness/assets/`, and `pyproject.toml`: local CLI
  package and packaged `vh init` templates.
- `scripts/`: lightweight utilities for validating benchmark manifests.

## Status

VibeHarness is an early workflow preview. It includes a portable runtime,
agent-specific adapters, executable examples, packaged CLI tooling, and
validation checks that can be run from a fresh checkout.

The current release focuses on replayable workflow mechanics. Broader empirical
claims require sanitized real episodes, baselines, and transfer evaluation.

## Practical Contribution

1. A taxonomy of intervention-triggered harness failures in vibe coding.
2. A repository-native episode package for every non-trivial agent run.
3. A supervisor-worker recovery protocol that converts intervention evidence
   into versioned harness changes and replays from a clean checkpoint.
4. Thin adapters for Codex, Claude Code, Cursor, and OpenHands.
5. Metrics beyond final task pass rate: intervention absorption, replay,
   attribution, trajectory safety, human-intervention reduction, and transfer.

## Prior Art

VibeHarness builds on recent harness-engineering, agent-recovery, benchmark, and
trajectory-audit work. See [Prior Art and Acknowledgements](docs/prior_art.md).

## Open Source

For open-source release readiness, see
[Open-Source Readiness](docs/open_source_readiness.md). The repository still
uses the Apache-2.0 license.

For attribution and reuse expectations, see
[Licensing and Attribution](docs/licensing.md). Citation metadata is available in
`CITATION.cff`, and attribution notices are in `NOTICE`.

## Example

Run the executable fixture and sanitized episode:

```sh
make example
make report
make ablation
```

## Verification

Run the full repository health check:

```sh
make validate
```

See [Verification](docs/verification.md) for the exact checks.

Current bundled example results are summarized in
[Example Results](docs/example_results.md).

## CLI

Use from checkout:

```sh
python3 -m vibeharness.cli validate
```

Or install the local CLI:

```sh
python3 -m pip install .
vh version
vh validate
vh ablation
vh episodes examples/episodes
vh init /path/to/target/repo
```

See [Installation](docs/installation.md).

## Suggested Next Milestones

1. Use VH-Lite on real Codex/Claude/Cursor/OpenHands tasks for one week.
2. Collect episodes where the user had to intervene.
3. Promote recurring interventions into VH-Recovery harness repairs.
4. Run held-out tasks by transfer group and compare against the old workflow.
5. Turn measured gains into a public evaluation report and benchmark pack.

## Local Commands

```sh
make validate
make example
make report
make ablation
make episodes
make i18n-check
make episode REQUEST="implement the user request"
EPISODE=.vibeharness/episodes/<id> make score-episode
```
