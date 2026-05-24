# 示例结果

[English](example_results.md) | 简体中文

本页记录当前内置 examples 的评估结果。它不是研究结果；它只证明开源 examples 可执行，并且 scorecard pipeline 能跑通。

## 当前内置 Examples

| Example | Failure class | Fixture | Episode |
| --- | --- | --- | --- |
| `todo_cli_spec_capture` | `spec_capture` | pass | pass |
| `env_bootstrap_notes` | `environment_bootstrap` | pass | pass |
| `ui_snapshot_tasks` | `tool_affordance` | pass | pass |

## Summary

- examples: 3
- fixture pass rate: 1.00
- episode primary pass rate: 1.00
- ablation visible-only pass rate: 1.00
- ablation gap-probe failure rate: 1.00
- ablation replay pass rate: 1.00
- ablation recovered-gap rate: 1.00

## Ablation Results

| Example | Failure class | Visible-only | Gap probe | Replay | Recovered |
| --- | --- | --- | --- | --- | --- |
| `todo_cli_spec_capture` | `spec_capture` | pass | exposed | pass | pass |
| `env_bootstrap_notes` | `environment_bootstrap` | pass | exposed | pass | pass |
| `ui_snapshot_tasks` | `tool_affordance` | pass | exposed | pass | pass |

## 复现

```sh
make report
make ablation
```

它会在 `reports/` 下写入本地生成报告。`reports/` 已被 git 忽略。

## 解读

examples 覆盖三个 recovery classes：

- `spec_capture`：用户澄清被转化为持久 acceptance criteria 和 acceptance test。
- `environment_bootstrap`：手动 export 环境变量被转化为可复用 harness bootstrap script。
- `tool_affordance`：手动 UI 检查被转化为机器可读 snapshot validation。

这些 examples 不证明 VibeHarness 能在真实项目中减少干预。这个主张仍然需要真实或现实化 intervention episodes、baselines，以及 `docs/evaluation.md` 中的评估计划。

ablation report 只证明内置 examples 上的一个更窄主张：visible-only checks 可能漏掉 harness gap，gap probe 能暴露它，而 repaired harness 路径可以成功 replay。
