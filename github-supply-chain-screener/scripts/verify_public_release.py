#!/usr/bin/env python3
"""Fail a public-release check for common secret files and token-like values.

This is deliberately conservative and uses no third-party packages. It is a
release guard, not a replacement for a human confidentiality review.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

IGNORED_PARTS = {".git", "__pycache__", ".venv", "node_modules"}
BLOCKED_NAMES = {".env", ".env.local", "credentials.json", "id_rsa", "id_ed25519"}
BLOCKED_SUFFIXES = {".pem", ".p12", ".pfx", ".key"}
PATTERNS = {
    "GitHub personal access token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "OpenAI API key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private key block": re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----"),
}


def should_skip(path: Path) -> bool:
    return any(part in IGNORED_PARTS for part in path.parts)


def scan(root: Path) -> list[str]:
    findings: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or should_skip(path.relative_to(root)):
            continue
        relative = path.relative_to(root)
        if path.name.lower() in BLOCKED_NAMES or path.suffix.lower() in BLOCKED_SUFFIXES:
            findings.append(f"Blocked secret file: {relative}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"Review non-text file before public release: {relative}")
            continue
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                findings.append(f"Possible {label}: {relative}")
    return findings


if __name__ == "__main__":
    release_root = Path(__file__).resolve().parents[1]
    problems = scan(release_root)
    if problems:
        print("Public-release check failed:")
        print("\n".join(f"- {problem}" for problem in problems))
        sys.exit(1)
    print("Public-release check passed. Complete a human confidentiality review before publishing.")
