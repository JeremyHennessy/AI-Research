#!/usr/bin/env python3
"""Bounded OpenAlex work-metadata collector. E0 leads only; no PDF/abstract copying.

As of 2026, meaningful API usage needs an API key; low-volume keyless queries
may work. Optional OPENALEX_API_KEY is read from environment and passed as a
Bearer header, never printed or stored in output.
https://help.openalex.org/api/authentication/
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

try:
    from .collect_arxiv import merge_records, write_queue
except ImportError:
    from collect_arxiv import merge_records, write_queue

API = "https://api.openalex.org/works"
MAX_BYTES = 4 * 1024 * 1024
ID_RE = re.compile(r"^https://openalex.org/(W\d+)$")


def build_url(query: str, limit: int = 20) -> str:
    q = query.strip()
    if not 1 <= len(q) <= 160 or not 1 <= limit <= 100:
        raise ValueError("query must be 1-160 chars and limit 1-100")
    return API + "?" + urlencode({"search": q, "per-page": limit,
                                  "sort": "publication_date:desc"})


def parse_response(data: bytes, query: str, retrieved_at: str) -> list[dict]:
    response = json.loads(data)
    records: list[dict] = []
    for work in response.get("results", []):
        match = ID_RE.fullmatch(str(work.get("id") or ""))
        title = " ".join(str(work.get("display_name") or "").split())
        if not match or not title:
            continue
        doi = work.get("doi")
        if doi and not (isinstance(doi, str) and doi.startswith("https://doi.org/")):
            doi = None
        authors = [entry.get("author", {}).get("display_name", "")
                   for entry in work.get("authorships", [])
                   if isinstance(entry, dict) and isinstance(entry.get("author"), dict)]
        records.append({
            "id": "openalex:" + match.group(1),
            "title": title, "url": doi or work["id"], "doi": doi,
            "year": work.get("publication_year"), "publication_date": work.get("publication_date"),
            "authors": [a for a in authors if a],
            "source": "openalex", "query": query, "retrieved_at": retrieved_at,
            "evidence_level": "E0", "review_status": "queued",
            "full_text_reviewed": False, "independently_reproduced": False,
        })
    return records


def fetch(url: str, key: str | None = None) -> bytes:
    headers = {"User-Agent": "AI-Research-Metadata/0.2 (bounded noncommercial discovery)",
               "Accept": "application/json"}
    if key:
        headers["Authorization"] = "Bearer " + key
    request = Request(url, headers=headers)
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                payload = response.read(MAX_BYTES + 1)
                if len(payload) > MAX_BYTES:
                    raise ValueError("OpenAlex response exceeds 4MB; reduce limit")
                return payload
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
    parser.add_argument("--fixture", type=Path)
    parser.add_argument("--output", type=Path, default=Path("data/discovered/openalex.jsonl"))
    args = parser.parse_args(argv)
    url = build_url(args.query, args.limit)
    raw = args.fixture.read_bytes() if args.fixture else fetch(url, os.getenv("OPENALEX_API_KEY"))
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
