#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Install the VibeHarness agent skill into local runtime skill directories.

Usage:
  ./install.sh [--force] [--codex-only | --claude-only | --cursor-only]
  ./install.sh [--force] --target /path/to/skills/vibeharness

Options:
  --force        Replace an existing vibeharness skill directory.
  --codex-only   Install only to Codex skill locations.
  --claude-only  Install only to ${CLAUDE_HOME:-$HOME/.claude}/skills/vibeharness.
  --cursor-only  Install only to ${CURSOR_HOME:-$HOME/.cursor}/skills/vibeharness.
  --target DIR   Install to an explicit final skill directory.
  -h, --help     Show this help.

The Python CLI is optional. Install it separately with:
  python3 -m pip install .
EOF
}

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SRC="$ROOT/skills/vibeharness"
MODE="both"
FORCE=0
CUSTOM_TARGET=""

while [ "$#" -gt 0 ]; do
  case "$1" in
    --force)
      FORCE=1
      ;;
    --codex-only)
      MODE="codex"
      ;;
    --claude-only)
      MODE="claude"
      ;;
    --cursor-only)
      MODE="cursor"
      ;;
    --target)
      shift
      if [ "$#" -eq 0 ]; then
        echo "--target requires a directory" >&2
        exit 2
      fi
      MODE="custom"
      CUSTOM_TARGET="$1"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

if [ ! -f "$SKILL_SRC/SKILL.md" ]; then
  echo "Missing skill source: $SKILL_SRC" >&2
  exit 1
fi

install_skill() {
  local label="$1"
  local dest="$2"

  if [ -e "$dest" ]; then
    if [ ! -d "$dest" ]; then
      echo "$label target exists but is not a directory: $dest" >&2
      return 1
    fi
    if diff -qr "$SKILL_SRC" "$dest" >/dev/null 2>&1; then
      echo "$label skill already up to date: $dest"
      return 0
    fi
    if [ "$FORCE" -ne 1 ]; then
      echo "$label skill already exists: $dest" >&2
      echo "Use --force to replace it." >&2
      return 1
    fi
    rm -rf "$dest"
  fi

  mkdir -p "$dest"
  cp -R "$SKILL_SRC"/. "$dest"/
  echo "Installed $label skill: $dest"
}

: "${HOME:?HOME is required}"

AGENTS_BASE="${AGENTS_HOME:-$HOME/.agents}"
CODEX_BASE="${CODEX_HOME:-$HOME/.codex}"
CLAUDE_BASE="${CLAUDE_HOME:-$HOME/.claude}"
CURSOR_BASE="${CURSOR_HOME:-$HOME/.cursor}"

install_codex_skill() {
  install_skill "Codex repo/user" "$AGENTS_BASE/skills/vibeharness"
  install_skill "Codex app compatibility" "$CODEX_BASE/skills/vibeharness"
}

case "$MODE" in
  both)
    install_codex_skill
    install_skill "Claude" "$CLAUDE_BASE/skills/vibeharness"
    ;;
  codex)
    install_codex_skill
    ;;
  claude)
    install_skill "Claude" "$CLAUDE_BASE/skills/vibeharness"
    ;;
  cursor)
    install_skill "Cursor" "$CURSOR_BASE/skills/vibeharness"
    ;;
  custom)
    install_skill "Custom" "$CUSTOM_TARGET"
    ;;
esac

cat <<'EOF'

VibeHarness skill installed.
Try: "Use $vibeharness to run this task as a checkpointed, replayable episode."
EOF
