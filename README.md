# Managerial Accounting (MBA 502) - Exam 1 prep

Version 2, rebuilt 2026-10-22 from two sources:

1. The seven class transcripts, sessions 1 to 7 (2026-09-03 to 2026-10-22), in
   `~/MegaMind/Resources/raw/granola-transcripts/`.
2. The instructor's own exam-prep package: the blueprint, the logistics sheet, the practice
   problems with solutions, the handouts with solutions, and the homework solutions.

The package files are copyrighted course material and are **not** in this repository. They
live in `~/Code/acct-midterm-sources/MBA-502-Exam-1-Prep/`. Nothing in that folder should ever
be copied in here.

## Exam, from the instructor's logistics sheet

| | |
|---|---|
| Opens | Thu 2026-10-22, 11:00 am |
| Closes | Sat 2026-10-31, 11:59 pm |
| Time limit | 2 hours 15 minutes |
| Items | 18, worth 100 points |
| Work | Individual |
| Proctoring | Proctorio |
| Notes allowed | one 8.5 x 11 sheet, handwritten |
| Excel | allowed, but the workbook must start blank |
| Not permitted | GoalSeek, Solver, any AI resource |
| Coverage | sessions 1 to 7, including Paper Airplanes / cost allocation; Blocher ch. 3, 8, 9 |

A Second Chance window of Nov 4 to 8 is on the sheet with a question mark beside it.

## The blueprint drives everything

| Item(s) | Topic | Points |
|---|---|---|
| 1 | Integrity statement | 0 |
| 2 | Cost behavior | 5 |
| 3 | CVP, short answer | 5 |
| 4 | Cost behavior | 5 |
| 5 to 6 | Regression | 10 |
| 7 to 9 | Single-product CVP | 15 |
| 10 to 11 | Multi-product CVP | 15 |
| 12 | DOL | 5 |
| 13 | Operating leverage, short answer | 5 |
| 14 to 15 | Cost accounting, the paper planes | 10 |
| 16 | Cost behavior | 5 |
| 17 | TenAlpina case 1, 50 words max | 10 |
| 18 | TenAlpina case 2, 90 words max | 10 |

`study-guide.md` is ordered by point weight, not by the order the topics were taught.

## Files

| File | What it is |
|---|---|
| `study-guide.md` | The whole course, ordered heaviest topic first. Per topic: his formula in his notation, when it applies, a worked example with real class numbers, the traps he plants. Ends with what this pack does not cover |
| `cheat-sheet.md` | A Click Note for the one handwritten sheet: twelve items, nothing obvious. Opens with the AI-policy caution, which is unresolved and needs a question to the professor |
| `excel-recipes.md` | Twelve cell-by-cell recipes mapped to blueprint items, all solvable on a blank sheet with no GoalSeek and no Solver |
| `questions.json` | Question bank, 181 questions. Single source of truth |
| `index.html` | Local practice quiz plus a timed mock-exam mode. No external libraries |
| `questions.js` | Generated from `questions.json` by `build.sh`. Never edit it |
| `build.sh` | Regenerates `questions.js` and validates the JSON |

## The bank

181 questions. Every computational answer in it was recomputed from first principles by an
independent script, not spot-checked: 62 of 62 numeric, 57 of 100 multiple-choice (the other
43 are conceptual and have no arithmetic), and 3 decision questions re-derived from the
underlying economics. All matched.

By source:

| Source | Count | What it is |
|---|---|---|
| `class transcript` | 81 | Built from what he said and worked in class |
| `instructor practice` | 54 | His own practice problems, carrying his worked solutions |
| `original drill` | 28 | Written for this pack, with numbers that appear in none of his files |
| `mock exam` | 18 | One original full-length mock, matching the blueprint exactly |

By blueprint item:

| Blueprint | Questions |
|---|---|
| 1, integrity | 1 |
| 2 / 4 / 16, cost behavior | 27 |
| 3, CVP short | 7 |
| 5 to 6, regression | 17 |
| 7 to 9, single CVP | 50 |
| 10 to 11, multi CVP | 23 |
| 12, DOL | 9 |
| 13, operating leverage short | 6 |
| 14 to 15, planes | 18 |
| 17, TenAlpina case 1 | 5 |
| 18, TenAlpina case 2 | 14 |
| exam logistics | 4 |

## Running the quiz

The quiz is already served continuously at <http://localhost:4181/> by the launchd job
`com.bjepp.acct-midterm`. Nothing to start. Run `./build.sh` after editing `questions.json`
so the served copy picks the change up.

To run it standalone instead:

```bash
./build.sh && open index.html
```

The build exists because `file://` blocks `fetch`. The page tries `questions.json` first and
falls back to `questions.js`.

## Practice mode

- Filter by topic. Modes: all questions, missed only, not yet seen.
- A worked solution appears after every answer.
- A wrong answer re-inserts the question a few places later in the queue.
- Misses persist in `localStorage`, so "Missed only" works across sessions. A question leaves
  the missed pool after two correct answers in a row.
- Short-answer and essay questions are self-graded: write the answer, read the model answer,
  mark yourself.
- The progress table shows attempts, misses and accuracy per topic.
- Mock-exam items never appear in practice mode. They are held back so the mock stays unseen.

## Mock exam mode

Pick the mock in the top row of controls and press **Start timed mock**. It gives you:

- all 18 items in blueprint order, each labelled with its item number and point value
- a 2:15:00 countdown that turns amber under 8 minutes, red under 2, and submits the exam
  automatically at zero
- free navigation: Back, Next, and a row of numbered buttons that mark which items you have
  answered
- a live word counter on the two case items, which turns red and tells you by how much you
  are over the 50-word and 90-word limits
- no feedback of any kind until you submit, which is the point of it

On submit it auto-grades the multiple-choice and numeric items, 70 of the 100 points, and
shows a per-item grid of what you got and what you missed. The remaining 30 points sit on the
two short-answer items and the two case items, which you grade yourself against the model
answers in the review screen.

## Known gaps

- **The two TenAlpina cases, 20 of the 100 points, are not in this pack as cases.** The
  instructor's AI policy bars using AI resources on the exam, and the case files are his.
  So the pack teaches the analysis method for each case and invents no case facts. Mock items
  17 and 18 are labelled "Method rehearsal, not the real case" and use generic firms.
  The case files themselves have to be read directly.
- **Whether AI-derived content may go on the handwritten sheet is unresolved.** The syllabus
  language is quoted at the top of `cheat-sheet.md`. This needs a direct question to
  Prof. Smith before the sheet is written out.
- **Whether the Excel Analysis ToolPak may be used is unresolved.** The logistics sheet bans
  GoalSeek and Solver by name and says nothing about the ToolPak, and a blank workbook plus the
  ToolPak is how regression was taught. `excel-recipes.md` gives hand formulas for every
  regression figure so nothing depends on the answer.
- **One rounding-order conflict is his own.** The CVP Part 2 handout solution gives 181,819
  where homework 9-36 gives 181,820 for the same shape of calculation. Both are his. Both are
  documented in `study-guide.md`; neither is silently preferred.
- **The 47,370 figure on his high-leverage slide reconciles to neither 47,369 nor 47,367.65.**
  Documented, unresolved, almost certainly a slide typo.
- **The labor-time allocation split in session 7 (63/37 versus 37/63) is unresolved** in the
  transcript, and is flagged where it is used.
- Names come from auto-transcription and may be misspelled. The professor is given as
  Steve Smith.
- **No real quiz items were ever available.** The bank is weighted to the blueprint and to his
  practice problems, which is the best available proxy, not to observed exam items.
