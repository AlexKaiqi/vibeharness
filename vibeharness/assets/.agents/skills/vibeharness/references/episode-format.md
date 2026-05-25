# Episode Format

Use this reference when the VibeHarness CLI is unavailable and an agent needs to
create or inspect an episode manually.

## Directory

Create one directory per run:

```text
.vibeharness/episodes/<episode-id>/
├── request.md
├── manifest.json
├── intervention_log.md
├── decision_contract.md
├── scorecard.json
└── audit.md
```

Use a short, stable `<episode-id>` such as
`2026-05-24-env-bootstrap-notes` or `todo-cli-spec-capture`.

## request.md

Record the user request and visible acceptance criteria:

```markdown
# Request

<original or summarized user request>

## Acceptance Criteria

- <visible criterion>
- <visible criterion>
```

## manifest.json

Keep enough metadata to replay the run:

```json
{
  "episode_id": "<episode-id>",
  "task_family": "spec_capture | environment_bootstrap | tool_affordance | verification_gap | other",
  "checkpoint": "<git commit, tag, branch, or explanation>",
  "agent_runtime": "<codex | claude-code | cursor | openhands | other>",
  "baseline_commands": ["<command used before harness repair>"],
  "replay_commands": ["<command used after harness repair>"],
  "harness_files_changed": [],
  "product_files_changed": []
}
```

## intervention_log.md

Log interventions as evidence, not blame:

```markdown
# Intervention Log

## Intervention 1

- Trigger:
- Human or tool action:
- Missing signal:
- Failure class:
- Evidence:
```

## decision_contract.md

Write this before modifying the harness:

```markdown
# Decision Contract

## Observed Failure

## Harness Gap

## Proposed Harness Change

## Replay Plan

## Success Evidence
```

## scorecard.json

The primary score is intentionally strict:

```json
{
  "task_passed": false,
  "intervention_absorbed": false,
  "replay_verified": false,
  "attribution_correct": false,
  "trajectory_safe": false,
  "primary_pass": false,
  "notes": ""
}
```

Only set `primary_pass` to true when all five booleans are true.

## audit.md

Close the episode with reviewer-facing evidence:

```markdown
# Audit

## Outcome

## Product Changes

## Harness Changes

## Replay Evidence

## Remaining Risks
```
