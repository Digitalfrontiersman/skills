# Evidence and interpretation

## What the numbers mean

Do not report one universal "chance a package is malicious." The denominator differs by ecosystem, package version, campaign, and detection vendor. A dependency vulnerability rate is also not a malware prevalence rate.

- A 2025 dependency dataset reported at least one known-vulnerable dependency for 6.93% of npm versions, 3.91% of Cargo versions, 7.5% of RubyGems versions, and 0.42% of PyPI versions. This measures known vulnerable dependencies, not malicious packages. [Dataset](https://www.sciencedirect.com/science/article/pii/S2352340925006274)
- Sonatype reported more than 454,600 newly identified malicious packages across several ecosystems in 2025. Treat it as vendor telemetry, not a probability for any individual package. [Report](https://www.sonatype.com/state-of-the-software-supply-chain/2026/open-source-malware)
- In a benchmark of agent attacks/defenses, the highest average attack success rate was 84.30%. That is a benchmark result, not a real-world prevalence rate. [Agent Security Bench](https://mlanthology.org/iclr/2025/zhang2025iclr-agent/)

## Authoritative verification sources

- [GitHub supply-chain security](https://docs.github.com/en/code-security/concepts/supply-chain-security/supply-chain-security): dependency graph, advisories, immutable releases, SBOMs, and artifact attestations.
- [GitHub dependency review](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review): package age, popularity, and vulnerability context for direct and transitive dependency changes.
- [GitHub Actions script-injection guidance](https://docs.github.com/en/actions/concepts/security/script-injections): treat event fields and other external content as untrusted; do not interpolate them into commands.
- [OWASP prompt-injection testing guidance](https://github.com/OWASP/www-project-ai-testing-guide/blob/main/Document/content/tests/AITG-APP-01_Testing_for_Prompt_Injection.md): prompt injection can redirect an agent toward unintended actions, data exposure, or unauthorized tool use.
- [GitHub agentic-workflow threat detection](https://github.github.com/gh-aw/reference/threat-detection/): examples of detecting prompt injection, secrets, and malicious patches before applying outputs.

## Practical evidence hierarchy

1. Cryptographic verification: checksum and signed provenance/attestation tied to the exact artifact.
2. Canonical upstream project and pinned commit/tag, corroborated by release history.
3. Source and manifest review with no unexplained installation/network/credential behavior.
4. Advisory and incident checks across GitHub Advisory Database and OSV.
5. Reputation signals such as stars, forks, and downloads. Use only as supporting context.

Absence of a known advisory, a clean static scan, stars, or a virus scan alone never proves safety.
