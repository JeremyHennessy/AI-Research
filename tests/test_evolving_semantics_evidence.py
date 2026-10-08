"""Offline checks for full-public-paper, permission-bound semantic ALife research.

No actual artificial chemistry, organism, world or third-party science code is run.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
E2 = {
    "doi:10.1098/rstb.2024.0298": "25-stepney-2025-complete-review.md",
    "doi:10.1162/artl_a_00180": "26-stringmol-2016-full-review.md",
    "doi:10.1098/rsif.2016.1033": "27-semantic-closure-2017-full-review.md",
    "doi:10.1007/978-3-540-39432-7_26": "28-physis-2003-full-review.md",
    "doi:10.1162/isal_a_00265": "30-stringmol-2020-novelty-full-review.md",
}
E1 = (
    "alife:adams-2026-transformational-novelty",
    "alife:stepney-2026-engineering",
)


def rows(name):
    return [
        json.loads(t) for t in (ROOT / name).read_text(encoding="utf-8").splitlines()
        if t.strip()
    ]


class EvolvingSemanticsEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = {p["id"]: p for p in rows("data/papers.jsonl")}
        cls.claims = rows("data/claims.jsonl")
        cls.audits = {x["paper_id"]: x for x in rows("data/alife/method-audits.jsonl")}
        cls.code = {x["study_id"]: x for x in rows("data/alife/code-inventory.jsonl")}

    def test_all_five_technical_audits_are_e2_not_reproductions(self):
        for pid, name in E2.items():
            paper, audit = self.papers[pid], self.audits[pid]
            self.assertEqual(paper["evidence_level"], "E2")
            self.assertEqual(paper["review_status"], "full_paper")
            self.assertTrue(paper["full_text_reviewed"])
            self.assertFalse(paper["independently_reproduced"])
            self.assertFalse(audit["source_code_executed"])
            self.assertFalse(audit["organism_implemented"])
            self.assertFalse(audit["independently_reproduced"])
            self.assertTrue(audit["review_document"].endswith(name))
            self.assertGreaterEqual(len(audit["reviewed_sections"]), 5)
            self.assertTrue((ROOT / audit["review_document"]).is_file())

    def test_short_conference_previews_remain_e1(self):
        for pid in E1:
            paper = self.papers[pid]
            self.assertEqual(paper["evidence_level"], "E1")
            self.assertFalse(paper["full_text_reviewed"])
            self.assertFalse(paper["independently_reproduced"])

    def test_twelve_source_claims_are_caveated(self):
        selected = [x for x in self.claims if "C055" <= x["claim_id"] <= "C066"]
        self.assertEqual(len(selected), 12)
        # C055–C066 predate the 2020 full-review promotion.
        # Historical claim levels and sources remain unchanged after promotion.
        self.assertEqual({x["paper_id"] for x in selected},
                         set(E2) - {"doi:10.1162/isal_a_00265"})
        for claim in selected:
            self.assertFalse(claim["independent_replication"])
            self.assertEqual(claim["evidence_level"], "E2")
            self.assertEqual(claim["source_url"], self.papers[claim["paper_id"]]["url"])
            self.assertGreater(len(claim["caveat"]), 50)

    def test_unauthorized_port_is_only_inventory(self):
        row = self.code["doi:10.1007/978-3-540-39432-7_26"]
        self.assertRegex(row["commit"], r"^[a-f0-9]{40}$")
        self.assertIn("not verified", row["license"].lower())
        self.assertFalse(row["executed"])
        self.assertFalse(row["models_trained"])
        self.assertFalse(row["rights_review_complete"])

    def test_future_studies_not_implemented(self):
        designs = rows("data/alife/experiment-designs.jsonl")
        self.assertEqual(len(designs), 11)
        for e in designs:
            self.assertTrue(e["future_authorization_required"])
            self.assertEqual(e["implementation_status"], "not_authorized")
        research = (ROOT / "docs/artificial-life/29-evolvable-semantics-cross-study.md").read_text(encoding="utf-8")
        self.assertIn("NOT implemented", research)
        self.assertIn("bureaucratic death", research)


if __name__ == "__main__":
    unittest.main()
