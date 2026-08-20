#!/usr/bin/env bash
# Stage the repo's markdown into the gitignored docs/ mirror for MkDocs.
# The repo root stays the single source of truth; docs/ is a throwaway copy.
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf docs
mkdir -p docs

rsync -a \
  --include='*/' \
  --include='*.md' \
  --include='diagrams/*.svg' \
  --include='.pre-commit-config.yaml' \
  --include='tools/glossary_check.py' \
  --exclude='sources/personal/**' \
  --exclude='docs/**' \
  --exclude='site/**' \
  --exclude='tools/**' \
  --exclude='tests/**' \
  --exclude='scripts/**' \
  --exclude='.claude/**' \
  --exclude='.github/**' \
  --exclude='*.drawio' \
  --exclude='*' \
  ./ docs/

# prune empty directories left by the include/exclude dance
find docs -type d -empty -delete

echo "staged $(find docs -name '*.md' | wc -l) markdown files + $(find docs -name '*.svg' | wc -l) diagrams into docs/"
