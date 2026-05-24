# Prior Art and Acknowledgements

[English](prior_art.md) | [简体中文](prior_art.zh-CN.md)

This page collects related work and acknowledgements. VibeHarness does not
directly reuse the methods, code, or benchmark data from these papers unless a
specific source is named near the relevant concept. The references below are
included to respect neighboring work and to make the project context clear.

## What VibeHarness Adds

The distinctive value is narrow:

- It treats user intervention as a first-class harness signal, not just a hint
  for the current patch.
- It separates product-code repair from harness repair.
- It requires a decision contract before harness edits.
- It requires rollback and replay from the original checkpoint after harness
  recovery.
- It evaluates whether future human interventions decrease, not only whether the
  current task passes.
- It provides thin adapters for existing tools instead of replacing Codex,
  Claude Code, Cursor, OpenHands, or other coding agents.

## Related Work We Acknowledge

### Harness Engineering

- OpenAI's Codex harness engineering report crystallized the practical view that
  agent reliability depends on the surrounding workflow, tools, validation,
  browser access, observability, and review loop.
  https://openai.com/index/harness-engineering/
- Agentic Harness Engineering studies observability-driven automatic evolution
  of coding-agent harnesses.
  https://arxiv.org/abs/2604.25850
- AI Harness Engineering formalizes the harness as a runtime substrate with
  responsibilities such as task specification, context selection, tool access,
  memory, state, observability, attribution, verification, permissions, entropy
  auditing, and intervention recording.
  https://arxiv.org/abs/2605.13357
- Natural-Language Agent Harnesses frames harness policy as executable,
  inspectable natural-language artifacts.
  https://arxiv.org/abs/2603.25723
- Code as Agent Harness surveys executable code artifacts as agent harnesses.
  https://arxiv.org/abs/2605.18747

### Recovery and Agent Optimization

- Wink studies production coding-agent misbehaviors and lightweight
  self-intervention to reduce engineer interventions.
  https://arxiv.org/abs/2602.17037
- VeRO provides versioning, rewards, observations, and structured execution
  traces for agents optimizing agents.
  https://arxiv.org/abs/2602.22480
- AgentFlow synthesizes typed multi-agent harnesses for vulnerability discovery.
  https://arxiv.org/abs/2604.20801
- AgentIssue-Bench studies whether agents can fix issues in agent systems.
  https://arxiv.org/abs/2505.20749

### Benchmarks and Evaluation

- SWE-bench established real repository-level issue solving.
  https://arxiv.org/abs/2310.06770
- OpenAI's SWE-bench Verified analysis highlighted why final pass rate can stop
  measuring frontier coding ability when tests are flawed or contaminated.
  https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- Vibe Code Bench evaluates end-to-end web app development with browser-based
  workflows.
  https://arxiv.org/abs/2603.04601
- FeatBench, SUSVIBES, and SWE-WebDevBench push evaluation toward realistic
  feature-level and app-building workflows.
  https://arxiv.org/abs/2509.22237
  https://arxiv.org/abs/2512.03262
  https://arxiv.org/abs/2605.04637
- HarnessAudit motivates trajectory-level safety audits instead of only
  evaluating final outputs.
  https://arxiv.org/abs/2605.14271

## Thanks

We thank the authors and maintainers of the work above for making harnesses,
benchmarks, coding-agent recovery, and trajectory audit concrete enough to build
on. VibeHarness should be read as an engineering synthesis around a recurring
operational problem: intervention evidence that is often lost after a coding
session ends.

## Citation Policy

When VibeHarness directly uses a concept, method, dataset, or implementation
from another work, the documentation should name the source near that use, not
only in a bibliography. Product-facing artifacts can link to this page as a
compact acknowledgement list.
