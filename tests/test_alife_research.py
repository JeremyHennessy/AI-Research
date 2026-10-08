"""Offline ALife *research metadata* checks only. No organism simulation permitted here."""
from pathlib import Path
import json
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ALIFE = DATA / "alife"


def read_jsonl(path: Path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


class ArtificialLifeResearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.papers = read_jsonl(DATA / "papers.jsonl")
        cls.source_notes = read_jsonl(ALIFE / "source-notes.jsonl")
        cls.hypotheses = read_jsonl(ALIFE / "hypotheses.jsonl")
        cls.proposals = read_jsonl(ALIFE / "experiment-designs.jsonl")
        cls.paper_map = {p["id"]: p for p in cls.papers}

    def test_sources_have_unique_ids_and_links(self):
        self.assertEqual(len(self.papers), len(self.paper_map))
        ids = set()
        for note in self.source_notes:
            pid = note["paper_id"]
            self.assertIn(pid, self.paper_map)
            self.assertNotIn(pid, ids)
            ids.add(pid)
            self.assertFalse(note["independent_replication_in_AI_Research"])
            self.assertFalse(note["source_rights_reviewed"])
        self.assertGreaterEqual(len(ids), 25)
        self.assertEqual(sum(p.get("research_initiative") ==
            "Artificial Life, Emergent Intelligence, and Digital Organisms"
            for p in self.papers), len(ids))

    def test_paper_evidence_not_claiming_replication(self):
        for note in self.source_notes:
            paper = self.paper_map[note["paper_id"]]
            self.assertIn(paper["evidence_level"], ("E1", "E2"))
            self.assertFalse(paper["independently_reproduced"])
            if paper["evidence_level"] == "E2":
                self.assertTrue(paper["full_text_reviewed"])
                self.assertEqual(paper["review_status"], "full_paper")

    def test_hypotheses_come_with_falsifiers(self):
        ids = set()
        proposal_ids = {e["id"] for e in self.proposals}
        self.assertEqual(len(self.hypotheses), 15)
        for hypothesis in self.hypotheses:
            hid = hypothesis["id"]
            self.assertNotIn(hid, ids)
            ids.add(hid)
            self.assertRegex(hid, r"^AL-H\d{2}$")
            self.assertEqual(hypothesis["hypothesis_type"], "original_unverified")
            self.assertEqual(hypothesis["reproduction_status"], "not_tested")
            self.assertIn(hypothesis["proposed_experiment"], proposal_ids)
            self.assertGreater(len(hypothesis["falsifier"]), 20)
            self.assertGreater(len(hypothesis["critical_null_control"]), 20)
            for sid in hypothesis["source_ids"]:
                self.assertIn(sid, self.paper_map)

    def test_future_experiments_require_separate_authorization(self):
        self.assertEqual({x["id"] for x in self.proposals},
                         {f"AL{i:02d}" for i in range(1, 12)})
        for proposal in self.proposals:
            self.assertTrue(proposal["future_authorization_required"])
            self.assertTrue(proposal["preregistration_required"])
            self.assertEqual(proposal["implementation_status"], "not_authorized")
            self.assertEqual(proposal["status"],
                "research_only_future_authorization_required")
            self.assertGreater(len(proposal["primary_outcomes"]), 20)
            self.assertGreater(len(proposal["controls"]), 20)
            self.assertGreater(len(proposal["falsifier"]), 20)

    def test_navigation_preserves_research_only_scope(self):
        index = (ROOT / "docs/artificial-life/README.md").read_text(encoding="utf-8")
        self.assertIn("No organism", index)
        self.assertIn("Ora", index)
        for name in ("01-life-and-organization.md", "02-historical-systems.md",
                     "03-architecture-comparison.md", "04-emergence-bottlenecks.md",
                     "05-evaluation-framework.md", "06-hypotheses-and-open-questions.md",
                     "07-experimental-roadmap.md", "08-source-bibliography.md",
                     "09-counterevidence.md", "10-handoff.md"):
            self.assertTrue((ROOT / "docs/artificial-life" / name).exists())


if __name__ == "__main__":
    unittest.main()
