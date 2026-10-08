"""Offline checks: paper and claim catalog links and source identities stay coherent."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ClaimCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = [json.loads(line) for line in (ROOT / "data/papers.jsonl").read_text().splitlines() if line]
        cls.claims = [json.loads(line) for line in (ROOT / "data/claims.jsonl").read_text().splitlines() if line]

    def test_claims_have_one_primary_source(self):
        paper_ids = {paper["id"]: paper for paper in self.papers}
        claim_ids = set()
        for claim in self.claims:
            self.assertNotIn(claim["claim_id"], claim_ids)
            claim_ids.add(claim["claim_id"])
            paper = paper_ids[claim["paper_id"]]
            self.assertEqual(paper["url"], claim["source_url"])
            self.assertEqual(claim["evidence_level"], "E1")
            self.assertFalse(claim["independent_replication"])
            self.assertGreater(len(claim["claim"]), 20)
            self.assertGreater(len(claim["caveat"]), 20)
        self.assertGreaterEqual(len(self.claims), 20)

    def test_every_catalog_paper_is_in_index(self):
        index = (ROOT / "docs/19-paper-index.md").read_text()
        self.assertIn(f"{len(self.papers)} curated research records", index)
        for paper in self.papers:
            self.assertIn("](" + paper["url"] + ")", index)


if __name__ == "__main__":
    unittest.main()
