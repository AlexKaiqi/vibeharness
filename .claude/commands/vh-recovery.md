Use VibeHarness recovery for the current task.

Follow this sequence:

1. Find the current episode under `.vibeharness/episodes`.
2. Record the user/tool intervention in `intervention_log.md`.
3. Classify the harness gap and implicated components.
4. Fill `decision_contract.md` before editing harness files.
5. Edit only harness artifacts needed to prevent the repeated failure.
6. Roll back product-code changes to the episode checkpoint if replay is required.
7. Replay the original request.
8. Fill `audit.md` and `scorecard.json`.

Do not treat the intervention as merely a hint for the current patch.
