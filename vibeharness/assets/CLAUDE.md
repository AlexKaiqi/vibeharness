# VibeHarness Instructions for Claude Code

This repository uses VibeHarness to turn user interventions into durable harness
improvements.

## Start

For non-trivial tasks, run:

```sh
vh start --request "$USER_REQUEST"
```

If `vh` is not installed but this checkout is available, use
`python3 -m vibeharness.cli start --request "$USER_REQUEST"`.

Use the created `.vibeharness/episodes/...` directory as the task notebook.

## Recovery Trigger

Escalate to VibeHarness recovery when:

- the user manually runs a command;
- the user manually verifies UI/API behavior;
- the user clarifies acceptance criteria after an incorrect patch;
- tests pass but the user-visible behavior is wrong;
- environment setup loops;
- review feedback reveals a missing recurring rule.

## Recovery Protocol

1. Record the intervention.
2. Write a decision contract before changing harness artifacts.
3. Keep harness edits separate from product-code edits.
4. Roll back product code to the original checkpoint when replay is required.
5. Replay the original request with the repaired harness.
6. Audit permissions and information boundaries.
7. Score the episode.

## Useful Commands

- `/vh-start <request>` creates an episode.
- `/vh-recovery` guides a harness repair.
- `/vh-audit <episode>` audits and scores an episode.
