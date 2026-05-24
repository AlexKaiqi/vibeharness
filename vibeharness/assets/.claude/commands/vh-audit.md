Audit and score a VibeHarness episode.

Run:

```sh
vh score "$ARGUMENTS"
```

If `vh` is unavailable in this checkout, run
`python3 -m vibeharness.cli score "$ARGUMENTS"`.

Then inspect missing artifacts and update:

- `audit.md`
- `scorecard.json`
- final verification notes

Report whether the task merely passed or whether the harness actually improved.
