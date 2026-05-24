# Decision Contract

## Failure Class

`environment_bootstrap`

## Harness Components

- `tool_access`
- `task_state`
- `verification`
- `intervention_recording`

## Evidence

- Visible test passed because it supplied `--db` explicitly.
- Acceptance test represented the real workflow and expected `NOTES_DB`.
- User had to manually export `NOTES_DB` to unblock validation.

## Hypothesis

The task failure is not primarily application logic. The harness is missing a
durable bootstrap step that configures the local notes data path for acceptance
validation.

## Harness Edit Scope

- Allowed: `harness/bootstrap.sh`, acceptance validation docs, episode scorecard.
- Forbidden: hard-coding an absolute user machine path in application code.

## Expected Effect

After adding the bootstrap script, replay can configure `NOTES_DB` and run
acceptance validation without a fresh user command.

## Falsification Check

Replay fails if `python3 tests/test_acceptance.py` still exits with
`NOTES_DB is not configured` or if a user must export the variable manually.

## Replay Plan

1. Reset product code to the checkpoint.
2. Keep `harness/bootstrap.sh` as the harness repair.
3. Run `bash harness/bootstrap.sh`.
4. Run visible and acceptance checks.
