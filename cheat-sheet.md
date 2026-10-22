# Cheat sheet — copy by hand onto one sheet, front and back

Draft. Not final: Crispin is gathering the Canvas practice problems, solutions and quizzes,
and this gets revised once they land.

Front is formulas only. Back is traps, the t table and the two case summaries. Write the front
first; if you run out of room, the back items are ranked, so drop from the bottom.

---

## FRONT

**HOME EQUATION**
Rev − VC − FC = Operating income
(P·Q) − (v·Q) − FC = OI
(P − v)·Q − FC = OI
Rev − (Rev·VC%) − FC = OI

**UNIT / RATIO**
CM/u = P − v
CM% = CM/Rev = CM/u ÷ P
VC% = VC/Rev = v ÷ P
CM% + VC% = 100%
FC is NEVER unitized

**BREAK-EVEN / TARGET**
BE units = FC ÷ CM/u
BE rev = FC ÷ CM%
Target units = (FC + target OI) ÷ CM/u
÷ dollar → units ; ÷ percent → dollars

**TAXES**
OI target = after-tax NI ÷ (1 − t)
Return: %·base = after-tax NI, then gross up
(ROE 25% × 300k = 75k → ÷0.7)

**MARGIN OF SAFETY**
MoS u = current u − BE u
MoS $ = current rev − BE rev
÷ BE → how far ABOVE BE
÷ current sales → how far sales can FALL

**OPERATING LEVERAGE**
DOL = total CM $ ÷ OI
%ΔOI = DOL × %ΔSales  (symmetric)
DOL high near BE, falls moving away

**MULTI-PRODUCT** (mix known + constant)
Basket rev = Σ(u/basket × P)
Basket VC = Σ(u/basket × v)
Basket CM = rev − VC
BE baskets = FC ÷ basket CM  ← DO NOT ROUND
unpack × u/basket, THEN round up
WA CM/u = total CM ÷ total u
BE total u = FC ÷ WA CM/u → split by VOLUME mix
BE rev = FC ÷ CM% → split by REVENUE mix

**HIGH-LOW**
m = (cost hi − cost lo) ÷ (act hi − act lo)
b = total cost at a point − (m × act there)
Annual ÷ 12 before mixing with monthly

**REGRESSION**
TC = intercept + (slope × volume)
intercept = FC ; slope = v
t = coef ÷ its own SE
F = (slope t)²
df = n − params (n−2 simple)
Coef CI = est ± (its SE × t)
Predict CI = est ± (t × SE OF REGRESSION)
use adjusted R² ; R² 0→1 ; corr −1→1
P < .05 reject null of zero

**EQUIVALENT UNITS**
EU = (sold × 100%) + (ending × %done)
rate = category spend ÷ category EU
to IS = rate × units SOLD
to BS = rate × EU in ending inv
CHECK: IS + BS = total spend

**ALLOCATION / PAYBACK**
rate = cost pool ÷ driver units
Payback = investment ÷ cash flow per period
(add depreciation back for cash)

---

## BACK

**TRAPS, ranked**
1. Identify X first. Units or dollars? Which product?
2. Revenue answer → X is revenue, VC term is VC%·X. NOT P × Q.
3. Never unitize FC.
4. Don't round baskets. Round only real units, UP.
5. VOLUME mix splits units. REVENUE mix splits revenue.
6. Prediction CI uses the REGRESSION SE, not a coefficient SE.
7. DOL uses total CM DOLLARS.
8. Expense only what was SOLD. Unsold WIP = asset.
9. One EU rate per cost category. Never blend.
10. Return targets are AFTER tax. Gross up.
11. Allocation moves cost between objects; firm total unchanged.
12. Never take allocated cost into a negotiation.
13. Don't mix sunk investment with operating cost (Volt). Use ROI/payback.
14. Labor is not variable by reflex. Check how it's paid.
15. Extra volume isn't free. Check capacity.
16. Essays: tight word limit, specific question, no brain dump.
17. Rounding errors are never penalized.

**t TABLE, 6 df**  95% = 2.447 | 90% = 1.943

**CASE 1 — Julia & Stanley (pitons)**
Julia: P 11, v 10.45, CM .55, FC 0 → BE 0, OI 550 at 1,000u
Stanley: P 9, v .29 (.11 sup + .18 pwr), CM 8.71
 FC 35,024.25 = 28,750 lab + 1,728 pwr + 2,750 occ + 600 adm + 1,196.25 dep
 BE 4,022 (cap 4,000, demand 1,000)
Labor variable: CM 1.5725, FC 6,274, BE 3,990, DOL 399
Labor fixed:    CM 8.76,  FC 35,024, BE 3,998, DOL 2,225
 BOTH OI = 15.75. Same profit, opposite risk.
 +10% vol → 645 vs 3,520.
Depreciation IN (sinking fund). 4,400u needs +10% productivity.

**CASE 2 — hammer line**
v 12.04 = 10.44 DM + .14 sup + .46 pwr + 1.00 frt
P 61 → CM 48.96 ; 350u/mo → rev 21,350, GM 7,414, OI 7,064 (no salary)
FC salary out 10,072 → BE 206, MoS 144  ← his preference
FC all in 15,343 → BE 314, MoS 36 ; cash 9,655 → BE 198
Payback 35,000/7,064 ≈ 5 mo ; cash 4.7 mo
Multi-prod 12:1 → basket rev 187, VC 32.92, CM 154.08, FC 45,096
 BE 292.68 baskets → 3,513 pitons + 293 hammers = 3,806 of 4,550
 MoS 744 → 16.35% (÷sales) or 19.6% (÷BE)
 BE rev 54,731 ; revenue mix 67/33 NOT 12:1
Incremental GM 35% vs allocated 3% (labor time 63/37)
 Allocated = VALUATION point, not decision point. Buyer wants
 GAAP comparability; integration differs from hers. Care about both.
Salary out = discretionary. Depreciation in = real consumption.
Payback limits: ignores TVM, assumes constant CF, blind after payback,
 time not dollars. Still right for "pay off the machine".
THE QUESTION: should she add hammers? Decision → incremental.

**PAYBACK / ALLOCATION ONE-LINERS**
"Why do you want to know?" decides the calculation.
Full absorption: GAAP + long-run pricing. Never a short-run decision.
Overproduce under absorption → cost to inventory → income up, nothing better.
