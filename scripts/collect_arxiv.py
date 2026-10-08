#!/usr/bin/env python3
"""Bounded arXiv Atom API metadata discovery. Does not download paper text or execute models.

Outputs an UNREVIEWED JSONL queue distinct from curated data/papers.jsonl.
See https://info.arxiv.org/help/api/user-manual.html and access policies.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import re
from pathlib import Path
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

API = "https://export.arxiv.org/api/query"
ATOM = "{http://www.w3.org/2005/Atom}"
MAX_BYTES = 4 * 1024 * 1024
MAX_RESULTS = 100
ID_RE = re.compile(r"/abs/((?:\d{4}\.\d{4,5}|[a-z-]+(?:\.[A-Z]{2})?/\d{7})(?:v\d+)?)$")


def build_url(query: str, limit: int) -> str:
    query = query.strip()
    if not query or len(query) > 160:
        raise ValueError("query must be 1-160 characters")
    if not (1 <= limit <= MAX_RESULTS):
        raise ValueError("limit must be between 1 and 100")
    # Phrase search avoids injecting operators through caller-supplied query strings.
    safe_term = query.replace('"', " ").replace("\\", " ")
    return API + "?" + urlencode({
        "search_query": 'all:"' + safe_term + '"',
        "start": 0,
        "max_results": limit,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    })


def parse_feed(xml_bytes: bytes, query: str, retrieved_at: str) -> list[dict]:
    root = ET.fromstring(xml_bytes)
    entries: list[dict] = []
    for element in root.findall(ATOM + "entry"):
        entry_id = (element.findtext(ATOM + "id") or "").strip()
        match = ID_RE.search(urlsplit(entry_id).path)
        if not match:
            continue
        identifier = re.sub(r"v\d+$", "", match.group(1))
        title = " ".join((element.findtext(ATOM + "title") or "").split())
        published = element.findtext(ATOM + "published") or ""
        updated = element.findtext(ATOM + "updated") or ""
        authors = [" ".join((a.findtext(ATOM + "name") or "").split())
                   for a in element.findall(ATOM + "author")]
        categories = [x.get("term", "") for x in element.findall(ATOM + "category")]
        if not title or not published:
            continue
        entries.append({
            "id": "arxiv:" + identifier,
            "title": title,
            "url": "https://arxiv.org/abs/" + identifier,
            "authors": [a for a in authors if a],
            "published": published,
            "updated": updated,
            "categories": [c for c in categories if c],
            "query": query,
            "retrieved_at": retrieved_at,
            "evidence_level": "E0",
            "review_status": "queued",
            "full_text_reviewed": False,
            "independently_reproduced": False,
        })
    return entries


def fetch_feed(url: str, attempts: int = 3) -> bytes:
    req = Request(url, headers={"User-Agent": "AI-Research-Metadata/0.1 (research-only; no PDF scraping)",
                                "Accept": "application/atom+xml"})
    for attempt in range(attempts):
        try:
            with urlopen(req, timeout=25) as response:
                data = response.read(MAX_BYTES + 1)
                if len(data) > MAX_BYTES:
                    raise ValueError("feed exceeds 4 MB; lower --limit")
                return data
        except HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504) or attempt + 1 >= attempts:
                raise
        except (URLError, TimeoutError):
            if attempt + 1 >= attempts:
                raise
        time.sleep(3 * (2 ** attempt))
    raise RuntimeError("unreachable")


def merge_records(old: list[dict], new: list[dict]) -> list[dict]:
    # Preserve existing manual annotations; fresh discovery never overwrites them.
    result = {r["id"]: r for r in old if isinstance(r, dict) and isinstance(r.get("id"), str)}
    for record in new:
        result.setdefault(record["id"], record)
    return sorted(result.values(), key=lambda r: (r.get("published", ""), r["id"]), reverse=True)


def write_queue(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # tempfile and replace prevent a mid-write truncated research queue
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                     prefix=path.name + ".", delete=False) as handle:
        tmp = Path(handle.name)
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    tmp.replace(path)


def run(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True, help="one bounded research phrase")
    parser.add_argument("--limit", type=int, default=20, help="1..100 metadata records")
    parser.add_argument("--output", type=Path,
                        default=Path("data/discovered/arxiv.jsonl"))
    parser.add_argument("--fixture", type=Path, help="read a local Atom fixture instead of the network")
    args = parser.parse_args(argv)
    url = build_url(args.query, args.limit)
    xml = args.fixture.read_bytes() if args.fixture else fetch_feed(url)
    rows = parse_feed(xml, args.query, datetime.now(timezone.utc).isoformat())
    current: list[dict] = []
    if args.output.exists():
        for line in args.output.read_text(encoding="utf-8").splitlines():
            if line.strip():
                current.append(json.loads(line))
    merged = merge_records(current, rows)
    write_queue(args.output, merged)
    print(json.dumps({"fetched": len(rows), "unique_total": len(merged),
                      "output": str(args.output), "mode": "fixture" if args.fixture else "api",
                      "status": "unreviewed_discovery_only"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
