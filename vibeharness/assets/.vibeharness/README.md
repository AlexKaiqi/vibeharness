# .vibeharness

This directory contains the portable VibeHarness runtime:

- `config.json`: default policy and scoring fields.
- `templates/`: files copied into each episode.
- `episodes/`: local run artifacts, ignored by git by default if desired by a
  host project.

In a product repository, commit the config and templates. Decide separately
whether to commit sanitized episode packages.
