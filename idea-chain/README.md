# IDEA CHAIN

Turn one rough seed into a short, causal chain of major ideas that reaches one clear goal.

## The moment

You have the beginning of something--a business, campaign, product, page, story, event, or half-formed thought--but the leap from "interesting" to "fully conceived" is still missing. Ordinary brainstorming creates more fragments when what you need is direction.

## The role

IDEA CHAIN is a creative fuse. It starts at one defined seed, makes every major idea ignite the next, and stops only when the chain reaches one defined goal.

The metaphor is simple; the behavior is concrete: the skill produces only 3-5 major links, explains why each matters, and makes every causal handoff explicit.

## What it does

- Asks the user to choose Fast, Pro, or God Mode before beginning unless a mode was already supplied.
- Establishes a clear `START -> GOAL` before building the concept.
- Produces 3-5 connected major ideas rather than a pile of disconnected options.
- Uses focused research in Pro Mode and multi-angle research plus pressure-testing in God Mode.
- Tests truth, tension, edge, causality, weak assumptions, and compression before answering.
- Expands only the selected link when the user asks to zoom in.
- Uses the approved chain as the creative spine for a brief, story, campaign, offer, page, or action plan.

## What it does not do

- It does not guarantee that an idea is original, commercially successful, factually complete, or right for every audience.
- It does not replace customer research, legal review, financial analysis, safety review, or human judgment.
- It does not silently activate a different model or reasoning setting; it can only use or recommend capabilities available in the hosting environment.
- It does not make publication, spending, access, deletion, or other consequential decisions for the user.

## Choose a mode

- **Fast Mode:** Move quickly from supplied context to three strong links.
- **Pro Mode:** Add focused research, authoritative sources, verification, and a non-obvious insight.
- **God Mode:** Use deep multi-angle research, counterexamples, audience evidence, second-order effects, and pressure-testing before distilling the result.

## Install

Clone the public collection:

```powershell
git clone --depth 1 https://github.com/Digitalfrontiersman/skills.git digitalfrontiersman-skills
```

Install on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\digitalfrontiersman-skills\idea-chain" "$env:USERPROFILE\.codex\skills\idea-chain"
```

Install on macOS or Linux:

```bash
mkdir -p ~/.codex/skills
cp -R digitalfrontiersman-skills/idea-chain ~/.codex/skills/idea-chain
```

Start a fresh Codex task and try:

```text
Use $idea-chain to turn this rough business idea into a clear concept.
```

Or select the mode immediately:

```text
Use $idea-chain in Pro Mode with a brutal reality check: create a launch concept for an AI workshop aimed at first-time founders.
```

## Proof scenario

**Before:** "I want to launch an AI workshop for first-time founders" produces dozens of disconnected names, topics, channels, and tactics.

**With IDEA CHAIN:** The user selects Pro Mode. The skill defines the founder's starting problem and the workshop's outcome, researches the decisive assumptions, then returns 3-5 linked moves in which the audience tension shapes the promise, the promise shapes the workshop mechanism, and the mechanism shapes the launch.

**Observable result:** one coherent concept that can immediately become a brief or campaign.

## Trust

- The public package contains no credentials, client details, private URLs, personal memory, or proprietary assets.
- Contract tests verify the required files, metadata, mode-selection behavior, chain-length rule, and common secret patterns.
- Pro and God research remain limited by the hosting model, available tools, source quality, and permissions.
- See [PRIVACY.md](PRIVACY.md), [SECURITY.md](SECURITY.md), and [PUBLIC_RELEASE.md](PUBLIC_RELEASE.md).

Run the public-release tests:

```powershell
python -m unittest discover -s idea-chain/tests -v
```

## Included files

| File | Purpose |
| --- | --- |
| `SKILL.md` | Operating instructions for the agent. |
| `agents/openai.yaml` | Display metadata for compatible skill interfaces. |
| `tests/test_skill_contract.py` | Deterministic public-package contract tests. |
| `PRIVACY.md` | Data and research privacy boundaries. |
| `SECURITY.md` | Private security-reporting route and scope. |
| `docs/RELEASE_BRIEF.md` | Promise, interpretation, trust signals, and release gate. |
| `docs/LAUNCH.md` | GitHub card, headlines, launch post, and proof scenario. |
| `LICENSE` | MIT public reuse terms. |
| `PUBLIC_RELEASE.md` | Public-release boundaries and review notes. |
