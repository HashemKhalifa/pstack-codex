from pathlib import Path
import sys
import tomllib
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_port import (
    EXPECTED_AGENTS,
    EXPECTED_EVIDENCE,
    EXPECTED_SKILLS,
    EXPECTED_UPSTREAM_RESOURCES,
    validate_agent_smoke,
    validate_port,
)


class ValidatePortTest(unittest.TestCase):
    def test_complete_codex_port_is_valid(self) -> None:
        plugin_root = Path(__file__).resolve().parents[1]
        repo_root = plugin_root.parents[1]

        self.assertEqual(45, len(EXPECTED_SKILLS))
        self.assertEqual(
            {
                "comment-sicko",
                "poteto-agent",
                "pstack_architect",
                "pstack_minimalist",
                "pstack_skeptic",
            },
            EXPECTED_AGENTS,
        )
        self.assertEqual(
            {
                "validation/2026-08-31-agent-smoke.json",
                "validation/2026-08-31-pstack-script-tests.md",
            },
            EXPECTED_EVIDENCE,
        )
        self.assertEqual(11, len(EXPECTED_UPSTREAM_RESOURCES))
        self.assertEqual([], validate_port(plugin_root, repo_root))

    def test_copyable_agents_are_self_contained(self) -> None:
        repo_root = Path(__file__).resolve().parents[3]
        for filename in ("poteto-agent.toml", "comment-sicko.toml"):
            agent = tomllib.loads((repo_root / ".codex" / "agents" / filename).read_text())
            self.assertNotIn("plugins/pstack-codex/", agent["developer_instructions"])

    def test_setup_documents_project_trust(self) -> None:
        repo_root = Path(__file__).resolve().parents[3]
        self.assertIn("trust", (repo_root / "README.md").read_text().lower())
        self.assertIn(
            "trust",
            (repo_root / "plugins" / "pstack-codex" / "skills" / "setup-pstack" / "SKILL.md")
            .read_text()
            .lower(),
        )

    def test_agent_smoke_receipt_requires_every_successful_agent(self) -> None:
        valid = {
            "schema": "pstack-codex-agent-smoke-v1",
            "codex_version": "codex-cli 0.151.0",
            "commit": "a" * 40,
            "agents": [
                {"agent": name, "success": True} for name in sorted(EXPECTED_AGENTS)
            ],
            "passed": True,
        }
        self.assertEqual([], validate_agent_smoke(valid))
        valid["agents"][0]["success"] = False
        self.assertIn("agent smoke did not pass all agents", validate_agent_smoke(valid))


if __name__ == "__main__":
    unittest.main()
