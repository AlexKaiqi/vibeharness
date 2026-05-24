# VibeHarnessBench

VibeHarnessBench evaluates whether an agentic coding workflow can transform
human intervention into durable harness improvement.

Most coding benchmarks score whether the final patch passes tests. This benchmark
adds a second-order requirement: when the agent fails because its harness lacks a
capability, a supervisor must diagnose the harness problem, patch the harness,
roll back to the original checkpoint, and replay the user task successfully.

## Task Unit

Each task is a small repository fixture plus a manifest:

- `task_id`: stable task identifier.
- `repo`: repository source and checkout revision.
- `transfer_group`: group used to test whether a repaired harness component
  transfers to related tasks.
- `user_request`: natural-language request shown to the worker agent.
- `harness_gap`: the intentionally exposed harness weakness.
- `harness_components`: runtime substrate components implicated in the failure.
- `observability`: component, trajectory, and decision signals required for
  attribution.
- `intervention_trace`: evidence that a human or tool intervention was needed.
- `decision_contract`: supervisor prediction before any harness edit.
- `safety_constraints`: permissions and information-flow boundaries for the
  run.
- `allowed_harness_edits`: files or configuration the supervisor may change.
- `forbidden_solution_edits`: files that must not be edited as a shortcut.
- `visible_checks`: checks the agent may run.
- `hidden_checks`: checks used for final scoring.
- `replay_protocol`: how to reset and replay from the checkpoint.
- `episode_package`: artifacts required to audit the run.

## Runtime Component Model

Tasks name the harness components implicated by the failure:

- `task_specification`: request, clarifications, and acceptance criteria.
- `context_selection`: source files, docs, and traces exposed to the agent.
- `tool_access`: shell, browser, logs, metrics, test, and search affordances.
- `project_memory`: durable learned facts that can transfer across tasks.
- `task_state`: checkpoints, assumptions, blockers, and current plan.
- `observability`: traces, logs, screenshots, DOM snapshots, and test output.
- `failure_attribution`: reasoning from symptoms to harness or task cause.
- `verification`: visible, hidden, replay, and behavioral checks.
- `permissions`: allowed files, tools, services, secrets, and escalation gates.
- `entropy_auditing`: detection of scope creep and irrelevant local state.
- `intervention_recording`: structured user commands, comments, screenshots,
  and manual validations.
- `coordination`: multi-agent role graph and handoff protocol.

## Failure Taxonomy

The initial taxonomy is deliberately practical:

- `environment_bootstrap`: the task fails because dependencies, services,
  ports, secrets, or setup scripts are not represented in the harness.
- `tool_affordance`: the agent lacks a usable tool path, such as browser
  automation, log querying, screenshots, or structured test output.
- `verification_blind_spot`: visible tests pass, but the user-visible behavior
  or hidden regression path fails.
- `state_drift`: the worker accumulates irrelevant edits, stale assumptions, or
  local state that should be discarded through checkpoint rollback.
- `spec_capture`: the user clarifies intent mid-run, but the clarification is
  not converted into durable acceptance criteria.
- `coordination_breakdown`: multi-agent review, ownership, or feedback routing
  fails even though a single local fix is straightforward.

## Metrics

- `task_pass`: hidden task validation passes after final replay.
- `harness_replay_pass`: the same task passes from the original checkpoint using
  the repaired harness without fresh human intervention.
- `intervention_absorption_rate`: fraction of intervention facts converted into
  durable harness artifacts.
- `attribution_accuracy`: whether the supervisor identifies the correct harness
  failure class.
- `regression_free_rate`: unrelated visible and hidden checks remain green.
- `human_interrupt_count`: number of required human interventions.
- `rollback_efficiency`: number of rollbacks and wasted edit distance before
  successful replay.
- `transfer_gain`: improvement when the repaired harness is reused on held-out
  tasks from the same failure class.
- `decision_contract_pass`: whether the predicted effect of a harness edit is
  borne out by replay evidence.
- `trajectory_safety_pass`: whether the successful run respects permissions and
  information-flow boundaries.
- `episode_completeness`: whether the run produces all required auditable
  artifacts.

## Baselines

Recommended baselines:

- `single_agent`: worker runs the task once with no checkpoint recovery.
- `single_agent_retry`: worker retries after failure, but cannot edit the
  harness.
- `multi_agent_review`: worker plus reviewer, no explicit harness repair.
- `supervisor_no_replay`: supervisor may edit the harness but does not replay
  from the original checkpoint.
- `supervisor_no_contract`: supervisor may edit and replay but does not write a
  falsifiable decision contract before editing.
- `supervisor_no_audit`: supervisor may edit and replay but trajectory safety is
  not audited.
- `vibeharness`: checkpoint, observe, repair harness, rollback, replay, verify.

## Data Collection Guidance

Good tasks should come from real or realistic traces where:

1. the worker's code ability was not the main blocker;
2. a human intervention unblocked the session;
3. the intervention can be represented as a harness artifact;
4. the task can be reset and replayed deterministically;
5. the final score cannot be won by hard-coding the application patch;
6. the episode package can be generated without exposing hidden checks to the
   worker.
