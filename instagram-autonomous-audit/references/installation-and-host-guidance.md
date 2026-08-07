# Installation and Host Guidance

This is a portable Markdown skill. Keep the `instagram-autonomous-audit` folder intact and place it in the host's skills directory. The agent must follow its own browser, approval, authentication, and data-handling policies.

## Host setup

| Host | Practical setup |
|---|---|
| Codex | Put the folder in `~/.codex/skills/`. Invoke `$instagram-autonomous-audit` or ask for an Instagram audit. Use a supported browser-control capability with the user already signed into Instagram. |
| Claude Code | Put the folder in the project's or user's Claude skill directory supported by that installation. Ensure the environment has an approved browser or data-export route; do not assume a Chrome session is available. |
| OpenClaw | Add the folder to the OpenClaw skills path configured by that installation. Connect a browser/account capability or request an exported Insights file. |
| Hermes or another agent | Give the complete folder or install it from the shared GitHub repository once published. Map the skill's read-only workflow to that agent's browser and approval system. |

## Conversation behavior

Start by explaining what data the audit can retrieve and what it cannot. Ask one clarifying question at a time. Do not ask the user to locate internal Instagram paths if the agent can navigate them. If a permission, login, CAPTCHA, or account switch is required, pause and state the exact action the user needs to take.

## Data safety

Treat professional dashboard metrics as private account data. Keep them inside the user-approved destination. Do not upload reports, exports, screenshots, or credentials to a third party without explicit permission.

## GitHub distribution

After this folder is in a GitHub repository, another compatible agent can install it by cloning/downloading the repository and placing the folder in its configured skills directory. A public GitHub URL makes the skill easy to retrieve; it does not grant Instagram access or bypass the host agent's browser and approval rules.
