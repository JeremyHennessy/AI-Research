# Pass 5 handoff — priority on validity, depth and genuine experimental evidence
Created 2026-10-08. This is a plan, not work already done.

## Verified predecessor
Pass 3 checkpoint main SHA: `17892e5967017d68243b4f4a8245d1cdd3850ba6` (CI success). Pass 4 builds incrementally. Inspect the current main SHA and latest CI before modifying files; **do not revert to the predecessor** merely because it is an earlier baseline.

## Current research coverage
- **146** source records across **25** subject tracks; recent additions in Bayesian calibration, graph learning, program induction, formal proofs, speech, active inference and multi-agent coordination.
- **34** source-linked claims, **8** documented conflicting research narratives and **3** detailed published corrections/discrepancies.
- **One** DeepSeek-Prover-V2 public **full-text paper audit (E2)**. All other sources E1 (abstract/official public release), without independent reproduction.
- Offline mathematical/methodology fixtures: temporal memory, binary calibration, correlated ensemble majority, arXiv/Crossref/OpenAlex collectors and DOI/arXiv reconciling.
- No new AI weights trained, no real-world LLM performance improvement independently measured, no claim of exhaustive database scraping.
- A separate daily **AI Research Custodian** automation is already enabled. Do not duplicate it.

## Highest-information next passes
1. **Confirm source revisions first:** systematically resolve the DeepSeek-Prover-V2 arXiv abstract/full text discrepancy, document exact v2 passage and corrected benchmark version. Seek independent prover checker audits rather than quoting a scoreboard.
2. **Increase depth:** complete methods/evaluations/appendices for at least eight high-priority papers; only then label E2 (examples: 2026 formal logic verification, 2026 debate collapse, calibration under shift, GNN expressivity, Olmo 3 public training, audio data mixtures, hybrid SSM retrieval, DLM inference study). Include study-specific results, limitations and reproducibility gaps.
3. **Run E01:** select licensed accessible small open model, pin exact model/hardware, freeze hidden tasks. Real measured outcome is required before calling any inference technique an advance.
4. **Establish E23 and E28 model-in-loop baselines:** first real binary answer confidence evaluation (separate source and model uncertainty); independent vs debate samples on unseen tasks. Preserve raw per-task answers and execution costs.
5. **Improve identity resolution:** DOI ↔ publisher versions ↔ arXiv aliases, corrections/retractions, same paper cross-posted between OpenReview and proceedings. All uncertain merges require manual review.
6. **Broaden remaining gaps:** MDP/POMDP theory, Bayesian filtering, spiking networks, GNN over-squashing, neurosymbolic logic, speech-codec and real-time audio, active causal inference, multi-agent credit assignment, and AI systems energy.
7. **Real automated collection:** manually test bounded live API calls under published policies, inspect output completeness and rate limits, verify artifact saving. Existing collectors have only **offline unit tests**; never claim an online sweep from these alone.

## Decision discipline
For each source: read actual full paper, collect methods/negative evidence/version, create a practical falsifier, choose cheapest independent test, record exact evidence level. For each model run: frozen task/data/weights/compute, independent graders, replicated results. For each code change: smallest surface, CI and rollback, research log with SHA. No use of confidential material without authorization.

## Navigation
[Pass 4 atlas](29-pass4-index.md) → [Paper index](19-paper-index.md) → [DeepSeek formal review](30-deepseek-prover-v2-review.md) → [Disagreements](35-research-disagreements.md) → [Experiments](36-pass4-experiments.md) → [Research log](../data/research-log.md).
