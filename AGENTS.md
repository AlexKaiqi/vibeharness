# VibeHarness Agent Instructions

Use this repository as a VibeHarness-enabled workspace.

## Default Workflow

For non-trivial implementation, debugging, or evaluation tasks:

1. Inspect `git status --short` and identify unrelated user changes.
2. Create an episode with:
   `python3 scripts/vh_start.py --request "<user request>"`
3. Treat the generated episode directory as the run log.
4. Implement the task using the repository's normal commands.
5. Record tests, interventions, and final scorecard in the episode.

## When the User Intervenes

If the user manually runs a command, validates UI/API behavior, clarifies missed
acceptance criteria, or points out a repeated failure, do not only patch the
symptom.

Instead:

1. record the intervention in `intervention_log.md`;
2. classify the harness gap;
3. write `decision_contract.md` before editing harness files;
4. edit only allowed harness artifacts;
5. roll product code back to the checkpoint when recovery mode is required;
6. replay the original request;
7. fill `scorecard.json` and run `python3 scripts/vh_score_episode.py <episode>`.

## Harness vs Product Code

Harness artifacts include setup scripts, agent instructions, validation commands,
browser/log/metric adapters, acceptance tests, memory, permissions, and review
protocols.

Do not hide an application fix inside a harness edit.

## Verification

Prefer this order:

1. visible deterministic checks;
2. behavior-level checks that exercise the user workflow;
3. replay from the original checkpoint when a harness failure was repaired;
4. trajectory audit for permissions, information flow, and scope creep.

## Safety

Never expose hidden-check implementation to worker prompts. Do not access
production services, secrets, or broad internet resources unless the task and
policy explicitly allow it.
