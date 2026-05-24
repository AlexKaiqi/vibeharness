# Publication Strategy

[English](publication_strategy.md) | [简体中文](publication_strategy.zh-CN.md)

## Short Answer

VibeHarness is worth publishing only if it is evaluated as a working system or
benchmark. As a concept paper, the risk is high because harness engineering,
agent recovery, and coding-agent benchmarks are already active areas.

The strongest path is:

1. open-source the workflow and tooling;
2. collect real intervention episodes;
3. show measurable reductions in repeated human interventions;
4. publish the dataset, benchmark protocol, and empirical results.

## What Is Publishable

The paper becomes worthwhile when it can claim:

- an open-source, agent-agnostic harness recovery runtime;
- adapters for multiple real coding-agent tools;
- a dataset of real or realistic user-intervention episodes;
- before/after evidence that harness recovery reduces repeated interventions;
- replay evidence from clean checkpoints;
- safety and information-flow audit results;
- transfer results across task groups.

## What Is Not Enough

The following are not enough for a strong paper:

- saying that harnesses matter;
- proposing checkpoint/rollback in prose only;
- adding another benchmark without executable fixtures;
- showing anecdotal examples only;
- reporting final task pass rate without replay or intervention metrics.

## Minimum Paper Bar

Before arXiv or conference submission, aim for:

- 20-50 executable episodes;
- 3-5 failure classes;
- at least 3 baselines;
- repeated runs with confidence intervals;
- explicit prior-art positioning;
- public code and sanitized example episodes;
- clear limits and failure cases.

## Best Framing

Do not frame VibeHarness as:

> We invented harness engineering.

Frame it as:

> We operationalize intervention-driven harness recovery: when a human
> intervention exposes a harness gap, the system records evidence, writes a
> decision contract, repairs the harness, rolls back product code, replays the
> original task, and evaluates whether future human intervention decreases.

## Likely Venues

Good-fit venues after empirical results:

- software engineering venues and workshops focused on AI-assisted development;
- agent evaluation workshops;
- systems/tooling tracks;
- arXiv as an open technical report paired with the open-source release.

The open-source project can launch before the paper. In fact, usage data from
the project is likely what makes the paper credible.
