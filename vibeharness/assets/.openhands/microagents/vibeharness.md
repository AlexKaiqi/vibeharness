---
name: vibeharness
type: general
---

This repository uses VibeHarness.

For non-trivial work:

1. Create an episode with `vh start --request "<request>"`, or with
   `python3 -m vibeharness.cli start --request "<request>"` from a checkout.
2. Use the episode directory as the run log.
3. Record manual user interventions.
4. Before harness edits, write a decision contract.
5. Separate harness changes from product-code changes.
6. Replay from the checkpoint after recovery.
7. Fill the scorecard and run `vh score <episode>` or
   `python3 -m vibeharness.cli score <episode>`.

Harness artifacts include setup scripts, validation commands, browser/log/metric
adapters, acceptance criteria, agent instructions, permissions, memories, and
coordination rules.
