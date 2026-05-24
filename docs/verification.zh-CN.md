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

它会运行：

- benchmark manifest validation；
- i18n status validation；
- 本地 Markdown link checking；
- executable fixture tests；
- 脱敏 example episode scoring；
- example evaluation report generation。

## 示例命令

```sh
make example
```

它只运行 todo CLI fixture 和 example episode scorecard。修改 example 文件时使用这个命令。

## 报告命令

```sh
make report
```

它会运行所有内置 executable examples，并写入：

- `reports/example_evaluation.json`
- `reports/example_evaluation.md`

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
- executable fixture 仍然可运行；
- example episode 的 primary score 通过；
- 内置 examples 能生成 evaluation report。

它不证明研究主张。研究主张仍然需要真实或现实化 episodes、baselines，以及 `docs/evaluation.md` 中描述的 intervention-reduction measurements。
