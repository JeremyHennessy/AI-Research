import json
from pathlib import Path
import tempfile
import unittest

from scripts.collect_arxiv import build_url, merge_records, parse_feed, run
from scripts.validate_catalog import validate_records

ATOM_FIXTURE = b'''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
 <entry>
  <id>http://arxiv.org/abs/2601.01234v2</id>
  <title> A New   Paper </title>
  <published>2026-01-02T00:00:00Z</published>
  <updated>2026-01-03T00:00:00Z</updated>
  <author><name>Jane Researcher</name></author>
  <category term="cs.LG"/>
  <summary>Source abstract that must not be copied automatically.</summary>
 </entry>
</feed>'''


class ResearchToolsTests(unittest.TestCase):
    def test_url(self):
        url = build_url("world models", 20)
        self.assertIn("max_results=20", url)
        self.assertIn("sortBy=submittedDate", url)
        with self.assertRaises(ValueError):
            build_url("world models", 101)

    def test_parse_atom(self):
        rows = parse_feed(ATOM_FIXTURE, "world models", "2026-10-08T00:00:00Z")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["id"], "arxiv:2601.01234")
        self.assertEqual(rows[0]["title"], "A New Paper")
        self.assertNotIn("summary", rows[0])
        self.assertEqual(rows[0]["review_status"], "queued")

    def test_merge_keeps_manual_notes(self):
        a = {"id": "arxiv:2601.01234", "published": "2026-01-01", "notes": "reviewed"}
        b = {"id": "arxiv:2601.01234", "published": "2026-10-01"}
        self.assertEqual(merge_records([a], [b])[0]["notes"], "reviewed")

    def test_offline_cli(self):
        with tempfile.TemporaryDirectory() as folder:
            feed = Path(folder) / "feed.xml"
            path = Path(folder) / "queue.jsonl"
            feed.write_bytes(ATOM_FIXTURE)
            self.assertEqual(run(["--query", "world models", "--fixture", str(feed), "--output", str(path)]), 0)
            self.assertEqual(len(path.read_text().splitlines()), 1)
            self.assertEqual(json.loads(path.read_text().splitlines()[0])["evidence_level"], "E0")

    def test_seed_catalog(self):
        path = Path(__file__).resolve().parents[1] / "data" / "papers.jsonl"
        n, errors = validate_records(path)
        self.assertGreaterEqual(n, 25)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
