# Launch and adoption plan

## Positioning

**One sentence:** Screen GitHub code, releases, skills, and MCP tools for supply-chain and prompt-injection risk before an agent installs or executes them.

**Primary audiences:**

1. AI-agent builders who install skills, MCP servers, and coding tools.
2. Security-minded maintainers and developer-experience teams.
3. Developers who need a fast first-pass review before trying an unfamiliar GitHub project.

**Promise:** Give people a short, evidence-backed `GREEN / AMBER / RED` report—not an unsupported “safe” label.

## Before publishing

- Create the public repository under `Digitalfrontiersman` with the name `github-supply-chain-screener`.
- Add repository description: `Evidence-first GitHub repo, package, skill, and MCP security screener.`
- Add topics: `supply-chain-security`, `prompt-injection`, `agent-security`, `mcp-security`, `devsecops`, `github-actions`, `open-source-security`, `python`.
- Add a social-preview image that says `Screen before you install` and shows the four checks: provenance, code, dependencies, instructions.
- Pin the repository to the GitHub profile and add a profile README linking to it.
- Enable discussions; use categories `Announcements`, `Security research`, `Show and tell`, and `Ideas`.
- Add branch protection and require the CI check before merges.

GitHub topics improve discovery, and the project can later demonstrate secure-maintenance practices through OpenSSF’s free best-practices program. See the sources in `references/evidence.md`.

## Launch sequence

### Week 1: earn trust

- Publish a short launch post: the problem, the scope, a 60-second example, and explicit limitations.
- Publish three transparent example reports: a low-risk established project, an ambiguous project, and an inert prompt-injection fixture. Never name a project as malicious without verifiable evidence and responsible disclosure.
- Create a "What this catches / what it cannot catch" diagram or post.
- Invite 10 security-minded builders to test it and report false positives.

### Weeks 2–4: make it useful in public

- Ship one small, tested improvement each week.
- Post a weekly "review pattern"—one safe rule, why it matters, and its false-positive trade-off.
- Turn the scanner into a GitHub Action or pre-merge check only after the command-line workflow has stable tests and documented false-positive behavior.
- Publish a public roadmap with three clear first issues: rule quality, test fixtures, and provenance checks.

### Months 2–3: create a contribution loop

- Run a monthly, opt-in community audit clinic for repositories that request it.
- Publish anonymized trend summaries from opt-in reports; do not collect or expose sensitive repository data.
- Welcome contributors with issue labels such as `good first issue`, `rule proposal`, `false positive`, and `research`.
- Partner with security communities and agent-framework maintainers through useful contributions, not mass outreach.

## Metrics

Do not optimize for stars alone. Track:

| Stage | 90-day indicator |
| --- | --- |
| Usefulness | 100 documented scanner runs or feedback reports |
| Trust | 0 unaddressed critical reports; published security policy; CI and release notes |
| Community | 10 external issue/PR participants and 3 repeat contributors |
| Reach | 1,000 GitHub stars is an aspiration, not a guarantee |
| Retention | 25 weekly active users or teams re-running the tool |

Thousands of users come from a repeatable loop: a fast first result, credible public evidence, a workflow that fits GitHub/CI, and contributors whose improvements are visible. Avoid star-for-star schemes, spam, or claims of detecting malware with certainty; they undermine the trust this project needs.
