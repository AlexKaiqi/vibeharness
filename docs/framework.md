# VibeHarness Framework

VibeHarness is an intervention-driven harness recovery loop for coding agents.
It treats a user intervention as a structured signal about the model-harness-
environment system, not as an isolated hint for the current patch.

## Design Principles Absorbed from Prior Work

VibeHarness intentionally borrows the strongest parts of recent harness work:

- From Agentic Harness Engineering: every editable harness component should be
  explicit, revertible, and linked to a falsifiable prediction.
- From AgentFlow: multi-agent orchestration should be represented as a typed
  graph of roles, tools, message channels, and coordination protocols.
- From Code as Agent Harness: harness artifacts should be executable,
  inspectable, stateful, and usable by agents as first-class project substrate.
- From OpenAI's Codex harness report: app state, browser behavior, logs,
  metrics, and review feedback should be made directly readable to agents.
- From AI Harness Engineering: harnesses should cover task specification,
  context selection, tool access, memory, task state, observability, attribution,
  verification, permissions, entropy auditing, and intervention recording.
- From HarnessAudit: final task success is insufficient; full trajectories must
  respect permissions, information boundaries, and execution fidelity.
- From SWE-bench critiques: hidden checks must avoid narrow/wide-test traps, and
  benchmark tasks need replayability, contamination awareness, and behavioral
  validation beyond a single patch pass.

## Core Loop

1. `checkpoint`: snapshot the repository, harness, dependency state, and
   supervisor configuration before the task begins.
2. `delegate`: assign the user request to one or more worker agents through a
   typed coordination graph.
3. `observe`: collect an episode package containing tool traces, test output,
   app/browser observations, logs, user interventions, and state transitions.
4. `attribute`: classify whether the failure is application logic, harness
   capability, coordination, permission, or benchmark ambiguity.
5. `contract`: before changing the harness, write a decision contract: the
   hypothesized cause, intended harness edit, expected effect, and falsification
   check.
6. `repair`: edit only allowed harness artifacts, such as bootstrap scripts,
   browser tools, acceptance tests, memory, routing, review protocol, or
   permission policy.
7. `rollback`: return task code to the original checkpoint while retaining the
   candidate harness repair in the controlled harness layer.
8. `replay`: rerun the original user request from the checkpoint.
9. `audit`: score task correctness, replay success, intervention absorption,
   attribution quality, trajectory safety, and transfer.

## Harness Component Model

Each task and harness edit should identify affected components:

- `task_specification`: user request, acceptance criteria, and clarifications.
- `context_selection`: repository files, docs, traces, and memories surfaced to
  the agent.
- `tool_access`: tools exposed to the worker, including shell, browser,
  observability, search, and testing.
- `project_memory`: durable facts learned from previous tasks.
- `task_state`: current plan, assumptions, blockers, and checkpoint identity.
- `observability`: trace, log, metric, screenshot, DOM, and test-output capture.
- `failure_attribution`: rules or models used to connect symptoms to causes.
- `verification`: visible checks, hidden checks, replay checks, and behavioral
  differential tests.
- `permissions`: allowed operations, file scopes, secrets, network boundaries,
  and human-escalation gates.
- `entropy_auditing`: detection of scope creep, stale state, unnecessary edits,
  and drift from the original request.
- `intervention_recording`: structured capture of human commands, comments,
  screenshots, clarifications, and manual validations.
- `coordination`: role graph, message schemas, review routing, and handoff
  protocol.

## Typed Coordination Graph

The minimal VibeHarness graph contains:

- `supervisor`: owns checkpoints, attribution, harness edits, and replay.
- `worker`: implements the user request using the current harness.
- `critic`: reviews task output and validates whether the user request is met.
- `harness_editor`: modifies allowed harness artifacts after a decision
  contract is written.
- `auditor`: checks replay evidence, permission boundaries, and intervention
  absorption.

Edges must declare:

- message type;
- allowed artifacts;
- tool permissions;
- whether information can flow from hidden validation into the worker context;
- termination criteria.

## Episode Package

Every run should produce an auditable episode package:

- initial checkpoint id;
- harness version id;
- user request and clarifications;
- role graph used for the run;
- tool calls and tool outputs;
- tests and verification reports;
- app/browser/log/metric observations;
- human interventions and their timestamps;
- supervisor attribution;
- decision contract;
- harness diff;
- rollback and replay proof;
- permission and information-flow audit;
- final scoring report.

This package is the unit of scientific evidence. A result that cannot produce an
episode package should not count as benchmark success.

## Maturity Ladder

- `VH0`: ordinary single-agent vibe coding; no checkpointed recovery.
- `VH1`: checkpoint and replay exist, but interventions are only logged.
- `VH2`: interventions are converted into harness edits with decision contracts.
- `VH3`: replay from the original checkpoint is required for success.
- `VH4`: harness repairs transfer to held-out tasks and pass trajectory audits.

The paper should evaluate systems by maturity level rather than only by pass
rate.
