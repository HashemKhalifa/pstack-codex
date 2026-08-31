from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from validate_release import extract_release_notes, set_manifest_version, validate_release


class ValidateReleaseTest(unittest.TestCase):
    def test_version_and_changelog_match_tag(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "plugins" / "pstack-codex" / ".codex-plugin"
            manifest.mkdir(parents=True)
            (manifest / "plugin.json").write_text(
                '{"name":"pstack-codex","version":"1.0.0"}\n'
            )
            (root / "CHANGELOG.md").write_text(
                "# Changelog\n\n## [1.0.0] - 2026-08-31\n\n### Added\n\n- Live agent smoke.\n"
            )
            self.assertEqual([], validate_release(root, "v1.0.0"))
            self.assertIn(
                "### Added",
                extract_release_notes(
                    (root / "CHANGELOG.md").read_text(), "1.0.0"
                ),
            )

    def test_set_manifest_version_preserves_other_fields(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "plugins" / "pstack-codex" / ".codex-plugin"
            manifest.mkdir(parents=True)
            path = manifest / "plugin.json"
            path.write_text(
                '{"name":"pstack-codex","version":"0.0.0-development","skills":"./skills/"}\n'
            )
            set_manifest_version(root, "1.2.3")
            contents = path.read_text()
            self.assertIn('"version": "1.2.3"', contents)
            self.assertIn('"skills": "./skills/"', contents)

    def test_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            manifest = root / "plugins" / "pstack-codex" / ".codex-plugin"
            manifest.mkdir(parents=True)
            (manifest / "plugin.json").write_text(
                '{"name":"pstack-codex","version":"1.0.1"}\n'
            )
            (root / "CHANGELOG.md").write_text("# Changelog\n")
            errors = validate_release(root, "v1.0.0")
            self.assertTrue(any("manifest version" in error for error in errors))
            self.assertTrue(any("changelog" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
