# Metrics And Diagnostics

## Collection Schema

Record IDs and names for campaign, ad set, and ad, then collect where available:

- delivery, status, objective, conversion location, performance goal
- attribution setting, budget, bid strategy, schedule
- spend, impressions, reach, frequency, CPM
- outbound/link clicks, unique clicks, CTR, CPC
- landing-page views and cost per landing-page view
- form opens, form completions, completion rate, leads, CPL
- messaging conversations started and cost per conversation
- video 3-second plays, ThruPlays, 25%, 50%, 75%, 95%, 100%, average watch time
- qualified leads, calls booked, calls attended, checkout starts, purchases, revenue, refunds
- cost per qualified lead, call, attended call, and purchase
- lead-to-qualified, qualified-to-call, call-to-sale, and lead-to-sale rates
- purchase value, ROAS, profit, and contribution after media spend

## Breakdown Order

1. Day and campaign to detect schedule or configuration changes.
2. Ad and creative to identify message and format effects.
3. Placement and device to detect unsuitable crops or accidental inventory.
4. Geography, age, and gender when sample size is sufficient and lawful to use.
5. Form answers and conversation outcomes for lead quality.

## Diagnostic Order

1. **Measurement:** Can the purchase and intermediate events be trusted?
2. **Delivery:** Did ads spend, reach intended people, and avoid excessive frequency?
3. **Attention:** Did the creative earn useful viewing or clicks?
4. **Intent:** Did the click-to-form or click-to-message transition preserve the promise?
5. **Qualification:** Did lead answers and conversations indicate capacity and fit?
6. **Sales execution:** Were leads contacted quickly, repeatedly, and directly asked to buy?
7. **Offer/checkout:** Did price, timing, proof, risk reversal, and checkout support conversion?

## Interpretation Rules

- Prefer within-account comparisons over generic benchmarks.
- Treat current benchmarks as directional and research them when needed.
- Do not make demographic or placement conclusions from tiny samples.
- Distinguish statistical noise from operational defects.
- A cheap lead is not a winner if qualified-lead or purchase economics are worse.
- High CTR with poor lead quality often indicates curiosity, ambiguity, sensational creative, or a promise mismatch.
- Strong lead volume with no contact may be a routing failure; strong contact with no progression may be qualification, offer, or sales execution.
- Zero reported purchases may mean zero sales, broken purchase tracking, or both. Reconcile the backend.
- Conflicting datasets or conversion events can fragment learning and optimize toward the wrong behavior.
- Report numerator and denominator for every rate.

## Root-Cause Confidence

- **High:** direct evidence from configuration, exports, or matched backend records.
- **Medium:** multiple consistent signals but incomplete attribution or sample size.
- **Low:** plausible explanation requiring a controlled test or missing evidence.

## Decision Guardrails

- Do not scale from CTR or CPL alone.
- Do not kill a new ad solely because it has less spend than the account's normal acquisition cost unless there is a clear policy, tracking, creative, or audience defect.
- Pause immediately when the event date or offer is invalid, destination is broken, tracking sends sensitive or incorrect data, or the campaign targets an obviously wrong audience.
- Before scaling, require trustworthy purchase/qualified-lead data, stable downstream conversion, sufficient fulfillment capacity, and a defined rollback threshold.
- Change one major variable per controlled test whenever practical.
