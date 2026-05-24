# 实用评估方案

[English](evaluation.md) | 简体中文

VibeHarness 应该作为工程工作流评估。关键问题不是“论文听起来是否新颖”，而是“团队是否需要更少人工干预，并交付更多经过验证的变更”。

## 评估层级

### Level 0: Episode Completeness

目标：确保流程可观察。

指标：

- 非平凡任务中有 episode 的比例；
- 有 checkpoint id 的比例；
- 记录 visible checks 的比例；
- 有 final scorecard 的比例。

通过标准：被纳入流程的任务达到 90% episode completeness。

### Level 1: Task Reliability

目标：衡量普通生产力。

指标：

- task pass rate；
- visible check pass rate；
- hidden/review failure rate；
- time to first correct patch；
- token 和 wall-clock cost。

通过标准：不低于团队当前 agent workflow。

### Level 2: Intervention Reduction

目标：验证 VibeHarness 的核心价值。

指标：

- 每个任务的人类干预次数；
- 按类别统计的重复干预；
- 转化为 harness artifacts 的 intervention 比例；
- 从原始 checkpoint replay 的通过率。

通过标准：两周后 top 3 重复干预类别下降 30%。

### Level 3: Harness Transfer

目标：证明 harness repair 可以泛化。

指标：

- held-out tasks 上的 transfer-group pass rate；
- component-localization accuracy；
- decision-contract pass rate；
- 每次成功 transfer 带来的 harness growth。

通过标准：至少一个 transfer group 产生正向收益，同时不增加 trajectory-safety violations。

### Level 4: Safety and Governance

目标：确保 autonomy 没有隐藏风险。

指标：

- 未授权文件、工具、服务访问；
- hidden-check 泄漏；
- secret 或 production resource 访问；
- cross-agent information-flow violations；
- 未 review 的 harness policy changes。

通过标准：零 critical violations；所有 medium violations 都有对应 harness patch。

## Baseline Matrix

每类任务跑以下对照：

- `current_workflow`：团队当前使用 Codex/Claude/Cursor 的方式。
- `instructions_only`：只增加 AGENTS.md/CLAUDE.md/rules，没有 episode tooling。
- `vh_lite`：episode + scorecard，不强制 rollback。
- `vh_recovery`：decision contract + harness edit + rollback + replay。
- `vh_full`：recovery 加 trajectory audit 和 transfer evaluation。

## 本地可执行检查

在真实 episodes 还不足之前，仓库包含三类本地检查：

- `make report`：验证内置 fixtures 和脱敏 episode scorecards。
- `make ablation`：针对内置 recovery classes 运行 visible-only checks、gap probes 和 repaired replay checks。
- `make episodes`：评分所有内置 episode packages。

这些是 evaluation harness 的 smoke tests，不能替代真实 intervention-reduction measurements。

## 每周复盘

每周检查：

- 最常重复出现的 intervention classes；
- 没有产生 transfer 的 harness edits；
- 过度膨胀或互相矛盾的 instructions；
- 最终任务成功但 trajectory 存在风险的案例；
- 导致用户手动工作的缺失工具。

最好的 harness 不是最大的 harness。不能减少干预或改善 replay 的规则和脚本应该删除。

## 停止条件

不要把每个任务都升级到 VH-Full。只有当 intervention 可能重复出现时，才使用完整 recovery。如果问题只是一次性的产品决策，把它作为 task context 记录，而不是继续扩张 harness。
