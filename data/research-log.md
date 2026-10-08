# Research log (append-only decisions)

## 2026-10-08 — Pass 1: initialization
**Decision:** create a curated navigable research atlas before scaling to automated metadata collection.
**Why:** "scrape everything" is unbounded and includes inaccessible/copyrighted sources. Scientifically useful progress requires provenance, review levels and falsifiable experiments.
**Scope:** major primary publications/venues, technical synthesis, ten hypotheses, nine proposed experiment tracks, first metadata collector.
**Evidence:** selection grounded in source abstracts and proceedings entries; no full-text systematic review/replication; zero training results.
**Risks:** source gaps in late-2026 literature, paper revisions, license/metadata ambiguity, evaluator contamination.
**Next:** test collection code, populate review queue, examine conflicting papers and actual method sections, then reproduce an open model baseline once hardware is specified.
**Baseline commit:** initial README 304aa9a5aa6fc21d596e68ea0378c14ae919297f, continued by subsequent commits.

## 2026-10-08 — Pass 2: public lab recipes, current architecture research, evaluation tooling
**Decision:** deepen public laboratory methods and 2026 research; ease blanket restrictions for lawful private copies while preserving attribution and access rights.
**Implemented:** Pass 2 atlas; technical dossiers on Olmo/DeepSeek/Qwen/Kimi/DAPO; hybrid/byte/diffusion; temporal memory/world models; reasoning/data/benchmark interpretation; private research policy; source ledger; 63 curated source entries; claim ledger; arXiv/Crossref/OpenAlex bounded metadata collectors; workflow_dispatch-only discovery workflow; deterministic temporal-memory fixture and tests.
**Evidence:** papers are E1 or official public documentation, not full verified replications. Claims explicitly include caveats.
**Verification:** Python 3.11 GitHub Actions CI passed after catalog-title minimum was corrected; additional code was subsequently added and requires its own CI confirmation.
**Failed test and fix:** CI run #37769514644 initially failed because valid short source title 'Olmo 3' triggered an arbitrary 8-character minimum. The schema title minimum was changed to 3 while keeping long summary requirements. CI run #37769620285 subsequently passed. The failed run remains visible.
**Open:** live source APIs not invoked from this session; manual discovery workflow unexecuted; no live weights trained; rights of full-text source archives not evaluated individually; source abstracts not equivalent to complete papers.
**Next:** focus on full-paper method/appendix reviews, compile executable training-recipe records and run a real E01 baseline with confirmed local compute (see docs/21-pass3-backlog.md).
