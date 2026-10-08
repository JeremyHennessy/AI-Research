import json
from pathlib import Path
import tempfile
import unittest

from scripts.collect_crossref import build_url as crossref_url, parse_response as crossref_parse, run as crossref_run
from scripts.collect_openalex import build_url as openalex_url, parse_response as openalex_parse, run as openalex_run

CROSSREF = json.dumps({"message": {"items": [{
    "DOI": "10.1234/AI.TEST", "title": ["Original Title"],
    "published": {"date-parts": [[2026, 6, 9]]},
    "type": "journal-article",
    "author": [{"given": "Ada", "family": "Lovelace"}],
    "abstract": "Should not be copied",
}, {"DOI": "", "title": ["Invalid"]}]}}).encode()
OPENALEX = json.dumps({"results": [{
    "id": "https://openalex.org/W98765432", "display_name": "Original Work",
    "doi": "https://doi.org/10.1234/demo", "publication_year": 2026,
    "publication_date": "2026-10-07",
    "authorships": [{"author": {"display_name": "Researcher"}}],
    "abstract_inverted_index": {"copyrighted": [1]}
}]}).encode()


class DiscoveryTests(unittest.TestCase):
    def test_crossref(self):
        self.assertIn("rows=20", crossref_url("state space", 20))
        with self.assertRaises(ValueError):
            crossref_url("a", 101)
        result = crossref_parse(CROSSREF, "state space", "2026-10-08")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "doi:10.1234/ai.test")
        self.assertEqual(result[0]["authors"], ["Ada Lovelace"])
        self.assertNotIn("abstract", result[0])

    def test_openalex(self):
        self.assertIn("per-page=20", openalex_url("language model", 20))
        result = openalex_parse(OPENALEX, "language model", "2026-10-08")
        self.assertEqual(result[0]["id"], "openalex:W98765432")
        self.assertNotIn("abstract_inverted_index", result[0])
        self.assertEqual(result[0]["doi"], "https://doi.org/10.1234/demo")

    def test_cli_fixture_does_not_touch_network(self):
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            src_a, dst_a = folder / "crossref.json", folder / "crossref.jsonl"
            src_b, dst_b = folder / "openalex.json", folder / "openalex.jsonl"
            src_a.write_bytes(CROSSREF)
            src_b.write_bytes(OPENALEX)
            self.assertEqual(crossref_run(["--query", "AI", "--fixture", str(src_a),
                                           "--output", str(dst_a)]), 0)
            self.assertEqual(openalex_run(["--query", "AI", "--fixture", str(src_b),
                                           "--output", str(dst_b)]), 0)
            self.assertEqual(len(dst_a.read_text().splitlines()), 1)
            self.assertEqual(len(dst_b.read_text().splitlines()), 1)


if __name__ == "__main__":
    unittest.main()
