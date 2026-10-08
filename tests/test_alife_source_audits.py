"""Validate ALife literature audit and source reproducibility receipts (metadata only).

These tests read JSONL and Markdown. They neither execute historical scientific
code nor instantiate artificial organisms, cellular automata or digital worlds.
"""
from __future__ import annotations
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def rows(path: str) -> list[dict]:
    return [json.loads(line) for line in (ROOT / path).read_text(encoding="utf-8").splitlines()
            if line.strip()]


class AlifeSourceAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = {p["id"]: p for p in rows("data/papers.jsonl")}
        cls.notes = rows("data/alife/source-notes.jsonl")
        cls.code = rows("data/alife/code-inventory.jsonl")

    def test_new_literature_links_have_deduped_canonical_ids(self):
        self.assertEqual(len(self.notes), 45)
        self.assertEqual(len({n["paper_id"] for n in self.notes}), 45)
        for n in self.notes:
            self.assertIn(n["paper_id"], self.papers)
            self.assertFalse(n["independent_replication_in_AI_Research"])
        self.assertEqual(
            sum(p.get("research_initiative") ==
                "Artificial Life, Emergent Intelligence, and Digital Organisms"
                for p in self.papers.values()), 45
        )
        self.assertIn("arxiv:2603.01701", self.papers)
        self.assertEqual(self.papers["arxiv:2603.01701"]["evidence_level"], "E2")

    def test_chemistry_full_paper_audit_is_e2_not_experiment(self):
        paper = self.papers["doi:10.1074/jbc.ra118.003795"]
        self.assertEqual(paper["evidence_level"], "E2")
        self.assertEqual(paper["review_status"], "full_paper")
        self.assertTrue(paper["full_text_reviewed"])
        self.assertFalse(paper["independently_reproduced"])
        self.assertIn("supplemental_details_not_fully_audited", paper["source_scope"])
        self.assertTrue((ROOT / paper["source_review_path"]).exists())
        review = (ROOT / paper["source_review_path"]).read_text(encoding="utf-8")
        self.assertIn("16,825", review)
        self.assertIn("6,886", review)
        self.assertIn("74/16,825", review)
        self.assertIn("unlimited reservoir", review)
        self.assertIn("no simulation or independent numerical replication", review.lower())

    def test_public_code_inventory_is_source_only(self):
        ids = set()
        self.assertEqual(len(self.code), 3)
        for source in self.code:
            self.assertIn(source["study_id"], self.papers)
            self.assertNotIn(source["study_id"], ids)
            ids.add(source["study_id"])
            self.assertRegex(source["commit"], r"^[0-9a-f]{40}$")
            self.assertTrue(source["public_code_url"].startswith("https://github.com/"))
            self.assertGreater(len(source["files_checked"]), 0)
            self.assertFalse(source["executed"])
            self.assertFalse(source["models_trained"])
            self.assertFalse(source["rights_review_complete"])
            self.assertGreater(len(source["relationship_to_paper"]), 30)
            if source["study_id"] == "arxiv:2506.08569":
                self.assertIn("not verified", source["relationship_to_paper"].lower())

    def test_no_new_ai_or_organism_implementation(self):
        experiments = rows("data/alife/experiment-designs.jsonl")
        for e in experiments:
            self.assertEqual(e["implementation_status"], "not_authorized")
            self.assertTrue(e["future_authorization_required"])
        for script_path in (ROOT / "experiments").glob("*.py"):
            # Legacy experiments may be deterministic *evaluation fixtures*.
            self.assertNotIn("alife", script_path.stem.lower())


if __name__ == "__main__":
    unittest.main()
