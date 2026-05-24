# Todo CLI Fixture

This fixture is a tiny executable example for VibeHarness.

It demonstrates a `spec_capture` recovery:

1. The original request asks for a friendlier todo listing.
2. The first visible test only checks that the CLI runs.
3. A user intervention clarifies that "friendly" means completed tasks must be
   shown after open tasks and marked with `[x]`.
4. The harness repair captures that clarification as an acceptance test.
5. Replay should implement the behavior and pass the acceptance test.

## Commands

```sh
python3 app/todo.py --list examples/sample_tasks.json
python3 tests/test_visible.py
python3 tests/test_acceptance.py
```
