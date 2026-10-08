import json
from pathlib import Path
import tempfile
import unittest

from scripts.reconcile_sources import normalize_doi, canonical_identity, reconcile, main

ROWS = [
    {"id":"arxiv:2601.01234", "url":"https://arxiv.org/abs/2601.01234",
     "title":"Interesting Paper", "evidence_level":"E0", "retrieved_at":"2026-10-08",
     "authors":["A. One"],"query":"models"},
    {"id":"doi:10.48550/ARXIV.2601.01234", "doi":"10.48550/ARXIV.2601.01234",
     "url":"https://doi.org/10.48550/arxiv.2601.01234", "title":"Interesting Paper!",
     "evidence_level":"E0","retrieved_at":"2026-10-09","authors":["Alice One"],"query":"agents"},
    {"id":"openalex:W123", "doi":"https://doi.org/10.48550/arxiv.2601.01234",
     "url":"https://doi.org/10.48550/arxiv.2601.01234", "title":"Interesting Paper",
     "evidence_level":"E0", "query":"models"},
    {"id":"openalex:W456", "url":"https://openalex.org/W456",
     "title":"Interesting Paper", "evidence_level":"E0"},  # title alone must not merge
]


class ReconcileTests(unittest.TestCase):
    def test_doi_normalization(self):
        self.assertEqual(normalize_doi("HTTPS://DOI.ORG/10.48550/ARXIV.2601.01234".replace("HTTPS://", "https://")),
                         "10.48550/arxiv.2601.01234")
        self.assertEqual(normalize_doi("10.1234/ABC"), "10.1234/abc")
        self.assertIsNone(normalize_doi("invalid"))

    def test_group_by_actual_identity_not_title(self):
        docs = reconcile([dict(r) for r in ROWS])
        self.assertEqual(len(docs), 2)
        group = next(x for x in docs if x["canonical_id"] == "arxiv:2601.01234")
        self.assertEqual(group["source_record_count"], 3)
        self.assertEqual(len(group["source_ids"]), 3)
        self.assertTrue(group["title_disagreement"])
        self.assertTrue(group["requires_review"])

    def test_order_independence(self):
        a = reconcile([dict(r) for r in ROWS])
        b = reconcile([dict(r) for r in reversed(ROWS)])
        self.assertEqual(a, b)

    def test_reject_pretend_reviewed(self):
        r = dict(ROWS[0], evidence_level="E2")
        with self.assertRaises(ValueError):
            reconcile([r])

    def test_offline_cli(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            source = p / "crossref.jsonl"
            source.write_text("\n".join(json.dumps(r) for r in ROWS)+"\n")
            output = p / "results.jsonl"
            self.assertEqual(main(["--inputs", str(source), "--output", str(output)]), 0)
            self.assertEqual(len(output.read_text().splitlines()), 2)


if __name__ == "__main__":
    unittest.main()
