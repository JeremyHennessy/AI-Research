# Eighth-pass source reconnaissance: independent evidence versus reused data

**Date:** 2026-10-08. **Scope:** research-only source reading; no simulation, implementation, dataset execution, or changes outside AI-Research.

## Finding 1 — Stepney & Hickinbotham (2024) is not an independent experimental replication

- Primary paper: https://doi.org/10.1162/artl_a_00399 ; author bibliography https://www-users.york.ac.uk/~ss44/bib/ss/nonstd/artl23.htm
- Its abstract explicitly identifies **eight long runs** of spatial Stringmol originally designed for parasite work; it compares system-generic evolutionary-activity measures with follow-on phenomenon-specific measures. The authors argue that fixed metrics can miss behavior outside their model.
- University of York supplementary methods explicitly state that input data were generated for **Hickinbotham et al. (2021)**, DOI https://doi.org/10.15124/305dfdb6-9483-4c5b-8a01-c030570b9c31. Thus this is an **analysis of previously generated runs**, not a new independent population experiment.
- Crucial newly identified derived-data archive: https://doi.org/10.15124/88a8bad0-b23f-4afc-80a6-77e6358b7a8f (York record describes **rundata.zip**, 42 MB, **CC BY**, plus methods PDF). It is separate from the **2021 input** archive. The methods document states derivation takes **over ten hours on a modern laptop**; this is a provenance and computational-cost report, **not independently checked**.
- Main article remains at **E1 / abstract verified plus supplementary method excerpts**, not E2. Neither article full text nor archive contents were independently inspected in this pass. Do not claim which novelty metrics passed or failed without full text and figures.

## Finding 2 — Furubayashi et al. (2020) establishes a different kind of comparison

- Open primary article, full methods and figures: https://elifesciences.org/articles/56038 ; DOI https://doi.org/10.7554/eLife.56038 (CC BY).
- The authors report **120 rounds / 600 hours** of RNA replication, including 43 rounds previously reported and **77 additional rounds**. Therefore even within this paper, early rounds are reused previous results rather than independent extra runs.
- Their RNA system supplies a reconstituted *E. coli* translation mixture and external water-in-oil droplet compartments. Host RNA encodes the catalytic beta subunit of Qβ replicase; parasitic RNAs lack an intact copy of that gene and rely on host-supplied replicase. These are **engineered experimental affordances**, not evolved new autonomous metabolism or self-produced cell boundaries.
- Sequencing reveals at least **two host** and **three parasite** lineages, with competitive replication assays comparing evolved clones. Evidence is **within-experiment molecular diversification and antagonistic evolution**, not origin of cellular life or indefinite evolution.
- Key methodological caveat: parasite concentration was estimated via gel band intensity, while host concentration used RT-qPCR. Parasite detection was approximately **30 nM**, creating under-detection intervals. Sequencing sampled **17 rounds**. Their detailed analyses concentrated on **72 sites** associated with dominant mutations, excluding rarer variation from those downstream analyses.
- This paper is a **different physical substrate**, but experimental resources, externally imposed droplets, measurement resolution, and controls preclude treating its outputs as directly comparable to Stringmol 'novelty counts'.
- Source has full HTML methods accessible here, but independent source-code/data reproduction was **not performed**. Keep E1 until an appropriately complete evidence-level and figure audit is integrated into the existing ledger.

## Cross-paper design implication — do not conflate independence levels

| Question | 2021 Stringmol | 2024 novelty metrics | 2020 RNA ecosystem |
|---|---|---|---|
| Empirical unit | computational world | **reanalysis of 2021 worlds** | controlled wet-lab evolving RNA experiment |
| Origin | preseeded coded replicator | identical inherited input data | prepared host RNA and translation machinery |
| Replication primitive | virtual machine copying primitives | no new world-generation | host-provided Qβ polymerase supported by lab mixture |
| Resource/boundary | designed spatial constraints | inherits earlier design | externally supplied fresh mixture and droplets |
| Measured novelty | evolved strategies and extinction | generic and focused metric interpretations | sequence lineages and competitive fitness |
| Independent replication of 2021 study? | original runs | **no** | **no, mechanistically distinct** |

**Original research inference, not published causal conclusion:** a strong cross-substrate assessment should compare *ancestry and heritable response to novel perturbation* while measuring externally supplied organizational functions (copying physics, resource refresh, boundaries and fitness). Absolute 'complexity' scores or lineages alone are not commensurate endpoints.

## Remaining checks before evidence promotion

1. Obtain and read complete 2024 journal paper (not just abstract), inspect all figures and negative/discordant metric examples.
2. Inspect 2024 derived-data archive manifest and provenance metadata without running computations; check software rights/versioned analysis code.
3. Review 2020 eLife figures, supplemental files and peer reviews systematically; distinguish repeated temporal samples from independent biological replicates, verify denominators and control groups.
4. Link these notes into bibliography/claims ledgers only after exact record identities and evidence-level conventions are confirmed.
5. Preserve the no-implementation boundary; no Ora or AgentTest changes.

**Reproducibility receipt:** source pages reviewed via web on 2026-10-08; no source data downloaded, no historical reproduction or independent statistical verification, no tests run. This document is a limited source reconnaissance note, **not E2 certification**.
