# Pass 4 program — make this an expert research library, not a frozen reading list
Last updated 2026-10-08. Preserve approved checkpoints, source provenance, CI, and interpretation of negative results.

## Current verified state
- AI-Research is a private GitHub repository containing an annotated curated bibliography and mechanism-specific dossiers.
- Literature and original hypotheses are **not** local replicated research.
- Offline metadata collection and validation were verified in previous CI; later modifications require fresh CI verification.
- No training or research breakthrough claimed.

## Pass 4: prioritized coverage and implementation
**P0 — source integrity**: reconcile DOI/OpenAlex/arXiv duplicates; maintain title corrections, revisions/retractions, original peer-review status and exact method-section refs. Explicitly distinguish original public author reports from independent replications, and retain negative evidence.

**P0 — topic depth**: read complete source papers/appendices and configurations for 10 priority works (2026 hybrid retrieval-aware distillation, architecture-aware inference scaling, Bolmo Nature, Olmo3 training, DAPO, 2026 interpretability causality critique, two memory-action papers, Genie/SIMA world transfer, recent diffusion). Extract equation + assumptions + code + benchmark + negative results, then promote from E1 to E2 **only** after complete read.

**P0 — experiment infrastructure**: run the deterministic memory fixture, write a small cross-domain evaluator, and reproduce a licensed open-weight model baseline. Link metrics to Git SHA and an immutable manifest. No user secrets or unapproved production deployments.

**P1 — source breadth**: add Bayesian/probabilistic reasoning, program synthesis, computational neuroscience, continual and transfer learning, speech/audio-native models, video and spatial AI, GNNs, formal logic and hybrid neurosymbolic systems, multicriteria RL, collective multi-agent learning, science discovery, and hardware energy economics.

**P1 — evidence synthesis**: create contrast cards for conflicting publications. Each needs explicit disagreement, populations/models, intervention, comparator, possible confounds, and a decisive experiment. Keep disconfirming evidence visible.

**P2 — reproduction program**: allocate hardware after profiling; choose E01 baseline, E14 interpretability intervention, E03 temporal memory with true LLM, E20 adapters and E21 verifier-guided optimizer. Propose a genuinely new mechanism only after all relevant comparators are understood.

## Outcome criteria
A successful pass yields net new **verified** information, not just links. Measures:
- new unique primary sources and **confirmed corrections** (not raw scraped count),
- sources promoted to E2 after full method review,
- new falsifiable experiments with frozen evaluation,
- actual reproducible model/test outcomes and null results,
- remaining blind spots accurately identified and ranked.

## Ongoing research cadence (separate from code)
A daily or weekly scan is useful, but should never automatically call a search result verified, import copyrighted full articles without rights, run unknown repository code or claim an improvement. A recurring research assistant should scan, deduplicate, inspect primary releases, amend the literature graph and run CI before pushing, then report evidence and blockers.

## Research custody
The current [research log](../data/research-log.md) is the append-only handoff. Record exact main commit and CI receipts after significant updates. No arbitrary reorganization or replacement of previously reviewed material during collection.
