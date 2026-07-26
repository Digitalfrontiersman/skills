# Public-release boundary

This repository is a public Digital Frontiersman project. Everything committed
here may be copied, indexed, or redistributed indefinitely.

## What belongs here

- reusable skills, scripts, tests, documentation, and examples that contain no
  personal, client, member, or business-confidential information;
- source code that can be safely inspected and run by the public; and
- generic configuration with secrets supplied only through environment
  variables or GitHub Actions secrets.

## What never belongs here

- API keys, passwords, tokens, cookies, private URLs, local paths containing
  personal data, or exported browser/account data;
- client work, paid-member materials, private prompts, contact lists, or
  unpublished product plans; and
- `.env` files, credential stores, private repositories copied as submodules,
  or unreviewed third-party binaries.

## Publishing rule

Private work stays in a separate **private repository and local worktree**.
Copying anything into a public repository is a deliberate release: review the
diff, run `python scripts/verify_public_release.py`, then commit. Never use a
sync job that automatically mirrors private work to public GitHub.

The verifier is a safety net, not proof that information is safe to publish.
It checks for common secret files and token-like strings; the human release
review remains required.
