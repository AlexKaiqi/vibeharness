# 发表策略

[English](publication_strategy.md) | 简体中文

## 简短结论

VibeHarness 值得发表，但前提是它作为一个可运行系统或 benchmark 被评估。只作为概念论文风险很高，因为 harness engineering、agent recovery、coding-agent benchmark 都已经是活跃方向。

最强路线是：

1. 先开源 workflow 和 tooling；
2. 收集真实 intervention episodes；
3. 证明重复人类干预确实下降；
4. 再发布 dataset、benchmark protocol 和实证结果。

## 什么内容值得发表

论文变得有价值，需要能主张：

- 一个开源、agent-agnostic 的 harness recovery runtime；
- 适配多个真实 coding-agent 工具；
- 一组真实或现实化的 user-intervention episodes；
- harness recovery 前后重复干预下降的证据；
- 从 clean checkpoint replay 的证据；
- safety 和 information-flow audit 结果；
- 跨 task group 的 transfer 结果。

## 什么还不够

下面这些不足以支撑强论文：

- 只是说 harness 很重要；
- 只在 prose 中提出 checkpoint/rollback；
- 又做一个没有 executable fixtures 的 benchmark；
- 只有 anecdotal examples；
- 只报告 final task pass rate，没有 replay 或 intervention metrics。

## 最低发表门槛

arXiv 或会议投稿前，建议至少做到：

- 20-50 个 executable episodes；
- 3-5 个 failure classes；
- 至少 3 个 baselines；
- 重复运行并报告 confidence intervals；
- 明确 prior-art positioning；
- 公开代码和脱敏 example episodes；
- 清楚说明 limits 和 failure cases。

## 最佳定位

不要把 VibeHarness 表述为：

> 我们发明了 harness engineering。

应该表述为：

> 我们把 intervention-driven harness recovery 工程化：当人类介入暴露 harness gap 时，系统记录证据、写 decision contract、修复 harness、回滚 product code、重放原始任务，并评估未来人类干预是否下降。

## 可能投稿方向

有实证结果后，比较适合：

- AI-assisted development 相关的软件工程会议和 workshop；
- agent evaluation workshop；
- systems/tooling track；
- 配合开源发布的 arXiv 技术报告。

开源项目可以先于论文发布。事实上，项目产生的使用数据很可能正是论文可信度的来源。
