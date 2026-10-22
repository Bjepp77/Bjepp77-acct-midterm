# Blank-Excel Recipes

Excel is allowed but **must be blank when the exam starts**. GoalSeek and Solver are banned. So every
recipe below is built from nothing, in under two minutes, using only arithmetic, `SUM`,
`SUMPRODUCT`, `ROUND` and `ROUNDUP`.

**How to use this file:** each recipe is a small block of cells. Type the labels in column A, the
inputs in column B, and the formulas exactly as shown. Then change an input and watch the answer
move, which is how you check your own work.

**One habit that pays for itself:** put every input in its own cell and never type a number inside a
formula. When the next part of the question changes one input, you retype one cell instead of
rebuilding.

**Coverage:** there is a recipe here for every computational item on the blueprint.

| Blueprint item | Topic | Recipe |
|---|---|---|
| 2, 4, 16 | Cost behavior | 1, 2, 3 |
| 5-6 | Regression | 4, 5 |
| 7-9 | Single-product CVP | 6, 7, 8 |
| 10-11 | Multi-product CVP | 9, 10 |
| 12 | DOL | 11 |
| 14-15 | Cost accounting, planes | 12 |

---

## Read this about ROUNDUP

`ROUNDUP` is unforgiving of floating-point noise. A division that should land exactly on a whole
number can come back as 50000.000000000007, and `ROUNDUP` then returns **50,001**.

**Always wrap the division in `ROUND(...,6)` before rounding up:**

```
=ROUNDUP(ROUND(B5/B6,6),0)
```

The inner `ROUND` kills the noise at six decimals, far finer than any answer on this exam, and the
outer `ROUNDUP` then does what you meant. Every recipe below uses this pattern.

---

## Recipe 1: High-low (items 2, 4, 16)

Type the data, then let formulas find the high and low **by activity**. This is the whole point: the
formula cannot be tempted to sort by cost.

| Cell | Content |
|---|---|
| A1 | `Activity` |
| B1 | `Cost` |
| A2:B7 | your data pairs, one row each |
| A9 | `Hi activity` |
| B9 | `=MAX(A2:A7)` |
| A10 | `Hi cost` |
| B10 | `=INDEX(B2:B7,MATCH(B9,A2:A7,0))` |
| A11 | `Lo activity` |
| B11 | `=MIN(A2:A7)` |
| A12 | `Lo cost` |
| B12 | `=INDEX(B2:B7,MATCH(B11,A2:A7,0))` |
| A14 | `b variable rate` |
| B14 | `=(B10-B12)/(B9-B11)` |
| A15 | `a fixed total` |
| B15 | `=B10-B14*B9` |
| A16 | `check at low point` |
| B16 | `=B12-B14*B11` |

**B15 and B16 must match.** If they do not, you have a data entry error. That check is the reason to
build this in Excel rather than on paper.

To predict a cost at any volume, add:

| Cell | Content |
|---|---|
| A18 | `volume` |
| B18 | your volume |
| A19 | `predicted TC` |
| B19 | `=B14*B18+B15` |

---

## Recipe 2: Rebuild variable and fixed from a GAAP statement (items 4, 16)

The statement gives you core versus run-the-business. You need variable versus fixed.

| Cell | Content |
|---|---|
| A1 | `units` |
| B1 | units sold |
| A2 | `COGS` |
| B2 | cost of goods sold |
| A3 | `SGA` |
| B3 | selling and admin |
| A5 | `VC per unit components` |
| B5:B8 | each per-unit variable cost, one per cell |
| A10 | `VC per unit` |
| B10 | `=SUM(B5:B8)` |
| A11 | `total VC` |
| B11 | `=B10*B1` |
| A12 | `total cost` |
| B12 | `=B2+B3` |
| A13 | `total FC` |
| B13 | `=B12-B11` |

Leave B5:B8 as separate cells. Problems commonly list four variable components and bury one of them
in selling expenses, and keeping them apart makes it obvious if you missed one.

---

## Recipe 3: Step costs (item 16)

| Cell | Content |
|---|---|
| A1 | `volume` |
| B1 | volume |
| A2 | `capacity each` |
| B2 | capacity per resource |
| A3 | `cost each` |
| B3 | cost per resource |
| A4 | `other fixed` |
| B4 | other fixed cost |
| A5 | `VC per unit` |
| B5 | variable cost per unit |
| A7 | `resources needed` |
| B7 | `=ROUNDUP(ROUND(B1/B2,6),0)` |
| A8 | `step cost` |
| B8 | `=B7*B3` |
| A9 | `total cost` |
| B9 | `=B8+B4+B5*B1` |
| A11 | `range low` |
| B11 | `=(B7-1)*B2+1` |
| A12 | `range high` |
| B12 | `=B7*B2` |

B11 and B12 give you the relevant range to quote in a written answer.

---

## Recipe 4: Confidence interval on a coefficient (items 5-6)

For an interval around **fixed cost** or around **variable cost**. Use that coefficient's own
standard error.

| Cell | Content |
|---|---|
| A1 | `coefficient` |
| B1 | the printed coefficient |
| A2 | `its own SE` |
| B2 | that coefficient's printed standard error |
| A3 | `t value` |
| B3 | the t from his table |
| A5 | `half width` |
| B5 | `=B3*B2` |
| A6 | `lower` |
| B6 | `=B1-B5` |
| A7 | `upper` |
| B7 | `=B1+B5` |

Set up a t table once, in D1:E4, so you stop second-guessing which number to use:

| Cell | Content | Cell | Content |
|---|---|---|---|
| D1 | `70` | E1 | `1.134` |
| D2 | `80` | E2 | `1.440` |
| D3 | `90` | E3 | `1.943` |
| D4 | `95` | E4 | `2.447` |

Then B3 becomes `=INDEX(E1:E4,MATCH(90,D1:D4,0))`, with 90 replaced by the confidence level asked
for. Those t values are for **6 degrees of freedom**, that is n = 8. If n differs, df = n - 2 and you
need his table for that df.

---

## Recipe 5: Confidence interval on a total cost estimate (items 5-6)

Different recipe, because this one uses the **regression's** standard error, not a coefficient's.

| Cell | Content |
|---|---|
| A1 | `intercept a` |
| B1 | printed intercept |
| A2 | `slope b` |
| B2 | printed slope |
| A3 | `volume` |
| B3 | the volume asked about |
| A4 | `SE regression` |
| B4 | **Standard Error from the top block** |
| A5 | `t value` |
| B5 | the t value |
| A7 | `point estimate` |
| B7 | `=B1+B2*B3` |
| A8 | `half width` |
| B8 | `=B5*B4` |
| A9 | `lower` |
| B9 | `=B7-B8` |
| A10 | `upper` |
| B10 | `=B7+B8` |

**Keep recipes 4 and 5 visually apart on the sheet.** Picking the wrong standard error is the trap
he sets, and two separate blocks make it hard to grab the wrong cell.

To check a t stat: `=B2/B2se`, that is the coefficient over its own standard error.

---

## Recipe 6: Break-even (items 7-9)

| Cell | Content |
|---|---|
| A1 | `price` |
| B1 | price |
| A2 | `VC per unit` |
| B2 | variable cost per unit |
| A3 | `total FC` |
| B3 | total fixed cost |
| A5 | `CM per unit` |
| B5 | `=B1-B2` |
| A6 | `BE units exact` |
| B6 | `=B3/B5` |
| A7 | `BE units` |
| B7 | `=ROUNDUP(ROUND(B6,6),0)` |
| A8 | `BE revenue` |
| B8 | `=B6*B1` |

**Keep both B6 and B7.** The unrounded B6 is what you use for a margin of safety in dollars; the
rounded B7 is the answer to a units question.

If the problem gives percentages instead of per-unit figures:

| Cell | Content |
|---|---|
| A10 | `VC ratio` |
| B10 | variable cost as a decimal, e.g. 0.62 |
| A11 | `BE revenue` |
| B11 | `=B3/(1-B10)` |

---

## Recipe 7: Target profit, with or without tax (items 7-9)

Build on recipe 6. This handles every version he asks.

| Cell | Content |
|---|---|
| A13 | `after-tax target` |
| B13 | after-tax target, or 0 if the target is pretax |
| A14 | `tax rate` |
| B14 | tax rate as a decimal, or 0 |
| A15 | `pretax target given` |
| B15 | a pretax target if that is what you were given, else 0 |
| A17 | `pretax target` |
| B17 | `=IF(B13>0,B13/(1-B14),B15)` |
| A18 | `units exact` |
| B18 | `=(B3+B17)/B5` |
| A19 | `units` |
| B19 | `=ROUNDUP(ROUND(B18,6),0)` |
| A20 | `revenue needed` |
| B20 | `=(B3+B17)/(1-B10)` |

B17 does the gross-up for you, which removes the commonest error on the exam. B20 is the revenue
version, for when variable cost was given as a ratio.

**For a return target,** compute the after-tax figure into B13 first:

| Cell | Content |
|---|---|
| A22 | `base (equity or assets)` |
| B22 | equity for ROE, **total assets** for ROA |
| A23 | `target return %` |
| B23 | the rate |
| A24 | `after-tax needed` |
| B24 | `=B22*B23` |

Then point B13 at B24. Read the question for which base: ROE is equity, ROA is assets.

**For a target stated as a percentage of revenue,** the unknown appears on both sides, so use this
instead:

| Cell | Content |
|---|---|
| A26 | `target % of revenue` |
| B26 | the rate, e.g. 0.25 |
| A27 | `units` |
| B27 | `=ROUNDUP(ROUND(B3/(B5-B26*B1),6),0)` |

That denominator is CM per unit less the share of price the target consumes.

---

## Recipe 8: Margin of safety, both denominators (items 7-9)

| Cell | Content |
|---|---|
| A29 | `current volume` |
| B29 | current volume |
| A31 | `MoS units` |
| B31 | `=B29-B7` |
| A32 | `MoS dollars` |
| B32 | `=(B29-B6)*B1` |
| A33 | `% above break-even` |
| B33 | `=B31/B7` |
| A34 | `% sales can fall` |
| B34 | `=B31/B29` |

**Compute both percentages and label them.** Then read the question once more and pick. B33 answers
"how far above break-even are we", B34 answers "how far can sales fall". B32 uses the unrounded B6
because the dollar margin of safety is a straight revenue difference.

---

## Recipe 9: Multi-product basket (items 10-11)

| Cell | Content |
|---|---|
| A1 | `product` |
| B1 | `price` |
| C1 | `VC` |
| D1 | `units expected` |
| A2:D4 | one row per product |
| E1 | `mix` |
| E2 | `=D2/MIN($D$2:$D$4)` |
| | fill E2 down to E4 |
| A6 | `basket price` |
| B6 | `=SUMPRODUCT(E2:E4,B2:B4)` |
| A7 | `basket VC` |
| B7 | `=SUMPRODUCT(E2:E4,C2:C4)` |
| A8 | `basket CM` |
| B8 | `=B6-B7` |
| A9 | `total FC` |
| B9 | total fixed cost |
| A10 | `target profit` |
| B10 | target, or 0 |
| A11 | `baskets` |
| B11 | `=(B9+B10)/B8` |
| F1 | `BE units` |
| F2 | `=ROUNDUP(ROUND($B$11*E2,6),0)` |
| | fill F2 down to F4 |
| A13 | `total units` |
| B13 | `=SUM(F2:F4)` |

**Do not round B11.** `SUMPRODUCT` handles any number of products, and column E does not need whole
numbers for the arithmetic to work, though reducing the mix keeps it readable. Column F unpacks
first and rounds each product up, which is his order.

For two products, use rows 2:3 and ranges `E2:E3`, `B2:B3`, `C2:C3`.

---

## Recipe 10: Multi-product revenue method (items 10-11)

For a **dollar** answer. Add to recipe 9's table:

| Cell | Content |
|---|---|
| G1 | `revenue` |
| G2 | `=B2*D2`, filled down |
| H1 | `var cost` |
| H2 | `=C2*D2`, filled down |
| A15 | `total revenue` |
| B15 | `=SUM(G2:G4)` |
| A16 | `total VC` |
| B16 | `=SUM(H2:H4)` |
| A17 | `VC ratio` |
| B17 | `=B16/B15` |
| A18 | `BE revenue` |
| B18 | `=(B9+B10)/(1-B17)` |
| I1 | `rev share` |
| I2 | `=G2/$B$15`, filled down |
| J1 | `BE revenue by product` |
| J2 | `=I2*$B$18`, filled down |

Column I is the **revenue** mix, which is not the unit mix. Use I for dollar splits and column E for
unit splits. Confusing the two is the standard error on this item.

---

## Recipe 11: DOL (item 12)

| Cell | Content |
|---|---|
| A1 | `price` |
| B1 | price |
| A2 | `VC per unit` |
| B2 | variable cost |
| A3 | `volume` |
| B3 | volume |
| A4 | `total FC` |
| B4 | total fixed cost |
| A6 | `total CM` |
| B6 | `=(B1-B2)*B3` |
| A7 | `operating profit` |
| B7 | `=B6-B4` |
| A8 | `DOL` |
| B8 | `=B6/B7` |
| A10 | `% change revenue` |
| B10 | the change, e.g. 0.15 or -0.20 |
| A11 | `% change profit` |
| B11 | `=B8*B10` |
| A12 | `new profit` |
| B12 | `=B7*(1+B11)` |
| A13 | `check directly` |
| B13 | `=(B1-B2)*B3*(1+B10)-B4` |

**B12 and B13 must agree.** That is the DOL shortcut checked against rebuilding the statement, and it
confirms you used total contribution margin rather than something else.

If you are given total CM and operating profit directly, DOL is just the one division.

---

## Recipe 12: Planes, units of production (items 14-15)

Two denominators. Build them as two separate cells so you cannot cross them.

| Cell | Content |
|---|---|
| A1 | `started` |
| B1 | units started |
| A2 | `completed and sold` |
| B2 | units completed and sold |
| A3 | `WIP units` |
| B3 | `=B1-B2` |
| A4 | `WIP % complete, conversion` |
| B4 | the percentage, e.g. 0.60 |
| A6 | `UoP materials` |
| B6 | `=B2+B3` |
| A7 | `UoP conversion` |
| B7 | `=B2+B3*B4` |
| A9 | `total DM cost` |
| B9 | total materials spend |
| A10 | `total DL cost` |
| B10 | total labor spend |
| A11 | `total OH cost` |
| B11 | total overhead spend |
| A13 | `DM rate` |
| B13 | `=B9/B6` |
| A14 | `DL rate` |
| B14 | `=B10/B7` |
| A15 | `OH rate` |
| B15 | `=B11/B7` |
| A17 | `price` |
| B17 | price per unit |
| A18 | `revenue` |
| B18 | `=B17*B2` |
| A19 | `COGS` |
| B19 | `=(B13+B14+B15)*B2` |
| A20 | `period costs` |
| B20 | selling and admin total |
| A21 | `operating profit` |
| B21 | `=B18-B19-B20` |
| A23 | `ending inventory` |
| B23 | `=B13*B3+(B14+B15)*B3*B4` |
| A25 | `tie-out` |
| B25 | `=B19+B23-(B9+B10+B11)` |

**B25 must be zero.** Cost of goods sold plus ending inventory has to equal everything spent on
manufacturing. If it is not zero, you have mixed up a denominator. Selling and admin is excluded
deliberately, because period costs never enter inventory.

When the problem states costs per unit or per employee rather than as totals, compute the totals into
B9:B11 first, for example `=16*4` for four folders at $16 each.

---

## A blank-sheet opening sequence

Two minutes at the start of the exam, before you read question 2:

1. In D1:E4, type the t table from recipe 4.
2. In A1:B8, type recipe 6. Most CVP items reuse it with one input changed.
3. Leave row 1 of columns G onward clear for the multi-product table.

Then for each question, change inputs rather than rebuilding. Label every cell, because an unlabelled
sheet is where the wrong-cell errors come from.

**Final reminder:** no GoalSeek, no Solver. Nothing above needs either. The Analysis ToolPak is not
mentioned in the course logistics either way, so **do not count on it**; every regression recipe here
works from the printed output block, which is how the exam presents regression anyway.
