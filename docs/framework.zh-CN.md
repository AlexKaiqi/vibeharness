# VibeHarness Framework

[English](framework.md) | 简体中文

VibeHarness 是一个 intervention-driven harness recovery loop，面向 coding agents。它把用户介入视为关于 model-harness-environment system 的结构化信号，而不是当前 patch 的一次孤立提示。

## 从已有工作中吸收的设计原则

VibeHarness 有意吸收近期 harness 工作中最扎实的部分：

- 来自 Agentic Harness Engineering：每个可编辑 harness component 都应显式、可回滚，并关联到可证伪预测。
- 来自 AgentFlow：multi-agent orchestration 应表示为 roles、tools、message channels 和 coordination protocols 的 typed graph。
- 来自 Code as Agent Harness：harness artifacts 应可执行、可检查、有状态，并能作为 agent 的一等 project substrate。
- 来自 OpenAI 的 Codex harness report：app state、browser behavior、logs、metrics 和 review feedback 应能被 agent 直接读取。
- 来自 AI Harness Engineering：harness 应覆盖 task specification、context selection、tool access、memory、task state、observability、attribution、verification、permissions、entropy auditing 和 intervention recording。
- 来自 HarnessAudit：最终 task success 不够；完整 trajectories 必须尊重 permissions、information boundaries 和 execution fidelity。
- 来自 SWE-bench critiques：hidden checks 必须避免 narrow/wide-test traps，benchmark tasks 需要 replayability、contamination awareness，以及超越单次 patch pass 的 behavioral validation。

## Core Loop

1. `checkpoint`：在任务开始前 snapshot repository、harness、dependency state 和 supervisor configuration。
2. `delegate`：通过 typed coordination graph，把用户请求分配给一个或多个 worker agents。
3. `observe`：收集 episode package，包括 tool traces、test output、app/browser observations、logs、user interventions 和 state transitions。
4. `attribute`：判断失败来自 application logic、harness capability、coordination、permission，还是 benchmark ambiguity。
5. `contract`：在修改 harness 前写出 decision contract：假设原因、计划的 harness edit、预期效果和 falsification check。
6. `repair`：只修改允许的 harness artifacts，例如 bootstrap scripts、browser tools、acceptance tests、memory、routing、review protocol 或 permission policy。
7. `rollback`：把 task code 回到原始 checkpoint，同时在受控 harness layer 中保留 candidate harness repair。
8. `replay`：从 checkpoint 重新运行原始用户请求。
9. `audit`：评分 task correctness、replay success、intervention absorption、attribution quality、trajectory safety 和 transfer。

## Harness Component Model

每个 task 和 harness edit 都应标注受影响组件：

- `task_specification`：用户请求、acceptance criteria 和 clarifications。
- `context_selection`：暴露给 agent 的 repository files、docs、traces 和 memories。
- `tool_access`：worker 可使用的工具，包括 shell、browser、observability、search 和 testing。
- `project_memory`：从过去任务中学到的 durable facts。
- `task_state`：当前 plan、assumptions、blockers 和 checkpoint identity。
- `observability`：trace、log、metric、screenshot、DOM 和 test-output capture。
- `failure_attribution`：把 symptoms 连接到 causes 的规则或模型。
- `verification`：visible checks、hidden checks、replay checks 和 behavioral differential tests。
- `permissions`：allowed operations、file scopes、secrets、network boundaries 和 human-escalation gates。
- `entropy_auditing`：检测 scope creep、stale state、不必要 edits，以及偏离原始 request 的 drift。
- `intervention_recording`：结构化捕获 human commands、comments、screenshots、clarifications 和 manual validations。
- `coordination`：role graph、message schemas、review routing 和 handoff protocol。

## Typed Coordination Graph

最小 VibeHarness graph 包含：

- `supervisor`：负责 checkpoints、attribution、harness edits 和 replay。
- `worker`：使用当前 harness 实现用户请求。
- `critic`：review task output，并验证是否满足用户请求。
- `harness_editor`：在 decision contract 写好后修改允许的 harness artifacts。
- `auditor`：检查 replay evidence、permission boundaries 和 intervention absorption。

Edges 必须声明：

- message type；
- allowed artifacts；
- tool permissions；
- hidden validation 是否能流入 worker context；
- termination criteria。

## Episode Package

每次 run 都应产生 auditable episode package：

- initial checkpoint id；
- harness version id；
- user request and clarifications；
- role graph used for the run；
- tool calls and tool outputs；
- tests and verification reports；
- app/browser/log/metric observations；
- human interventions and their timestamps；
- supervisor attribution；
- decision contract；
- harness diff；
- rollback and replay proof；
- permission and information-flow audit；
- final scoring report。

这个 package 是科学证据的基本单位。无法产生 episode package 的结果，不应计入 benchmark success。

## Maturity Ladder

- `VH0`：普通 single-agent vibe coding；没有 checkpointed recovery。
- `VH1`：存在 checkpoint 和 replay，但 interventions 只被记录。
- `VH2`：interventions 会通过 decision contracts 转化为 harness edits。
- `VH3`：成功必须从原始 checkpoint replay。
- `VH4`：harness repairs 能迁移到 held-out tasks，并通过 trajectory audits。

论文应按 maturity level 评估系统，而不是只看 pass rate。
