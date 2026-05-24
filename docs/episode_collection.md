# Episode Collection

[English](episode_collection.md) | [简体中文](episode_collection.zh-CN.md)

VibeHarness treats an episode as the smallest publishable unit of evidence. A
claim should be backed by replayable episodes, not only by a final patch or a
conversation summary.

## Minimum Episode Artifacts

Every publishable episode must include:

- `manifest.json`: task metadata, checkpoint id, mode, fixture or repository
  source, and harness version.
- `request.md`: original user request plus durable acceptance criteria.
- `intervention_log.md`: human or tool interventions with timestamps and
  material facts.
- `decision_contract.md`: pre-edit attribution, proposed harness repair,
  expected effect, and falsification check.
- `audit.md`: permissions, information boundaries, entropy, and trajectory
  safety notes.
- `scorecard.json`: primary score fields and diagnostic scores.

Use:

```sh
vh start --request "original user request"
vh score .vibeharness/episodes/<id>
vh episodes .vibeharness/episodes
```

Fresh episodes start with a failing template scorecard. They should pass only
after the intervention log, decision contract, audit, and replay evidence have
been filled in.

## Sanitization Rules

Before publishing an episode:

- replace private repository names, user names, customer names, internal URLs,
  secrets, tokens, and production resource identifiers;
- preserve the failure class, intervention facts, decision contract, command
  shape, and replay evidence;
- keep enough logs to audit attribution, but remove irrelevant local paths and
  machine-specific noise;
- do not expose hidden checks to the worker transcript;
- record any redaction that changes what a reader could infer.

## Inclusion Criteria

An episode is useful for the benchmark only when:

- the blocker is primarily a harness gap, not missing domain knowledge or a
  one-off product decision;
- the intervention can be converted into a durable harness artifact;
- the task can be reset and replayed deterministically;
- the harness repair does not hard-code the application solution;
- safety and information-flow boundaries can be audited.

## Dataset Splits

Use three groups:

- `examples`: small executable fixtures committed to the repository.
- `sanitized_real`: real traces with private details removed.
- `held_out_transfer`: tasks used only to test whether harness repairs transfer.

Do not tune harness instructions on held-out transfer tasks.

## Reporting

For each dataset split, report:

- episode count;
- primary pass rate;
- replay pass rate;
- intervention absorption rate;
- attribution accuracy;
- trajectory safety pass rate;
- human interrupt count;
- transfer gain when applicable.

Local smoke checks:

```sh
make episodes
make report
make ablation
```
