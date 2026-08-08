from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
OPENAI_YAML = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
INTEGRATION = (ROOT / "references" / "integration.md").read_text(encoding="utf-8")
PREFLIGHT = (ROOT / "scripts" / "preflight.py").read_text(encoding="utf-8")


class HiggsfieldGoblinPublicContract(unittest.TestCase):
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
            "references/higgsfield-playbook.md",
            "references/prompt-system.md",
            "references/directing-editing.md",
            "references/integration.md",
            "references/quality-control.md",
            "references/source-map.md",
            "scripts/preflight.py",
        }
        present = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file()
        }
        self.assertTrue(required.issubset(present), required - present)

    def test_skill_metadata_and_modes(self) -> None:
        self.assertRegex(SKILL, r"(?m)^name: higgsfield-goblin$")
        for mode in ("Spark", "Greenlight", "Pre-production", "Shoot", "Rescue", "Post", "Campaign", "Teach"):
            self.assertIn(f"**{mode}**", SKILL)
        self.assertIn("$higgsfield-goblin", OPENAI_YAML)

    def test_approval_and_quality_boundaries(self) -> None:
        self.assertIn("Never install software, authenticate, publish, or spend generation credits without the user's approval", SKILL)
        self.assertIn("Never claim a generation succeeded without reviewing the returned artifact", SKILL)
        self.assertIn("consent", SKILL.lower())
        self.assertIn("https://mcp.higgsfield.ai/mcp", OPENAI_YAML)
        self.assertIn("default_tools_approval_mode = \"writes\"", INTEGRATION)

    def test_preflight_declares_and_avoids_mutation(self) -> None:
        self.assertIn('"mutations_performed": False', PREFLIGHT)
        for forbidden in ("pip install", "npm install", "auth login", "mcp add", "generate create"):
            self.assertNotIn(forbidden, PREFLIGHT)

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
