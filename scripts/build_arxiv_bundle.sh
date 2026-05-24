#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
out_dir="$repo_root/dist"
bundle_dir="$out_dir/arxiv-source"

mkdir -p "$bundle_dir"
make -C "$repo_root" paper

cp "$repo_root/paper/main.tex" "$bundle_dir/"
cp "$repo_root/paper/references.bib" "$bundle_dir/"
cp "$repo_root/paper/main.bbl" "$bundle_dir/"

tar -C "$bundle_dir" -czf "$out_dir/vibeharness-arxiv-source.tar.gz" .
echo "$out_dir/vibeharness-arxiv-source.tar.gz"
