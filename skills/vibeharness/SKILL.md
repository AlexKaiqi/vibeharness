---
name: vibeharness
description: Use when AI coding work gets stuck, a human intervention reveals missing setup, tooling, spec, tests, or verification, or a task should produce a checkpointed and replayable recovery episode. Captures interventions, separates harness edits from product edits, replays from checkpoint, scores the run, and audits the trajectory.
---

# VibeHarness

Use this skill to turn a stuck or intervention-heavy coding-agent task into a
durable harness improvement. The useful outcome is not just "the task passed";
it is "the next agent can replay the task from a clean checkpoint with less
human rescue."

## When To Use

Use VibeHarness when any of these happen:

- The agent is blocked by missing environment setup, fixtures, tools, docs,
  prompts, permissions, or acceptance criteria.
- The user has to intervene with a command, diagnosis, correction, screenshot,
  hidden requirement, or manual patch.
- A task needs supervisor-worker execution, clean rollback, replay, or an audit
  trail before the result is trusted.
- A recurring failure should become reusable project harness instead of staying
  as one-off chat knowledge.

For trivial edits, use judgment. A full episode is most useful when the failure
or intervention could plausibly recur.

## Fast Path

If the VibeHarness CLI is available:

```sh
vh init .
vh start --request "summarize the user task here"
vh score .vibeharness/episodes/<id>
vh episodes .vibeharness/episodes
```

If this repository is checked out but `vh` is not installed:

```sh
python3 -m vibeharness.cli init .
python3 -m vibeharness.cli start --request "summarize the user task here"
python3 -m vibeharness.cli score .vibeharness/episodes/<id>
```

If only this skill is installed, run the workflow manually. Create an episode
under `.vibeharness/episodes/<id>/` and record the request, intervention log,
decision contract, scorecard, and audit. For the exact portable file shape,
read `references/episode-format.md` when installed as a skill folder, or
`skills/vibeharness/references/episode-format.md` when using the repository
root copy.

## Recovery Loop

1. Preserve the starting state.
   Inspect `git status` first. Do not overwrite unrelated user changes. Create
   a checkpoint using the local project's normal git workflow, or record why a
   checkpoint was not possible.

2. Start an episode.
   Capture the user's request, visible acceptance criteria, baseline commands,
   and the initial repository state. Keep the episode in the repo so it can be
   reviewed and replayed.

3. Delegate implementation separately from supervision.
   The supervisor tracks evidence, risk, and replayability. Worker agents or
   normal implementation steps solve the product task. Do not let the worker
   silently edit harness files unless the supervisor has identified a harness
   gap.

4. Treat interventions as data.
   When the user or a tool rescues the run, log what happened, what signal was
   missing, and whether the failure was caused by product code, harness setup,
   underspecified requirements, unavailable tools, or missing verification.

5. Write a decision contract before changing the harness.
   The contract should name the observed failure, the harness gap, the proposed
   harness edit, how it will be replayed, and what evidence will count as
   success.

6. Repair only the harness gap.
   Harness edits can include setup scripts, fixtures, tests, docs, agent
   adapter instructions, templates, commands, or validation checks. Keep product
   fixes and harness fixes distinguishable in the diff and in the audit.

7. Roll back and replay.
   Return to the checkpoint or recreate the clean starting state, then rerun the
   task with the improved harness. The task is not fully absorbed until the
   replay works without the same human intervention.

8. Score and audit.
   Mark primary success only when the user task passes, the intervention is
   absorbed, replay is verified, attribution is correct, and the trajectory is
   safe. Record unresolved gaps instead of upgrading the score by optimism.

## Attribution Rules

- If the fix belongs in application code, call it a product fix.
- If the fix makes future agents more capable of running, understanding, or
  verifying the task, call it a harness fix.
- If both are needed, split them explicitly.
- Do not hide product behavior changes inside harness maintenance.
- Do not claim benchmark or empirical improvement without replay evidence.

## Final Report

When finishing a VibeHarness run, report:

- The user-visible task outcome.
- The intervention that triggered harness work, if any.
- The harness change made or the reason no harness change was justified.
- The replay and verification commands that passed.
- Remaining risks or gaps that should become future episodes.
