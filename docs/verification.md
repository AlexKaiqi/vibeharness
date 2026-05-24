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

This runs:

- benchmark manifest validation;
- i18n status validation;
- local Markdown link checking;
- executable fixture tests;
- sanitized example episode scoring;
- example evaluation report generation.

## Example Command

```sh
make example
```

This runs only the todo CLI fixture and the example episode scorecard. Use it
when changing example files.

## Report Command

```sh
make report
```

This runs all bundled executable examples and writes:

- `reports/example_evaluation.json`
- `reports/example_evaluation.md`

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
- the executable fixture still works;
- the example episode has a passing primary score;
- the bundled examples can produce an evaluation report.

It does not prove the research claim. That requires real or realistic episodes,
baselines, and intervention-reduction measurements as described in
`docs/evaluation.md`.
