# Research Memo: Vibe Harness Instead of the Problem

Date: 2026-05-24

## Short Verdict

The broad idea has been partially preempted. "Agent harness engineering" is now
an active research direction, and several 2026 papers already argue that the
harness around a model is a major determinant of coding-agent success.

The narrower idea still has publishable potential if framed as:

> intervention-driven harness recovery for interactive vibe-coding workflows.

The paper should not claim that it introduces harness engineering. It should
claim that existing evaluations do not adequately measure whether a system can
turn human interventions into durable, replayable harness improvements.

## Closest Prior Work

- OpenAI, "Harness engineering: leveraging Codex in an agent-first world"
  (2026-02-11). This is a strong industry precedent for treating missing agent
  capability as a harness problem.
  https://openai.com/index/harness-engineering/
- Lin et al., "Agentic Harness Engineering: Observability-Driven Automatic
  Evolution of Coding-Agent Harnesses" (arXiv:2604.25850). This is the closest
  academic overlap: autonomous harness evolution with component, experience, and
  decision observability.
  https://arxiv.org/abs/2604.25850
- Ning et al., "Code as Agent Harness" (arXiv:2605.18747). This is a broad
  survey that frames code as the substrate for executable, verifiable, stateful
  agents.
  https://arxiv.org/abs/2605.18747
- Liu et al., "Synthesizing Multi-Agent Harnesses for Vulnerability Discovery"
  (arXiv:2604.20801). This covers multi-agent harness synthesis in a security
  domain.
  https://arxiv.org/abs/2604.20801
- Rahardja et al., "Can Agents Fix Agent Issues?" (arXiv:2505.20749). This
  benchmarks agents fixing agent-system issues, but not intervention replay.
  https://arxiv.org/abs/2505.20749
- Zhong and Zhu, "AI Harness Engineering: A Runtime Substrate for
  Foundation-Model Software Agents" (arXiv:2605.13357). This is very relevant
  for its list of harness responsibilities: task specification, context
  selection, tool access, memory, task state, observability, attribution,
  verification, permissions, entropy auditing, and intervention recording.
  https://arxiv.org/abs/2605.13357
- Liu et al., "Auditing Agent Harness Safety" (arXiv:2605.14271). This adds an
  important safety constraint: final task success can hide trajectory-level
  permission or information-flow violations.
  https://arxiv.org/abs/2605.14271
- Pan et al., "Natural-Language Agent Harnesses" (arXiv:2603.25723). This is
  directly relevant because it treats harness policy as an executable
  natural-language artifact rather than hidden controller code.
  https://arxiv.org/abs/2603.25723
- Nanda et al., "Wink: Recovering from Misbehaviors in Coding Agents"
  (arXiv:2602.17037). This is the closest recovery-system neighbor: it studies
  production coding-agent misbehaviors and interventions at scale.
  https://arxiv.org/abs/2602.17037
- Ursekar et al., "VeRO: An Evaluation Harness for Agents to Optimize Agents"
  (arXiv:2602.22480). This informs the versioning, rewards, observations, and
  structured trace side of the evaluation design.
  https://arxiv.org/abs/2602.22480

## Adjacent Benchmark Work

- SWE-bench established real GitHub issue solving.
  https://arxiv.org/abs/2310.06770
- OpenAI later reported that SWE-bench Verified no longer measures frontier
  coding capabilities well because of flawed tests and contamination.
  https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- FeatBench evaluates natural-language feature implementation.
  https://arxiv.org/abs/2509.22237
- SUSVIBES evaluates security of vibe-coded feature requests.
  https://arxiv.org/abs/2512.03262
- SWE-WebDevBench evaluates AI app builders as virtual software agencies.
  https://arxiv.org/abs/2605.04637
- Saving SWE-Bench mutates formal benchmark tasks into realistic chat-style
  user queries.
  https://arxiv.org/abs/2510.08996
- Vibe Code Bench evaluates end-to-end web application development with
  browser-based workflows and human-aligned evaluators.
  https://arxiv.org/abs/2603.04601

## Novelty Gap

Existing work mostly evaluates one of three things:

1. Can the agent solve the software task?
2. Can the harness be optimized from trajectories?
3. Can agent systems themselves be repaired?

The proposed gap is different:

1. The user intervenes during an interactive coding session.
2. That intervention reveals a missing harness capability.
3. The system must repair the harness, roll back the task, and replay from the
   original checkpoint.
4. Success requires task completion, no repeat intervention, and an auditable
   trajectory that respects permissions and information-flow boundaries.

This makes the contribution concrete and defensible.

## Recommended Paper Shape

Best target framing:

- Title family: "Harnessing the Vibe" or "VibeHarness".
- Type: benchmark + method + empirical study.
- Primary category: `cs.SE`.
- Secondary categories: `cs.AI`, `cs.CL`.

Avoid:

- A pure position paper saying "harness matters".
- A survey of harness engineering.
- A claim that a skill alone is the research contribution.

Need before arXiv:

- At least 20 executable tasks.
- At least 3 baselines.
- Repeated runs with confidence intervals.
- Clear hidden checks and replay protocol.
- No fabricated or anecdotal-only results.

## Minimum Viable Experiment

Start with 24 tasks:

- 4 failure classes.
- 6 tasks per class.
- 12 synthetic fixtures, 12 real trace-derived fixtures.

Run:

- single agent;
- single agent with retry;
- worker plus reviewer;
- VibeHarness supervisor with checkpoint, harness repair, rollback, replay.

Report:

- VH-score;
- task pass;
- replay pass;
- human interruptions;
- token cost;
- per-class attribution accuracy;
- trajectory safety and permission-boundary violations;
- transfer gain from each repaired harness component.

## Publication Risk

Risk is medium-high if the work remains conceptual because several close papers
appeared in April and May 2026. Risk becomes much lower if the project releases
a benchmark and shows empirical results on intervention-driven replay, because
that exact scoring target is still a crisp gap.
