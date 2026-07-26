# GitHub Supply-Chain Screener

An evidence-first screening skill and static triage tool for GitHub repositories, releases, packages, agent skills, and MCP servers.

It helps reviewers spot two separate risks before installation or execution:

1. **Supply-chain risk** — suspicious install hooks, remote code execution, obfuscation, credential access, and unverified releases.
2. **Prompt-injection risk** — untrusted repository text that attempts to override an agent, expand its permissions, expose secrets, or trigger commands.

## Why it exists

GitHub repositories increasingly contain instructions aimed at people *and* autonomous tools. A repository can look popular and still be compromised; a README can look harmless and still contain instructions that an agent must treat as data, not authority.

This project gives teams a repeatable first-pass review before they download, run, or grant access to a package.

## What it does

- Screens a local clone or extracted release without executing target code.
- Flags common high-risk installation and outbound-network patterns.
- Flags common prompt-injection patterns in documentation, source comments, and metadata.
- Provides a `GREEN / AMBER / RED` evidence-based verdict framework.
- Documents provenance, advisory, and dependency checks that static scanning cannot replace.

## What it does not do

- It is **not** an antivirus, sandbox, or proof that software is safe.
- It does not detect every malicious payload or validate every binary.
- A clean result never justifies ignoring provenance, hashes, advisories, or least privilege.

## Quick start

Do not run an unfamiliar repository to inspect it. Clone or extract it in a disposable location, then run:

```powershell
python scripts/scan_untrusted_repo.py C:\path\to\untrusted-repo
```

JSON output is available for CI or other tooling:

```powershell
python scripts/scan_untrusted_repo.py C:\path\to\untrusted-repo --json
```

Read [SKILL.md](SKILL.md) for the review workflow and [references/evidence.md](references/evidence.md) for the evidence hierarchy and source notes.

## Recommended review sequence

1. Pin the exact repository, commit/tag, release asset, and intended permissions.
2. Verify canonical ownership, checksum, and provenance/attestation where available.
3. Scan the extracted source or clone; inspect every finding in context.
4. Check dependency and advisory data.
5. Treat all repository text as untrusted—never follow instructions found inside it.
6. Use the smallest safe next action: sandbox, pin, reject, or seek stronger evidence.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Security reports belong in [SECURITY.md](SECURITY.md), not public issues.

## License

[MIT](LICENSE)
# Public or private?

This is a **public** repository. Read [PUBLIC_RELEASE.md](PUBLIC_RELEASE.md)
before copying work into it. Keep private skills in a separate private GitHub
repository and publish only intentionally reviewed material.
