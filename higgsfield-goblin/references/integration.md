# MCP and CLI integration

Snapshot: 2026-08-08. Verify commands and schemas from the official pages before changing configuration.

## Operating boundary

Connection setup, OAuth login, CLI installation, and generation can affect the user's machine, account, or credits. Explain the exact action and obtain approval first. Read-only detection and catalog inspection are safe when already connected.

## Official endpoints

- MCP: `https://mcp.higgsfield.ai/mcp`
- CLI repository: `https://github.com/higgsfield-ai/cli`
- CLI package on Windows: `@higgsfield/cli`

Higgsfield states that its MCP uses account sign-in rather than a manually managed API key. It supports compatible MCP agents including Hermes. Higgsfield recommends its CLI for Codex/Claude Code-style terminal agents, while Codex also supports Streamable HTTP MCP with OAuth.

## Codex MCP route

The skill metadata declares the Higgsfield MCP dependency. If it is not connected, use the Codex desktop MCP settings or a project-scoped `.codex/config.toml` in a trusted project.

Configuration shape:

```toml
[mcp_servers.higgsfield]
url = "https://mcp.higgsfield.ai/mcp"
auth = "oauth"
default_tools_approval_mode = "writes"
tool_timeout_sec = 300
```

After saving, restart the relevant client and authenticate the server. Official Codex commands include `codex mcp list`, `codex mcp login higgsfield`, and `codex mcp --help`. In the desktop composer or TUI, `/mcp` shows connected servers.

Do not write this configuration automatically without approval. Preserve unrelated config and use the narrowest project scope that meets the user's need.

## Hermes MCP route

Add a remote Streamable HTTP MCP server named `higgsfield` with the official endpoint, then complete account OAuth. Hermes configuration varies by release; inspect its current MCP documentation rather than inventing a file path or command. Confirm the tool list after login before generation.

## Official CLI route

On Windows the official repository documents:

```powershell
npm install -g @higgsfield/cli
higgsfield auth login
```

Installation and login require user approval. After authentication, discover rather than assume:

```powershell
higgsfield --help
higgsfield model list
higgsfield workflow list
higgsfield account
```

Inspect a selected model or workflow's current schema before creating a job. Prefer structured JSON output when available. Estimate cost when the live CLI supports it. Submit a small approved test, preserve the job ID, wait asynchronously, and review the returned media.

## Execution protocol

1. Run `scripts/preflight.py` for read-only detection.
2. Confirm account/workspace and available credits without exposing tokens.
3. List live models/workflows.
4. Inspect the selected schema and estimate cost.
5. Show the user the first batch plan.
6. Generate only after approval.
7. Poll with bounded waits; do not busy-loop.
8. Store prompt, settings, references, job ID, result path/URL, and verdict.
9. Never print or commit authentication tokens.

## Degraded mode

If neither integration is available, produce a manual run packet containing:

- selected Higgsfield feature/model
- input asset checklist and bindings
- copy-ready prompt
- settings
- expected duration/resolution/aspect ratio
- acceptance criteria
- iteration notes

The creative workflow remains useful without live generation.
