# Mega cheat sheet: Exam 1 (copy by hand, front and back)

Before you copy: ask Prof. Smith whether AI-assisted notes may go on the sheet (see the caution in
`cheat-sheet.md`). Copying by hand is the point either way: rework one problem per section from
the sheet alone as you go.

Layout: FRONT = the 65 computation points. BACK = planes, leverage, words, rounding, clock.
Section numbers match blueprint items. Anchors (in brackets) are worked answers to check yourself.

---

## FRONT

### A. Home equation (everything) [items 3, 7-11]
```
Rev - VC - FC = Profit          P(V) - vc(V) - FC = Profit
CM/u(V) - FC = Profit           Rev - VC%(Rev) - FC = Profit
TC = vc(V) + FC                 CM ratio = 1 - VC ratio
```
Write it, fill 3, solve the 4th. NEVER unitize FC or profit: x back to totals first.

### B. Single-product CVP [7-9, 15 pts]
```
BE units  = FC / CM/u                  ROUND UP
BE $      = FC / CM ratio
Target V  = (FC + Target) / CM/u       ROUND UP
Pretax    = After-tax / (1 - t)        DIVIDE, never x(1-t)
```
Return target: (1) % x base = after-tax $ (2) / (1-t) (3) into home eq.
ROE -> EQUITY. ROA -> TOTAL ASSETS. Rest of balance sheet = decoy.
Target as % of revenue: [CM/u - k(P)]V = FC  (can't add it to FC).
[P 8, vc 4.20, FC 180k: BE 47,369 u, $378,947; +120k target -> 78,948]
[tax-003: 500k after tax @30% -> 714,286 pretax]

### C. Margin of safety [7-9]
```
MoS = Current - BE      (units or $)
"how far ABOVE BE?"        MoS / BE         [12,631/47,369 = 26.7%]
"how far can sales FALL?"  MoS / CURRENT    [12,631/60,000 = 21.05%]
```
The words pick the denominator.

### D. Multi-product CVP [10-11, 15 pts]
| Method | Weight by | Answer in |
|---|---|---|
| Basket | unit ratio | units per product |
| Wtd avg CM | UNIT share | total units |
| Revenue | REVENUE share | dollars |

Basket: ratio -> basket P, basket VC -> basket CM -> baskets = (FC + target)/basket CM
-> UNPACK, then round EACH product UP. Do not round baskets ("not a thing").
Revenue: BE $ = (FC + target) / (1 - total VC / total Rev). Split $ by REVENUE share.
No unique multi-product BE: new mix = recompute from scratch.
[mock-1-10: 8:3, basket CM 480, 2,177.08 baskets -> 17,417 + 6,532]
[Goldman 3:1 -> 160,000; 9:1 -> 181,819. One-unit-off option = rounding order]

### E. Cost behavior [2, 4, 16, 15 pts]
GAAP (COGS vs S&A) is NOT variable vs fixed. Rebuild: vc/u x V = total VC; total cost - VC = FC.
[mock-1-04: vc 35 x 24,000 = 840k; 1,292k - 840k = FC 452k]
```
High-low:  b = (Hi$ - Lo$) / (Hi act - Lo act)     pick by ACTIVITY, not cost
           a = Hi$ - b(Hi act)     CHECK a at the low point too
```
[mock-1-02: b 19.00, a 106,400 both points]
Step cost: resources = V / capacity, ROUND UP, then total. Never average to a per-unit rate.
[mock-1-16: 1,640/500 -> 4 techs; 29,600 + 46,000 + 31,160 = 106,760]
Relevant range: model only valid inside observed data. High-low = 2 points; regression = all.

### F. Regression [5-6, 10 pts]
| CI around | Use SE of |
|---|---|
| Fixed cost | INTERCEPT row |
| Variable cost | SLOPE (driver) row |
| Total cost estimate | REGRESSION (top block) |
```
CI = point +/- t(SE)       df = n - 2
t @ 6 df: 70% 1.134 | 80% 1.440 | 90% 1.943 | 95% 2.447
t stat = coef / own SE: >=2 useful, >3 near certain. p < .05. Report ADJ R^2.
Point estimate from PRINTED rounded coefficients, compute it FIRST.
```
[Sailmaster: 95% total @325 = 273,116.04 +/- 2.447(27,771.27) -> 205,159.74 to 341,072.34]

---

## BACK

### G. Planes: cost accounting [14-15, 10 pts]
Mfg costs (DM, DL, VOH, AND FIXED OH) attach to units -> inventory until sold.
S&A = period cost, expensed now.
```
Units of production DM   = sold + ALL WIP              (materials in at start)
Units of production conv = sold + WIP x % complete
Rate = cost / its own denominator     (two denominators, never one)
Op profit: revenue - (rates x SOLD units)
End inventory: DM rate x WIP + conv rates x (WIP x %)
TIE OUT: expensed + inventory = total spent
```
[23 started, 18 sold, 5 WIP @60%: denominators 23 and 21; profit 262.72; inv 51.21;
 277.29 + 51.21 = 328.50]
Absorption: produce more -> FOH moves to balance sheet -> reported profit rises with no extra sales.
Same as "equivalent units" / "work done".

### H. DOL [12, 5 pts]
```
DOL = TOTAL CM $ / Op profit         (not CM ratio, not revenue)
%chg OP = DOL x %chg Rev             cuts BOTH ways; point-in-time, recompute after V moves
```
[mock-1-12: 836k / 308k = 2.71; +/-10% rev -> +/-27.1% OP]

### I. Operating leverage, short answer [13, 5 pts]
OL = cost STRUCTURE (share of cost that is fixed), stable. DOL = sensitivity AT today's volume.
High OL: more FC, higher CM/u, higher BE, smaller MoS, bigger swings both ways.
Fixed-for-variable swap (machines for labor, buy vs royalty) RAISES OL and BE even as unit cost falls.
[Alpine vs Basin: same V, Basin DOL 2.81 vs 1.71; after -20% rev 206k vs 276k]

### J. CVP short answer [3, 5 pts], one line each
- Unitized FC is true only at the volume where computed; CVP always moves volume.
- GAAP splits core vs run-the-business; COGS and S&A are both mixed.
- CM = revenue less ALL variable costs, wherever they sit.
- CVP uses: pricing, fixed-for-variable swaps, outsourcing, target profit. NOT quality specs.
- Two MoS %: denominator follows the question.

### K. Case answers [17: 50 words, 18: 90 words, 20 pts]
Read the question twice. Answer THAT question. No preamble, no restating.
- Case 1 (cost structure): labor as variable = low BE, slow profit growth; as fixed = high BE,
  fast growth. Same profit today, different risk. Format: rec -> 2 driving numbers -> 1 caveat.
- Case 2 (shared cost, lines): allocation changes reported line profit ONLY, not total profit or
  cash. Basis = what causes the cost. Judge a line on CM - its AVOIDABLE FC. Dropping a
  contributing line leaves shared cost behind -> total profit falls. Finish on the recommendation.
- Hammer line: 12:1 unit mix ~ 2:1 revenue mix; BE $54,731 x 33% = 18,061 (exact 32.62% = 17,853).

### L. Rounding
BE / required volume UP. Baskets never. Unpack then round each UP. Regression from printed coefs.
He never takes points for rounding: pick the nearest option and move on.

### M. Clock and Excel
2h15m, 18 items. ~6 min per computation; keep ~30 min for items 3, 13, 17, 18.
Do the cases before the last 10 minutes. Excel starts blank. No GoalSeek, no Solver.
Item 1 (integrity): read it, answer yes.
