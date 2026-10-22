# Managerial Accounting — Exam 1 prep

Built 2026-10-22 from the seven class transcripts (sessions 1 to 7, 2026-09-03 to 2026-10-22)
in `~/MegaMind/Resources/raw/granola-transcripts/`.

## Exam

Opens Thu 2026-10-22 11:00 AM, closes midnight Sat 2026-10-31. 19 questions, 2h15m.
Mostly multiple-choice computational plus some short essay on the cases. Proctorio.
One sheet of handwritten notes, front and back. Excel allowed but must begin blank.
Case files not allowed. The last question is conceptual, from the session 7 hammer-line
discussion. No class Thu 10-29.

## Files

| File | What it is |
|---|---|
| `study-guide.md` | Per topic: the formula, when to use it, a worked example with class numbers, the traps. Section 13 is a one-sheet formula list for copying onto the handwritten page |
| `questions.json` | Question bank, 81 questions. Single source of truth |
| `index.html` | Local practice quiz. No external libraries |
| `questions.js` | Generated from `questions.json` by `build.sh`. Never edit it |
| `build.sh` | Regenerates `questions.js` and validates the JSON |

## Running the quiz

Either open `index.html` directly after running the build once:

```bash
./build.sh && open index.html
```

Or serve the folder, which skips the build step:

```bash
python3 -m http.server 8777
```

then open http://localhost:8777/

### Always-on copy

The quiz is also served continuously at <http://localhost:4181/> by the launchd job
`com.bjepp.acct-midterm`. Nothing to start. Run `./build.sh` after editing `questions.json`
so the served copy picks the change up.

The build exists because `file://` blocks `fetch`. The page tries `questions.json` first and
falls back to `questions.js`.

## Quiz behaviour

- Filter by topic. Modes: all questions, missed only, not yet seen.
- A worked solution appears after every answer, with the session it came from.
- A wrong answer re-inserts the question a few places later in the queue.
- Misses persist in `localStorage`, so "Missed only" works across sessions. A question leaves
  the missed pool after two correct answers in a row.
- Short-essay questions are self-graded: write your answer, read the model answer, mark
  yourself.
- Progress table shows attempts, misses and accuracy per topic.

## Known gaps

- **No quiz screenshots were available.** iCloud `Tray Accounting` was empty when this was
  built. The bank is weighted toward the question styles the professor described in class
  (computational MC, regression-output interpretation, "what's direct labor on the income
  statement, what's the value of inventory"), not toward observed quiz items. Drop screenshots
  into that folder and the bank can be re-weighted against real items.
- The transcripts are noisy auto-transcriptions. Where the professor's spoken numbers did not
  reconcile, the figure that makes his own arithmetic close is used and the discrepancy is
  flagged in `study-guide.md`. Two cases are unresolved and marked as such: the labor-time
  allocation split in session 7 (63/37 versus 37/63), and the complements-versus-substitutes
  label for pitons and hammers.
- Names come from the auto-transcript and may be wrong. The professor is given as Steve Smith.
