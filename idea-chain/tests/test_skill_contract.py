from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
OPENAI_YAML = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")


class IdeaChainPublicContract(unittest.TestCase):
    def test_required_public_files_exist(self) -> None:
        required = {
            "SKILL.md",
            "README.md",
            "LICENSE",
            "PRIVACY.md",
            "SECURITY.md",
            "PUBLIC_RELEASE.md",
            "agents/openai.yaml",
            "docs/RELEASE_BRIEF.md",
            "docs/LAUNCH.md",
        }
        present = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file()
        }
        self.assertTrue(required.issubset(present), required - present)

    def test_skill_metadata_and_mode_gate(self) -> None:
        self.assertRegex(SKILL, r"(?m)^name: idea-chain$")
        self.assertIn("Which IDEA CHAIN mode do you want", SKILL)
        for mode in ("FAST MODE", "PRO MODE", "GOD MODE"):
            self.assertIn(mode, SKILL)

    def test_chain_contract_is_present(self) -> None:
        self.assertIn("3-5 numbered sections total", SKILL)
        self.assertIn("This unlocks ->", SKILL)
        self.assertIn("This achieves ->", SKILL)
        self.assertIn("START -> GOAL", SKILL)

    def test_interface_metadata_invokes_the_skill(self) -> None:
        self.assertIn('display_name: "IDEA CHAIN"', OPENAI_YAML)
        self.assertIn("$idea-chain", OPENAI_YAML)

    def test_public_text_has_no_common_secrets_or_private_paths(self) -> None:
        windows_users = r"[A-Za-z]:\\" + "Users" + r"\\[^\\\s]+"
        macos_users = "/" + "Users" + r"/[^/\s]+"
        patterns = {
            "GitHub token": r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b",
            "OpenAI API key": r"\bsk-[A-Za-z0-9_-]{20,}\b",
            "AWS access key": r"\bAKIA[0-9A-Z]{16}\b",
            "private key": r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
            "Windows user path": windows_users,
            "macOS user path": macos_users,
        }
        text_files = [
            path
            for path in ROOT.rglob("*")
            if path.is_file() and path.suffix.lower() not in {".pyc"}
        ]
        for path in text_files:
            text = path.read_text(encoding="utf-8")
            for label, pattern in patterns.items():
                self.assertIsNone(re.search(pattern, text), f"{label} in {path}")


if __name__ == "__main__":
    unittest.main()
