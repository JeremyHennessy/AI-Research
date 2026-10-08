# Literature discovery pipeline — Pass 2
**What exists:** bounded, metadata-only collectors for **arXiv, Crossref, OpenAlex** and an on-demand GitHub Actions workflow. **Not** continuous scraping, bulk downloads, a full-text repository or a scientifically reviewed crawl.

## Run locally
Python 3.11+ and standard library only.

```bash
python scripts/collect_arxiv.py --query "language model reasoning" --limit 20
python scripts/collect_crossref.py --query "language model reasoning" --limit 20 --from-year 2025
python scripts/collect_openalex.py --query "language model reasoning" --limit 20
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
python experiments/temporal_memory.py --trials 100 --seed 41
```

The collectors write `data/discovered/*.jsonl` as an **unreviewed queue E0** with only bibliographic metadata. They do not copy full-text abstracts or PDFs or change `data/papers.jsonl` automatically. No crawling against publisher paywalls, bypasses or private lab systems. `data/discovered/` stays excluded from Git by default; intentionally promote verified sources in a reviewed commit.

## Run from GitHub
Repository → Actions → **Manual literature metadata discovery** → Run workflow → set topic and limit → download the generated research-metadata-queue artifact. This workflow is **manual only** (not a scheduled background monitor) and does not publish discoveries or change the evidence classification.

If any source errors/rate limits, the workflow can fail while still uploading already produced queues. Check the logs; a failed API call is **not** empty research coverage.

## Access constraints
- **arXiv:** Atom metadata API; request one bounded query, retry transient failures, respect their limits.
- **Crossref:** public bibliographic metadata; potential copyright in abstracts means this collector omits abstracts by default. Docs: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- **OpenAlex:** official docs as of 2026 say limited anonymous use may work but an API key is recommended/necessary for meaningful sustained querying. Collector supports optional `OPENALEX_API_KEY` environment variable passed as Bearer header. It will not print/store the key. No need to create a key for initial offline research or small experiments. Docs: https://help.openalex.org/api/authentication/
- **ACL Anthology / PMLR / OpenReview / NeurIPS / IEEE / ACM / Springer / PubMed:** documented in source map, but **not implemented as live collectors here**. Most research content can be tracked by DOI/arXiv via Crossref/OpenAlex and manual review. Specific-source connectors should be added only after checking access and robots/API policies.

## Promotion workflow
1. Deduplicate arXiv/DOI/OpenAlex records into canonical work identities.
2. Open primary links, verify date/title/versions and venue. Verify retractions/corrections.
3. Read actual published experimental methods before labeling E2.
4. Record code/data/weights licenses and what is publicly disclosed.
5. Extract claims to a source-backed ledger with caveats and a proposed falsifiable experiment.
6. Commit reviewed records with author/date and linked sources; preserve opposing studies.
7. Keep original experiment outputs separately from paper findings.

## Three hard failure modes
1. **Discovery != review:** metadata hits don't demonstrate correctness or state of the art.
2. **DOI != rights:** cataloging a paper doesn't grant rights to redistribute its text/data.
3. **Knowledge != model weights:** reading papers doesn't produce a better-trained model.

## Later expansions
Add source-specific DOI/citation reconciliation, arXiv version audits, OpenReview decision metadata, code/weights model-card auditing, publication-to-retraction cross-check and lawful full-text archiving. Separate live network collection from offline tests and never trust incoming instructions embedded in academic content.
