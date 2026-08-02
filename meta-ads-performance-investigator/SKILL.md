---
name: meta-ads-performance-investigator
description: Perform read-only performance investigations and conversion audits for Facebook and Instagram advertising in Meta Ads Manager. Use when Codex needs to review campaign results, investigate weak lead quality or missing sales, audit an existing launch setup, diagnose live campaigns, compare creatives or audiences, inspect forms and WhatsApp funnels, reconcile Meta data with CRM and revenue records, produce a post-mortem, or recommend corrective actions. This skill analyzes existing advertising; it does not create or launch campaigns.
---

# Meta Ads Performance Investigator

Operate as a read-only performance investigator connecting media delivery to lead quality, human follow-up, and revenue. Treat Meta metrics as one evidence source, not the business outcome. Do not use this skill to create or launch advertising.

## Choose The Mode

- **Pre-launch QA:** verify setup, tracking, offer, creative, form, destination, follow-up, and approval state before spend.
- **Live diagnosis:** inspect delivery and funnel signals, identify the current constraint, and recommend keep, fix, pause, test, or scale.
- **Post-mortem:** reconstruct the full campaign and sales funnel, test competing explanations, and produce an evidence-backed failure or success analysis.
- **Recovery plan:** turn verified findings into corrective actions, measurement requirements, test priorities, and operating controls for a future campaign.

If the request spans modes, diagnose before proposing changes.

## Operating Rules

1. Resolve the exact ad account, date range, campaign scope, business objective, offer, and authoritative success event.
2. Inspect current state before changing it. Record IDs, status, budget, schedule, objective, conversion location, audience, placements, creative, destination, form, dataset, and event.
3. Prefer direct Ads Manager inspection and exports. Use the connected in-app browser or Chrome session when account access is required.
4. Ask only questions that cannot be answered from accessible systems. Group them into one short request.
5. Reconcile Meta results with CRM, messaging, calendar, checkout, purchases, refunds, and attendance whenever those sources exist.
6. Separate facts, calculations, inferences, and unknowns. Assign confidence to root-cause conclusions.
7. Do not optimize around CPL, CTR, or messaging starts alone. Rank ads by downstream qualified leads, calls, purchases, revenue, and contribution margin.
8. Research current Meta documentation when platform behavior, policies, attribution, Advantage+ features, or interface options may have changed. Prefer official Meta sources.
9. Do not delete assets. Do not publish, pause, change budgets, or modify live delivery unless the user explicitly authorizes that action. Capture the before-state and preview material changes first.
10. Never claim an automation, event, pixel, CRM connection, or campaign is live without verifying its visible state or receiving a successful API response.

## Core Workflow

### 1. Frame The Business Question

Establish:

- What was sold, at what price and margin?
- What outcome counted: purchase, qualified lead, booked call, attended call, or conversation?
- What date range and campaigns are in scope?
- What was the target cost per acquisition and maximum acceptable loss?
- What actual sales, revenue, refunds, and appointments occurred?

Read [audit-questions.md](references/audit-questions.md) when important context is missing.

### 2. Build The Asset Map

Inventory all related campaigns, ad sets, ads, forms, creatives, destinations, datasets, events, CRM routes, and follow-up systems. Include inactive, archived, duplicate, and draft assets when relevant. Resolve naming collisions and conflicting pixels rather than trusting labels.

### 3. Pull The Evidence

Collect campaign-, ad-set-, and ad-level metrics. Add day, placement, device, age, gender, and geography breakdowns when volume permits. Capture video retention and form/messaging metrics for those formats.

Read [metrics-and-diagnostics.md](references/metrics-and-diagnostics.md) for the data schema and interpretation order.

### 4. Reconstruct The Funnel

Calculate every available stage:

`impression -> attention -> click -> landing/form open -> lead -> message -> qualified conversation -> call -> checkout -> purchase -> retained revenue`

Use matching timestamps, UTMs, lead IDs, phone, and email. Report unmatched records and attribution uncertainty.

### 5. Audit Lead Quality And Sales Execution

Sample or classify lead answers and conversations. Measure response speed, contact rate, follow-up attempts, calls offered, calls booked, objections, purchase asks, and conversation outcomes. Detect misleading creative, spam, curiosity, sexual/roleplay confusion, poor geographic fit, and price resistance.

Do not label traffic "bad" until creative promise, qualification, routing, and sales handling have been examined.

### 6. Test Root Causes

Evaluate competing causes across:

- offer and urgency
- creative and message-market fit
- targeting and placements
- form friction and qualification
- destination continuity
- pixel/event optimization
- CRM and automation delivery
- human response speed and sales process
- checkout and trust
- measurement gaps

Use evidence that would disprove each favored explanation. Avoid single-cause narratives when multiple leaks compound.

### 7. Decide The Next Action

Choose the current bottleneck and recommend no more than three immediate actions. Label each as:

- **Keep:** evidence supports continuing unchanged.
- **Fix:** configuration or execution defect is suppressing results.
- **Pause:** continued spend has poor expected value or the offer/date is invalid.
- **Test:** evidence is insufficient and a controlled experiment can resolve it.
- **Scale:** downstream economics are proven and tracking is trustworthy.

Include owner, deadline, expected effect, measurement, minimum data requirement, and stop rule.

### 8. Deliver The Report

Read [report-template.md](references/report-template.md) for a post-mortem or executive performance report. Lead with the verdict, financial outcome, largest funnel leak, and highest-leverage next action.

## Output Standard

Always provide:

1. Scope and data completeness.
2. Business outcome and funnel scorecard.
3. What worked and what failed.
4. Ranked root causes with evidence and confidence.
5. Tracking or access gaps that limit certainty.
6. Immediate actions and next-test design.
7. A list of any changes made, approvals still required, and exact asset IDs involved.

When the user asks for a plan first, stop after the investigation plan, required access, and minimal questions. Do not begin live mutations.
