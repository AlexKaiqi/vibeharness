# Licensing and Attribution

[English](licensing.md) | [简体中文](licensing.zh-CN.md)

This is not legal advice. It documents the intended open-source posture for
VibeHarness.

## License Choice

VibeHarness uses the Apache License, Version 2.0.

This is the recommended license for this project because:

- the project is tooling and documentation, so adoption matters;
- the implementation is intentionally lightweight, so strong patent strategy is
  not the core value;
- the license still requires preservation of copyright and license notices;
- the license has an explicit patent grant and patent termination clause;
- the Apache `NOTICE` mechanism gives us a practical place to ask users to keep
  attribution visible.

MIT would be simpler, but it is less explicit about patents and attribution
notices. GPL or AGPL would force more sharing, but they would also make adoption
harder for teams that want to embed VibeHarness in internal agent workflows.

## What Is Covered

Unless a file says otherwise, the Apache-2.0 license covers:

- source code and scripts;
- agent adapter files;
- documentation;
- example fixtures;
- benchmark specifications;
- sanitized example episodes.

Future real datasets may need separate terms if they contain third-party
material, private project traces, or contributor-provided episodes.

## Attribution Expectations

Apache-2.0 allows commercial and private use, modification, and redistribution.
It also requires preservation of copyright and license notices.

For research, benchmarks, articles, talks, or derivative tools, please cite or
acknowledge VibeHarness. The repository includes:

- `NOTICE` for attribution notices;
- `CITATION.cff` for GitHub and citation tooling;
- `docs/prior_art.md` for lineage and related work.

## What This Does Not Do

The license does not prevent commercial use.

The license does not require derivative works to be open sourced.

The license does not grant trademark rights or imply endorsement by the
VibeHarness contributors.

The license does not replace data-sanitization obligations for shared episodes.
