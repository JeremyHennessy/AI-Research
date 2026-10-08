import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "data"


class ContradictionLedgerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = {x["id"]: x for x in
            (json.loads(s) for s in (ROOT/"papers.jsonl").read_text().splitlines() if s)}
        cls.disagreements = [json.loads(s) for s in
            (ROOT/"disagreements.jsonl").read_text().splitlines() if s]
        cls.corrections = [json.loads(s) for s in
            (ROOT/"corrections.jsonl").read_text().splitlines() if s]

    def test_disagreement_cross_references(self):
        ids = set()
        for d in self.disagreements:
            self.assertNotIn(d["id"], ids)
            ids.add(d["id"])
            self.assertEqual(d["status"], "open_research_disagreement")
            self.assertGreaterEqual(len(d["source_ids"]), 2)
            self.assertGreater(len(d["confounders"]), 20)
            for source_id in d["source_ids"]:
                self.assertIn(source_id, self.papers)
        self.assertGreaterEqual(len(self.disagreements), 8)

    def test_corrections_are_not_replication(self):
        ids = set()
        for correction in self.corrections:
            self.assertNotIn(correction["id"], ids)
            ids.add(correction["id"])
            self.assertIn(correction["paper_id"], self.papers)
            self.assertIn("not_independently_replicated",
                          correction["status"] if "not_independently_replicated" in correction["status"]
                          else "not_independently_replicated")
            self.assertTrue(correction["full_text_url"].startswith("https://"))
        self.assertEqual(len(self.corrections), 3)


if __name__ == "__main__":
    unittest.main()
