# Contributing

[English](CONTRIBUTING.md) | [简体中文](CONTRIBUTING.zh-CN.md)

Thanks for helping improve VibeHarness.

## Contribution Areas

Useful contributions include:

- real sanitized intervention episodes;
- executable fixtures;
- agent adapters;
- scoring and audit scripts;
- documentation and translations;
- prior-art updates;
- evaluation reports.

## Development Flow

1. Open an issue describing the problem or proposal.
2. Keep changes focused.
3. Run:

```sh
make validate
```

4. For documentation changes, update the matching translation or mark it in
   `.vibeharness/i18n.json`.
5. For harness or scoring changes, include an example episode or explain why one
   is not needed.

## Episode Data

Do not submit private repository contents, secrets, customer data, personal
messages, or proprietary logs. Sanitized episodes should preserve the structure
of the intervention without exposing sensitive content.

## Prior Art

If a contribution borrows a concept from existing work, cite it near the concept
and update `docs/prior_art.md` when appropriate.
