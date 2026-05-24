# Examples

This directory contains executable fixtures and sanitized episode packages.

## Fixtures

- `fixtures/todo_cli`: a tiny Python CLI used to demonstrate VH-Lite and
  VH-Recovery around a `spec_capture` intervention.
- `fixtures/env_bootstrap_notes`: a tiny Python CLI used to demonstrate
  VH-Recovery around an `environment_bootstrap` intervention.
- `fixtures/ui_snapshot_tasks`: a tiny HTML renderer used to demonstrate
  VH-Recovery around a `tool_affordance` intervention.

## Episodes

- `episodes/todo_cli_spec_capture`: a sanitized example episode showing how a
  user clarification becomes a decision contract, acceptance test, replay, and
  scorecard.
- `episodes/env_bootstrap_notes`: a sanitized example episode showing how a
  manual environment export becomes a bootstrap harness artifact.
- `episodes/ui_snapshot_tasks`: a sanitized example episode showing how manual
  UI inspection becomes machine-readable snapshot validation.

## Evaluation Report

```sh
make report
make ablation
make episodes
```

This writes `reports/example_evaluation.json` and
`reports/example_evaluation.md`, plus ablation reports that check whether the
bundled harness gaps are exposed and recovered.
