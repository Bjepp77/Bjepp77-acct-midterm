# Managerial Accounting — Exam 1 Study Guide

Built from the seven class transcripts, sessions 1 through 7 (2026-09-03 to 2026-10-22).
Every number below is traced to a session. Where the auto-transcript garbled a figure, the
guide gives the figure that makes the professor's own arithmetic close, and says so.

---

## 0. Exam logistics

| Item | Detail |
|---|---|
| Window | Opens Thu 2026-10-22, 11:00 AM, after class. Closes midnight Sat 2026-10-31 |
| Questions | 19 |
| Mix | Mostly multiple-choice computational. Some short essay, primarily about the cases |
| Time | 2 hours 15 minutes |
| Proctoring | Proctorio, light settings. On campus or the testing center |
| Notes | One sheet of **handwritten** notes. Front and back is fine |
| Excel | Allowed, but **must begin blank**. No prefab templates, no notes typed in Excel |
| Case files | **Not** allowed during the exam |
| Last question | Conceptual, drawn from the session 7 (10-22) hammer-line discussion |
| Practice | Problems plus a solution file are posted to Canvas |
| No class | Thu 2026-10-29 |

Two warnings the professor gave about the essay questions:

1. Word limits are tight by design. Answer the specific question asked. Do not brain-dump
   everything you know about a concept hoping something lands.
2. The case questions are not computational and do not require you to recall case details.
   They are about the conclusions the class reached in discussion.

**Final exam** covers sessions 8 through 11 only. It is not comprehensive.

---

## 1. The one equation (the "home equation")

The professor calls this "the one formula to rule them all." His advice when a problem looks
unfamiliar: "when in doubt, just go home" — write the home equation, plug in what you know,
solve for what you don't.

```
Revenue  -  Variable cost  -  Fixed cost  =  Operating income
```

Four interchangeable forms. Which one you use depends on what X is.

| Form | Equation | X is |
|---|---|---|
| Unit | (Price × Q) − (VC/unit × Q) − FC = Profit | volume |
| Contribution | (Price − VC/unit) × Q − FC = Profit | volume |
| Percent | Rev − (Rev × VC%) − FC = Profit | revenue dollars |
| Ratio | CM% × Rev − FC = Profit | revenue dollars |

### Scaling rule (memorize this one)

| You divide fixed cost by | You get |
|---|---|
| A **dollar** value (CM per unit) | A **volume** answer (units) |
| A **percentage** (CM ratio) | A **dollar** answer (revenue) |

### Never unitize fixed cost

Fixed cost per unit is what the professor calls "a spready number." It changes with volume,
which is the one thing it is not supposed to do. In the home equation, **fixed cost is left
alone in full**. There is no step where you divide it by units.

### Derived identities

```
CM per unit   = Price per unit - VC per unit
CM ratio      = CM / Revenue        (also = CM per unit / Price)
VC ratio      = VC / Revenue        (also = VC per unit / Price)
CM ratio + VC ratio = 100%          "two sides of the revenue coin"
```

### Break-even and target profit

```
Break-even units    = FC / CM per unit
Break-even revenue  = FC / CM ratio
Target-profit units = (FC + target operating income) / CM per unit
```

For target profit, the honest method is to put the target on the right side of the home
equation instead of zero. The shortcut above is the same thing after algebra.

### Relevant range

"Variable" and "fixed" are linear simplifications that hold only inside the relevant range.
Economists object to the straight lines; accountants accept them inside a limited band of
activity. If a problem pushes volume far outside the observed data, the labels stop holding.

---

## 2. Worked example: the calculator problem (session 3)

This one example reappears in sessions 3, 6 and in the practice set. Learn it cold.

**Given**

| Item | Total | Per unit |
|---|---:|---:|
| Volume | 60,000 units | |
| Revenue | $480,000 | $8.00 |
| Variable cost | $252,000 | $4.20 |
| Contribution margin | $228,000 | $3.80 |
| Fixed cost | $180,000 | leave alone |
| Operating income | $48,000 | |

**Step 1. Unitize the variable items only.**

| | Calculation | Result |
|---|---|---:|
| Price | 480,000 / 60,000 | $8.00 |
| VC per unit | 252,000 / 60,000 | $4.20 |
| CM per unit | 8.00 − 4.20 | $3.80 |

**Step 2. Ratios.**

| | Calculation | Result |
|---|---|---:|
| VC ratio | 4.20 / 8.00 | 52.5% |
| CM ratio | 3.80 / 8.00, or 228,000 / 480,000 | 47.5% |

**Step 3. Break-even in units.**

```
8.00x - 4.20x - 180,000 = 0
3.80x = 180,000
x = 47,368.42  ->  47,369 units
```

**Step 4. Break-even in revenue.** Three routes, same answer.

| Route | Calculation | Result |
|---|---|---:|
| Ratio | 180,000 / 0.475 | $378,947.37 |
| Percent form | x − 0.525x − 180,000 = 0 | $378,947.37 |
| Units × price | 47,368.42 × 8.00 | $378,947.37 |

**Step 5. Target operating income of $120,000.**

```
3.80x = 180,000 + 120,000 = 300,000
x = 78,947.37  ->  78,948 units
```

**Traps on this problem**

- Asked for revenue dollars, X is revenue and the variable term is `0.525 × X`. It is **not**
  `$8 × volume`. Getting this backwards is the single most common error here.
- Rounding: the professor said flatly "you would never lose points for rounding errors," and
  he designs questions to avoid rounding traps. Do not burn time on it.
- You cannot sell a partial calculator, so unit break-even rounds **up**.

---

## 3. Operating leverage and DOL

**Operating leverage** is the mix of fixed to variable cost. It is a structural fact about how
a firm is built. Do not confuse it with **financial leverage**, which is debt versus equity.

```
DOL = Total contribution margin (dollars) / Operating income (dollars)

% change in operating income = DOL x % change in sales
```

Two things that cost points:

1. DOL uses **total contribution margin in dollars**, not the CM ratio and not a percentage.
2. DOL is symmetric. A DOL of 4.75 means a 20% sales drop cuts operating income by 95%, the
   same magnitude as a 20% rise. "Leverage giveth and leverage taketh away."

**Worked, continuing the calculator problem**

| | Calculation | Result |
|---|---|---:|
| DOL | 228,000 / 48,000 | 4.75 |
| Sales +20% | 4.75 × 20% | +95% income |
| Check: new CM | 228,000 × 1.20 | $273,600 |
| Check: new op income | 273,600 − 180,000 | $93,600 |
| Check: % change | (93,600 − 48,000) / 48,000 | +95% |

(The transcript says "93,000" and "1.95" here. Both are transcription noise; $93,600 and 95%
are what the professor's own numbers produce.)

### DOL is unstable — this is an exam-worthy concept

DOL is not a clean measure of cost structure, because it conflates two different things:

| Driver of a high DOL | What it means |
|---|---|
| Heavy fixed-cost intensity | genuine structural leverage |
| Sitting close to break-even | small denominator, nothing about structure |

DOL is largest near break-even and shrinks as you move away from it, even with the cost
structure held completely constant. So DOL alone is not interpretable. Its value is in the
sensitivity statement it produces.

### Same break-even, different risk

The professor's illustration: hold break-even at 47,369 units and change the cost structure.

| | Original | High-leverage alternative |
|---|---:|---:|
| VC per unit | $4.20 | $1.20 |
| Fixed cost | $180,000 | $322,100 |
| Break-even | 47,369 | 47,369 |

Identical break-even. The high-leverage version loses more below it and earns more above it.
On the CVP graph, raising fixed cost lifts the total-cost intercept and flattens its slope, so
both the loss wedge and the profit wedge get bigger.

---

## 4. Cost estimation

### 4a. High-low method (session 5)

Fit a line through exactly two data points. The slope is the variable rate, and the intercept
falls out of either point.

```
Variable rate (m) = (Cost at high - Cost at low) / (Activity at high - Activity at low)
Fixed cost (b)    = Total cost at a point - (m x Activity at that point)
```

**Worked: Stanley's power bill**

| | Value |
|---|---:|
| Cost at 1,300 units | $1,962 |
| Cost at 1,000 units | $1,908 |
| Rise | $54 |
| Run | 300 units |
| Variable rate | $0.18 per unit |
| Fixed portion | 1,908 − (0.18 × 1,000) = **$1,728** |

(The transcript wavers between 1,729 and 1,728. 1,728 is correct.)

A **mixed cost** has a fixed piece and a variable piece. Two data points are enough to split it.

### 4b. Regression (session 4)

Same line, more data. Excel's Data Analysis ToolPak produces the output. The intercept is
fixed cost; the slope is the variable rate.

**Sail Master, 8 observations of total cost against boats**

```
Total cost = $49,701.29 + $687.43 per boat
```

| Output line | Value | How to read it |
|---|---:|---|
| Multiple R | 0.955 | Correlation. Range −1 to 1. Direction and strength |
| Adjusted R² | 89.8% | Share of variation in Y explained by X. **Always use adjusted** |
| Standard error (regression) | $27,771 | Average distance from point to line |
| Observations | 8 | |
| Significance F | very small | P value for the whole model |
| Intercept coefficient | $49,701.29 | Fixed cost |
| Intercept t stat | 1.96 | |
| Intercept P value | 0.0974 | Above 0.05, so you **cannot** reject a zero fixed cost |
| Slope coefficient | $687.43 | Variable cost rate |
| Slope standard error | 87.06 | |
| Slope t stat | 7.9 | 687.43 / 87.06 |
| Slope P value | very small | Reject the null; the rate is not zero |

**Relationships to know**

```
t stat = Coefficient / its Standard error
F      = (t stat on the slope) squared
Degrees of freedom = n - (number of parameters estimated)
                   = n - 2 for simple regression   (here 8 - 2 = 6)
                   = n - 3 or n - 4 for multiple regression
```

**Null hypothesis.** Start by assuming every relationship is zero. The P value is the
probability of observing this coefficient if the truth were zero. Threshold 0.05.

**Confidence interval on a coefficient**

```
Estimate  +/-  (its own standard error  x  t)
```

t for 6 df: **2.447** at 95%, **1.943** at 90%. Lower confidence gives a narrower interval.

Slope at 95%: 687.43 ± (87.06 × 2.447) = 687.43 ± 213.04 → **$474.39 to $900.47**

**Confidence interval on a total-cost prediction — different standard error**

This is the distinction most likely to be tested.

```
Point estimate = Intercept + (Slope x Volume)
Interval       = Point estimate  +/-  (t  x  standard error OF THE REGRESSION)
```

You use the regression's standard error ($27,771), **not** either coefficient's standard error.

**Worked at 400 boats**

| Step | Calculation | Result |
|---|---|---:|
| Point estimate | 49,701.29 + 687.43 × 400 | $324,675.14 |
| Half-width | 2.447 × 27,771 | $67,955.6 |
| Lower bound | 324,675.14 − 67,956.29 | $256,718.85 |
| Upper bound | 324,675.14 + 67,956.28 | $392,631.42 |

(Both bounds are his own numbers off the Excel output. Reproducing them by hand needs the
unrounded standard error, around 27,771.3, not the printed 27,771, so the half-width is about
$67,956.3 rather than $67,955.6. Recomputing the point estimate from the rounded coefficients
gives $324,673.29, a $1.85 gap for the same reason. Method is right; the last dollar is Excel's
extra decimals. On the exam, read the bounds straight off the output.)

That interval is enormous, and the professor's point is that a CEO will say so. The only two
fixes: accept lower confidence, or get more data.

**Regression traps**

- **Spurious correlation.** Regression is a tool, not a judgment. It will not tell you which
  costs are fixed and which are variable. Ask whether the relationship makes sense.
- Every coefficient is an estimate and is "inherently and by definition wrong." The
  probability the true rate is exactly $687.43 is **zero** — it is a continuous distribution.
- A t stat is a count of standard errors from zero. It is not a percentage.
- Correlation ranges −1 to 1. R² ranges 0 to 1.
- In Excel, leaving the **Labels** box ticked when the top row is data corrupts the output.
- The intercept's P value being above 0.05 matters less in practice here, because the firm
  never operates at zero volume.

---

## 5. Allocation, and why it misleads (session 1)

```
Allocation rate = Total indirect cost pool / Total units of the driver
```

**Worked:** the consulting case allocated overhead at **$114.02 per student hour**. Each
client's allocated overhead is that rate times the client's student hours.

**Vocabulary**

| Term | Definition as given |
|---|---|
| Cost object | The thing you are asking "what does this cost me?" about. Here, a client |
| Driver | The activity base used to spread costs that are not directly traceable |
| Distortion | What you get when the driver is not correlated with or causing the cost |
| Management accounting | "Run the business accounting, not report the business." Not bound by GAAP, IRS or FASB |

### The central lesson

Allocation **moves** overhead between cost objects. It does not change the firm's total.

When the class deleted the lost client and its student hours, firm-wide profit did not move.
The overhead simply landed on the remaining clients. Every client then looked profitable while
firm profit was unchanged. The professor's verdict on that rosier-looking column: "just as
misleading as the other."

**The test for a bad driver.** When the professor removed a different client, total overhead
went *up*, not down. Conclusion: the cost "doesn't appear to be student hours." A driver that
fails this test produces distortion "as egregious or more" than the one you started with.

### Do not take allocated cost into a negotiation

The professor's most pointed warning of the semester. On being told the allocated numbers
justify a price position: "Resist that call." Allocation "just distorted the map," and it
"might even make us behave in a negotiation in exactly the opposite way that would be the best
for our business." The sibling argument to resist is "we need more clients to spread the
overhead."

### The denominator effect

Spreading a fixed or sunk amount over more units lowers cost per unit without changing any
cash flow. It is an accounting fiction.

**The Chevy Volt (Reuters, 2012).** The reported "loss of as much as $49,000 per car" came from
dividing roughly $1.2B of development and tooling over 21,500 cars sold, about $56,000 per car,
and adding $20,000 to $32,000 of actual build cost. The error is combining sunk investment and
operating cost in one numerator. Investment has its own metrics: **ROI** and **payback**.

**The BYU credit-hour example.** Cutting average credits at graduation from about 153 to 135
produces a headline saving of "over $100,000 per student" that will never show up as cash.

### The paralegal fallacy

A paralegal bills $150/hour, is paid $60,000/year, and brought in almost $300,000. Revenue
minus direct labor says enormously profitable. That ignores overhead entirely. The better
question is counterfactual: **"If you quit, where would we be?"**

### When full allocation *is* right

| Use | Full absorption appropriate? |
|---|---|
| External GAAP reporting | Yes, required |
| Long-run pricing and product mix | Yes |
| A specific short-term decision | No — use incremental |

Accounting software and the general ledger default to allocating everything, which answers a
different question than the one you are usually asking. Do not lift a QuickBooks P&L into a
decision. The professor's recurring question: **"Why do you want to know?"** The right
calculation depends on the answer.

---

## 6. Cost versus expense, and equivalent units (session 2)

| Term | Definition |
|---|---|
| Cost | A spend |
| Expense | An expired cost, on the income statement |
| Capitalized | A cost attached to unexpired units; sits on the balance sheet as inventory |
| WIP | Work in process |
| Equivalent units | "A fancy word for a measure of work done" |
| Direct labor | Production labor traceable to the unit |
| Indirect labor | Supervisor, accountant. Rolls into overhead |
| Manufacturing overhead | Production-related cost not directly traceable to a unit |

```
Equivalent units  = (units completed and sold x 100%)  +  (ending units x % complete)
Rate per category = Category spend / Equivalent units for THAT category
To income statement = Rate x units sold
To balance sheet    = Rate x equivalent units in ending inventory
Check: income statement amount + balance sheet amount = total spend, per category
```

### Worked: the paper airplane run

**Given.** Spend of $30 direct labor, $120 manufacturing overhead, $15 direct materials, total
$165. Eleven planes completed and sold, four unfinished. Completion judgments: materials 100%,
labor 25%, overhead 25% (overhead is applied on a labor basis).

**Step 1. Equivalent units, one category at a time.**

| Category | Calculation | EU |
|---|---|---:|
| Direct materials | 11 + (4 × 100%) | 15 |
| Direct labor | 11 + (4 × 25%) | 12 |
| Overhead | 11 + (4 × 25%) | 12 |

**Step 2. Rates.**

| Category | Calculation | Rate |
|---|---|---:|
| Direct materials | $15 / 15 | $1.00 |
| Direct labor | $30 / 12 | $2.50 |
| Overhead | $120 / 12 | $10.00 |

**Step 3. Split the spend.**

| Category | To income statement (× 11) | To balance sheet (× EU in WIP) | Total |
|---|---:|---:|---:|
| Direct materials | $11.00 | 4 × 1.00 = $4.00 | $15.00 |
| Direct labor | $27.50 | 1 × 2.50 = $2.50 | $30.00 |
| Overhead | $110.00 | 1 × 10.00 = $10.00 | $120.00 |
| **Total** | **$148.50** | **$16.50** | **$165.00** |

**Step 4. Income statement.**

| | |
|---|---:|
| Revenue (11 × $10) | $110.00 |
| Cost of goods sold | (148.50) |
| **Operating loss** | **($38.50)** |

**Step 5. The check that catches everything.** $148.50 expensed + $16.50 in ending WIP =
$165.00 spent. Every dollar spent must be accounted for in one place or the other.

**Traps**

- Do not expense every plane you *worked on*. Only the ones **sold**. Unsold WIP is an asset.
- Do not "conglomerate the rates." Materials, labor and overhead get separate rates because
  they are consumed at different rates.
- Use **equivalent** units in the denominator, not physical units. Materials happen to match,
  because all material goes in at the start.
- The overhead driver does not have to equal the labor driver. Machine time is another option.
- The professor said he would **never** ask you to build a T-account.

### The perverse incentive

Because absorption costing parks labor and overhead in inventory, producing more than you can
sell lowers expensed cost per unit and **raises** reported income, with no improvement in the
business. Two papers were assigned on this:

| Paper | Finding |
|---|---|
| Contemporary Accounting Research, 2011 | Interviews at an automaker; managers overproduced to drive down per-vehicle fixed cost, because operating margin under absorption costing drove their performance pay. A quarter of 2004 vehicles sat over 60 days, and a $5M loss followed in 2005 |
| Journal of Management Accounting Research | Firms raise production relative to sales to shift fixed cost into inventory. Markets reward inventory growth, but discount the signal for repeat manipulators |

The point is not that absorption costing is bad. It is correct for external reporting. The
point is that current-period incentive pay layered on top of it "can cause all kinds of
behaviors that ignore the downstream consequences."

---

## 7. CVP with taxes and target returns (session 6)

Operating income in the home equation is a **pre-tax** number. If the target is stated after
tax, convert it up before you use it.

```
Grossing up:  Operating income target = After-tax net income target / (1 - tax rate)
```

**Worked.** After-tax target $500,000, tax rate 30%.
`500,000 / (1 − 0.30) = $714,286`

### When the target is a return, not a dollar

```
Step 1: Return % x base (equity or assets)  =  after-tax net income target
Step 2: Gross up that target for taxes
Step 3: Put the result on the right side of the home equation
```

**Worked.** ROE target 25% on equity of $300,000 → 0.25 × 300,000 = $75,000 after tax, then
gross up.

This is as far as the course goes with taxes.

### Worked: the video game price problem

**Given.** 25,000 units, VC $40/unit, fixed cost $120,000, equity $300,000, ROE target 30%,
tax rate 40%. **The unknown is price, not volume.**

| Step | Calculation | Result |
|---|---|---:|
| 1. After-tax target | 0.30 × 300,000 | $90,000 |
| 2. Gross up | 90,000 / (1 − 0.40) | $150,000 |
| 3. Home equation | 25,000P − (40 × 25,000) − 120,000 = 150,000 | |
| 4. Collect | 25,000P = 150,000 + 120,000 + 1,000,000 | $1,270,000 |
| 5. Solve | 1,270,000 / 25,000 | **$50.80** |

**Traps**

- Identify X first. Here X is price, so revenue is `25,000 × P`, not `$X`.
- A return target is after tax. Gross it up. Forgetting this understates the needed price.
- Do not recompute per-unit data the problem already gives you.
- A target stated as a percent of sales (not of equity) puts X on both sides of the equation.
  That is fine — collect terms. Example, the Tom Flannery restaurant: pre-tax profit of at
  least 20% of sales, fixed $24,000/yr, variable about 40% of sales.
  `x − 0.4x − 24,000 = 0.2x` → `0.4x = 24,000` → **$60,000 of sales**.

---

## 8. Margin of safety (session 6)

One subtraction, then a choice of denominator. The professor said he would ask one of the two
percentage questions on the exam.

```
MoS in units   = Current sales volume - Break-even volume
MoS in dollars = Current sales revenue - Break-even revenue
```

**The two percentages share a numerator. Only the denominator changes.**

| Divide MoS by | Question it answers |
|---|---|
| **Break-even** | How far **above** break-even are we? |
| **Current sales** | How far can sales **decline** before we hit break-even? |

The dollar value of MoS is the same either way. "Might be nice if these had different names,
but they don't." Compute MoS first, then pick the denominator from the question.

### Worked: the PVC company

**Given.** Volume 60,000, price $8.00, VC $4.20, CM $3.80, fixed cost $180,000.

| Step | Calculation | Result |
|---|---|---:|
| Break-even units | 180,000 / 3.80 | 47,369 |
| MoS units | 60,000 − 47,369 | **12,631** |
| MoS dollars | 12,631.58 × 8.00 | **$101,053** |
| MoS % of current sales | 12,631 / 60,000 | **21.05%** — how far it can fall |
| MoS % of break-even | 12,631 / 47,369 | **26.7%** — how far above break-even |

### Structural leverage and margin of safety together

Structural operating leverage (fixed-cost intensity) is **not** the same thing as DOL. Crossed
with margin of safety it gives four positions. The professor warns that slotting industries
into cells is "always a little dangerous."

| Leverage | Margin of safety | Label | Examples given |
|---|---|---|---|
| High | Low | Precarious leverage | airlines, hotels, auto manufacturers |
| High | High | Powerful but risky | data centers, software platforms, streaming platforms post-scale |
| Low | Low | Fragile but flexible | restaurants, local retailers, freelance operators |
| Low | High | The sweet spot | insurance agencies, asset-light service firms |

Low leverage means more ability to pull cost levers as revenue moves. High margin of safety
means more distance from the cliff. Leverage is about **sensitivity** of income to volume;
margin of safety is about **distance** from break-even.

---

## 9. Multi-product CVP (sessions 6 and 7)

Three methods. They always agree. **Pick the method from what the question asks for.**

| Question asks for | Use |
|---|---|
| Units, by product | Basket, or weighted average then split by **volume** mix |
| Total revenue, or revenue by product | Revenue approach, then split by **revenue** mix |

Standing assumption in all three: **the sales mix is known and constant.** State it if asked.

### 9a. Basket method

```
1. Set the mix in smallest whole terms (3 to 1, 12 to 1).
2. Basket revenue       = sum over products of (units per basket x price)
3. Basket variable cost = sum over products of (units per basket x VC per unit)
4. Basket CM            = basket revenue - basket variable cost
5. Break-even baskets   = Total fixed cost / Basket CM      <- DO NOT ROUND
6. Unpack: multiply by units per basket, THEN round up.
```

Why you do not round baskets: "baskets are not a thing." They exist only as a mathematical
tool. Rounding is legitimate only once you are back in real units.

### 9b. Weighted-average method

```
1. Weighted-average price   = Total revenue / Total units
2. Weighted-average VC      = Total variable cost / Total units
3. Weighted-average CM      = (1) - (2)
4. Break-even TOTAL units   = Total fixed cost / Weighted-average CM
5. Split by the sales VOLUME mix.
```

### 9c. Revenue approach

```
1. VC ratio   = Total variable cost / Total revenue
2. CM ratio   = 1 - VC ratio
3. Break-even REVENUE = Total fixed cost / CM ratio
4. Split by the sales REVENUE mix.
```

### Worked: calculators and abacuses, all three ways

**Given**

| | Calculators | Abacuses | Total |
|---|---:|---:|---:|
| Units | 60,000 | 20,000 | 80,000 |
| Revenue | $480,000 | $80,000 | $560,000 |
| Price | $8.00 | $4.00 | |
| Variable cost | $252,000 | $56,000 | $308,000 |
| VC per unit | $4.20 | $2.80 | |
| CM per unit | $3.80 | $1.20 | |
| Fixed cost | | | $210,000 |

Volume mix 3 to 1. (6 to 2 or 60,000 to 20,000 all give the same answer; smallest form is the
convention, not a requirement.)

**Basket method**

| Step | Calculation | Result |
|---|---|---:|
| Basket revenue | 3 × 8.00 + 1 × 4.00 | $28.00 |
| Basket variable cost | 3 × 4.20 + 1 × 2.80 | $15.40 |
| Basket CM | 28.00 − 15.40 | $12.60 |
| Break-even baskets | 210,000 / 12.60 | 16,666.67 |
| Calculators | 16,666.67 × 3 | **50,000** |
| Abacuses | 16,666.67 × 1, round up | **16,667** |

(The transcript says basket CM is "$12." It is $12.60 — which is what produces the professor's
own 16,666.67.)

Full home-equation form, with X as baskets:
`28.00X − 15.40X − 210,000 = 0` → `12.60X = 210,000`

**Weighted-average method**

| Step | Calculation | Result |
|---|---|---:|
| WA price | 560,000 / 80,000 | $7.00 |
| WA variable cost | 308,000 / 80,000 | $3.85 |
| WA CM | 7.00 − 3.85 | $3.15 |
| Break-even total units | 210,000 / 3.15 | 66,667 |
| Calculator share, by volume | 60,000 / 80,000 | 75% |
| Calculators | 66,667 × 75% | **50,000** |
| Abacuses | 66,667 × 25% | **16,667** |

Note $7.00 is a price nobody charges. It is a weighted average, and that is fine.

**Revenue approach**

| Step | Calculation | Result |
|---|---|---:|
| VC ratio | 308,000 / 560,000 | 55% |
| CM ratio | 1 − 0.55 | 45% |
| Break-even revenue | 210,000 / 0.45 | **$466,666.67** |
| Calculator share, by **revenue** | 480,000 / 560,000 | 85.71% |
| Calculator revenue at break-even | 466,666.67 × 85.71% | **$400,000** |

Cross-check: 50,000 calculators × $8.00 = $400,000. Everything ties.

### The trap that costs the most points here

**Volume mix is not revenue mix.**

| Mix type | Calculators | Abacuses |
|---|---:|---:|
| Volume (60,000 : 20,000) | 75% | 25% |
| Revenue (480,000 : 80,000) | 85.71% | 14.29% |

Use volume mix to split a **unit** answer. Use revenue mix to split a **revenue** answer.
Splitting break-even revenue by 75% is wrong.

### Worked: Golden, and why mix matters

**Question 1.** Total CM $1.5M on 200,000 units; fixed cost $1.2M; mix 3 to 1.

| Step | Calculation | Result |
|---|---|---:|
| WA CM per unit | 1,500,000 / 200,000 | $7.50 |
| Break-even total units | 1,200,000 / 7.50 | 160,000 |
| Standard (75%) | 160,000 × 0.75 | 120,000 |
| Deluxe (25%) | 160,000 × 0.25 | 40,000 |

**Question 2.** Same 200,000 units, but only 20,000 are deluxe, so the mix is 9 to 1.

| | Standard | Deluxe |
|---|---:|---:|
| Price | $20 | $30 |
| VC per unit | $14 | $18 |
| CM per unit | $6 | $12 |

| Step | Calculation | Result |
|---|---|---:|
| Basket CM | 9 × 6 + 1 × 12 | $66 |
| Break-even baskets | 1,200,000 / 66 | 18,181.8181… |
| Standard | × 9, round up | **163,637** |
| Deluxe | × 1, round up | **18,182** |
| Total units | | **181,819** |

Break-even rose from 160,000 to 181,819 with no change in prices, costs or fixed costs. The mix
tilted toward the $6 product and away from the $12 one. "Behold the power of sales mix."

The moment you have a multi-product CVP answer, the next question is always: **how do these
numbers flex if the mix changes?** Build sensitivity cells. Ask whether the products are
complements (mix moves together) or substitutes (mix moves in opposite directions), because
that governs how the mix is likely to shift.

---

## 10. Case 1 — Julia and Stanley (session 5)

Titanium pitons for climbing. Julia sells; Stanley forges. Four scenarios in an Excel template.

### Julia's baseline: no contract, no purchase

| | Value |
|---|---:|
| Volume | 1,000 units/month |
| Price | $11.00 |
| Variable cost | $10.45 |
| CM per unit | **$0.55** |
| Fixed cost | $0 |
| Break-even | **0 units** |
| Operating income | $550 |

Zero fixed cost means break-even is zero. Check that against intuition rather than assuming
an error.

### Stanley's cost structure

Revenue $9.00/unit. Capacity 4,000 units; actual demand 1,000.

**Variable**

| Item | Derivation | Per unit |
|---|---|---:|
| Supplies | $110/month ÷ 1,000 units | $0.11 |
| Power (variable part) | high-low slope, section 4a | $0.18 |
| **CM per unit** | 9.00 − 0.11 − 0.18 | **$8.71** |

**Fixed**

| Item | Derivation | Monthly |
|---|---|---:|
| Labor | 345,000 / 12 | $28,750.00 |
| Power (fixed part) | 1,908 − (0.18 × 1,000) | $1,728.00 |
| Occupancy | 33,000 / 12 | $2,750.00 |
| Administrative | given | $600.00 |
| Depreciation | 14,355 / 12 | $1,196.25 |
| **Total fixed** | | **$35,024.25** |

Break-even: 35,024.25 / 8.71 = 4,021.15 → **4,022 units**, rounded up. Excel shows 4,021.
"Didn't matter."

At demand of 1,000 against capacity of 4,000, Stanley is deeply underwater.

### The scenario that matters: does labor treatment change the answer?

Scenarios 3 and 4 both assume Julia buys the forge and sells 4,000 units. The only difference
is whether direct labor is treated as variable or fixed.

| | Scenario 3: labor variable | Scenario 4: labor fixed |
|---|---:|---:|
| Volume | 4,000 | 4,000 |
| CM per unit | $1.5725 | $8.76 |
| Total CM | $6,290 | $35,040 |
| Fixed cost | $6,274.25 | $35,024.25 |
| Break-even units | 3,990 | 3,998 |
| **Operating income** | **$15.75** | **$15.75** |
| DOL | 6,290 / 15.75 = **399.37** | 35,040 / 15.75 = **2,224.76** |

Identical profit. The professor's line: "it didn't matter at all how she treats direct labor."
In class he calls the $15.75 "16 bucks" and treats it as a rounding.

### Why identical profit is not the end of the analysis

Push volume up 10%, to 4,400 units, and the two scenarios diverge violently.

| | Scenario 3 | Scenario 4 |
|---|---:|---:|
| New operating income | 4,400 × 1.5725 − 6,274.25 = **$644.75** | 4,400 × 8.76 − 35,024.25 = **$3,519.75** |
| Change in dollars | $629 | $3,504 |
| Change in percent | 629 / 15.75 = **3,994%** | 3,504 / 15.75 = **22,248%** |
| Check against DOL | 399.37 × 10% = 3,994% | 2,224.76 × 10% = 22,248% |

"Who cares if the outcome is the same? Well, it matters" — because the moment volume moves,
the fixed-labor structure produces $3,520/month instead of $645. That is "no longer trivial."
And it cuts both ways on the downside.

### Judgment calls the class argued about

| Issue | The argument |
|---|---|
| Is direct labor fixed or variable? | Stanley pays salary-like wages, so it behaves as fixed, even though the textbook definition ("no unit, no labor") says variable. Do not label it variable by reflex |
| Step-fixed labor | Beyond capacity she could hire temps (variable-ish) or add salaried staff (a step up in fixed) |
| Include depreciation? | Yes. It is "an accounting fiction" that captures a real economic effect — it works as a sinking fund, a reminder to save for replacement |
| Is 4,400 units free? | **No.** Workers are already full-time at 4,000. Getting 4,400 requires 10% more productivity from an unchanged labor force. Otherwise the $7.19 labor cost multiplies by 4,400 |
| Cost behavior is not fate | "In some cases you can bring skills." Management choices shape whether a cost is fixed or variable |
| What the case ignores | Financing and the purchase price of the forge. The professor: "it's the biggest fantasy land of all" |
| Contract downside | Capped at 4,000 units plus 10%, for two years |

---

## 11. Case 2 — the hammer line (session 7, 10-22)

**The last exam question is conceptual and comes from this session.** Learn the reasoning, not
just the arithmetic.

### The question, first

"Should she add hammers?" That is a **decision** between two futures, so the relevant analysis
is **incremental**: what is *added*. The professor: "Remember, if you got nothing else out of
the class, I hope you get this. What are we trying to answer?"

### Her goals

| Horizon | Goals named |
|---|---|
| Short term | Pay off the machine, pay herself a salary, build supplier relationships, diversify the product line, proof of concept |
| Long term | Revenue, profitability, an exit or spin-off, selling a product line, access to capital markets |

### 11a. Incremental monthly analysis

**Variable cost per hammer**

| Item | Per unit |
|---|---:|
| Direct materials | $10.44 |
| Supplies | $0.14 |
| Variable power | $0.46 |
| Freight | $1.00 |
| **Total** | **$12.04** |

`CM per unit = 61.00 − 12.04 = $48.96`

**At 350 hammers per month**

| Line | Derivation | Amount |
|---|---|---:|
| Revenue | 350 × $61 | $21,350 |
| Direct materials | 350 × 10.44 | (3,654) |
| Direct labor | 2 workers × $4,791.50 † | (9,583) |
| Supplies | 350 × 0.14 | (49) |
| Variable power | 350 × 0.46 | (161) |
| Fixed power | 864 / 12 | (72) |
| Depreciation | 35,000 / 7 / 12 | (417) |
| **Gross margin** | | **$7,414** |
| Freight | 350 × 1.00 | (350) |
| **Operating income, salary excluded** | | **$7,064** |
| Salary | 57,500 × 1.1 / 12 | (5,270.83) |
| **Operating income, salary included** | | **$1,793** |

(The transcript garbles the salary as "5,002 71." $5,270.83 is the figure that makes the
professor's own totals close: 10,072 + 5,270.83 = $15,343, exactly his "everything in" fixed
cost.)

† He says "two workers at 4792 per month" and then "that's incremental 9583." The two do not
multiply: 2 × 4,792 = 9,584. The $9,583 total is the one he carries forward, so the per-worker
figure behind it is $4,791.50. Use 9,583.



### 11b. Three break-evens, three answers

CM per unit is $48.96 in all three. Only fixed cost changes.

| Treatment | Fixed cost | Break-even units | Margin of safety at 350 |
|---|---:|---:|---:|
| Everything in, salary included | $15,342.83 | 314 | 36 |
| **Salary excluded (his preference)** | **$10,072** | **206** | **144** |
| Salary and depreciation excluded (cash) | $9,655 | 198 | 152 |

He prefers the middle case: **depreciation in, salary out.**

### 11c. Why leave the salary out — the discretion argument

| Point | Reasoning |
|---|---|
| It is discretionary | She does not *have* to pay it. That is what separates it from the other costs |
| It can flip the decision | A negative number with salary included could wrongly say "don't do it" |
| It narrows the lens | Treating the salary as the only use of the income hides the alternatives: reinvest, pay down the machine, repay debt, fund a new product |
| Including it is not wrong | He does not penalize it. He just leaves it out of the decision analysis |

### 11d. Payback

```
Payback = Investment / Cash flow (or income) per period
```

| Basis | Calculation | Result |
|---|---|---:|
| On operating income | 35,000 / 7,064 | ~5 months |
| On cash flow (add back depreciation) | 35,000 / 7,481 | 4.7 months |

Depreciation is the only non-cash item in the analysis. (Taxes would also matter for cash and
are out of scope.)

**Payback's limits — likely essay material**

| Limit | Fix or note |
|---|---|
| Ignores the time value of money | Use discounted payback |
| Assumes constant cash flows | |
| Says nothing about value *after* payback | It is blind to the whole rest of the asset's life |
| It is a time measure, not dollars | Not a value metric at all |

It is still useful to her, given her situation.

### 11e. The allocated GAAP view, and why it is not a mistake

Allocate everything above gross margin (other than materials) by productive labor time,
**63% to hammers and 37% to pitons**.

| View | Hammer gross margin |
|---|---:|
| Incremental | **35%** |
| Allocated (GAAP) | **3%** |

(L21 of the transcript says 37% hammers and L35 says 63%. The 63/37 split is the one tied to
her stated assumption. Flagging the conflict.)

The 3% looks absurd next to the 35%. **It is still the number that matters downstream**, and
this is the argument the professor spent the most time on:

| Reason | Detail |
|---|---|
| Different question, different point in time | Allocation belongs at the **valuation** point, not the **decision** point |
| The decision is already made | By then hammers are integrated and cannot be unwound, so incremental analysis is no longer the relevant question |
| Capital markets run on comparability | GAAP-style allocated statements are "the currency" of that conversation |
| A buyer's integration differs from hers | However cleverly she reorganizes her own operation, a buyer folds the line into *theirs*. So what the buyer wants is comparability against the other product lines they might buy, in a "GAAP compliant, auditable way" |
| Performance is not appearance | "I need to care about both how my firm performs, but also how it appears" |
| It does not reverse the decision | A 3% allocated margin does not mean she shouldn't add hammers. It means she must care about both views |
| Due diligence still happens | A serious buyer will look at contribution margin too |

Direct labor is a common allocation driver.

**The caution:** "You can't anchor on this [incremental view] and say this is hammers now."

### 11f. Multi-product CVP on pitons and hammers

Mix is 12 pitons to 1 hammer, so 350 baskets per month: 4,200 pitons and 350 hammers,
4,550 total units and $65,450 total revenue.

**Basket method**

| Step | Value |
|---|---:|
| Basket revenue | $187.00 |
| Basket variable cost | $32.92 |
| Basket CM | $154.08 |
| Total fixed cost | $45,096 |
| Break-even baskets | 292.68 — **do not round** |
| Pitons (× 12, round up) | 3,513 |
| Hammers (× 1, round up) | 293 |
| **Break-even total units** | **3,806** |

**Margin of safety, and the two denominators again**

| Measure | Calculation | Result |
|---|---|---:|
| MoS units | 4,550 − 3,806 | 744 |
| ÷ sales volume | 744 / 4,550 | **16.35%** — how far sales could drop |
| ÷ break-even units | 744 / 3,806 | **19.55%** (he says "20%") — how far above break-even |

**Weighted-average / revenue method**

| Step | Value |
|---|---:|
| VC ratio | 18% |
| CM ratio | 82.4% |
| Break-even revenue | 45,096 / 0.8240 = **$54,731** |
| Piton revenue share | 67% |
| Hammer revenue share | 33% |
| MoS dollars | 65,450 − 54,731 = $10,719 |
| MoS percent | 10,719 / 65,450 = **16.38%** |

16.35% versus 16.38% is purely the effect of rounding units up. "It's exactly the same."

**Note:** the unit mix is 12 to 1, but the revenue mix is roughly 2 to 1. Same trap as section 9.

**Also note:** margin of safety in a multi-product CVP is computed on **total** units, not
per product.

---

## 12. Recurring traps, one list

| # | Trap | Guard |
|---|---|---|
| 1 | Answering the wrong question | Identify X first. Units or dollars? Which product? Above break-even or room to fall? |
| 2 | Unitizing fixed cost | Fixed cost is left alone in full, always |
| 3 | Rounding baskets | Baskets are not a thing. Round only after unpacking into real units, and round **up** |
| 4 | Volume mix used on a revenue answer | Volume mix splits units. Revenue mix splits revenue |
| 5 | Using a coefficient's standard error for a total-cost interval | Use the **regression's** standard error for predictions |
| 6 | DOL from the CM ratio | DOL uses total CM **dollars** |
| 7 | Reading DOL as a cost-structure measure | It also reflects distance from break-even, so it is unstable |
| 8 | Expensing everything produced | Only what was **sold**. Unsold WIP is an asset |
| 9 | Conglomerating equivalent-unit rates | One rate per cost category |
| 10 | Treating allocated cost as decision-relevant | Allocation moves cost between objects; the firm total does not change |
| 11 | Taking allocated cost into a negotiation | "Resist that call" |
| 12 | Combining sunk investment with operating cost | That is the Volt error. Investment has ROI and payback |
| 13 | Labor is variable by reflex | Check how it is actually paid |
| 14 | Assuming extra volume is free | Check capacity and whether labor has to rise |
| 15 | Forgetting to gross up an after-tax target | Return targets are after tax |
| 16 | Brain-dumping on an essay | Word limits are tight and questions are specific |
| 17 | Obsessing over rounding | "You would never lose points for rounding errors" |

---

## 13. One-sheet formula list

Ordered for copying onto the handwritten sheet.

```
HOME EQUATION
  Revenue - Variable cost - Fixed cost = Operating income

PER UNIT
  CM/unit  = Price - VC/unit
  CM ratio = CM / Revenue           VC ratio = VC / Revenue
  CM ratio + VC ratio = 100%

BREAK-EVEN AND TARGET
  BE units       = FC / CM per unit
  BE revenue     = FC / CM ratio
  Target units   = (FC + target operating income) / CM per unit
  divide by a dollar -> units       divide by a percent -> dollars

TAXES
  Operating income target = after-tax NI target / (1 - tax rate)
  Return target: % x base = after-tax NI, then gross up

MARGIN OF SAFETY
  MoS units   = current units - BE units
  MoS dollars = current revenue - BE revenue
  / BE            -> how far ABOVE break-even
  / current sales -> how far sales can FALL

OPERATING LEVERAGE
  DOL = total CM dollars / operating income
  % change operating income = DOL x % change sales

MULTI-PRODUCT
  Basket CM        = basket revenue - basket VC
  BE baskets       = FC / basket CM            (do not round)
  WA CM/unit       = total CM / total units
  BE total units   = FC / WA CM per unit       (split by VOLUME mix)
  BE revenue       = FC / CM ratio             (split by REVENUE mix)

HIGH-LOW
  m = (cost high - cost low) / (activity high - activity low)
  b = total cost at a point - (m x activity at that point)

REGRESSION
  Total cost = intercept + (slope x volume)
  t stat = coefficient / its standard error
  df = n - parameters      (n - 2 simple)
  t at 6 df: 2.447 (95%), 1.943 (90%)
  Coefficient CI = estimate +/- (its SE x t)
  Prediction CI  = estimate +/- (t x REGRESSION standard error)

EQUIVALENT UNITS
  EU = (units sold x 100%) + (ending units x % complete)
  Rate = category spend / category EU
  To income statement = rate x units sold
  To balance sheet    = rate x EU in ending inventory
  Check: IS + BS = total spend

ALLOCATION
  Rate = total indirect cost pool / total driver units

PAYBACK
  Payback = investment / cash flow per period
  (add depreciation back for a cash basis)
```

---

## 14. Source map

| Session | Date | Topics | Transcript |
|---|---|---|---|
| 1 | 2026-09-03 | Overhead allocation, drivers, distortion, the Volt, negotiation | `2026-09-03_0801_management-accounting-for-client-negotiations-overhead-allocation-and-.txt` |
| 2 | 2026-09-10 | Cost vs expense, equivalent units, absorption, overproduction incentive | `2026-09-10_0804_accounting-spe-10th-lecture.txt` |
| 3 | 2026-09-17 | Contribution margin statement, CVP, break-even, target profit, DOL | `2026-09-17_0802_class-session-three-recap.txt` |
| — | 2026-09-24 | **No class** (MBA trips) | — |
| 4 | 2026-10-01 | Regression, confidence intervals, prediction intervals | `2026-10-01_0801_managerial-accounting-regression.txt` |
| 5 | 2026-10-08 | Case 1: Julia and Stanley. High-low, mixed costs, four scenarios, DOL | `2026-10-08_0819_break-even-analysis-for-julia.txt` |
| 6 | 2026-10-15 | Taxes, target return, margin of safety, multi-product CVP, exam logistics | `2026-10-15_0804_cbp-analysis-and-exam-prep.txt` |
| 7 | 2026-10-22 | Case 2: the hammer line. Incremental vs allocated, payback, multi-product CVP | `2026-10-22_0809_hammer-line-profitability-analysis.txt` |

All transcripts live in `~/MegaMind/Resources/raw/granola-transcripts/`.

Names as the auto-transcript rendered them, so they may be wrong: the professor is given as
Steve Smith. The TA's name is garbled in every mention.
