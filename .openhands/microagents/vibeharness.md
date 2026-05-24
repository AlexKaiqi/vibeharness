---
name: vibeharness
type: general
---

This repository uses VibeHarness.

For non-trivial work:

1. Create an episode with `python3 scripts/vh_start.py --request "<request>"`.
2. Use the episode directory as the run log.
3. Record manual user interventions.
4. Before harness edits, write a decision contract.
5. Separate harness changes from product-code changes.
6. Replay from the checkpoint after recovery.
7. Fill the scorecard and run `python3 scripts/vh_score_episode.py <episode>`.

Harness artifacts include setup scripts, validation commands, browser/log/metric
adapters, acceptance criteria, agent instructions, permissions, memories, and
coordination rules.
