#!/usr/bin/env bash
# Writes questions.js from questions.json so index.html works when opened
# directly from the filesystem (file:// blocks fetch). questions.json stays
# the single source of truth; questions.js is generated, never edited.
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 -c "import json,sys; json.load(open('questions.json'))"   # fail loudly on bad JSON
{ printf 'window.QUESTIONS='; cat questions.json; printf ';\n'; } > questions.js
printf 'questions.js written (%s questions)\n' \
  "$(python3 -c "import json;print(len(json.load(open('questions.json'))['questions']))")"
