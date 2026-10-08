# Evidence standards and reproducibility policy

## Evidence levels (never conflate them)
- **E0 — lead:** title or search hit only; unverified.
- **E1 — primary metadata:** verified title, authors, abstract, DOI or canonical URL; source content not fully reviewed.
- **E2 — reviewed publication:** claims, methods, evaluation and limitations read in full.
- **E3 — reproduced:** independent implementation or run matches defined published outcome within tolerance.
- **E4 — transferred:** replicated advantage on new private or time-held-out tasks under comparable costs.
- **E5 — deployed safely:** staged validated live behavior, monitored risks, measured ongoing degradation.
A number printed in a paper is only an **author-reported result**, never E3 by default.

## Claim types
- **Published finding:** “the authors report …” with paper link and caveat.
- **Engineering inference:** a principled extrapolation that might not replicate.
- **Original hypothesis:** has explicit falsifier and baseline; avoid asserting it as fact.
- **Experiment result:** include run ID, artifacts, commit, seed, exact dataset, model and metric.
- **Fact about deployment:** demands observable current service tests.

## Paper record checklist
Identifier; canonical URL; version and published/updated dates; authors; title; venue; sources; abstract summary in our words; stated novelty; experimental setup; baselines; measured costs; strongest result; counterexamples; limitations; dataset and code links; weights/license; known critiques/replications; confidence; claim IDs; proposed follow-up experiment.

## Experiment record checklist
Hypothesis; exact independent variable; preregistered primary metric; explicit test split provenance; model and tokenizer hash; dataset hashes; commit; hardware and compiler; driver/CUDA; random seeds; deterministic environment controls; batch size; context length; prompt template; per-example outputs; costs (tokens, wall clock, VRAM, energy if available); confidence intervals; failure clusters; rollback point; conclusion and next decision.

## Minimum acceptance rule
For an exploratory run, improvement can be treated as a *signal*, not proof. For promotion to "better": (1) repeatable results; (2) baseline with equal resources and optimization effort; (3) predeclared holdout and uncertainty bounds; (4) meaningful effect size; (5) no hidden task regressions, significant reliability failures or license violations.

## Anti-contamination rule
Archive a never-seen test split before tuning. Keep prompt templates, problem statements, solutions, near-duplicates and synthetic paraphrases out of training and development. If the split has been consulted while tuning, reclassify as development and acquire a new test set. Time-of-publication after *both* model and agent-scaffold freeze is especially useful, though not sufficient by itself.

## Legal/security/provenance
Store links + metadata + concise original summaries. Do not mirror full papers, datasets or weights without permission. Check licenses separately for model weights, source code and datasets (licenses do not automatically transfer). Store only lawful data; redact personal and secret information. Untrusted academic code must be sandboxed before running. No automated publishing to production systems from research experiments.

## Negative result template
**Attempt** / **expected mechanism** / **actual result** / **diagnostic evidence** / **why interpretation is limited** / **reversion** / **next hypothesis**. Keep failed trials discoverable, not deleted.

## Research status as of 2026-10-08
Initial literature selection E1 for many sources, some contextual synthesis; **zero local experiment/replication claims**. A metadata search, citation or link checker does not validate a scientific finding.
