# Higgsfield Goblin

Turn a rough creative idea into a controlled cinematic production plan for Higgsfield—from concept and shot design through prompts, continuity, review, editing, and delivery.

## The moment

You know the film, commercial, trailer, short, or social sequence you want to make, but the work is scattered across prompting, model selection, storyboards, character consistency, product accuracy, editing, sound, and exports. A beautiful isolated generation is not yet a finished piece.

## The role

Higgsfield Goblin is the production creature living between your idea and the final cut.

The behavior is concrete: it turns intent into a north star, treatment, Director DNA, asset bible, beat map, shot list, model route, copy-ready prompts, staged generation plan, continuity review, edit, sound, color, and platform deliverables. When an approved Higgsfield connection is available, it can route execution through the official MCP or CLI.

## What it does

- Directs cinematic films, commercials, product ads, trailers, music videos, YouTube sequences, and vertical social work.
- Converts filmmaker references into controllable camera, lens, light, blocking, performance, edit, and sound decisions instead of relying on name-dropping.
- Builds recurring character, product, prop, location, visual, and audio bibles before motion generation.
- Routes each shot to a suitable current Higgsfield tool or model after inspecting live capabilities.
- Compiles image, single-shot, multi-shot, dialogue, audio, and constraint prompts.
- Preserves job IDs, prompt versions, asset references, acceptance criteria, and continuity handoffs.
- Reviews outputs as footage inside an edit and classifies them as approve, post-fix, revise, salvage, or kill.
- Plans finishing, captions, clean masters, cutdowns, thumbnails, and provenance archives.
- Works in manual packet mode when Higgsfield is not connected.

## What it does not do

- It does not include Higgsfield, free credits, paid models, private courses, or proprietary prompt libraries.
- It does not install software, authenticate accounts, spend credits, publish work, or alter configuration without user approval.
- It cannot guarantee model availability, generation quality, perfect continuity, legal clearance, factual advertising claims, or platform performance.
- It does not replace a human director, editor, brand owner, rights review, or final quality-control pass.
- It must not train or reproduce a real person's identity or voice without appropriate consent.

## Install

Clone the public collection:

```powershell
git clone --depth 1 https://github.com/Digitalfrontiersman/skills.git digitalfrontiersman-skills
```

Install on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
Copy-Item -Recurse -Force ".\digitalfrontiersman-skills\higgsfield-goblin" "$env:USERPROFILE\.codex\skills\higgsfield-goblin"
```

Install on macOS or Linux:

```bash
mkdir -p ~/.codex/skills
cp -R digitalfrontiersman-skills/higgsfield-goblin ~/.codex/skills/higgsfield-goblin
```

Start a fresh Codex task and try:

```text
Use $higgsfield-goblin to turn my product idea into a 15-second cinematic vertical ad. Build the treatment, asset plan, shot list, prompts, and review criteria before generating anything.
```

Higgsfield's official MCP endpoint is declared as an optional tool dependency in `agents/openai.yaml`. Connection requires a compatible client, Higgsfield account authentication, and user approval. The skill remains useful without it.

## Proof scenario

**Input:** “Make a tense, elegant 15-second vertical ad for a premium black coffee can in a rain-soaked city. Keep the can perfectly accurate. I like precise framing and tactile, fragmented night imagery, but I do not want a cheap director imitation. Higgsfield is not connected.”

**Observable result:** The skill selects manual Greenlight and Pre-production modes, defines the creative north star and anti-goal, translates the references into camera/light/edit rules, creates a product truth-sheet workflow, maps the 15-second edit, writes four shot prompts with immutable product constraints, and recommends testing the highest-risk continuity shot first. It does not claim to generate footage or spend credits.

## Trust

- The package passed the Codex skill validator and deterministic public-package contract tests.
- The operating workflow was forward-tested on the proof scenario without a Higgsfield connection or paid generation.
- No credentials, private URLs, client details, local machine paths, unpublished plans, or paid course material are bundled.
- External generations send user-provided prompts and media to the connected service under that service's terms and privacy practices.
- See [PRIVACY.md](PRIVACY.md), [SECURITY.md](SECURITY.md), and [PUBLIC_RELEASE.md](PUBLIC_RELEASE.md).

Run the tests:

```powershell
python -m unittest discover -s higgsfield-goblin/tests -v
```

## Included files

| File | Purpose |
| --- | --- |
| `SKILL.md` | Core production workflow and operating boundaries. |
| `agents/openai.yaml` | Skill metadata and optional official Higgsfield MCP dependency. |
| `references/` | Model-independent directing, prompting, integration, quality, and source guidance. |
| `scripts/preflight.py` | Read-only local detection; it does not install, log in, configure, or generate. |
| `tests/test_skill_contract.py` | Deterministic public-package and boundary tests. |
| `PRIVACY.md` | Data and external-service privacy boundaries. |
| `SECURITY.md` | Private reporting route and integration scope. |
| `docs/RELEASE_BRIEF.md` | Promise, interpretation, trust signals, and release gate. |
| `docs/LAUNCH.md` | GitHub card, headlines, launch post, and proof scenario. |
| `LICENSE` | MIT public reuse terms. |

## Independent project notice

Higgsfield Goblin is an independent community skill. It is not affiliated with, sponsored by, or endorsed by Higgsfield, Inc. “Higgsfield” and related product names belong to their respective owners. Official public links are included for interoperability and source attribution.
