# Create Public Skill

A release workflow for turning a private Codex skill into a safe, understandable public GitHub package.

## What it does

It audits a source skill, removes private or unsafe material, builds a complete public folder, validates it, publishes it intentionally, and adds the linked one-line entry to the repository's main skill catalog.

## Included files

| File | Purpose |
| --- | --- |
| `SKILL.md` | The agent workflow for public releases. |
| `agents/openai.yaml` | Display metadata for compatible skill interfaces. |
| `LICENSE` | Public reuse terms. |
| `PUBLIC_RELEASE.md` | Release boundaries and checks. |

## Important boundary

This skill never publishes automatically. A user must explicitly decide to make the specific skill public.
