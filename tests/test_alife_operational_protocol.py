"""Static research protocol checks: NOT an organism experiment or simulation."""
from __future__ import annotations
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ALifeOperationalProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec = json.loads((ROOT / "data/alife/operational-tests.json").read_text(encoding="utf-8"))
        cls.papers = {p["id"]: p for p in (
            json.loads(line) for line in (ROOT / "data/papers.jsonl").read_text().splitlines() if line
        )}

    def test_protocol_declares_no_authorization(self):
        self.assertEqual(self.spec["status"], "proposed_research_only")
        self.assertFalse(self.spec["organism_implementation_authorized"])
        self.assertNotIn("alive_or_dead_score", self.spec)
        self.assertGreater(len(self.spec["global_rule"]), 20)

    def test_ten_claim_axes_with_independent_null_controls(self):
        cs = self.spec["criteria"]
        self.assertEqual(len(cs), 10)
        self.assertEqual({c["id"] for c in cs}, {f"AL-C{i:02d}" for i in range(1,11)})
        for c in cs:
            self.assertGreater(len(c["claim"]), 10)
            self.assertGreater(len(c["positive_evidence"]), 40)
            self.assertGreater(len(c["critical_null"]), 20)
            self.assertGreater(len(c["falsifier"]), 35)
            self.assertGreaterEqual(len(c["required_artifacts"]), 3)
            self.assertGreaterEqual(len(c["primary_sources"]), 1)
            for source_id in c["primary_sources"]:
                self.assertIn(source_id, self.papers)

    def test_replication_is_not_assumed_heredity(self):
        by_id = {c["id"]: c for c in self.spec["criteria"]}
        self.assertEqual(by_id["AL-C02"]["axis"], "replication")
        self.assertEqual(by_id["AL-C04"]["axis"], "heredity")
        self.assertEqual(by_id["AL-C05"]["axis"], "maintenance")
        self.assertEqual(by_id["AL-C09"]["axis"], "computational_language")
        self.assertNotEqual(by_id["AL-C02"]["positive_evidence"],by_id["AL-C04"]["positive_evidence"])

    def test_separate_project_requires_permission(self):
        designs = [json.loads(s) for s in (ROOT/"data/alife/experiment-designs.jsonl").read_text().splitlines() if s]
        self.assertEqual(len(designs),8)
        for design in designs:
            self.assertTrue(design["future_authorization_required"])
            self.assertEqual(design["implementation_status"], "not_authorized")

    def test_dossier_exists(self):
        text = (ROOT/"docs/artificial-life/23-unified-organism-evidence-standard.md").read_text(encoding="utf-8")
        self.assertIn("AL-C01", text)
        self.assertIn("no deployment", text.lower()) if "no deployment" in text.lower() else self.assertIn("not an approved",text.lower())


if __name__ == "__main__":
    unittest.main()
