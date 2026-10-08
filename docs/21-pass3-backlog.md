# Pass 3 research handoff — prioritized, evidence-led
Created 2026-10-08. Maintain a clean distinction between **catalog**, **understood method**, **replicated baseline**, and **novel tested improvement**.

## Current checkpoint
- Private repository main contains 63 curated research source records and 24 claim records in separate machine-readable ledgers.
- Source-linked public recipe dossiers and design/hypothesis documents are in `docs/`.
- Standard-library discovery: arXiv Atom, Crossref, OpenAlex; manual GitHub Actions discovery, **not** automatically scheduled.
- Deterministic synthetic temporal memory benchmark fixture, **not an LLM test**.
- No training budget/GPU baseline, model weight derivative, or claim of scientific novelty.

## Prioritized next tasks with tangible acceptance criteria
| Priority | Task | Done when |
|---|---|---|
| P0 | Verify current CI on final commit | Python compile, catalog, source-ledger and fixture tests pass |
| P0 | Full-method review of 8-12 high-value papers (Bolmo Nature, Olmo 3, DAPO, hybrid SSM, Sigma, Clock Diffusion, Mem2ActBench, AMA-Bench) | Paper methods/eval/ablation/limits summarized with section references, evidence E2 only when whole paper checked |
| P0 | Implement E01 benchmark contract for accessible frozen open small model | Exact model revision, dataset hash, grading and actual per-item results + cost |
| P0 | Extend E03b toy ledger to **model-in-loop** benchmark | Freeze prompts/tools and compare naive vs temporal memory on unseen tasks, with input/output logs |
| P1 | Build cross-database DOI/arXiv identity deduplicator | 3-source records for same work collapse to one canonical work, without lost provenance |
| P1 | Full public recipe matrices | Exact scripts/config/SHA/optimizer, midtrain tokens, sequence lengths, system and missing fields |
| P1 | E02 compute router ablation | Quality-vs-actual-time curve with strong fixed-budget baseline and independent verifier |
| P1 | Contradictory synthetic-data research survey | Opposing papers with independent source and test plan |
| P2 | Hybrid head retention and byte tokenizer pilot | Accessible tiny model, strong baseline and VRAM/latency/correctness tests |
| P2 | Diffusion-vs-AR apples-to-apples | Exact NFE, wall time and quality for selected model family |
| P2 | Task-sufficient world model pilot | Unseen transition-combination success and calibrated error rates |

## Source refresh questions
- What was released or peer-reviewed after October 8, 2026?
- Which paper was corrected, retracted or revised after our archive date?
- Which claimed gains are benchmark-only or fail matched-cost transfer?
- Can published lab recipes be compiled **fully** from public config repositories, rather than inferred from marketing releases?
- What negative results challenge our preferred hypotheses?

## Scientific “do not advance” gates
- No experimental claims without source hashes, exact model and dataset, repeatable test traces.
- No claims of novel intelligence from a memory harness or agent scaffolding.
- No attributing observed improvement to model weights if only tools/retrieval changed.
- No proprietary or private lab recipe access without permission.
- No copying full copyrighted articles without applicable rights, despite private noncommercial purpose.
- No secret credential request as prerequisite for basic research.
- No destructive change to an approved baseline.

## How to resume
Read `README.md` → `docs/10-pass2-index.md` → `docs/17-verified-sources.md` → `data/research-log.md`, then inspect the exact current main SHA and CI. Work on one hypothesis at a time. Preserve negative results.
