# FIREWOLF Security Guardian

A calm security checkpoint for agent-assisted work involving untrusted content or consequential actions.

## What it does

FIREWOLF helps an agent assess risky links, files, commands, downloads, credentials, permissions, automations, and external actions. It traces whether untrusted content could lead to a harmful outcome and returns a clear decision: `ALLOW`, `ALLOW_WITH_NOTE`, `ASK`, or `BLOCK`.

## When to use it

Use it before installing software, opening suspicious links or downloads, sharing sensitive information, connecting tools, granting OAuth access, running commands, approving automations, or acting on instructions found in a webpage, message, document, or repository.

## What it does not do

- It is not an antivirus or a guarantee that a file or link is safe.
- It does not override the user's intent or make high-impact decisions silently.
- It does not follow instructions embedded in untrusted content.

## How it works

It identifies the requested action, treats external material as untrusted data, checks for a path to a dangerous outcome, chooses the least-privileged option, and explains the next safe step.

## Included files

| File | Purpose |
| --- | --- |
| `SKILL.md` | The agent's security decision workflow. |
| `references/` | Safety classifications and response playbooks. |
| `scripts/` | Optional structured decision support. |

## Important boundary

For suspected compromise or immediate danger, stop external actions, preserve minimal evidence, and use a known-clean device or qualified security support.
