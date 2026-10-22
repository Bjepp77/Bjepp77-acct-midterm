# Design: where the tokens come from

This app borrows the BYU AI Foundry site's visual language: navy and white, square
corners, hairline rules, an 8px grid, one orange moment per view. It is **not** a
Foundry product. It carries no logo, no wordmark and no Foundry branding of any kind,
because no approved Foundry mark exists. It is Brandon's personal study tool.

Two source trees, both read-only. Nothing in them was changed.

- `SITE` = `~/MegaMind/BYU AIFOUNDRY/official-site/`
- `BRAND` = `~/MegaMind/BYU AIFOUNDRY/brand/`

All tokens live in the three `:root` blocks at the top of `index.html`. Components read
the semantic tokens only, never the raw `--byu-*` primitives.

## Colour

### Primitives, copied exactly

| Token | Value | Source |
|---|---|---|
| `--byu-navy` | `#002e5d` | SITE `src/app/globals.css:29` |
| `--byu-navy-deep` | `#001f3f` | SITE `src/app/globals.css:30` |
| `--byu-navy-soft` | `#00396f` | SITE `src/app/globals.css:31` |
| `--byu-off-white` | `#f2f5f7` | SITE `src/app/globals.css:33` |
| `--byu-light-blue` | `#bdd6e6` | SITE `src/app/globals.css:36` |
| `--byu-orange` | `#d14124` | SITE `src/app/globals.css:37` |
| `--byu-orange-deep` | `#a7341d` | SITE `src/app/globals.css:38` |

### Semantic tokens

| Token | Light | Dark | Source and measured ratio |
|---|---|---|---|
| `--bg` | off-white | navy-deep | SITE `globals.css:47` (subtle band), `:49` (inverse-soft) |
| `--panel` | white | navy | SITE `globals.css:46`, `:48` |
| `--ink` | navy | white | SITE `globals.css:55`. 12.38:1 on bg, 13.56:1 on panel |
| `--muted` | `#4d5f6e` | light blue | see the slate-gray note below. 6.04:1 light, 8.99:1 dark |
| `--line` | `#ced7e0` | `#2e547a` | SITE `globals.css:71` and `:73`, flattened (below) |
| `--accent` | orange | orange | fill only, never text. SITE `globals.css:62-63` |
| `--accent-ink` | white | white | 4.67:1 on the orange fill |
| `--accent-text` | orange-deep | light blue | SITE `globals.css:62`. 6.08:1 light, 8.99:1 dark |
| `--fill` | navy | light blue | structural fill: progress bars, step nodes, current item |
| `--focus` | orange | light blue | 4.27:1 light, 10.98:1 dark, both over the 3:1 a ring needs |
| `--code` | `#e7edf2` | navy-soft | SITE `globals.css:31` for the dark value |

Three rules from the site's contrast contract (SITE `globals.css:100-140`) drove the
shape of this table:

1. **Orange is a fill on dark, never a text colour.** Orange on navy measures 2.90:1
   (SITE `globals.css:63`, `:120`). So `--accent` and `--accent-text` are two different
   tokens here, where the old palette had one. `--accent` paints the primary button and
   the focus ring; `--accent-text` is the only one allowed to colour type, and on dark it
   is light blue, not orange.
2. **BYU Slate Gray is large-text only.** `#7c878e` measures 3.68:1 on white and 3.36:1
   on off-white (SITE `globals.css:56`, `:114`). Every muted string in this app is small
   text, so slate gray is not used. `--muted` light is `#4d5f6e`, a darker navy-grey that
   measures 6.61:1 on panel, 6.04:1 on bg and 5.60:1 on code.
3. **Royal blue never carries text on navy** (1.43:1, SITE `globals.css:121`). Royal is
   not used at all here.

`--line` is the one place the values are not copied verbatim. The site writes its
hairlines with `color-mix(in srgb, ...)` (SITE `globals.css:71`, `:73`). This app has to
run from `file://` with no network and no build step, so the two mixes are flattened to
the hex they resolve to: navy at 15% over off-white is `#ced7e0`, white at 18% over navy
is `#2e547a`.

### Green and red stay green and red

The BYU palette has no success or error colour. Correct and wrong feedback keeps a green
and a red, retuned so they sit on the navy field and clear AA:

| | Light | on its background | Dark | on its background |
|---|---|---|---|---|
| `--ok` | `#17643a` | 6.14:1 on `--ok-bg` | `#86d3a3` | 7.84:1 on `--ok-bg` |
| `--bad` | `#941b1b` | 7.33:1 on `--bad-bg` | `#f3a69b` | 8.00:1 on `--bad-bg` |
| `--warn` | `#8a4a00` | 5.81:1 on `--code` | `#f5a623` | 5.71:1 on `--code` |

This is a deliberate departure from the palette. Colour is never the only signal: every
correct or wrong state also carries a tick or cross icon and a worded verdict.

## Type

Scale from SITE `SPEC.md:177-197`.

| Where | Size | Line height | Source |
|---|---|---|---|
| Body, question stems, nav, buttons | 16px | 1.63 | `SPEC.md:186` |
| Eyebrows and labels, uppercase, 600, tracked 0.1em | 12px | 1.5 | `SPEC.md:184`, SITE `globals.css:210-218` |
| Page heading `h1`, tracked -0.02em | 20px | 1.3 | `SPEC.md:188` (20 to 30px, 1.2 to 1.4) and the site's `tracking-[-0.02em]` on headings |
| Big counts on the picker | 24px | 1.2 | `SPEC.md:188`, same band |
| Measure cap | 62-68ch | | `SPEC.md:196-198` gives 65 to 75 characters as the band |

Font stack is `Inter, ui-sans-serif, -apple-system, "Segoe UI", Roboto, Helvetica, Arial,
sans-serif`. Inter is the site's sans (SITE `globals.css:177`). There is no `@import` and
no CDN link, so if Inter is not installed the stack falls through to the system sans and
the app still works offline from `file://`. Nothing about function depends on a font
loading.

## Spacing, shape, layout

| Rule | Value | Source |
|---|---|---|
| Spacing grid | 8px: `--s1` 8, `--s2` 16, `--s3` 24, `--s4` 32, `--s6` 48 | BRAND `04_website-branding-elements.md:34` |
| Gutters | 24px | `SPEC.md:211` |
| Corner radius | 0 | the site's own components use no `rounded-*` class anywhere |
| Rules | 1px hairlines, no shadows | SITE `globals.css:71-74` |
| Orange | one moment per view | BRAND `04_website-branding-elements.md:34` |
| Ember bar | 3-4px vertical bar marking the current thing | SITE `globals.css:221-223` |

The ember bar appears twice: on the active rail row (`box-shadow: inset 3px 0 0`) and down
the left edge of the home-equation box. Both are painted in `--fill`, not orange, so the
orange budget stays with the primary action.

## The 2026-10-22 layout pass

Five changes went in after the skin. They added no colour tokens: the study header, the
three counts and the mastery labels all read existing semantic tokens (`--fill`, `--code`,
`--line`, `--muted`, `--ink`).

| Piece | What it is | Type |
|---|---|---|
| Top bar | `h1` on one line, with the long exam metadata folded into an `Exam details` disclosure | 20px heading, 14px summary |
| Study header | Shown only while a session is running: topic, position, accuracy this session, End session, and a 4px progress rule in `--fill` | 12px eyebrow, 14px stats |
| Picker counts | Not yet seen, Missed, Seen for the chosen topic | 24px numbers, 12px labels |
| Keyboard answering | 1 to 9 or A to I pick a choice, Enter goes to the next question. Hidden on touch pointers | 14px hint |
| Mastery levels | Not started, Attempted, Familiar, Proficient, Mastered, on the rail bars and in the stats table | 14px |

The practice controls panel now hides itself while a question is on screen (`setStep`
owns that). Before this pass, at 375px the header plus that panel filled the whole
812px viewport and the question began below the fold.

## What was deliberately not followed

1. **Two orange buttons can be on screen at once.** `button.primary` is one class and it
   paints both the Start button in the picker and Submit in the question card. Splitting
   them would mean inventing a second button style for a difference the user does not
   care about. The site's "one orange moment" rule is broken here by one button.
2. **Dense panel text sits at 14px, not 16px.** `SPEC.md:185` reserves 14px for the
   footer colophon and sets a 16px floor on prose. The equations panel, the symbol
   definitions, the stats tables and the rail rows are a dense reference index, not body
   copy, and at 16px the panel would not fit a 286px rail or a 375px phone. Nothing is
   below 12px, which is the site's hard floor (`SPEC.md:180`).
3. **Green and red for correctness**, as described above.
4. **The pulse dot stays round.** Everything else is square.
5. **No serif.** The site pairs Inter with Fraunces (SITE `globals.css:178`, falling back
   to Georgia at `:196`). Nothing in this app is editorial enough to need it.

## Not verified

- Contrast was measured in Chrome against the rendered DOM, every visible text node, in
  ten state and theme combinations: practice question, worked solution, See more open,
  mock at the 8-minute and 2-minute warnings, grade grid and review, light and dark each.
  Zero failures. It was not checked with a separate audit tool.
- Rendering was checked in the Chromium of the Claude desktop app's browser pane only.
  Not Safari, not Firefox, not a real iPhone.
- Inter is not installed on this machine, so every screenshot shows the system fallback.
  The Inter rendering was never seen.
- The app is pinned to the light theme at `index.html:2` (`data-theme="light"`, commit
  3d7ee90, the owner's decision on 2026-10-22). The dark tokens are still in the file and
  still measured, but nothing reaches them, so dark was not re-verified after that commit.
- The `prefers-color-scheme` block and the `data-theme` block hold the same values. Neither
  was exercised after the theme was pinned.
