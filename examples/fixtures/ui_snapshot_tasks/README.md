# UI Snapshot Tasks Fixture

This fixture demonstrates a `tool_affordance` recovery without requiring a real
browser in CI.

The app renders a small HTML todo list. The visible test only checks that HTML
is produced. The acceptance test uses a harness-provided UI snapshot verifier to
assert that the empty state disappears after the first item is rendered.

The recovery story:

1. The worker can run visible tests.
2. The user manually inspects the rendered UI and reports an empty-state overlap.
3. The harness lacks a machine-readable UI snapshot tool.
4. The harness repair adds `harness/snapshot.py`.
5. Replay can validate the UI behavior without manual visual inspection.

## Commands

```sh
python3 tests/test_visible.py
python3 tests/test_acceptance.py
```
