# Decision Contract

## Failure Class

`tool_affordance`

## Harness Components

- `tool_access`
- `observability`
- `verification`
- `intervention_recording`

## Evidence

- Visible validation checked only that the renderer produced HTML.
- The user had to inspect the UI behavior manually.
- The harness lacked a machine-readable UI snapshot or DOM-like validation tool.

## Hypothesis

The task failure repeats because the harness cannot observe UI state transitions
as structured evidence. Adding a snapshot verifier should turn manual UI
inspection into replayable validation.

## Harness Edit Scope

- Allowed: `harness/snapshot.py`, acceptance tests, episode scorecard.
- Forbidden: hard-coding acceptance output into the renderer.

## Expected Effect

Replay should validate both empty and one-task UI states without a fresh manual
inspection.

## Falsification Check

Replay fails if the acceptance test cannot detect empty-state presence/absence or
if the user must manually inspect rendered HTML again.

## Replay Plan

1. Reset product code to the checkpoint.
2. Keep the snapshot verifier as a harness repair.
3. Render empty and one-task states.
4. Run snapshot acceptance checks.
