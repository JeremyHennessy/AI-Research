#!/usr/bin/env python3
"""Conservatively reconcile UNREVIEWED bibliographic metadata across sources.

Supports arXiv, Crossref DOI, and OpenAlex DOI identity. Does not infer sameness
from title alone, silently modify curated papers, or download full text. Source
records, title discrepancies, and search provenance are preserved for reviewers.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    from .collect_arxiv import write_queue
except ImportError:
    from collect_arxiv import write_queue

ARXIV_ID = re.compile(r"^arxiv:(\d{4}\.\d{4,5})$")
ARXIV_DOI = re.compile(r"^10\.48550/arxiv\.(\d{4}\.\d{4,5})$", re.I)
DOI = re.compile(r"^10\.\d{4,9}/\S+$", re.I)


def normalize_doi(text: str | None) -> str | None:
    if not isinstance(text, str) or not text.strip():
        return None
    raw = text.strip().lower()
    if raw.startswith("https://doi.org/"):
        raw = raw[len("https://doi.org/"):]
    elif raw.startswith("http://dx.doi.org/"):
        raw = raw[len("http://dx.doi.org/"):]
    raw = unquote(raw).strip()
    # Keep DOI identity conservative: terminal punctuation can be meaningful.
    return raw if DOI.fullmatch(raw) else None


def canonical_identity(record: dict) -> str:
    doi = normalize_doi(record.get("doi"))
    rid = record.get("id") if isinstance(record.get("id"), str) else ""
    if doi is None and rid.startswith("doi:"):
        doi = normalize_doi(rid[4:])
    if doi is None:
        candidate = record.get("url")
        if isinstance(candidate, str) and urlsplit(candidate).netloc.lower() == "doi.org":
            doi = normalize_doi(candidate)
    if doi is not None:
        arx = ARXIV_DOI.fullmatch(doi)
        return "arxiv:" + arx.group(1) if arx else "doi:" + doi
    arx = ARXIV_ID.fullmatch(rid)
    if arx:
        return rid
    if rid.startswith("arxiv:"):
        return rid
    # No DOI and no arXiv ID: retain independent identity; do not title-merge.
    if not rid:
        raise ValueError("record lacks stable id")
    return rid


def normalized_title(text: str) -> str:
    # Only for flagging potential metadata disagreement. Not for merging.
    return " ".join(re.findall(r"\w+", text.casefold(), flags=re.UNICODE))


def reconcile(records: list[dict]) -> list[dict]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in records:
        if not isinstance(row, dict) or row.get("evidence_level") != "E0":
            raise ValueError("only unreviewed E0 discovery records may be reconciled")
        key = canonical_identity(row)
        groups[key].append(row)
    output: list[dict] = []
    for key in sorted(groups):
        source_rows = groups[key]
        source_rows.sort(key=lambda r: (str(r.get("id","")), str(r.get("source","")),
                                        str(r.get("query",""))))
        titles = sorted({str(r.get("title","")).strip() for r in source_rows if r.get("title")})
        normalized = {normalized_title(t) for t in titles}
        urls = sorted({str(r.get("url")) for r in source_rows if r.get("url")})
        authors = sorted({name for r in source_rows for name in r.get("authors",[])
                          if isinstance(name, str) and name.strip()})
        output.append({
            "canonical_id": key, "evidence_level": "E0", "review_status": "queued",
            "title": titles[0] if titles else None, "title_variants": titles,
            "title_disagreement": len(normalized) > 1,
            "source_ids": sorted({str(r.get("id")) for r in source_rows}),
            "source_urls": urls,
            "authors": authors,
            "years": sorted({int(r["year"]) for r in source_rows
                             if isinstance(r.get("year"), int)}),
            "queries": sorted({str(r.get("query")) for r in source_rows
                               if r.get("query")}),
            "retrieval_times": sorted({str(r.get("retrieved_at")) for r in source_rows
                                       if r.get("retrieved_at")}),
            "source_record_count": len(source_rows),
            "requires_review": True,
        })
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", nargs="*", type=Path, help="input E0 queues; default discovery feeds")
    parser.add_argument("--output", type=Path, default=Path("data/discovered/reconciled.jsonl"))
    args = parser.parse_args(argv)
    inputs = args.inputs if args.inputs is not None else [
        Path("data/discovered") / f"{name}.jsonl" for name in ("arxiv", "crossref", "openalex")
    ]
    if args.output in inputs:
        raise ValueError("output cannot also be an input")
    records = []
    for path in inputs:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                records.append(json.loads(line))
    result = reconcile(records)
    write_queue(args.output, result)
    print(json.dumps({"unreviewed_records": len(records), "unique_works": len(result),
                      "title_conflicts": sum(r["title_disagreement"] for r in result),
                      "status": "unreviewed_identity_only",
                      "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
