# Create a Public Skill

Use this checklist whenever adding a new public skill to this repository.

## Required folder structure

```text
skill-slug/
├── SKILL.md          # Required: instructions for the agent
├── README.md         # Required: plain-English guide for people
├── LICENSE           # Required for public reuse
├── PUBLIC_RELEASE.md # What was checked before publication
└── references/       # Optional: only when the skill relies on source material
```

## What to put where

- **SKILL.md** — the agent's operating instructions, boundaries, and workflow.
- **README.md** — what the skill does, who it helps, what it includes, how to use it, and what it does not do.
- **Root README catalog** — add one row under **Available skills** with the skill name, a relative link to its folder, and one clear sentence explaining it.
- **Commit message** — say what changed, for example: `Add [Skill Name] public release`. This is change history, not the public description.

## Root README row

Copy and adapt this line:

```md
| [Skill Name](skill-slug/) | One clear sentence explaining the outcome the skill helps people achieve. |
```

## Public-release checks

- No secrets, credentials, private links, client information, or personal data.
- No copied proprietary courses, exercises, or paid material.
- Clear safety and scope boundaries where the topic has real-world risk.
- Links work, file names are clear, and the README matches the files actually published.
- Add the catalog row before announcing the skill.
