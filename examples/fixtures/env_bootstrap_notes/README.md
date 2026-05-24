# Environment Bootstrap Notes Fixture

This fixture demonstrates an `environment_bootstrap` recovery.

The notes CLI searches notes by tag. The visible test passes without any
environment file, but the acceptance test expects a harness-provided notes data
path through `NOTES_DB`.

The recovery story:

1. The worker can run a visible smoke test.
2. Acceptance validation fails because `NOTES_DB` is missing.
3. The user intervention reveals a missing bootstrap step.
4. The harness repair adds `harness/bootstrap.sh`.
5. Replay succeeds without the user manually exporting `NOTES_DB`.

## Commands

```sh
python3 tests/test_visible.py
bash harness/bootstrap.sh
python3 tests/test_acceptance.py
```
