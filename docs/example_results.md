# Example Results

[English](example_results.md) | [简体中文](example_results.zh-CN.md)

This page records the current bundled example evaluation. It is not a research
result; it only proves that the open-source examples are executable and that the
scorecard pipeline works.

## Current Bundled Examples

| Example | Failure class | Fixture | Episode |
| --- | --- | --- | --- |
| `todo_cli_spec_capture` | `spec_capture` | pass | pass |
| `env_bootstrap_notes` | `environment_bootstrap` | pass | pass |
| `ui_snapshot_tasks` | `tool_affordance` | pass | pass |

## Summary

- examples: 3
- fixture pass rate: 1.00
- episode primary pass rate: 1.00
- ablation visible-only pass rate: 1.00
- ablation gap-probe failure rate: 1.00
- ablation replay pass rate: 1.00
- ablation recovered-gap rate: 1.00

## Ablation Results

| Example | Failure class | Visible-only | Gap probe | Replay | Recovered |
| --- | --- | --- | --- | --- | --- |
| `todo_cli_spec_capture` | `spec_capture` | pass | exposed | pass | pass |
| `env_bootstrap_notes` | `environment_bootstrap` | pass | exposed | pass | pass |
| `ui_snapshot_tasks` | `tool_affordance` | pass | exposed | pass | pass |

## Reproduce

```sh
make report
make ablation
```

This writes local generated reports under `reports/`, which is ignored by git.

## Interpretation

The examples cover three recovery classes:

- `spec_capture`: a user clarification becomes durable acceptance criteria and
  an acceptance test.
- `environment_bootstrap`: a manual environment export becomes a reusable
  harness bootstrap script.
- `tool_affordance`: manual UI inspection becomes machine-readable snapshot
  validation.

These examples do not prove that VibeHarness reduces interventions in real
projects. That requires real or realistic intervention episodes, baselines, and
the evaluation plan in `docs/evaluation.md`.

The ablation report proves only a narrower claim for the bundled examples:
visible-only checks can miss the harness gap, the gap probe exposes it, and the
repaired harness path replays successfully.
