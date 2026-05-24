#!/usr/bin/env bash
set -euo pipefail

fixture_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
env_file="$fixture_root/.env.vibeharness"

cat > "$env_file" <<EOF
export NOTES_DB="$fixture_root/data/notes.json"
EOF

echo "$env_file"
