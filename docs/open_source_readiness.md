# Open-Source Readiness

[English](open_source_readiness.md) | [简体中文](open_source_readiness.zh-CN.md)

This document tracks what VibeHarness needs before a public GitHub release.

## Release Readiness

Ready enough for an early open-source release:

- Apache-2.0 license;
- NOTICE and CITATION.cff for attribution;
- clear README and Chinese README;
- prior-art and acknowledgements page;
- VibeHarness runtime config and templates;
- Codex, Claude Code, Cursor, and OpenHands adapters;
- episode creation and scoring scripts;
- benchmark manifest validator;
- i18n status checker;
- GitHub Actions for `make validate`;
- contribution, security, conduct, issue, and pull request templates;
- one executable example fixture;
- one sanitized example episode;
- three bundled recovery classes in examples: `spec_capture`,
  `environment_bootstrap`, and `tool_affordance`;
- local example evaluation report runner;
- executable ablation runner for bundled harness-gap probes;
- episode-set scorer for validating collected episode directories;
- installable local CLI package with packaged `vh init` templates;
- current Chinese translations for the high-priority docs and benchmark pages.
- release notes and release process docs for the workflow preview.

Not ready for a polished release:

- no real-world intervention dataset yet;
- no external user study or multi-repository evaluation yet.

## Must Add Before Polished Announcement

- real sanitized episodes from multiple agent tools;
- multi-repository evaluation with at least one transfer group;
- version tag after final release review.

## License Recommendation

Do not publish without a license. GitHub's documentation notes that without an
open-source license, default copyright law applies even if the repository is
public.

Recommended options:

- Apache-2.0 for code and scripts: good default for tooling because it includes a
  patent grant.
- MIT for code and scripts: simpler and widely understood.
- CC BY 4.0 for docs, benchmark specs, and papers if you want explicit reuse and
  attribution.

Current choice: Apache-2.0 for the repository. NOTICE and CITATION.cff are used
to make attribution and citation expectations visible. Add a note later if docs
or datasets use a different license.

## Public Positioning

Position VibeHarness as:

> A portable recovery workflow that turns human interventions in coding-agent
> sessions into durable, replayable harness improvements.

Avoid:

- claiming to invent harness engineering;
- claiming benchmark results before data exists;
- implying official endorsement from OpenAI, Anthropic, Cursor, or OpenHands.

## First Public Milestone

The first public milestone should be `v0.1`:

- VH-Lite works end to end;
- VH-Recovery is documented and manually runnable;
- at least one example episode is included;
- bundled ablations expose harness gaps and recover them through replay;
- `make validate` passes in CI;
- issue templates are available;
- Apache-2.0 license is present;
- i18n status is checked in CI.
