# 已有工作与致谢

[English](prior_art.md) | 简体中文

本页收集相关工作与致谢。除非在具体概念旁明确说明来源，否则 VibeHarness 当前没有直接复用这些论文的方法、代码或 benchmark 数据。下面的 references 主要用于尊重邻近工作，并说明项目所处的上下文。

## VibeHarness 的增量价值

项目的独特价值很窄，但很具体：

- 把用户介入视为一等 harness 信号，而不是只把它当成本次 patch 的提示。
- 明确区分 product-code repair 和 harness repair。
- 修改 harness 前必须写 decision contract。
- harness recovery 后必须从原始 checkpoint rollback/replay。
- 评估未来人类干预是否下降，而不只看当前任务是否通过。
- 为 Codex、Claude Code、Cursor、OpenHands 等现有工具提供薄适配，而不是替代它们。

## 相关工作与致谢

### Harness Engineering

- OpenAI 的 Codex harness engineering report 清楚说明了 agent 可靠性依赖外层 workflow、tools、validation、browser access、observability 和 review loop。
  https://openai.com/index/harness-engineering/
- Agentic Harness Engineering 研究了 observability-driven automatic evolution of coding-agent harnesses。
  https://arxiv.org/abs/2604.25850
- AI Harness Engineering 把 harness 形式化为 runtime substrate，并列出 task specification、context selection、tool access、memory、state、observability、attribution、verification、permissions、entropy auditing、intervention recording 等职责。
  https://arxiv.org/abs/2605.13357
- Natural-Language Agent Harnesses 把 harness policy 作为可执行、可检查的自然语言 artifact。
  https://arxiv.org/abs/2603.25723
- Code as Agent Harness 综述了作为 agent harness 的可执行代码 artifacts。
  https://arxiv.org/abs/2605.18747

### Recovery 与 Agent Optimization

- Wink 研究了生产 coding-agent misbehaviors，并用轻量 self-intervention 减少 engineer interventions。
  https://arxiv.org/abs/2602.17037
- VeRO 提供 versioning、rewards、observations 和 structured execution traces，用于 agents optimizing agents。
  https://arxiv.org/abs/2602.22480
- AgentFlow 使用 typed multi-agent harnesses 做漏洞发现。
  https://arxiv.org/abs/2604.20801
- AgentIssue-Bench 研究 agents 能否修复 agent systems 本身的问题。
  https://arxiv.org/abs/2505.20749

### Benchmarks 与 Evaluation

- SWE-bench 开创了真实 repository-level issue solving 的评估方式。
  https://arxiv.org/abs/2310.06770
- OpenAI 对 SWE-bench Verified 的分析提醒我们：当 tests flawed 或 contaminated 时，final pass rate 可能不再衡量前沿 coding 能力。
  https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/
- Vibe Code Bench 用 browser-based workflows 评估端到端 web app development。
  https://arxiv.org/abs/2603.04601
- FeatBench、SUSVIBES、SWE-WebDevBench 把评估推进到更真实的 feature-level 和 app-building workflows。
  https://arxiv.org/abs/2509.22237
  https://arxiv.org/abs/2512.03262
  https://arxiv.org/abs/2605.04637
- HarnessAudit 强调 trajectory-level safety audit，而不是只评估最终输出。
  https://arxiv.org/abs/2605.14271

## 致谢

我们感谢以上工作和作者，它们让 harness、benchmark、coding-agent recovery 和 trajectory audit 这些概念足够具体，可以被进一步工程化。VibeHarness 应被理解为围绕一个反复出现的生产问题做出的工程实践：coding session 结束后，intervention evidence 往往没有被保留下来。

## 引用策略

当 VibeHarness 直接使用其他工作的概念、方法、数据集或实现时，文档应在使用处附近说明来源，而不是只放在 bibliography。产品型 artifact 可以链接到本页，作为简洁的致谢列表。
