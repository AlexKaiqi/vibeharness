# Decision Contract

## Failure Class

`spec_capture`

## Harness Components

- `task_specification`
- `verification`
- `intervention_recording`

## Evidence

- The original request used the ambiguous phrase "friendlier".
- The visible test only checked that both task titles were printed.
- The user clarified ordering and markers after the first attempt.

## Hypothesis

The failure occurred because the harness did not convert a vague product phrase
into durable acceptance criteria before implementation.

## Harness Edit Scope

- Allowed: acceptance criteria, fixture acceptance tests, episode scorecard.
- Forbidden: hidden checks leaked into worker prompts, unrelated CLI behavior.

## Expected Effect

After adding a durable acceptance test, replaying the original request should
lead to output that puts open tasks first and marks completed tasks with `[x]`
without asking the user to repeat the clarification.

## Falsification Check

Replay fails if `python3 tests/test_acceptance.py` fails or if the user must
clarify the same output semantics again.

## Replay Plan

1. Reset product code to the checkpoint.
2. Keep the acceptance criteria and test as harness artifacts.
3. Replay the original request.
4. Run visible and acceptance checks.
