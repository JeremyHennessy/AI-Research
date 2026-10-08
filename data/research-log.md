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

## 2026-10-08 — Pass 3: broader AI domains and integrity controls
**Decision:** continue building an 18-track knowledge atlas covering not only LLMs but mechanistic interpretability, causal representation, continual learning, security, alignment, robotics, AI for science and hardware efficiency.
**Publication work:** appended 45 source records, 63→108; new papers and primary institutional reports from ICML/ICLR, Anthropic, DeepMind, METR, MLCommons, OpenAI and arXiv. Added dossiers, cross-domain experiment specifications E14–E22, field map and prioritization for the next pass. Unreviewed full papers remain E1.
**Scientific caveat:** journal/conference publication is not independent replication. Anthropic claims about workspace and interpretation do not prove consciousness; scientific discovery claims require result-level mathematical verification; benchmark scores depend on graders/harness.
**Engineering:** created conservatively deduplicating `scripts/reconcile_sources.py` with DOI/arXiv identity and explicit conflicting-title flags; integrated manual discovery workflow. Tests were run in GitHub Actions, not by executing live external API collection from this session.
**Test failure and correction:** run #37771234981 failed because a test expected punctuation-only titles to count as a substantive disagreement. The reconciler normalized punctuation intentionally; fixture changed to genuinely different titles without changing reconciler behavior. Follow-up run #37771298447 passed. The failure remains documented.
**Continuity:** exact previously passing source-code commit a35eb13fe106cedc751f5e55ab3968b39fe6d956 (October 8, 2026). Later documentation commits should be validated as well. No model trained; no private lab materials retrieved; no live arXiv/Crossref/OpenAlex data collection executed as part of this session.
**Next:** expand 2026 conflict/negative evidence, run permitted API collectors when possible, audit full-text methods to E2, then establish frozen E01 benchmark before training/new-model claims. See docs/28-next-research-program.md.
