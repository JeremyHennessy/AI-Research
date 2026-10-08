"""Validate only source review records: no simulation or organism code is run."""
from __future__ import annotations
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
IDS = {
    "arxiv:2506.08569": "16-flow-lenia-2025-full-review.md",
    "arxiv:2604.11248": "17-pbt-nca-2026-full-review.md",
    "arxiv:2603.01701": "18-tolsim-2026-full-review.md",
}


def load(path: str) -> list[dict]:
    return [json.loads(line) for line in (ROOT / path).read_text(encoding="utf-8").splitlines() if line.strip()]


class ALifeFulltextEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = {r["id"]: r for r in load("data/papers.jsonl")}
        cls.notes = {r["paper_id"]: r for r in load("data/alife/source-notes.jsonl")}
        cls.audits = load("data/alife/method-audits.jsonl")
        cls.claims = load("data/claims.jsonl")

    def test_three_reviews_have_exact_source_and_depth(self):
        self.assertEqual({x["paper_id"] for x in self.audits}, set(IDS))
        for a in self.audits:
            pid = a["paper_id"]
            p = self.papers[pid]
            n = self.notes[pid]
            self.assertEqual(p["evidence_level"], "E2")
            self.assertTrue(p["full_text_reviewed"])
            self.assertEqual(p["review_status"], "full_paper")
            self.assertFalse(p["independently_reproduced"])
            self.assertEqual(a["evidence_level"], "E2")
            self.assertFalse(a["independently_reproduced"])
            self.assertFalse(a["source_code_executed"])
            self.assertFalse(a["organism_implemented"])
            self.assertEqual(p["source_review_path"], a["review_document"])
            self.assertEqual(n["method_audit_path"], a["review_document"])
            self.assertEqual(p["full_text_url"], a["full_text_url"])
            self.assertTrue(a["full_text_url"].startswith("https://arxiv.org/html/"))
            self.assertGreaterEqual(len(a["reviewed_sections"]), 5)
            self.assertGreater(len(a["author_reported_results"]), 80)
            self.assertGreater(len(a["limitations"]), 75)
            self.assertTrue((ROOT / a["review_document"]).is_file())
            self.assertIn(IDS[pid], a["review_document"])

    def test_compendium_index_preserves_citation_evidence(self):
        index = (ROOT / "docs/19-paper-index.md").read_text(encoding="utf-8")
        self.assertIn("183 curated research records", index)
        self.assertIn("Six complete public-paper", index)
        for pid in IDS:
            p = self.papers[pid]
            self.assertIn(f"[{p['title']}]({p['url']}) | E2 |", index)

    def test_primary_claims_have_caveats_and_exact_primary_links(self):
        relevant = [x for x in self.claims if x["paper_id"] in IDS]
        self.assertGreaterEqual(len(relevant), 9)
        for x in relevant:
            self.assertEqual(x["evidence_level"], "E2")
            self.assertFalse(x["independent_replication"])
            self.assertEqual(x["source_url"], self.papers[x["paper_id"]]["url"])
            self.assertEqual(x["source_detail"], self.papers[x["paper_id"]]["full_text_url"])
            self.assertGreater(len(x["caveat"]), 45)

    def test_source_specific_falsifiers_present(self):
        root = ROOT / "docs/artificial-life"
        cases = {
            "16-flow-lenia-2025-full-review.md": ["mass-normalized", "mutation", "species", "five"],
            "17-pbt-nca-2026-full-review.md": ["DINOv2", "500", "novelty", "0.25"],
            "18-tolsim-2026-full-review.md": ["shadow", "20", "0 / 20", "eyesight"],
        }
        for name, terms in cases.items():
            page = (root / name).read_text(encoding="utf-8").lower()
            for term in terms:
                self.assertIn(term.lower(), page, (name, term))

    def test_no_new_organism_or_simulation_artifacts(self):
        for e in load("data/alife/experiment-designs.jsonl"):
            self.assertEqual(e["implementation_status"], "not_authorized")
            self.assertTrue(e["future_authorization_required"])


if __name__ == "__main__":
    unittest.main()
