# Release Process

[English](release_process.md) | 简体中文

本文档定义 VibeHarness 的轻量 release process。

## Release Types

- `workflow preview`：可运行的开源 workflow，包含 examples 和 validation，但不声称真实世界 intervention reduction。
- `evaluation preview`：包含脱敏真实 episodes 和 baseline reports。
- `benchmark release`：包含稳定 task set、held-out transfer groups 和公开 scoring rules。

版本 `0.1.0` 是 workflow preview。

## Pre-Release Checklist

打 tag 前运行：

```sh
make sync-assets
make validate
python3 -m pip install .
vh version
vh validate
vh ablation
vh episodes examples/episodes
```

同时检查：

- `CHANGELOG.md` 和 `CHANGELOG.zh-CN.md` 已更新；
- `README.md` 和 `README.zh-CN.md` 指向当前命令；
- `docs/open_source_readiness.md` 反映已知限制；
- 除非明确需要，否则不要提交 generated reports 和 build artifacts；
- committed episodes 中没有 hidden checks、secrets、customer data 或 private paths。

## Tagging

使用 annotated tags：

```sh
git tag -a v0.1.0 -m "VibeHarness v0.1.0"
git push origin main
git push origin v0.1.0
```

在脱敏真实 episodes 和 baseline reports 可用前，不要给 evaluation preview 打 tag。

## Release Notes Positioning

对于 `0.1.x`，把 VibeHarness 描述为 workflow preview。不要在 evaluation plan 有真实或现实化 episodes 之前，声称 intervention reduction 或 benchmark superiority。
