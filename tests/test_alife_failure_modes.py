"""Static integrity checks for source-linked artificial-life failure research only.

No organisms, environments, external scripts or automata chemistries are run.
"""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path):
    return [
        json.loads(line) for line in (ROOT / path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


class FailureResearchLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = {r["id"]: r for r in read_jsonl("data/papers.jsonl")}
        cls.failures = read_jsonl("data/alife/failure-modes.jsonl")

    def test_twelve_mechanisms_have_distinct_ids_and_source_links(self):
        self.assertEqual(len(self.failures), 12)
        self.assertEqual({x["id"] for x in self.failures},
                         {f"AL-FM{i:02d}" for i in range(1, 13)})
        for case in self.failures:
            source = self.papers[case["paper_id"]]
            self.assertEqual(source["evidence_level"], case["evidence_level"])
            self.assertGreater(len(case["mechanism"]), 35)
            self.assertGreater(len(case["falsification_control"]), 30)
            self.assertFalse(case["independently_reproduced"])
            self.assertFalse(case["implemented"])
            self.assertRegex(case["experiment_id"], r"^AL\d{2}$")

    def test_2020_full_paper_does_not_claim_intrinsic_type_two(self):
        paper = self.papers["doi:10.1162/isal_a_00265"]
        self.assertEqual(paper["evidence_level"], "E2")
        self.assertTrue(paper["full_text_reviewed"])
        doc = (ROOT / paper["source_review_path"]).read_text(encoding="utf-8")
        self.assertIn("extrinsic emergence", doc.lower())
        self.assertIn("type-2", doc)
        self.assertIn("retrospective", doc.lower())
        self.assertIn("does not report a new independent experiment", doc.lower())

    def test_brief_2026_author_item_stays_e1(self):
        abstract = self.papers["alife:adams-2026-transformational-novelty"]
        self.assertEqual(abstract["evidence_level"], "E1")
        self.assertFalse(abstract["full_text_reviewed"])
        doc = (ROOT / "docs/artificial-life/31-physis-2026-source-boundaries.md").read_text(encoding="utf-8")
        self.assertIn("complete three-page contribution was NOT inspected", doc)

    def test_2021_ecological_study_full_paper_review_is_not_reproduction(self):
        paper = self.papers["doi:10.1098/rsos.210441"]
        self.assertEqual(paper["evidence_level"], "E2")
        self.assertTrue(paper["full_text_reviewed"])
        self.assertFalse(paper["independently_reproduced"])
        self.assertTrue((ROOT / paper["source_review_path"]).is_file())

    def test_evidence_not_running_organism(self):
        experiments = read_jsonl("data/alife/experiment-designs.jsonl")
        self.assertEqual(len(experiments), 11)
        for e in experiments:
            self.assertTrue(e["future_authorization_required"])
            self.assertEqual(e["implementation_status"], "not_authorized")


if __name__ == "__main__":
    unittest.main()
