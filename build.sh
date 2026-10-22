#!/usr/bin/env bash
# Writes questions.js and equations.js from their .json sources so index.html works when
# opened directly from the filesystem (file:// blocks fetch). The .json files stay the
# single source of truth; the .js files are generated, never edited.
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 -c "import json,sys; json.load(open('questions.json'))"   # fail loudly on bad JSON
python3 -c "import json,sys; json.load(open('equations.json'))"
{ printf 'window.QUESTIONS='; cat questions.json; printf ';\n'; } > questions.js
{ printf 'window.EQUATIONS='; cat equations.json; printf ';\n'; } > equations.js
printf 'questions.js written (%s questions), equations.js written (%s topics)\n' \
  "$(python3 -c "import json;print(len(json.load(open('questions.json'))['questions']))")" \
  "$(python3 -c "import json;print(len(json.load(open('equations.json'))['topics']))")"
