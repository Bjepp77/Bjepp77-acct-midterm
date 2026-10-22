# Click Note - Exam 1

> ## Read this first
>
> **Confirm with Prof. Smith before you copy anything from this file onto your exam sheet.**
>
> The syllabus says: *"our class policy is that use of AI tools is not permitted on post-class
> quizzes or exams. Similarly, feeding case documents into an AI tool for any purpose is not
> permitted."* It also says that to the extent such tools help you learn, he fully supports it.
>
> The course materials ban AI tools **during** the exam. They do **not** say whether content derived
> with AI help may be transcribed onto the permitted handwritten sheet. That gap is unresolved, and
> this file was AI-assisted. **Ask him. Do not assume.**
>
> If the answer is no, this file still works as a study checklist: close it, and write your own sheet
> from the practice problems. That is what he wants anyway.

---

## His rules for this sheet

From *Managing Your Workload*, his own guidance:

| Rule | Detail |
|---|---|
| Purpose | distill each topic to its basic concepts, definitions, models and formulae |
| Length | **no more than a dozen items** |
| Space | clear and concise, **one side of one sheet** |
| Content | **nothing obvious.** He says nobody needs to write that sales less variable cost is contribution margin |
| Origin | items should come from a mental "click" or "A-ha" while working problems |
| Test | **use the sheet to redo problems.** If it does not carry you through, it is not finished |

Exam logistics allow a single 8.5x11 sheet, handwritten. His Click Note philosophy says one side;
the exam permits the sheet, and in class he indicated front and back. Either way, a dozen items is
the target, not a transcription of the course.

**Twelve items follow.** Each one is a thing people get wrong, not a definition you already know.

---

### 1. The home equation, four forms

```
Revenue - Variable Cost - Fixed Cost = Profit

Price(Vol) - VCrate(Vol) - TotalFC = Profit      given per-unit figures
CM/unit(Vol) - TotalFC = Profit                  given CM per unit
Rev - VC%(Rev) - TotalFC = Profit                given percentages
TC = VCrate(Vol) + TotalFC                       splitting a total cost
```

Write the equation, fill in three, solve for the fourth.

### 2. Never unitize fixed cost or profit

FC per unit and profit per unit are valid **only at the volume where computed**. When a problem hands
you a fixed cost per unit, multiply back to a total first, then work in totals.

### 3. Rounding

| | |
|---|---|
| Break-even units, required volume | round **up** |
| Baskets | **do not round.** "Baskets are not a thing" |
| Product volumes from baskets | unpack first, **then** round each up |

### 4. Tax: gross up, and watch the denominator

```
Pretax = After-tax / (1 - t)          DIVIDE. Never multiply.
```

ROE uses **equity**. ROA uses **total assets**. The rest of the balance sheet is a decoy.

### 5. Margin of safety: two denominators

```
MoS = Current Volume - Break-even Volume

"how far ABOVE break-even?"   ->  MoS / break-even
"how far can sales FALL?"     ->  MoS / current sales
```

The words choose the denominator. Right arithmetic against the wrong question scores zero.

### 6. High-low

```
b = variable = (Hi cost - Lo cost) / (Hi activity - Lo activity)
a = fixed    = Hi cost - b(Hi activity)
```

**Pick high and low by ACTIVITY, not by cost.** Then check `a` at the other point; if the two
disagree beyond rounding, the slope is wrong.

### 7. Regression: three standard errors

| Interval around | Standard error to use |
|---|---|
| fixed cost | **intercept's** SE |
| variable cost | **slope's** SE |
| a total cost estimate | **the regression's** SE (top block) |

```
Interval = point estimate +/- t(SE)        df = n - 2
t at 6 df:  70% 1.134   80% 1.440   90% 1.943   95% 2.447
t = coefficient / its own SE      t>=2 useful, t>3 near certain, want p<0.05
```

Compute the point estimate first, from the **printed rounded** coefficients.

### 8. DOL

```
DOL = Total CM in DOLLARS / Operating Profit
DOL x %change Revenue = %change Operating Profit
```

Not the CM ratio, not revenue. **Point-in-time:** DOL changes once volume moves, so never reuse one
DOL for a second step. It cuts both ways.

### 9. Multi-product: three methods, weights differ

| Method | Weight by | Answer in |
|---|---|---|
| Basket | unit ratio | units per product |
| Weighted average CM | **unit** volume | total units |
| Revenue | **revenue** share | dollars |

**No unique multi-product break-even.** Every answer assumes a mix. Goldman: 160,000 units at 3:1,
181,819 at 9:1. Change the mix, recompute from scratch.

### 10. Planes: two denominators, and FOH goes into inventory

```
Units of production, materials  = sold + ALL of WIP
Units of production, conversion = sold + (WIP x % complete)
```

Fixed manufacturing overhead **attaches to units** and sits in inventory. Selling and admin never
does. **Tie-out:** expensed + inventory must equal total spent.

### 11. Target stated as a % of revenue

The target carries the unknown, so it cannot be added to fixed cost. Collect terms:

```
(CM/unit)D - FC = k(Price)D   ->   [(CM/unit) - k(Price)]D = FC
```

### 12. Step costs

Round the **resource count up** (no fractional technician), then total. Averaging a step cost to a
per-unit rate understates total cost whenever the last unit of capacity is partly idle. State the
relevant range.

---

## Now test it

Close the study guide. Using only the twelve items above, work `mock-1` end to end in the quiz, or
redo the instructor's practice problems. Every place you reach for something that is not on the
sheet, decide: does it belong on the sheet, or did you not know it well enough? Usually the second.

That is his test, and it is the only one that matters before Thursday.
