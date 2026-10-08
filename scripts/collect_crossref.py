#!/usr/bin/env python3
"""Bounded Crossref REST metadata collector, not a copyrighted full-text downloader.
Input is treated only as search data. Writes E0 unreviewed records.
https://www.crossref.org/documentation/retrieve-metadata/rest-api/
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import re
from pathlib import Path
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

try:
    from .collect_arxiv import merge_records, write_queue
except ImportError:  # CLI execution from scripts/ directory
    from collect_arxiv import merge_records, write_queue

API = "https://api.crossref.org/works"
MAX_BYTES = 4 * 1024 * 1024


def build_url(query: str, limit: int = 20, from_year: int | None = None) -> str:
    term = query.strip()
    if not 1 <= len(term) <= 160 or not 1 <= limit <= 100:
        raise ValueError("query must be 1-160 chars and limit 1-100")
    opts = {"query.bibliographic": term, "rows": limit,
            "sort": "published", "order": "desc"}
    if from_year is not None:
        if not 1950 <= from_year <= datetime.now(timezone.utc).year:
            raise ValueError("year outside allowed range")
        opts["filter"] = f"from-pub-date:{from_year}-01-01"
    return API + "?" + urlencode(opts)


def parse_response(data: bytes, query: str, retrieved_at: str) -> list[dict]:
    body = json.loads(data)
    items = body.get("message", {}).get("items", [])
    output: list[dict] = []
    for item in items:
        doi = str(item.get("DOI") or "").strip().lower()
        name = item.get("title") or []
        title = " ".join(str(name[0]).split()) if isinstance(name, list) and name else ""
        if not doi or not title or not re.fullmatch(r"10\.\d{4,9}/\S+", doi):
            continue
        authors = [f"{a.get('given', '')} {a.get('family', '')}".strip()
                   for a in item.get("author", []) if isinstance(a, dict)]
        published = (item.get("published") or item.get("created") or {}).get("date-parts", [[]])
        year = published[0][0] if published and published[0] else None
        output.append({
            "id": "doi:" + doi, "url": "https://doi.org/" + doi,
            "doi": doi, "title": title, "authors": authors,
            "year": year, "source_type": item.get("type"),
            "query": query, "retrieved_at": retrieved_at, "source": "crossref",
            "evidence_level": "E0", "review_status": "queued",
            "full_text_reviewed": False, "independently_reproduced": False,
        })
    return output


def fetch(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "AI-Research-Metadata/0.2 (noncommercial research; contact through GitHub repo)",
                                    "Accept": "application/json"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                content = response.read(MAX_BYTES + 1)
                if len(content) > MAX_BYTES:
                    raise ValueError("Crossref response exceeds 4MB; reduce limit")
                return content
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
        except (URLError, TimeoutError):
            if attempt == 2:
                raise
        time.sleep(3 * (2 ** attempt))
    raise RuntimeError("unreachable")


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--from-year", type=int)
    parser.add_argument("--fixture", type=Path)
    parser.add_argument("--output", type=Path, default=Path("data/discovered/crossref.jsonl"))
    args = parser.parse_args(argv)
    url = build_url(args.query, args.limit, args.from_year)
    raw = args.fixture.read_bytes() if args.fixture else fetch(url)
    rows = parse_response(raw, args.query, datetime.now(timezone.utc).isoformat())
    prior = [json.loads(line) for line in args.output.read_text(encoding="utf-8").splitlines()
             if line.strip()] if args.output.exists() else []
    combined = merge_records(prior, rows)
    write_queue(args.output, combined)
    print(json.dumps({"fetched": len(rows), "unique_total": len(combined),
                      "output": str(args.output), "status": "unreviewed_metadata_only",
                      "mode": "fixture" if args.fixture else "api"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
