#!/usr/bin/env python3
"""Validate curated research metadata; no network access, no scientific fact checking."""
from __future__ import annotations
import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

TRACKS = {
    "foundations", "data", "architecture", "reasoning", "agents", "memory",
    "world-models", "multimodal", "systems", "evaluation", "safety",
    "interpretability", "causality", "continual-learning", "security", "alignment",
    "robotics", "science", "hardware",
    "graph-learning", "probabilistic", "neuroscience", "formal-reasoning",
    "audio", "program-synthesis", "multi-agent",
    "artificial-life", "digital-evolution", "open-ended-evolution",
    "artificial-chemistry", "morphogenesis",
}
REQUIRED = {
    "id", "title", "year", "track", "url", "evidence_level",
    "review_status", "full_text_reviewed", "independently_reproduced",
    "original_summary", "implementation_question", "experiment_ids",
    "rights_review", "added_at",
}
ARXIV = re.compile(r"^arxiv:\d{4}\.\d{4,5}$")
EXPERIMENT = re.compile(r"^(?:E\d{2}|AL\d{2})$")


def validate_records(path: Path) -> tuple[int, list[str]]:
    errors: list[str] = []
    ids: set[str] = set()
    urls: set[str] = set()
    n = 0
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        return 0, [str(exc)]
    for line_no, line in enumerate(lines, 1):
        if not line.strip():
            continue
        n += 1
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_no}: invalid JSON: {exc}")
            continue
        if not isinstance(record, dict):
            errors.append(f"line {line_no}: expected JSON object")
            continue
        missing = REQUIRED - record.keys()
        if missing:
            errors.append(f"line {line_no}: missing {sorted(missing)}")
            continue
        pid, url = record["id"], record["url"]
        if not isinstance(pid, str) or not (ARXIV.fullmatch(pid) or re.fullmatch(r"(?:pmlr|acl|iclr|lab|nature|anthropic|deepmind|openai|metr|mlcommons|ijcai|springer):[A-Za-z0-9_.-]+", pid) or re.fullmatch(r"doi:10\.\d{4,9}/[A-Za-z0-9._;()/:-]+", pid) or re.fullmatch(r"alife:[a-z0-9-]+", pid)):
            errors.append(f"line {line_no}: bad paper id {pid!r}")
        if pid in ids:
            errors.append(f"line {line_no}: duplicate id {pid}")
        ids.add(pid)
        if not isinstance(url, str) or urlsplit(url).scheme != "https" or not urlsplit(url).netloc:
            errors.append(f"line {line_no}: invalid https url")
        if url in urls:
            errors.append(f"line {line_no}: duplicate url {url}")
        urls.add(url)
        if record["track"] not in TRACKS:
            errors.append(f"line {line_no}: invalid track {record['track']!r}")
        if record["evidence_level"] not in {"E0", "E1", "E2", "E3", "E4", "E5"}:
            errors.append(f"line {line_no}: invalid evidence level")
        if record["review_status"] not in {"queued", "abstract_only", "full_paper", "replicated"}:
            errors.append(f"line {line_no}: invalid review status")
        for key in ["title", "original_summary", "implementation_question"]:
            if not isinstance(record[key], str) or len(record[key].strip()) < (3 if key == "title" else 8):
                errors.append(f"line {line_no}: missing/short {key}")
        if type(record["year"]) is not int or not (1950 <= record["year"] <= dt.date.today().year):
            errors.append(f"line {line_no}: invalid publication year")
        if not isinstance(record["experiment_ids"], list) or not all(
            isinstance(x, str) and EXPERIMENT.fullmatch(x) for x in record["experiment_ids"]
        ):
            errors.append(f"line {line_no}: invalid experiment ids")
        if record["full_text_reviewed"] is not True and record["review_status"] in ("full_paper", "replicated"):
            errors.append(f"line {line_no}: full paper status without review flag")
        if record["independently_reproduced"] is not True and record["evidence_level"] in ("E3", "E4", "E5"):
            errors.append(f"line {line_no}: unreplicated paper cannot be E3+")
        try:
            dt.date.fromisoformat(record["added_at"])
        except (ValueError, TypeError):
            errors.append(f"line {line_no}: invalid added_at")
    return n, errors


def main(argv: list[str] | None = None) -> int:
    path = Path(argv[0]) if argv else Path(__file__).resolve().parents[1] / "data" / "papers.jsonl"
    count, errors = validate_records(path)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"INVALID: {count} records, {len(errors)} errors", file=sys.stderr)
        return 1
    print(f"VALID: {count} curated records (schema only; scientific claims NOT verified)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
