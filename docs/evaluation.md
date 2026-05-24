# Practical Evaluation Plan

VibeHarness should be evaluated as an engineering workflow. The question is not
"does the paper sound novel?" but "does the team need fewer interventions and
ship more verified changes?"

## Evaluation Levels

### Level 0: Episode Completeness

Goal: make sure the process is observable.

Metrics:

- percentage of non-trivial tasks with an episode;
- percentage with checkpoint id;
- percentage with visible checks recorded;
- percentage with final scorecard.

Pass bar: 90% episode completeness for instrumented tasks.

### Level 1: Task Reliability

Goal: measure ordinary productivity.

Metrics:

- task pass rate;
- visible check pass rate;
- hidden/review failure rate;
- time to first correct patch;
- token and wall-clock cost.

Pass bar: no regression versus the team's current agent workflow.

### Level 2: Intervention Reduction

Goal: test the core VibeHarness value.

Metrics:

- human interventions per task;
- repeat interventions by class;
- percentage of interventions converted into harness artifacts;
- replay pass rate from original checkpoint.

Pass bar: repeat interventions in the top three classes drop by 30% after two
weeks.

### Level 3: Harness Transfer

Goal: prove the harness repair generalizes.

Metrics:

- transfer-group pass rate on held-out tasks;
- component-localization accuracy;
- decision-contract pass rate;
- harness growth per successful transfer.

Pass bar: at least one transfer group shows positive gain without increasing
trajectory-safety violations.

### Level 4: Safety and Governance

Goal: make sure autonomy is not hiding risk.

Metrics:

- unauthorized file/tool/service access;
- hidden-check leakage;
- secret or production-resource access;
- cross-agent information-flow violations;
- unreviewed harness policy changes.

Pass bar: zero critical violations; all medium violations have a harness patch.

## Baseline Matrix

Run each task class through:

- `current_workflow`: how the team already uses Codex/Claude/Cursor.
- `instructions_only`: AGENTS.md/CLAUDE.md/rules added, no episode tooling.
- `vh_lite`: episode + scorecard, no mandatory rollback.
- `vh_recovery`: decision contract + harness edit + rollback + replay.
- `vh_full`: recovery plus trajectory audit and transfer evaluation.

## Weekly Review

Every week, review:

- top repeated intervention classes;
- harness edits that did not transfer;
- bloated or contradictory instructions;
- tasks where final success hid trajectory risk;
- missing tools that caused manual user work.

The best harness is not the largest one. Delete rules and scripts that do not
reduce interventions or improve replay.

## Stop Conditions

Do not escalate to VH-Full for every task. Use full recovery only when the
intervention is likely to recur. If an issue is a one-off product decision, log
it as task context rather than growing the harness.
