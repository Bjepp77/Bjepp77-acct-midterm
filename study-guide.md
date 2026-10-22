# Exam 1 Study Guide - Managerial Accounting (MBA 502-001, Prof. Steve Smith)

**Exam window:** opens Thursday 2026-10-22 at 11:00 AM MDT, closes Saturday 2026-10-31 at 11:59 PM MDT.
**Format:** 18 numbered items, 100 points, 2 hours 15 minutes, individual, Proctorio.
**Allowed:** one 8.5x11 sheet of handwritten notes; Excel, which must be blank when you start.
**Not allowed:** GoalSeek, Solver, and any AI resources during the exam.
**Coverage:** sessions 1-7. Blocher, *Cost Management*, chapters 3, 8 and 9.

This guide is ordered by **points on the exam**, heaviest first. Study top to bottom and you are
spending your time where the marks are.

| Blueprint item | Topic | Points | Section below |
|---|---|---|---|
| 7-9 | Single-product CVP, 3 computations | 15 | [1](#1-single-product-cvp-items-7-9-15-points) |
| 10-11 | Multi-product CVP, 2 computations | 15 | [2](#2-multi-product-cvp-items-10-11-15-points) |
| 2, 4, 16 | Cost behavior, 3 computations | 15 | [3](#3-cost-behavior-items-2-4-and-16-15-points) |
| 5-6 | Regression, 2 computations | 10 | [4](#4-regression-items-5-6-10-points) |
| 14-15 | Cost accounting, planes, 2 computations | 10 | [5](#5-cost-accounting-the-planes-problem-items-14-15-10-points) |
| 17 | TenAlpina Case 1, 50 words or fewer | 10 | [6](#6-tenalpina-case-1-item-17-10-points) |
| 18 | TenAlpina Case 2, 90 words or fewer | 10 | [7](#7-tenalpina-case-2-item-18-10-points) |
| 3 | CVP, 1 short question | 5 | [8](#8-cvp-short-question-item-3-5-points) |
| 12 | DOL, 1 computation | 5 | [9](#9-degree-of-operating-leverage-item-12-5-points) |
| 13 | Operating leverage, 1 short question | 5 | [10](#10-operating-leverage-short-question-item-13-5-points) |
| 1 | Integrity statement | 0 | read it and answer yes |

**Where the computations are:** 13 of the 18 items are computations worth 65 points. Two are short
written answers worth 10. Two are the case answers worth 20. One is the integrity statement.

---

## The one formula everything comes from

He calls this the **"One" Formula**, or the **Home Equation**. Every CVP question on this exam is this
equation with a different unknown.

```
Revenue  -  Variable Cost  -  Fixed Cost  =  Profit
```

Four forms of the same equation. Pick the one whose inputs you were given.

| You were given | Use this form |
|---|---|
| Price and variable cost per unit | `Sale Price(Volume) - VC Rate(Volume) - Total FC = Profit` |
| Contribution margin per unit | `CM/unit(Volume) - Total FC = Profit` |
| Variable cost as a percentage of sales | `Revenue - VC%(Revenue) - Total FC = Profit` |
| Total cost, and you want to split it | `TC = VC Rate(Volume) + Total FC` |

**Method, every single time:**

1. Write the equation.
2. Fill in the three things you know.
3. Solve for the fourth.

That is the whole subject. If a question looks unfamiliar, it is because the unknown moved, not
because the equation changed.

### The rule he marks hardest

> **Never unitize fixed cost. Never unitize profit.**

His income statement slide has red "NO" symbols on four lines: fixed cost per unit, fixed cost as a
percentage, profit per unit, and profit as a percentage. Those four numbers are only true at the one
volume where they were computed, and a CVP question always moves the volume.

| Quantity | Per unit? | Why |
|---|---|---|
| Revenue | yes | the price |
| Variable cost | yes | constant per unit by definition |
| Contribution margin | yes | price minus variable cost |
| **Fixed cost** | **no** | total is constant, so per unit changes with volume |
| **Profit** | **no** | it is what is left after a fixed lump |

When a problem *hands* you a fixed cost per unit, that is the trap. Multiply it back out to a total
first, then work in totals. See item 16 below and question `ip-cm-008`.

---

## 1. Single-product CVP (items 7-9, 15 points)

Three computations, the largest single block on the exam. Expect break-even, a target-profit volume
with tax, and a margin of safety.

### 1a. Break-even

Set profit to zero.

```
Sale Price(Volume) - VC Rate(Volume) - Total FC = 0
CM/unit(Volume) = Total FC
Volume = Total FC / CM per unit
```

**Worked:** price $8.00, variable cost $4.20, fixed cost $180,000.

| Step | Calculation | Result |
|---|---|---|
| CM per unit | $8.00 - $4.20 | $3.80 |
| Break-even units | $180,000 / $3.80 | 47,368.42 |
| Round | always up | **47,369 units** |
| Break-even revenue | 47,368.42 x $8.00 | **$378,947** |

**Round break-even up, always.** You cannot sell 0.42 of a unit, and 47,368 units still loses money.

For a revenue answer when you were given percentages rather than per-unit figures:

```
Break-even Revenue = Total FC / CM ratio          where CM ratio = 1 - VC ratio
```

**Worked:** variable costs are 62% of revenue, fixed costs $148,800.
CM ratio = 38%. Break-even revenue = $148,800 / 0.38 = **$391,578.95**.

### 1b. Target profit

The target sits beside fixed cost in the numerator. Nothing else changes.

```
Volume = (Total FC + Target Profit) / CM per unit
```

**Worked:** price $8.00, variable cost $4.20, fixed cost $180,000, target operating income $120,000.
($180,000 + $120,000) / $3.80 = 78,947.37 -> **78,948 units**.

### 1c. Taxes: gross up first

Tax turns up constantly in this block. The exam gives you an **after-tax** target and the home
equation works in **pretax** dollars, so convert before you do anything else.

```
Operating Income (pretax) = After-tax Net Income / (1 - tax rate)
```

**Divide, never multiply.** You must earn *more* than $500,000 pretax to keep $500,000 after tax.
$500,000 / (1 - 0.30) = **$714,286**. Multiplying by 0.70 gives $350,000 and is the single most
common error on this topic.

**Return targets.** When the target is a return on something, do it in three steps:

| Step | What | Example: 30% ROE on $300,000 equity, 40% tax |
|---|---|---|
| 1 | Return target to after-tax dollars | $300,000 x 30% = $90,000 |
| 2 | Gross up to pretax | $90,000 / 0.60 = $150,000 |
| 3 | Put into the home equation | solve for the unknown |

**Watch the denominator.** ROE uses **equity**. ROA uses **total assets**. The problem will hand you
a balance sheet with current assets, plant, payables, debt and equity, and almost all of it is a
decoy. Read which two letters the question used.

**Worked (`tax-003`):** volume 25,000, variable cost $40, fixed cost $120,000, equity $300,000, ROE
target 30%, tax 40%. Pretax target $150,000.
Price(25,000) = $40(25,000) + $120,000 + $150,000 = $1,270,000, so price = **$50.80**.

### 1d. Margin of safety: the denominator decides the answer

Margin of safety in units or dollars is a simple difference:

```
Margin of Safety = Current Volume - Break-even Volume
```

The **percentage** has two versions and he asks for both. The words in the question tell you which.

| He asks | Denominator | Reads as |
|---|---|---|
| "How far **above break-even** are we?" | **break-even** | we are X% above the break-even point |
| "How far can sales **fall** / decline?" | **current sales** | we can lose X% of current sales |

**Worked:** current 60,000 units, break-even 47,369 units. Margin of safety 12,631 units, or
12,631.58 x $8.00 = **$101,053** in revenue.

| Question asked | Calculation | Answer |
|---|---|---|
| How far above break-even? | 12,631 / 47,369 | **26.7%** |
| How far can sales fall? | 12,631 / 60,000 | **21.05%** |

Same company, same margin of safety, two different percentages. Both are correct answers to
different questions. Getting the right arithmetic against the wrong question scores zero.

### Thin spot
Nothing here is thin. This block has the most practice material of any topic: 50 questions tagged
7-9 in the bank.

---

## 2. Multi-product CVP (items 10-11, 15 points)

Two computations. Tied with single-product CVP and cost behavior for the heaviest block.

### 2a. Three methods, one answer

| Method | Build the mix from | Use when the answer wanted is |
|---|---|---|
| **Basket** | unit ratio | units of each product |
| **Weighted average** | unit ratio | total units |
| **Revenue** | revenue ratio | dollars |

They always agree. They differ only in what the answer is denominated in.

### 2b. Basket method, step by step

1. Reduce the unit volumes to a whole-number ratio. 16,000 and 6,000 becomes **8 : 3**.
2. Basket price = sum of (units in basket x each price).
3. Basket variable cost = sum of (units in basket x each variable cost).
4. Basket CM = basket price minus basket variable cost.
5. Baskets needed = (Total FC + Target Profit) / basket CM.
6. **Unpack first, then round each product up.**

**Worked (`mock-1-10`):** Trail $85 price / $49 variable cost / 16,000 units. Summit $140 / $76 /
6,000 units. Fixed costs $1,045,000.

| Step | Calculation | Result |
|---|---|---|
| Unit mix | 16,000 : 6,000 | 8 : 3 |
| Basket price | 8($85) + 3($140) | $1,100 |
| Basket variable cost | 8($49) + 3($76) | $620 |
| Basket CM | $1,100 - $620 | $480 |
| Baskets | $1,045,000 / $480 | 2,177.0833 |
| Trail | 2,177.0833 x 8 = 17,416.67 | **17,417** |
| Summit | 2,177.0833 x 3 = 6,531.25 | **6,532** |

**"Baskets are not a thing."** His words. Do not round the basket count, because a basket is an
arithmetic device, not a product. Round only the real product volumes, and round them up.

**Any proportional basket works.** His Goldman slide uses a 6 : 2 basket where the lecture used
3 : 1. The basket CM differs ($25.20 against $12.60) and the basket count differs (8,333.33 against
16,666.67), but 8,333.33 x 6 equals 16,666.67 x 3, so the unpacked product volumes are identical.
Reduce the ratio or do not; it cannot change your answer.

### 2c. Weighted average method

Weight each product's CM per unit by its share of **unit** volume.

**Worked:** calculators CM $3.80, abacuses CM $1.20, mix 3 : 1.
Weighted average CM per unit = 0.75($3.80) + 0.25($1.20) = $3.15.
Total break-even units = $210,000 / $3.15 = 66,666.67 -> **66,667 units**.

Weight by **unit** volume here. Revenue weights belong to the next method. Mixing the two is the
classic error.

### 2d. Revenue method

```
VC ratio = Total Variable Cost / Total Revenue
Break-even Revenue = (Total FC + Target Profit) / (1 - VC ratio)
```

**Worked (`ip-mp-006`, Noosh):** revenues $140,000 + $320,000 + $180,000 = $640,000; variable costs
$56,000 + $160,000 + $90,000 = $306,000. VC ratio 0.478125. Fixed $150,000.
Break-even revenue = $150,000 / 0.521875 = **$287,425.15**.

To split a revenue answer by product, use each product's **share of revenue**, not its share of
units.

### 2e. Mix is an assumption, and it dominates

> **There is no single multi-product break-even.** Every answer is conditional on an assumed mix.

Goldman, same 200,000 units and same $1.2 million of fixed cost, two mixes:

| Mix | Break-even total units |
|---|---|
| 3 standard : 1 deluxe | 160,000 |
| 9 standard : 1 deluxe | 181,819 |

A 21,819-unit swing from the mix alone. If a question changes the mix, you must recompute from
scratch; you cannot adjust the old answer.

### 2f. Unresolved in his own materials: rounding order

Two of his files handle the Goldman 9 : 1 rounding differently and land one unit apart.

| Source | Order | Answer |
|---|---|---|
| CVP Part 2 handout | unpack unrounded baskets, round each product up | 181,819 |
| Homework 9-36 | round the total up, then apply mix % to the rounded total | 181,820 |

**What to do:** use the handout's order, which is the one his lecture follows. Unpack, then round
each product up. If a multiple-choice option sits one unit from your answer, the other order is why;
take the nearer option and move on. He said you will **never** lose points for rounding.

---

## 3. Cost behavior (items 2, 4 and 16, 15 points)

Three separate computations, spread across the exam. Three distinct skills.

### 3a. Cost function versus cost behavior

These are two different cuts through the same costs, and the exam tests whether you can convert.

| Cut | Splits costs into | Used for |
|---|---|---|
| **Cost function** (GAAP) | core, meaning cost of sales, versus run-the-business, meaning operating expenses | external reporting |
| **Cost behavior** | variable versus fixed | CVP, every decision |

A GAAP income statement **cannot** be used for CVP as it stands. Cost of goods sold is not the
variable cost and selling and administrative is not the fixed cost. Both lines are mixtures.

**Rebuilding the split (`mock-1-04`):** 24,000 cabinets. Cost of goods sold $1,018,000, selling and
admin $274,000. Per cabinet: materials $17.00, labor $11.50, variable overhead $4.00, variable
selling $2.50.

| Step | Calculation | Result |
|---|---|---|
| Variable cost per unit | $17.00 + $11.50 + $4.00 + $2.50 | $35.00 |
| Total variable cost | $35.00 x 24,000 | $840,000 |
| Total cost | $1,018,000 + $274,000 | $1,292,000 |
| **Total fixed cost** | $1,292,000 - $840,000 | **$452,000** |

### 3b. High-low method

```
b  =  variable rate  =  (High cost - Low cost) / (High activity - Low activity)
a  =  total fixed    =  High cost - b(High activity)
```

His notation: **a is fixed, b is variable.** Same letters as the regression output.

> **Pick the high and low points by ACTIVITY, not by cost.**

This is the trap he plants most often. In the Dana problem November has the highest cost ($36,920)
but only 54 listings, while October has 56 listings at $36,020. Sorting by cost gives $706.29 per
listing; sorting by activity gives the correct $610.

**Worked (`mock-1-02`):** Q3 is the low at 2,800 units / $159,600. Q4 is the high at 5,600 units /
$212,800.

| Step | Calculation | Result |
|---|---|---|
| b | ($212,800 - $159,600) / (5,600 - 2,800) = $53,200 / 2,800 | $19.00 per unit |
| a | $212,800 - $19.00(5,600) = $212,800 - $106,400 | **$106,400** |
| Check at the low point | $159,600 - $19.00(2,800) = $159,600 - $53,200 | $106,400 OK |

**Always run the check at the other point.** If the two intercepts disagree by more than rounding,
your slope is wrong. It costs five seconds and catches nearly every arithmetic slip.

### 3c. Step costs

A cost that is fixed within a band and jumps at the boundary. You cannot hire 0.6 of a technician.

**Worked (`mock-1-16`):** technicians $7,400 each, capacity 500 visits, other fixed $46,000,
supplies $19 per visit, volume 1,640 visits.

| Step | Calculation | Result |
|---|---|---|
| Technicians | 1,640 / 500 = 3.28, round **up** | 4 |
| Technician cost | 4 x $7,400 | $29,600 |
| Other fixed | | $46,000 |
| Supplies | $19 x 1,640 | $31,160 |
| **Total cost** | | **$106,760** |

Averaging the technician cost to $14.80 per visit gives $101,320 and understates the total, because
the fourth technician is only 28% used. The relevant range here is 1,501 to 2,000 visits.

### 3d. Relevant range

Every cost function is only valid over the range you observed. Inside it you interpolate with
confidence. Outside it the linear assumption fails: fixed costs step, volume discounts kick in,
overtime starts. If a question pushes you far outside the data, say so.

### 3e. High-low versus regression

| | High-low | Regression |
|---|---|---|
| Data used | **two points only** | **all points** |
| That is a | weakness | strength |
| Speed | instant, by hand | needs Excel |

His framing: high-low "essentially ignores the rest of the data"; regression "plots a line of best
fit between all data points" where the slope is the variable cost and the y-intercept is the total
fixed cost. High-low survives because it is fast, which is also why it is on the exam.

---

## 4. Regression (items 5-6, 10 points)

Two computations. This block is pure pattern recognition: pick the right standard error, multiply by
the right t value.

### 4a. Reading his output

The Excel Regression output has **three different standard errors**, and choosing between them is
the whole topic.

| Standard error | Where it sits | Use it for |
|---|---|---|
| **Standard Error of the regression** | top block, Regression Statistics | an interval around a **total cost estimate** |
| **Intercept's standard error** | coefficient table, Intercept row | an interval around **fixed cost** |
| **Slope's standard error** | coefficient table, driver row | an interval around **variable cost** |

> A **coefficient** interval uses that coefficient's own standard error.
> A **total cost** interval uses the regression's standard error.

His words on the total-cost case: "I don't use either. I use the standard error for the regression as
a whole." This is the most likely regression trap on the exam.

### 4b. Confidence intervals

```
Interval  =  Point Estimate  +/-  ( t  x  the appropriate standard error )
```

Degrees of freedom = **n - 2**. With 8 observations, df = 6.

t values at 6 df, which he provides:

| Confidence | 70% | 80% | 90% | 95% |
|---|---|---|---|---|
| t | 1.134 | 1.440 | 1.943 | 2.447 |

Lower confidence gives a narrower interval. Being less sure lets you make a tighter claim.

**Sailmaster, his worked examples.** Intercept $49,701.29 (SE 25,332.98), slope $687.43 (SE 87.06),
regression SE 27,771.27, n = 8.

| Question | Standard error used | Calculation | Interval |
|---|---|---|---|
| 80% CI on variable cost | slope, 87.06 | $687.43 +/- 1.440(87.06) = +/- $125.37 | **$562.06 to $812.80** |
| 70% CI on fixed cost | intercept, 25,332.98 | $49,701.29 +/- 1.134(25,332.98) = +/- $28,727.60 | **$20,973.70 to $78,428.89** |
| 95% CI on total cost at 325 boats | regression, 27,771.27 | point $273,116.04 +/- 2.447(27,771.27) = +/- $67,956.30 | **$205,159.74 to $341,072.34** |

For that last one the point estimate comes first:
$49,701.29 + $687.43(325) = $49,701.29 + $223,414.75 = $273,116.04.

**Build point estimates from the printed, rounded coefficients.** Use 687.43 and 49,701.29 exactly as
shown. Excel's own Lower 95% and Upper 95% columns are computed from unrounded standard errors, so
they can sit a few cents off your hand calculation. On the slope at 95% the ToolPak prints 474.42 and
900.45 where hand arithmetic gives 474.39 and 900.47. Either is accepted; do not chase cents.

He says "confidence interval around this estimate". He never uses the phrase "prediction interval".

### 4c. t stats and p-values

```
t  =  coefficient / its own standard error
```

| t stat | His reading |
|---|---|
| 2 or more | the coefficient is useful |
| more than 3 | essentially no chance the true coefficient is zero |

He reads a **p-value** as the probability that the true coefficient is zero, and wants it below 0.05.

**Sailmaster intercept:** t = 1.96, p = 0.0974. His own interpretation, verbatim: "There is a 9.74
percent chance that the true fixed cost at Sailmaster is 0." So the fixed cost is only marginally
supported. The slope, at t = 7.90 and p = 0.0002, is solid.

A wide confidence interval and a weak p-value are two views of the same fact. The 90% interval on
that intercept runs from $479.31 to $98,923.27, which very nearly includes zero.

### 4d. Which R to report

Report **adjusted R squared**, range 0 to 1. It penalizes added variables, so it does not improve
just because you threw another column at the model.

---

## 5. Cost accounting, the planes problem (items 14-15, 10 points)

Two computations, from the session 2 paper airplanes exercise. Expect operating profit and the value
of ending inventory.

### 5a. The core idea

Manufacturing costs **attach to units** and follow them. They leave the balance sheet only when the
unit is sold. Selling and administrative costs are **period costs** and are expensed now, whatever
happens to inventory.

| Cost | Attaches to units? | Where unsold units' share sits |
|---|---|---|
| Direct materials | yes | inventory |
| Direct labor | yes | inventory |
| Variable overhead | yes | inventory |
| **Fixed** manufacturing overhead | **yes** | inventory |
| Selling and administrative | no | expensed in full |

Fixed manufacturing overhead going into inventory is the part people get wrong.

### 5b. Units of production

His term is **units of production**. He never says "equivalent units". Same idea: partially finished
work counted as a fraction of a whole unit.

**You need separate denominators for materials and for conversion**, because materials usually go in
at the start and labor goes in gradually.

**Worked (`ip-plane-001` and `ip-plane-002`):** 23 planes started, 18 completed and sold, 5 in
ending work-in-process at 60% complete for labor and overhead, materials 100% complete. Price $30,
materials $2.50 per sheet, labor $16 x 4 folders = $64, overhead $16 x 2 staffers + $175 = $207.

| Step | Calculation | Result |
|---|---|---|
| Units of production, materials | 18 + 5 | 23 units |
| Units of production, labor and overhead | 18 + (5 x 60%) | 21 units |
| Materials rate | $2.50 per sheet | $2.50 |
| Labor rate | $64 / 21 | $3.0476 |
| Overhead rate | $207 / 21 | $9.8571 |

Operating profit, costing only the 18 sold:

| Line | Calculation | Amount |
|---|---|---|
| Revenue | 18 x $30 | $540.00 |
| Direct materials | 18 x $2.50 | (45.00) |
| Direct labor | $3.0476 x 18 | (54.86) |
| Overhead | $9.8571 x 18 | (177.43) |
| **Operating profit** | | **$262.72** |

Ending inventory, the 5 unfinished planes:

| Line | Calculation | Amount |
|---|---|---|
| Materials | 5 x $2.50 | $12.50 |
| Labor | $3.0476 x (5 x 60%) | 9.14 |
| Overhead | $9.8571 x (5 x 60%) | 29.57 |
| **Ending inventory** | | **$51.21** |

**Always tie it out.** What was expensed plus what sits in inventory must equal what was spent:
$277.29 + $51.21 = $328.50, which equals materials $57.50 (23 x $2.50) + labor $64 + overhead $207.
If that does not tie, something is wrong.

**The trap:** dividing everything by 23. Materials and conversion have different denominators, 23
and 21. Using one rate for both gives the wrong profit.

### 5c. Absorption costing lets you move profit with production

A manager can raise reported income **without selling anything extra**, by producing more. The extra
units absorb a share of fixed overhead, which moves from the income statement to the balance sheet.
That is why production volume is a lever on reported profit, and why it matters.

The matching error in the exercise: a group charged all 21 planes they worked on to the income
statement though only 18 were sold. The 3 unsold planes belong on the balance sheet as inventory.

### 5d. Why allocation misleads (session 1 background)

Allocated cost is not avoidable cost. Three cases he used:

| Case | The error |
|---|---|
| Chevy Volt "losing $49,000 per car" | spreading $1.2B of development over only the cars sold so far; the development cost is sunk and does not change per car sold |
| Dropping a client | its allocated overhead does not leave with it; firm-wide overhead is unchanged and the remaining clients absorb more |
| The profitable paralegal | billings minus salary ignores the support costs she consumes; the better question is incremental |

**For decisions, use avoidable and incremental cost.** Full absorption costing is right for one
purpose: external reporting under GAAP, that is, valuing inventory and cost of goods sold.

### Thin spot
This block is 10 points and rests on a single in-class exercise. The bank has 18 questions tagged
14-15, but only two of them are the instructor's own worked planes computation. If you have time
after the CVP blocks, redo `ip-plane-001` and `ip-plane-002` from a blank sheet until the two
denominators are automatic.

---

## 6. TenAlpina Case 1 (item 17, 10 points)

**50 words or fewer.** Not a computation. The case facts are supplied in the exam.

### What he said about the case questions
- They are **not computational** and do not require recalling case details.
- Word limits are deliberate: "You just don't have enough words to just kind of splash it all out
  there and hope the right answer is in there somewhere."
- "Read them carefully and make sure you're answering the right question and not just doing sort of
  a brain dump."

### The analysis method
Case 1 is a cost-structure question: the same labor cost treated as variable in one scenario and
fixed in another, and what that does to risk and to profit as volume moves.

| Treat labor as | CM per unit | Fixed cost | Consequence |
|---|---|---|---|
| Variable | low | low | low break-even, profit grows slowly with volume |
| Fixed | high | high | high break-even, profit grows fast with volume |

Identical profit at today's volume, completely different exposure if volume moves. That is operating
leverage, and it is the point of the case.

### How to write 50 words
1. **Recommendation first.** One sentence.
2. **The two numbers that drive it.** One sentence.
3. **The one caveat.** One sentence.

No preamble, no restating the question, no listing what you are about to say. Under this limit a
wasted clause is a lost mark. Practise on `mock-1-17`, then count the words.

### Thin spot, and an honest warning
**This section contains no TenAlpina case facts, names or figures, by design.** The syllabus states
that feeding case documents into an AI tool is not permitted for any purpose, so nothing in this pack
was built from the case narratives. What you have here is the analysis method and the writing format.
**Work the case itself from the case documents.** That is 10 points this pack cannot prepare for you.

---

## 7. TenAlpina Case 2 (item 18, 10 points)

**90 words or fewer.** Not a computation.

### The analysis method
Case 2 is a shared-cost and product-line question. Four things to be able to say:

| Point | The content |
|---|---|
| What allocation changes | reported profit by line, and nothing else |
| What it does not change | total company profit, and any cash flow |
| What should drive the basis | what actually causes the shared cost, not convenience |
| The decision it can wrongly trigger | dropping a line that still contributes |

**The figure to judge a line on:** contribution margin less that line's **avoidable** fixed costs.
Not its allocated share. If a line's revenue covers its own variable and avoidable fixed costs,
dropping it leaves the shared cost behind and total profit falls.

### Multi-product CVP shows up here too
The hammer-line material joins this case to section 2. Break-even across two products at a 12 : 1
unit mix, and a revenue split at the break-even point.

One worked detail worth carrying: at a 12 : 1 **unit** mix the **revenue** mix was about 2 : 1, and
he multiplied break-even revenue of $54,731 by 33% to get hammer revenue of **$18,061**. The exact
revenue share is 32.62%, which gives $17,853. His rounded 2 : 1 is the one he worked on the board.
If two options sit about $200 apart, that is why.

### How to write 90 words
Roughly four or five sentences, one per requirement above. Write the four-part answer, then cut
adjectives rather than content. **Finish with the recommendation**, because a truncated answer loses
its conclusion. Practise on `mock-1-18`.

### Thin spot
Same warning as section 6. **No TenAlpina case facts are in this pack.** Method and format only.

---

## 8. CVP short question (item 3, 5 points)

One short written answer. The likely subjects are the conceptual traps, not arithmetic.

**Be able to state, in three or four sentences:**

| Prompt | The answer |
|---|---|
| Why you cannot unitize fixed cost | total fixed cost does not change with volume, so fixed cost per unit falls as volume rises; it is valid only at the volume where it was computed |
| Why a GAAP statement will not do for CVP | it splits core versus run-the-business, not variable versus fixed; cost of goods sold and selling and admin are both mixtures |
| What contribution margin means | revenue less **all** variable costs, wherever they sit on the statement; what each unit contributes toward fixed cost and then profit |
| What CVP is used for | pricing, fixed-for-variable technology swaps, outsourcing, target profit. **Not** quality control specifications |
| Why margin of safety has two percentages | the denominator follows the question: above break-even divides by break-even, how far sales can fall divides by current sales |

Work `mock-1-03`, which is the unitizing trap in a classmate's voice.

---

## 9. Degree of operating leverage (item 12, 5 points)

One computation. Short and reliably worth all 5 marks.

```
DOL  =  Total Contribution Margin  /  Operating Profit
```

**Total contribution margin in dollars.** Never the CM ratio, never a percentage, never revenue.

```
DOL  x  % change in Revenue  =  % change in Operating Profit
```

**Worked (`mock-1-12`):** 19,000 units, price $96, variable cost $52, fixed cost $528,000.

| Step | Calculation | Result |
|---|---|---|
| Total CM | $44 x 19,000 | $836,000 |
| Operating profit | $836,000 - $528,000 | $308,000 |
| **DOL** | $836,000 / $308,000 | **2.71** |

A 10% revenue rise lifts operating profit 27.1%. A 10% fall cuts it 27.1%. **It cuts both ways**, and
he asks it in the falling direction as often as the rising one.

**DOL is a point-in-time number.** As soon as volume moves, DOL changes. Do not reuse one DOL for a
second step.

---

## 10. Operating leverage, short question (item 13, 5 points)

One short written answer, and the distinction below is almost certainly what it is testing.

| Term | What it is |
|---|---|
| **Operating leverage** | a characteristic of the cost structure: how much of total cost is fixed. Stable |
| **Degree of operating leverage** | a point-in-time sensitivity measured at today's volume. Changes as volume moves |

**High operating leverage means:** more fixed cost, higher contribution margin per unit, higher
break-even, smaller margin of safety, and profit that swings harder in **both** directions.

**Worked comparison (`dr-dol-003`).** Two firms, 12,000 units at $200, identical profit today.

| | Alpine | Basin |
|---|---|---|
| Variable cost per unit | $140 | $90 |
| Fixed costs | $300,000 | $850,000 |
| Operating profit at 12,000 | $420,000 | $470,000 |
| DOL | 1.71 | 2.81 |
| Break-even units | 5,000 | 7,728 |
| Profit after a 20% revenue fall | $276,000 | **$206,000** |

Basin trades variable cost for fixed cost. It earns more at volume and loses more when volume falls.

**The fixed-for-variable swap is the standard question.** Buying equipment instead of paying a
per-unit royalty, or replacing assembly-line labor with machinery, raises operating leverage. Note
that it **raises** break-even even though unit cost falls: see `ip-mos-009`, where a $30 cut in unit
labor plus $250,000 more fixed cost pushes break-even **up** by 293 units.

### Thin spot
**The thinnest block in the pack.** 5 points, and the bank holds only 2 questions tagged item 13
against 9 for DOL. The table above and `mock-1-13` are the preparation. Make sure you can write the
operating leverage versus DOL distinction cold.

---

## Rounding rules, collected

| Situation | Rule |
|---|---|
| Break-even in units | **round up** |
| Required volume for a target profit | **round up** |
| Baskets in multi-product CVP | **do not round**, "baskets are not a thing" |
| Product volumes unpacked from baskets | round each **up**, after unpacking |
| Regression point estimates | build from the **printed rounded** coefficients |
| Everything else | he said you will **never** lose points for rounding errors |

---

## Exam mechanics

| Item | Detail |
|---|---|
| Window | opens Thu 2026-10-22 11:00 AM, closes Sat 2026-10-31 11:59 PM MDT |
| Time | 2 hours 15 minutes once started |
| Items | 18 numbered, 100 points. In class he said 19; the blueprint slide shows 18 summing to 100 |
| Proctoring | Proctorio |
| Notes | one 8.5x11 sheet, **handwritten**, front and back |
| Excel | allowed, must be **blank** at the start |
| Banned | GoalSeek, Solver, any AI resource during the exam |
| Second chance | a "Second Chance Exam 1" window is listed Nov 4-8, marked uncertain on the schedule |

**On the handwritten sheet,** his reasoning: "A lot of the learning that you haven't had so far will
take place in that handwriting notes and I support that." Writing the sheet is part of the
preparation. See `click-notes.md` for what to put on it, and read the caution at the top of that file
first.

**Budget your time.** 65 points of computation across 13 items, 2 hours 15 minutes. That is roughly
6 minutes per computation with about 30 minutes left for the two case answers and the two short
questions. The case answers are 20 points for maybe 140 words; do not leave them to the last five
minutes.

---

## What this pack does not cover

Stated plainly, so you know where the gaps are.

1. **TenAlpina case facts.** Nothing. By design, per the syllabus policy on feeding case documents to
   AI tools. That is 20 of the 100 points. Work both cases from the case documents.
2. **Item 13, operating leverage short answer.** 2 questions in the bank. Thin.
3. **Whether the Excel Analysis ToolPak is permitted.** The logistics ban GoalSeek and Solver by
   name and say nothing about the ToolPak on a blank workbook. **Unverified.** The regression items
   are solvable from a printed output block without it, which is how this pack drills them. If you
   would need it to run a regression from raw data, ask Prof. Smith first.
4. **Whether AI-derived content may go on the handwritten sheet.** The syllabus bans AI tools *on*
   the exam and bans feeding case documents to AI tools. It does not address transcribing
   AI-assisted study notes onto the permitted sheet. **Ask before you rely on it.**
5. **The 47,370 figure** on his high-leverage slide reconciles to neither 47,369 nor the $322,100 /
   $6.80 = 47,367.65 the surrounding numbers imply. Minor, and unresolved.
