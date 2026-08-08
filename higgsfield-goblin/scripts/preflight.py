#!/usr/bin/env python3
"""Read-only Higgsfield/Codex integration preflight.

Detects relevant executables and reports safe next steps. It does not install,
authenticate, edit configuration, call remote APIs, or spend credits.
"""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import asdict, dataclass


@dataclass
class Check:
    name: str
    found: bool
    path: str | None
    version: str | None


def executable_check(name: str) -> Check:
    path = shutil.which(name)
    if not path:
        return Check(name=name, found=False, path=None, version=None)
    version = None
    for args in ([name, "--version"], [name, "version"]):
        try:
            completed = subprocess.run(
                args,
                capture_output=True,
                text=True,
                timeout=5,
                check=False,
            )
            output = (completed.stdout or completed.stderr).strip()
            if output:
                version = output.splitlines()[0]
                break
        except (OSError, subprocess.TimeoutExpired):
            continue
    return Check(name=name, found=True, path=path, version=version)


def main() -> int:
    checks = [executable_check("higgsfield"), executable_check("codex")]
    report = {
        "checks": [asdict(check) for check in checks],
        "mcp_endpoint": "https://mcp.higgsfield.ai/mcp",
        "mutations_performed": False,
        "next_steps": [],
    }
    if not checks[0].found:
        report["next_steps"].append(
            "Higgsfield CLI is absent. Ask before installing @higgsfield/cli."
        )
    else:
        report["next_steps"].append(
            "CLI found. Ask before login; then inspect auth/account and live models."
        )
    if not checks[1].found:
        report["next_steps"].append(
            "Codex CLI is absent or not on PATH; MCP may still be configured in desktop settings."
        )
    else:
        report["next_steps"].append(
            "Codex CLI found. Use `codex mcp list` only when live connection inspection is needed."
        )
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
