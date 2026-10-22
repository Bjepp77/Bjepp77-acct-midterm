# Blank-Excel recipes

The exam allows Excel but it must begin blank: no templates, no notes typed in it. So every
recipe below is typed from scratch. Each is under 2 minutes if you know the layout.

Conventions used throughout:
- Labels go in column A, inputs in column B, computed cells in column B below them.
- Type the inputs first, then the formulas. Never retype a number you already entered.
- Every formula references a cell. If a number appears twice, you have made a mistake.

Keyboard: `Alt =` for AutoSum, `F4` to toggle `$` anchoring, `Ctrl ;` nothing useful here.
Format as currency only at the end, if at all. It costs time and earns no points.

---

## 1. CVP core — the one to memorize

Covers break-even in units and dollars, target profit, and CM ratio. Everything else builds
on this block.

| Cell | Type this | Meaning |
|---|---|---|
| A1:B1 | `Price` / your number | |
| A2:B2 | `VC per unit` / your number | |
| A3:B3 | `Fixed cost` / your number | |
| A4:B4 | `Volume` / your number | |
| A5:B5 | `Target OI` / your number or `0` | |
| A7:B7 | `CM per unit` / `=B1-B2` | |
| A8:B8 | `CM ratio` / `=B7/B1` | |
| A9:B9 | `BE units` / `=ROUNDUP(B3/B7,0)` | round up |
| A10:B10 | `BE revenue` / `=B3/B8` | do not round |
| A11:B11 | `Target units` / `=ROUNDUP((B3+B5)/B7,0)` | |
| A12:B12 | `Total CM` / `=B7*B4` | |
| A13:B13 | `Operating income` / `=B12-B3` | |

**If you are given totals instead of per-unit figures,** add these two above and point B1/B2 at
them: `Price` = `=Revenue/Volume`, `VC per unit` = `=TotalVC/Volume`.

**If the unknown is price, not volume** (the video game problem): leave B1 blank and type in
B15 `=(B5+B3+B2*B4)/B4`. That is the home equation solved for price.

---

## 2. Margin of safety

Add to the block above. Both percentages share a numerator, so compute it once.

| Cell | Type this |
|---|---|
| A15:B15 | `MoS units` / `=B4-B9` |
| A16:B16 | `MoS dollars` / `=B15*B1` |
| A17:B17 | `MoS % of sales` / `=B15/B4` |
| A18:B18 | `MoS % of BE` / `=B15/B9` |

**Read the question before you read a cell.** B17 answers "how far can sales fall." B18
answers "how far above break-even are we."

---

## 3. DOL and sensitivity

| Cell | Type this |
|---|---|
| A20:B20 | `DOL` / `=B12/B13` |
| A21:B21 | `% change in sales` / your number, e.g. `0.1` |
| A22:B22 | `% change in OI` / `=B20*B21` |
| A23:B23 | `New OI, check` / `=B7*B4*(1+B21)-B3` |

B23 is the longhand check on B22. If `(B23-B13)/B13` does not equal B22, one of them is wrong.
Note that B23 holds fixed cost constant, which is the whole point.

---

## 4. Gross-up for taxes and target returns

Put this ABOVE the CVP block so its output feeds `Target OI`.

| Cell | Type this |
|---|---|
| A1:B1 | `Return %` / your number, e.g. `0.3` |
| A2:B2 | `Base (equity or assets)` / your number |
| A3:B3 | `Tax rate` / your number |
| A4:B4 | `After-tax NI target` / `=B1*B2` |
| A5:B5 | `Pre-tax OI target` / `=B4/(1-B3)` |

If the target is already a dollar after-tax figure, skip B1/B2 and type it straight into B4.
Then point the CVP block's `Target OI` at B5, never at B4. That one wrong reference is the
most expensive mistake available on this topic.

---

## 5. High-low

| Cell | Type this |
|---|---|
| A1:B1:C1 | `Activity` / `Cost` headers |
| A2:B2 | high activity / cost at high |
| A3:B3 | low activity / cost at low |
| A5:B5 | `Variable rate` / `=(B2-B3)/(A2-A3)` |
| A6:B6 | `Fixed cost` / `=B3-(B5*A3)` |
| A7:B7 | `Fixed, check` / `=B2-(B5*A2)` |

B6 and B7 must match. They use different data points, so if they disagree your rate is wrong.

**Annual figures:** divide by 12 in the cell, `=345000/12`, rather than in your head. The
grader never sees it and you keep the audit trail.

---

## 6. Regression

**Running it.** `Data` tab → `Data Analysis` → `Regression`. Y range is cost, X range is the
activity. **Untick `Labels` unless your top row really is a header** — leaving it ticked when
the top row is data corrupts every number in the output.

Tick `Confidence Level` and set it to whatever the question asks (it gives 95% for free, so
type 90 or 80 when asked for those). That saves you building intervals by hand.

**Reading it.** Intercept coefficient is fixed cost; the X coefficient is the variable rate.

**Building an interval by hand,** when the question asks for a confidence level Excel did not
print, or asks for a prediction interval:

| Cell | Type this |
|---|---|
| A1:B1 | `Intercept` / paste from output |
| A2:B2 | `Slope` / paste from output |
| A3:B3 | `Slope SE` / paste from output |
| A4:B4 | `Regression SE` / paste from output |
| A5:B5 | `n` / your number |
| A6:B6 | `Volume` / your number |
| A7:B7 | `Confidence` / e.g. `0.95` |
| A9:B9 | `df` / `=B5-2` |
| A10:B10 | `t` / `=T.INV.2T(1-B7,B9)` |
| A12:B12 | `Slope CI low` / `=B2-B3*B10` |
| A13:B13 | `Slope CI high` / `=B2+B3*B10` |
| A15:B15 | `Point estimate` / `=B1+B2*B6` |
| A16:B16 | `Predict CI low` / `=B15-B4*B10` |
| A17:B17 | `Predict CI high` / `=B15+B4*B10` |

`T.INV.2T` is the two-tailed inverse. For 6 df at 95% it returns 2.447, which is the number to
sanity-check against.

**The distinction the exam is most likely to test:** rows 12 and 13 use `B3`, the slope's own
standard error. Rows 16 and 17 use `B4`, the standard error of the whole regression. Using B3
for a prediction interval is the error.

---

## 7. Multi-product, basket method

| Cell | Type this |
|---|---|
| B1:C1 | product A / product B headers |
| A2 | `Units per basket` → B2, C2 |
| A3 | `Price` → B3, C3 |
| A4 | `VC per unit` → B4, C4 |
| A6:B6 | `Fixed cost` / your number |
| A8:B8 | `Basket revenue` / `=B2*B3+C2*C3` |
| A9:B9 | `Basket VC` / `=B2*B4+C2*C4` |
| A10:B10 | `Basket CM` / `=B8-B9` |
| A11:B11 | `BE baskets` / `=B6/B10` |
| A13:B13 | `BE units A` / `=ROUNDUP(ROUND(B11*B2,6),0)` |
| A13:C13 | `BE units B` / `=ROUNDUP(ROUND(B11*C2,6),0)` |
| A14:B14 | `BE total units` / `=B13+C13` |

**B11 has no ROUNDUP and must not get one.** Baskets are a mathematical device. Rounding
happens in row 13, after unpacking, and it rounds up.

**Why the inner `ROUND(...,6)`.** Unpacking often lands on a whole number that floating-point
arithmetic stores a hair above it. `210000/12.6*3` is 50000.000000000007, and `ROUNDUP` of that
is 50,001 rather than 50,000. The inner `ROUND` to six decimals kills the artefact without
touching a genuine fraction like 16,666.67. If a break-even unit count ever comes out exactly
one higher than you expect, this is why.

---

## 8. Multi-product, weighted average and revenue

Use when you are handed totals rather than a mix ratio.

| Cell | Type this |
|---|---|
| A1 | `Units` → B1 (A), C1 (B), D1 `=B1+C1` |
| A2 | `Revenue` → B2, C2, D2 `=B2+C2` |
| A3 | `Variable cost` → B3, C3, D3 `=B3+C3` |
| A4:B4 | `Fixed cost` / your number |
| A6:D6 | `WA price` / `=D2/D1` |
| A7:D7 | `WA VC per unit` / `=D3/D1` |
| A8:D8 | `WA CM per unit` / `=D6-D7` |
| A9:D9 | `CM ratio` / `=1-D3/D2` |
| A11:D11 | `BE total units` / `=D4/D8` |
| A12:D12 | `BE revenue` / `=D4/D9` |
| A14:B14 | `Volume mix A` / `=B1/D1` |
| A15:B15 | `Revenue mix A` / `=B2/D2` |
| A17:B17 | `BE units A` / `=ROUNDUP(ROUND(D11*B14,6),0)` |
| A18:B18 | `BE revenue A` / `=D12*B15` |

**Rows 14 and 15 are different numbers and that is the trap.** Row 17 must use row 14. Row 18
must use row 15. Build both mix cells even when the question only asks for one, so you cannot
grab the wrong one under time pressure.

Cross-check: row 17 × that product's price should equal row 18.

---

## 9. Equivalent units

One column per cost category, because the rates differ.

| Cell | Type this |
|---|---|
| B1:C1:D1 | `Materials` / `Labor` / `Overhead` |
| A2 | `Spend` → B2, C2, D2 |
| A3 | `% complete on ending` → B3, C3, D3 |
| A5:B5 | `Units sold` / your number |
| A6:B6 | `Ending units` / your number |
| A8 | `Equivalent units` → B8 `=$B$5+$B$6*B3`, drag to D8 |
| A9 | `Rate` → B9 `=B2/B8`, drag to D9 |
| A10 | `To income statement` → B10 `=B9*$B$5`, drag to D10 |
| A11 | `To balance sheet` → B11 `=B9*($B$6*B3)`, drag to D11 |
| A12 | `Check` → B12 `=B10+B11-B2`, drag to D12 |
| A14:B14 | `COGS` / `=SUM(B10:D10)` |
| A15:B15 | `Ending inventory` / `=SUM(B11:D11)` |
| A16:B16 | `Total check` / `=B14+B15-SUM(B2:D2)` |

**Row 12 and B16 must all be zero.** That check is the single most valuable cell in this
recipe: it catches a wrong completion percentage, a transposed spend and a blended rate all at
once. The `$` anchors are what let you type row 8 once and drag it.

Income statement: revenue `=units sold × price`, less B14.

---

## 10. Incremental product line and payback

| Cell | Type this |
|---|---|
| A1:B1 | `Volume` / your number |
| A2:B2 | `Price` / your number |
| A4 | `Variable items, one per row` → B4, B5, B6, B7 as per-unit figures |
| A9:B9 | `VC per unit` / `=SUM(B4:B7)` |
| A10:B10 | `CM per unit` / `=B2-B9` |
| A12 | `Fixed items, one per row` → B12, B13, B14 as monthly figures |
| A16:B16 | `Fixed total` / `=SUM(B12:B14)` |
| A18:B18 | `Revenue` / `=B1*B2` |
| A19:B19 | `Total CM` / `=B10*B1` |
| A20:B20 | `Operating income` / `=B19-B16` |
| A22:B22 | `BE units` / `=ROUNDUP(B16/B10,0)` |
| A23:B23 | `MoS units` / `=B1-B22` |
| A25:B25 | `Investment` / your number |
| A26:B26 | `Depreciation` / point at its fixed-cost cell |
| A27:B27 | `Payback, months` / `=B25/B20` |
| A28:B28 | `Payback, cash` / `=B25/(B20+B26)` |

**Build the fixed block so you can switch a cost in or out by deleting one cell.** The hammer
case turns on exactly this: salary out gives break-even 206, salary in gives 314. Keep salary
in its own row and the sensitivity is one keystroke.

Freight is variable and belongs in rows 4 to 7 even though it sits below gross margin on a
GAAP statement. Fixed power and depreciation are fixed and belong in rows 12 to 14 even though
they sit above it.

---

## What not to spend time on

- Formatting, borders, colours. No points.
- The professor said he would never ask you to build a T-account.
- Rounding to match a posted solution. Rounding errors are not penalized.
- Allocation schedules, unless a question explicitly asks for an allocated view.
