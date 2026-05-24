# VibeHarnessBench

[English](README.md) | 简体中文

VibeHarnessBench 评估一个 agentic coding workflow 是否能把 human intervention 转化为 durable harness improvement。

大多数 coding benchmark 只评估最终 patch 是否通过测试。这个 benchmark 增加了二阶要求：当 agent 因为 harness 缺少某种能力而失败时，supervisor 必须诊断 harness 问题、patch harness、回滚到原始 checkpoint，并成功 replay 用户任务。

## Task Unit

每个 task 是一个小型 repository fixture 加 manifest：

- `task_id`：稳定 task identifier。
- `repo`：repository source 和 checkout revision。
- `transfer_group`：用于测试 repaired harness component 是否能迁移到相关 tasks 的分组。
- `user_request`：展示给 worker agent 的自然语言请求。
- `harness_gap`：故意暴露的 harness weakness。
- `harness_components`：失败涉及的 runtime substrate components。
- `observability`：attribution 所需的 component、trajectory 和 decision signals。
- `intervention_trace`：human 或 tool intervention 曾经必要的证据。
- `decision_contract`：任何 harness edit 之前的 supervisor prediction。
- `safety_constraints`：run 的 permissions 和 information-flow boundaries。
- `allowed_harness_edits`：supervisor 可以修改的文件或配置。
- `forbidden_solution_edits`：不能作为 shortcut 修改的文件。
- `visible_checks`：agent 可以运行的 checks。
- `hidden_checks`：最终 scoring 使用的 checks。
- `replay_protocol`：如何 reset 并从 checkpoint replay。
- `episode_package`：audit run 所需的 artifacts。

## Runtime Component Model

Tasks 会标注失败涉及的 harness components：

- `task_specification`：request、clarifications 和 acceptance criteria。
- `context_selection`：暴露给 agent 的 source files、docs 和 traces。
- `tool_access`：shell、browser、logs、metrics、test 和 search affordances。
- `project_memory`：可以跨任务迁移的 durable learned facts。
- `task_state`：checkpoints、assumptions、blockers 和 current plan。
- `observability`：traces、logs、screenshots、DOM snapshots 和 test output。
- `failure_attribution`：从 symptoms 推断 harness 或 task cause。
- `verification`：visible、hidden、replay 和 behavioral checks。
- `permissions`：allowed files、tools、services、secrets 和 escalation gates。
- `entropy_auditing`：检测 scope creep 和 irrelevant local state。
- `intervention_recording`：结构化记录 user commands、comments、screenshots 和 manual validations。
- `coordination`：multi-agent role graph 和 handoff protocol。

## Failure Taxonomy

初始 taxonomy 故意保持实用：

- `environment_bootstrap`：任务失败是因为 dependencies、services、ports、secrets 或 setup scripts 没有被 harness 表达。
- `tool_affordance`：agent 缺少可用 tool path，例如 browser automation、log querying、screenshots 或 structured test output。
- `verification_blind_spot`：visible tests 通过，但 user-visible behavior 或 hidden regression path 失败。
- `state_drift`：worker 积累了 irrelevant edits、stale assumptions 或应通过 checkpoint rollback 丢弃的 local state。
- `spec_capture`：用户在 run 中澄清意图，但 clarification 没有转成 durable acceptance criteria。
- `coordination_breakdown`：multi-agent review、ownership 或 feedback routing 失败，尽管单个 local fix 很直接。

## Metrics

- `task_pass`：最终 replay 之后 hidden task validation 通过。
- `harness_replay_pass`：使用 repaired harness、没有新的 human intervention 时，同一任务能从原始 checkpoint 通过。
- `intervention_absorption_rate`：intervention facts 中被转成 durable harness artifacts 的比例。
- `attribution_accuracy`：supervisor 是否识别出正确 harness failure class。
- `regression_free_rate`：无关 visible 和 hidden checks 是否保持绿色。
- `human_interrupt_count`：所需 human interventions 数量。
- `rollback_efficiency`：成功 replay 前的 rollbacks 数量和 wasted edit distance。
- `transfer_gain`：repaired harness 被复用于同类 held-out tasks 时带来的改进。
- `decision_contract_pass`：harness edit 的预测效果是否被 replay evidence 证实。
- `trajectory_safety_pass`：成功 run 是否尊重 permissions 和 information-flow boundaries。
- `episode_completeness`：run 是否产生全部 required auditable artifacts。

## Baselines

推荐 baselines：

- `single_agent`：worker 单次运行任务，没有 checkpoint recovery。
- `single_agent_retry`：worker 失败后重试，但不能编辑 harness。
- `multi_agent_review`：worker 加 reviewer，没有显式 harness repair。
- `supervisor_no_replay`：supervisor 可以编辑 harness，但不从原始 checkpoint replay。
- `supervisor_no_contract`：supervisor 可以编辑并 replay，但编辑前不写 falsifiable decision contract。
- `supervisor_no_audit`：supervisor 可以编辑并 replay，但不 audit trajectory safety。
- `vibeharness`：checkpoint、observe、repair harness、rollback、replay、verify。

## Data Collection Guidance

好的 tasks 应来自真实或现实化 traces，并满足：

1. worker 的代码能力不是主要 blocker；
2. human intervention 曾经 unblock session；
3. intervention 可以被表示为 harness artifact；
4. task 可以 deterministic reset 并 replay；
5. final score 不能通过 hard-code application patch 获得；
6. episode package 可以生成，且不把 hidden checks 暴露给 worker。
