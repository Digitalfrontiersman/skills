# Instagram Autonomous Audit

A portable, read-only skill for turning Instagram Professional Dashboard insights into a useful content-performance audit. It works with Codex, Claude Code, OpenClaw, Hermes, and other autonomous agents that can use an approved browser session or analyze a user-provided Insights export.

## What it does

- Guides the user through a short, one-question-at-a-time intake.
- Collects available 90-day content data from the Professional Dashboard.
- Captures views, reach, follower and non-follower distribution, likes, comments, shares, saves, follows, profile visits, link taps, and other visible metrics.
- Separates top posts by views (authority) from top posts by follows (conversion).
- Produces a fact-based audit with hook, CTA, cadence, repetition, and monetization recommendations.

## What it does not do

- It does not publish, edit, delete, boost, message, or change Instagram settings.
- It does not treat public-profile counts as a substitute for Professional Dashboard insights.
- It does not upload private dashboard data, screenshots, exports, or credentials without explicit permission.

## Install and use

Copy the complete `instagram-autonomous-audit` folder into the skills directory supported by your agent platform. In Codex, place it in `~/.codex/skills/`, then ask for an Instagram audit or invoke `$instagram-autonomous-audit`.

For host-specific setup and data-safety guidance, read [installation-and-host-guidance.md](references/installation-and-host-guidance.md).

## Example request

```text
Use $instagram-autonomous-audit to run a complete 90-day audit of @myhandle using my Instagram Professional Dashboard.
```
