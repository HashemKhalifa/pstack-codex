from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_port import (
    EXPECTED_AGENTS,
    EXPECTED_EVIDENCE,
    EXPECTED_SKILLS,
    EXPECTED_UPSTREAM_RESOURCES,
    validate_port,
)


class ValidatePortTest(unittest.TestCase):
    def test_complete_codex_port_is_valid(self) -> None:
        plugin_root = Path(__file__).resolve().parents[1]
        repo_root = plugin_root.parents[1]

        self.assertEqual(45, len(EXPECTED_SKILLS))
        self.assertEqual({"comment-sicko", "poteto-agent"}, EXPECTED_AGENTS)
        self.assertEqual({"validation/2026-08-31-pstack-script-tests.md"}, EXPECTED_EVIDENCE)
        self.assertEqual(11, len(EXPECTED_UPSTREAM_RESOURCES))
        self.assertEqual([], validate_port(plugin_root, repo_root))


if __name__ == "__main__":
    unittest.main()
