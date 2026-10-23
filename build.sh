#!/usr/bin/env bash
# Writes questions.js and equations.js from their .json sources so index.html works when
# opened directly from the filesystem (file:// blocks fetch). The .json files stay the
# single source of truth; the .js files are generated, never edited.
set -euo pipefail
cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 -c "import json,sys; json.load(open('questions.json'))"   # fail loudly on bad JSON
python3 -c "import json,sys; json.load(open('equations.json'))"
# The badge on a question card is its style string. A numeric or short-answer item
# labelled "... MC" tells the reader to look for choices that are not there.
python3 - <<'PY'
import json, sys
bad = [q['id'] for q in json.load(open('questions.json'))['questions']
       if q.get('type') != 'mc' and 'MC' in (q.get('style') or '')]
if bad:
    sys.exit('style says MC but the question is not multiple choice: ' + ', '.join(bad))
PY
{ printf 'window.QUESTIONS='; cat questions.json; printf ';\n'; } > questions.js
{ printf 'window.EQUATIONS='; cat equations.json; printf ';\n'; } > equations.js
printf 'questions.js written (%s questions), equations.js written (%s topics)\n' \
  "$(python3 -c "import json;print(len(json.load(open('questions.json'))['questions']))")" \
  "$(python3 -c "import json;print(len(json.load(open('equations.json'))['topics']))")"
