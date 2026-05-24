# 贡献指南

[English](CONTRIBUTING.md) | 简体中文

感谢你帮助改进 VibeHarness。

## 可贡献方向

有价值的贡献包括：

- 真实脱敏 intervention episodes；
- executable fixtures；
- agent adapters；
- scoring 和 audit scripts；
- 文档和翻译；
- prior-art updates；
- evaluation reports。

## 开发流程

1. 先开 issue 描述问题或提案。
2. 保持改动聚焦。
3. 运行：

```sh
make validate
```

4. 文档改动需要更新对应翻译，或在 `.vibeharness/i18n.json` 标记状态。
5. harness 或 scoring 相关改动请附带 example episode，或说明为什么不需要。

## Episode 数据

不要提交私有仓库内容、secrets、客户数据、个人消息或专有日志。脱敏 episode 应保留 intervention 的结构，但不能暴露敏感内容。

## 已有工作

如果贡献借用了已有工作的概念，请在概念附近引用，并在必要时更新 `docs/prior_art.md`。
