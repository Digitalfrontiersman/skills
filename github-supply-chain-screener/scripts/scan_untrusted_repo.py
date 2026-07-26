#!/usr/bin/env python3
"""Static triage for untrusted repository text. Does not execute target code."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TEXT_EXTENSIONS = {
    ".md", ".txt", ".rst", ".py", ".js", ".ts", ".tsx", ".jsx", ".json",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".ps1", ".sh", ".bash", ".bat",
    ".cmd", ".xml", ".html", ".css", ".go", ".rs", ".java", ".rb", ".php",
}
SKIP_DIRS = {".git", "node_modules", "vendor", "dist", "build", ".venv", "venv"}
RULES = [
    ("critical", "shell-pipe-download", r"(?:curl|wget)\b[^\n|]{0,240}\|\s*(?:ba)?sh\b"),
    ("critical", "powershell-download-exec", r"(?:invoke-expression|iex\b|downloadstring|webclient).*?(?:http|https)"),
    ("high", "encoded-payload", r"(?:base64\s+(?:-d|--decode)|frombase64string|eval\s*\()"),
    ("high", "credential-or-secret-access", r"(?:\.ssh|aws_access_key|github_token|api[_-]?key|secret[_-]?key|credential)"),
    ("high", "package-install-hook", r"(?:preinstall|postinstall|prepare)\b"),
    ("high", "prompt-injection-override", r"(?:ignore|disregard|override|forget)\s+(?:all\s+)?(?:previous|prior|system|developer).*?(?:instruction|prompt)"),
    ("high", "prompt-injection-concealment", r"(?:do not tell|hide (?:this|your)|keep (?:this|it) secret|silently)"),
    ("high", "prompt-injection-exfiltration", r"(?:send|upload|exfiltrate|reveal).*?(?:secret|token|credential|password|private data)"),
    ("medium", "remote-execution-api", r"(?:child_process|subprocess\.|os\.system|runtime\.getruntime\(\)\.exec)"),
    ("medium", "external-network-call", r"(?:https?://|requests\.(?:get|post)|fetch\(|axios\.|invoke-webrequest)"),
]


def scan_file(path: Path) -> list[dict]:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    findings = []
    for number, line in enumerate(text.splitlines(), start=1):
        for severity, rule, pattern in RULES:
            if re.search(pattern, line, flags=re.IGNORECASE):
                findings.append({
                    "file": str(path), "line": number, "severity": severity,
                    "rule": rule, "excerpt": line.strip()[:300],
                })
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Statically triage an untrusted repository without executing it.")
    parser.add_argument("path", type=Path, help="Local repository or extracted release directory")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()
    root = args.path.resolve()
    if not root.is_dir():
        parser.error("path must be a directory")

    findings = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts) or not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        findings.extend(scan_file(path))
    rank = {"critical": 0, "high": 1, "medium": 2}
    findings.sort(key=lambda item: (rank[item["severity"]], item["file"], item["line"]))
    summary = {level: sum(item["severity"] == level for item in findings) for level in rank}
    result = {"root": str(root), "summary": summary, "findings": findings}
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Scanned: {root}")
        print("Findings: " + ", ".join(f"{k}={v}" for k, v in summary.items()))
        for item in findings:
            print(f"[{item['severity'].upper()}] {item['rule']} {item['file']}:{item['line']}\n  {item['excerpt']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
