"""Research-only regression tests for ALife seventh pass.

These tests read metadata and do not execute Stringmol, Physis or organisms.
"""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
E2 = {
 "doi:10.1098/rsos.210441": "35-stringmol-spatial-parasitism-2021-full-review.md",
 "doi:10.1007/s12064-016-0229-7": "36-banzhaf-2016-open-ended-novelty-full-review.md",
}


def read(name):
 return [json.loads(v) for v in (ROOT/name).read_text(encoding="utf-8").splitlines() if v.strip()]


class SeventhPassAlifeTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.papers={r["id"]:r for r in read("data/papers.jsonl")}
  cls.notes={r["paper_id"]:r for r in read("data/alife/source-notes.jsonl")}
  cls.methods={r["paper_id"]:r for r in read("data/alife/method-audits.jsonl")}
  cls.claims=read("data/claims.jsonl")

 def test_two_primary_works_are_e2_without_E3(self):
  for ident,filename in E2.items():
   p,m,n=self.papers[ident],self.methods[ident],self.notes[ident]
   self.assertEqual(p["evidence_level"],"E2")
   self.assertTrue(p["full_text_reviewed"])
   self.assertFalse(p["independently_reproduced"])
   self.assertFalse(m["source_code_executed"])
   self.assertFalse(m["organism_implemented"])
   self.assertEqual(p["source_review_path"],m["review_document"])
   self.assertEqual(n["method_audit_path"],m["review_document"])
   self.assertTrue((ROOT/p["source_review_path"]).is_file())
   self.assertTrue(p["source_review_path"].endswith(filename))

 def test_code_version_discrepancies_transparent(self):
  row={x["study_id"]:x for x in read("data/alife/code-inventory.jsonl")}["doi:10.1098/rsos.210441"]
  self.assertEqual(row["commit"],"aa6c7301822a93b74ad60b46437515ef6804784f")
  self.assertIn("0.3.1",row["relationship_to_paper"])
  self.assertIn("0.1.0",row["relationship_to_paper"])
  self.assertIn("GNU GPL v2",row["license"])
  self.assertFalse(row["executed"])
  self.assertFalse(row["rights_review_complete"])

 def test_two_new_external_contexts_stay_E1(self):
  for ident in ("doi:10.1162/artl_a_00399","doi:10.7554/elife.56038"):
   p=self.papers[ident]
   self.assertEqual(p["evidence_level"],"E1")
   self.assertFalse(p["full_text_reviewed"])
   self.assertFalse(p["independently_reproduced"])

 def test_thirteen_new_claims_stay_caveated(self):
  new=[c for c in self.claims if 75<=int(c["claim_id"][1:])<=87]
  self.assertEqual(len(new),13)
  for c in new:
   p=self.papers[c["paper_id"]]
   self.assertEqual(c["source_url"],p["url"])
   self.assertEqual(c["evidence_level"],p["evidence_level"])
   self.assertFalse(c["independent_replication"])
   self.assertGreater(len(c["caveat"]),45)

 def test_failure_ledger_promotion_remains_qualified(self):
  failure={r["id"]:r for r in read("data/alife/failure-modes.jsonl")}["AL-FM02"]
  self.assertEqual(failure["evidence_level"],"E2")
  self.assertFalse(failure["implemented"])
  for e in read("data/alife/experiment-designs.jsonl"):
   self.assertTrue(e["future_authorization_required"])
   self.assertEqual(e["implementation_status"],"not_authorized")


if __name__=="__main__":
 unittest.main()
