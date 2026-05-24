# Episode Collection

[English](episode_collection.md) | 简体中文

VibeHarness 把 episode 视为最小可发表证据单位。一个主张应由可 replay 的 episodes 支撑，而不只是 final patch 或 conversation summary。

## Minimum Episode Artifacts

每个可公开 episode 必须包含：

- `manifest.json`：task metadata、checkpoint id、mode、fixture 或 repository source，以及 harness version。
- `request.md`：原始用户请求和 durable acceptance criteria。
- `intervention_log.md`：带 timestamps 和 material facts 的 human 或 tool interventions。
- `decision_contract.md`：pre-edit attribution、计划的 harness repair、expected effect 和 falsification check。
- `audit.md`：permissions、information boundaries、entropy 和 trajectory safety notes。
- `scorecard.json`：primary score fields 和 diagnostic scores。

使用：

```sh
vh start --request "original user request"
vh score .vibeharness/episodes/<id>
vh episodes .vibeharness/episodes
```

新建 episode 的 template scorecard 默认不通过。只有在 intervention log、decision contract、audit 和 replay evidence 填完整之后，它才应该通过。

## Sanitization Rules

公开 episode 前：

- 替换 private repository names、user names、customer names、internal URLs、secrets、tokens 和 production resource identifiers；
- 保留 failure class、intervention facts、decision contract、command shape 和 replay evidence；
- 保留足够 logs 以 audit attribution，但删除无关 local paths 和 machine-specific noise；
- 不要把 hidden checks 暴露到 worker transcript；
- 记录任何会改变读者推断的 redaction。

## Inclusion Criteria

只有满足以下条件的 episode 才适合进入 benchmark：

- blocker 主要是 harness gap，而不是缺少 domain knowledge 或一次性 product decision；
- intervention 可以转化为 durable harness artifact；
- task 可以 deterministic reset 和 replay；
- harness repair 没有 hard-code application solution；
- safety 和 information-flow boundaries 可以被 audit。

## Dataset Splits

使用三组数据：

- `examples`：提交到仓库的小型 executable fixtures。
- `sanitized_real`：真实 traces，移除 private details。
- `held_out_transfer`：只用于测试 harness repairs 是否迁移的 tasks。

不要在 held-out transfer tasks 上调 harness instructions。

## Reporting

每个 dataset split 应报告：

- episode count；
- primary pass rate；
- replay pass rate；
- intervention absorption rate；
- attribution accuracy；
- trajectory safety pass rate；
- human interrupt count；
- transfer gain when applicable。

本地 smoke checks：

```sh
make episodes
make report
make ablation
```
