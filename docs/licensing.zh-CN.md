# License 与署名

[English](licensing.md) | 简体中文

这不是法律意见。本文档只记录 VibeHarness 的开源授权意图。

## License 选择

VibeHarness 使用 Apache License, Version 2.0。

这个项目推荐使用 Apache-2.0，原因是：

- 项目主要是 tooling 和 documentation，采用率很重要；
- 实现刻意保持轻量，强专利策略不是核心价值；
- license 仍然要求保留 copyright 和 license notices；
- license 有明确的 patent grant 和 patent termination clause；
- Apache 的 `NOTICE` 机制给了我们一个实际位置，让使用者保留 attribution。

MIT 更简单，但在专利和 attribution notices 上不如 Apache-2.0 明确。GPL 或 AGPL 会强制更多开放共享，但也会增加团队把 VibeHarness 嵌入内部 agent workflow 的采用成本。

## 覆盖范围

除非文件另有说明，Apache-2.0 覆盖：

- source code 和 scripts；
- agent adapter files；
- documentation；
- example fixtures；
- benchmark specifications；
- sanitized example episodes。

未来如果加入真实数据集，且包含第三方材料、私有项目 traces 或贡献者提供的 episodes，可能需要单独的数据条款。

## 署名期待

Apache-2.0 允许商业使用、私有使用、修改和再分发，同时要求保留 copyright 和 license notices。

如果在 research、benchmarks、articles、talks 或 derivative tools 中使用 VibeHarness，请引用或致谢。本仓库提供：

- `NOTICE`：attribution notices；
- `CITATION.cff`：GitHub 和引用工具使用的 citation metadata；
- `docs/prior_art.md`：思想 lineage 和 related work。

## 它不做什么

该 license 不阻止商业使用。

该 license 不要求 derivative works 开源。

该 license 不授予 trademark rights，也不暗示 VibeHarness contributors 背书。

该 license 不替代共享 episodes 时的数据脱敏义务。
