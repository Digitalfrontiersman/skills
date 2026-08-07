---
name: instagram-autonomous-audit
description: Run a guided, read-only Instagram Professional Dashboard audit across Codex, Claude Code, OpenClaw, Hermes, or another autonomous agent. Use when a user wants an Instagram audit, detailed top-post metrics, content-performance rankings, hooks/CTA analysis, or a strategy based on views, comments, shares, saves, follows, reach, and profile activity.
---

# Instagram Autonomous Audit

Use this skill with the host agent's supported browser, account connector, or exported Insights data. Keep the workflow read-only: never publish, edit, delete, boost, appeal, message, change settings, or accept a site permission prompt unless the host platform's policy and the user explicitly allow it.

## Start with guided intake

Open naturally and explain the workflow in one short paragraph. Then ask only the first unanswered question below; do not ask the whole questionnaire at once.

1. **Account:** Ask: Which Instagram handle should I audit?
2. **Access:** Ask: Are you logged into the account that manages it, and can this agent access Instagram in a browser?
3. **Goal:** Ask: Do you want a complete 90-day audit, a top-post metric report, or both?
4. **Scope:** If unspecified, use the last 90 days and include Posts, Reels, and any still-available Stories.
5. **Output:** Offer a concise report, copy-ready Markdown, or Google-Docs-ready document.

If the agent cannot access the account dashboard, explain exactly what is missing and offer two routes: the user switches/logs in, or the user exports Insights/Meta Business Suite data for analysis. Do not present public-profile metrics as equivalent to dashboard metrics.

## Professional Dashboard workflow

1. Confirm account ownership or management controls before collecting private metrics.
2. Open **Professional dashboard > Insights > Content**.
3. Set **Last 90 days**.
4. Filter **Posts** and **Reels** separately. Capture Stories separately when available.
5. Sort by **Views / Highest**, then open each item’s detail panel. If the interface supports it, repeat sorting by **Follows** and **Shares**.
6. Record every item in scope. If a screen, rate limit, or session timeout stops work, state the exact last completed item instead of silently skipping content.

## Required per-post metric matrix

Capture only metrics visible in the dashboard. Mark unavailable values as **Unavailable** — never as zero.

| Identity | Reach & distribution | Engagement | Conversion |
|---|---|---|---|
| format, title/first-frame hook, date if visible, post URL if visible | views, accounts reached, follower %, non-follower %, traffic sources | likes, comments, shares, saves, total interactions, accounts engaged | profile activity, profile visits, external-link taps, follows |

Calculate only when all source values exist:

- engagement rate = interactions / accounts reached
- save rate = saves / views
- share rate = shares / views
- follow rate = follows / views

Always state the denominator. Do not calculate a metric using an unavailable field.

## Analysis rules

- Separate dashboard facts from strategic interpretation.
- Rank authority by views and conversion by follows gained; do not substitute one for the other.
- Assess discovery using non-follower view share; assess durable value using saves and shares; assess conversation using comments; assess business intent using profile visits, link taps, and follows.
- Treat collaborator content showing `--` or no panel as an access/data limitation, not poor performance.
- Explain why winning hooks work: specificity, consequence, novelty, utility, identity, proof, tension, or timeliness.

## Deliverable

Return a structured report with:

1. Account Snapshot
2. Full Content Inventory (T1 - 90 days)
3. Top Performers: Full Dashboard Metrics
4. Top Performers by Views (Authority)
5. Top Performers by Follows (Conversion)
6. Underperformers and data limitations
7. Content Mix, Cadence, and Repetition Audit
8. Hook, CTA, and Monetization Analysis
9. Audience and Engagement Quality
10. Prioritized Action Plan

Use tables for inventories and rankings. Finish with 5–10 ordered actions. If the host supports only a 90-day window, say so explicitly and recommend a 12-month Meta Business Suite/mobile export for annual rankings and follower growth.

## Host portability

Read [installation-and-host-guidance.md](references/installation-and-host-guidance.md) when installing this skill or adapting it to a specific agent platform.
