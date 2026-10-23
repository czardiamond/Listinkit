"""Regression tests for build_seo.py --check exit status."""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent


class CheckExitTests(unittest.TestCase):
    def run_check(self, mutate=False):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copy2(ROOT / "build_seo.py", root / "build_seo.py")
            shutil.copytree(ROOT / "seo_content", root / "seo_content",
                            ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copytree(ROOT / "site", root / "site")
            if mutate:
                script = root / "build_seo.py"
                source = script.read_text(encoding="utf-8")
                original = "Free Real Estate Marketing Templates | ListingKit"
                self.assertIn(original, source)
                script.write_text(source.replace(original, original + " " + "x" * 80),
                                  encoding="utf-8")
            return subprocess.run([sys.executable, "build_seo.py", "--check"],
                                  cwd=root, capture_output=True, text=True, timeout=30)

    def test_valid_metadata_exits_successfully(self):
        result = self.run_check()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("problems: 0", result.stdout)

    def test_invalid_metadata_exits_nonzero(self):
        result = self.run_check(mutate=True)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("long title", result.stdout)


if __name__ == "__main__":
    unittest.main()
