# 验证

[English](verification.md) | 简体中文

VibeHarness 把验证视为产品的一部分，而不是最后的清理步骤。一个 workflow 只有在新贡献者 clone 仓库后能用一个命令判断健康状态时，才真正可维护。

## 主命令

```sh
make validate
```

等价的 CLI 命令是：

```sh
vh validate
```

如果直接从 checkout 使用、没有安装 CLI，也可以运行：

```sh
python3 -m vibeharness.cli validate
```

它会运行：

- benchmark manifest validation；
- i18n status validation；
- 本地 Markdown link checking；
- packaged `vh init` asset sync checking；
- skill distribution 和 install smoke testing；
- Codex adapter smoke testing：在临时 git repository 中通过 `AGENTS.md`、
  `vh init`、episode creation 和 scoring 验证；
- Codex、Claude Code、Cursor 和 OpenHands 的 adapter surface checks，并在
  临时目标仓库中检查 `vh init` output；
- executable fixture tests；
- 脱敏 example episode scoring；
- bundled episode-set scoring；
- example evaluation report generation；
- executable ablation report generation。

## 示例命令

```sh
make example
```

它只运行 todo CLI fixture 和 example episode scorecard。修改 example 文件时使用这个命令。

## Episodes 命令

```sh
make episodes
```

等价 CLI 形式：

```sh
vh episodes examples/episodes
python3 -m vibeharness.cli episodes examples/episodes
```

它会评分给定路径下的每个 episode directory。

## 报告命令

```sh
make report
```

等价 CLI 形式：

```sh
vh report
python3 -m vibeharness.cli report
```

它会运行所有内置 executable examples，并写入：

- `reports/example_evaluation.json`
- `reports/example_evaluation.md`

## Ablation 命令

```sh
make ablation
```

等价 CLI 形式：

```sh
vh ablation
python3 -m vibeharness.cli ablation
```

它会运行内置 gap probes，并写入：

- `reports/ablation_evaluation.json`
- `reports/ablation_evaluation.md`

## 论文命令

```sh
make paper
```

它用 `tectonic` 编译论文草稿。论文编译故意不放进普通 CI，因为开源 workflow 不应该要求普通贡献者安装 TeX。

## 成功意味着什么

`make validate` 应该证明：

- task manifests 结构合法；
- 双语文档状态被追踪；
- 仓库内 Markdown 链接可解析；
- packaged `vh init` templates 与 source files 保持一致；
- skill-first install 路径可以写入本地 Codex/Claude-style skills 目录；
- Codex adapter 可以 bootstrap 目标仓库、创建 episode 并完成 scoring，且不依赖 repository-local helper scripts；
- 所有支持的 adapters 都暴露同一套轻量 method contract，且不会把本仓库的 helper scripts 硬编码进初始化后的目标仓库；
- executable fixture 仍然可运行；
- 内置 example episodes 的 primary scores 通过；
- 内置 examples 能生成 evaluation report；
- visible-only checks 可以通过，而 gap probes 会失败；repaired harness 路径能在内置 ablations 上 replay 成功。

它不证明研究主张。研究主张仍然需要真实或现实化 episodes、baselines，以及 `docs/evaluation.md` 中描述的 intervention-reduction measurements。
