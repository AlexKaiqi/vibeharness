# Verification

[English](verification.md) | [简体中文](verification.zh-CN.md)

VibeHarness treats verification as part of the product, not as a final cleanup
step. A workflow is only useful if a new contributor can clone the repository,
run one command, and understand what passed.

## Main Command

```sh
make validate
```

The equivalent CLI command is:

```sh
vh validate
```

From a checkout, the same command is available without installing the CLI:

```sh
python3 -m vibeharness.cli validate
```

This runs:

- benchmark manifest validation;
- i18n status validation;
- local Markdown link checking;
- packaged `vh init` asset sync checking;
- skill distribution and install smoke testing;
- Codex adapter smoke testing through `AGENTS.md`, `vh init`, episode creation,
  and scoring in a temporary git repository;
- executable fixture tests;
- sanitized example episode scoring;
- bundled episode-set scoring;
- example evaluation report generation;
- executable ablation report generation.

## Example Command

```sh
make example
```

This runs only the todo CLI fixture and the example episode scorecard. Use it
when changing example files.

## Episodes Command

```sh
make episodes
```

Equivalent CLI forms:

```sh
vh episodes examples/episodes
python3 -m vibeharness.cli episodes examples/episodes
```

This scores every episode directory under the given path.

## Report Command

```sh
make report
```

Equivalent CLI forms:

```sh
vh report
python3 -m vibeharness.cli report
```

This runs all bundled executable examples and writes:

- `reports/example_evaluation.json`
- `reports/example_evaluation.md`

## Ablation Command

```sh
make ablation
```

Equivalent CLI forms:

```sh
vh ablation
python3 -m vibeharness.cli ablation
```

This runs bundled gap probes and writes:

- `reports/ablation_evaluation.json`
- `reports/ablation_evaluation.md`

## Paper Command

```sh
make paper
```

This compiles the paper draft with `tectonic`. Paper compilation is intentionally
separate from CI because the open-source workflow should not require TeX for
normal contributors.

## What Success Means

`make validate` should prove that:

- task manifests remain structurally valid;
- bilingual documentation status is tracked;
- repository-local documentation links resolve;
- packaged `vh init` templates match their source files;
- the skill-first install path can populate local Codex/Claude-style skill
  directories;
- the Codex adapter can bootstrap a target repository, create an episode, and
  score it without relying on repository-local helper scripts;
- the executable fixture still works;
- the bundled example episodes have passing primary scores;
- the bundled examples can produce an evaluation report;
- visible-only checks can pass while gap probes fail, and the repaired harness
  path can replay successfully on bundled ablations.

It does not prove the research claim. That requires real or realistic episodes,
baselines, and intervention-reduction measurements as described in
`docs/evaluation.md`.
