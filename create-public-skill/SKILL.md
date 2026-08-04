---
name: create-public-skill
description: Prepare an existing private or local Codex skill for an intentional public GitHub release. Use when a user asks to make a skill public, publish a skill, move a private skill into a public skills repository, or check that a skill is ready to share.
---

# Create Public Skill

Turn a private skill into a public, reusable release without exposing private context or weakening safety.

## 1. Confirm the release target

Identify the exact source skill, the public repository, and whether the user has authorized publication. Keep private work private until the user explicitly decides to release it.

## 2. Audit the source before copying it

Check every file for credentials, tokens, private URLs, client or account details, personal data, internal project names, confidential workflow steps, and copied proprietary material.

Also check for instructions that infer authority too broadly. Require explicit user authority for publishing, sending, spending, deleting, permission changes, or sharing sensitive data.

## 3. Build the public package

Create a folder named after the skill's hyphen-case name. Include:

- `SKILL.md` with concise, safe operating instructions;
- `agents/openai.yaml` with display metadata;
- `README.md` explaining the skill in plain language;
- `LICENSE` and `PUBLIC_RELEASE.md`;
- only those references, scripts, and assets that are necessary and safe to publish.

Do not copy private ledgers, personal memory, client configurations, credentials, or account-specific operating notes.

## 4. Validate and publish intentionally

Run the skill validator. Verify every public file locally. Publish only the public package to the approved repository.

Update the root README's single **Available skills** table with:

```md
| [Skill Name](skill-slug/) | One clear sentence explaining the outcome the skill helps people achieve. |
```

The repository file list's commit-message column is change history, not the public explanation; use the root catalog and the skill README to help people understand the skill.

## 5. Verify the live release

Confirm the published folder, `SKILL.md`, metadata, supporting files, and root README link all resolve. Report what was intentionally excluded and the commit or live URL.
