# Pass 15 — learned knowledge has a resource cost

Date: 2026-11-24. Input commit `cbdc25c1fa70f83695fa7b6af03dea0a46ed04f5`. Data commit `07fb9a34a108290936f8b963ffa4eb06e49bec49`. Preserved main baseline `18f37bebca2f650aff8ab844ddb1ab9c8896158b`. [Draft PR #70](https://github.com/JeremyHennessy/AI-Research/pull/70).

## Custody and scope

Read Pass 2, Pass 14, Pass 13 and all eight earlier architecture ledgers at pinned input HEAD. Initial PR open, draft and unmerged; 32 additive files, 32 commits ahead and zero behind original main baseline. Reconstructed 46 profiled IDs and 38 pending from the 84-entry queue. This batch covers the next five IDs, ARCH-032–036. [Structured profiles](../../data/historical-cognition/2026-11-24-pass15-architecture-profiles.jsonl) contain ten primary-source records. Scoped exact identifier/title-phrase duplicate screen against 405 JSONL lines in 14 files (including canonical paper catalog and historical records) yielded no hits; not exhaustive deduplication of prose, title variants, or prior citations. Five new architecture dispositions, zero duplicate IDs, zero blocked profiles. Ten source records newly registered within this scoped screen; one subscription-restricted full chapter (DSO 2017) and one failed screenshot (Disciple 2000, HTTP 502) explicitly recorded. Other abstract-only sources are not full-method reviews. No new bibliography dispositions, FOIA year coverage, or E2/E3 promotions. Only metadata and original analysis retained.

## Mechanisms and evidence

- Disciple: [Tecuci et al., 2000](https://lac.gmu.edu/publications/2000/TecuciG_Experiment_COG_IJHCS.pdf) report a one-week expert teaching exercise in August 1999 under DARPA/AFOSR High Performance Knowledge Bases. The learner extends a supplied ontology-based knowledge base through guided examples, explanations and corrections. [2005 RKF paper](https://doi.org/10.1111/j.1467-8640.2005.00282.x) continues mixed-initiative learning. Expert-supplied knowledge and creative reasoning are integral, not autonomous acquisition from unstructured experience. HPKB programme association is supported by the author text, not an authenticated exact award number; no funding amount or final acceptance inferred.
- DSO: [2010 prototype](https://doi.org/10.2991/agi.2010.35) integrates image and contextual knowledge; [2017 paper](https://doi.org/10.1007/978-3-319-63703-7_5) describes a workspace-inspired memory design and image-captioning application. Public affiliation establishes Cognition and Fusion Lab 2, DSO National Laboratories, Singapore, as an institutional research participant. No claim about nonpublic work. Full 2017 methods subscription restricted; no general learning or consciousness inferred.
- DUAL: [Kokinov 1994](https://escholarship.org/uc/item/0wj7w24k) and [Kokinov and Petrov 2001](https://www.alexpetrov.com/pub/analogy01/intro.html) describe context-sensitive computation and analogy/memory models, respectively. Changing activation across designed micro-agents is not by itself durable learning.
- EPIC: [Kieras and Meyer 1997](https://doi.org/10.1207/s15327051hci1204_4) and [Meyer and Kieras 1997](https://pubmed.ncbi.nlm.nih.gov/9009880/) model concurrent cognitive and perceptual-motor tasks. A human performance model can have excellent fit without acquiring the modeled executive machinery.
- ERE: [NASA-TM-107867, February 1991](https://ntrs.nasa.gov/citations/19920016498) and [NASA-TM-111483, June 12, 1992](https://ntrs.nasa.gov/citations/19960022269) establish public NASA Ames research outputs. No procurement instrument recovered. Both records mark US government work public use permitted.

## ERE: negative utility of useful knowledge

Selected methods and results from [Kedar and McKusick 1992](https://ntrs.nasa.gov/api/citations/19960022269/downloads/19960022269.pdf), sections 2–4. The authors used simplified ERE/MTR software, a 10 by 10 TileWorld grid, 20% obstacle density, ten sets of 50 training problems and 100 test problems, results averaged over ten runs. The start and goal were diagonally opposite corners. Learning repaired deliberately incomplete action models. The precondition experiment reached about 85% goal achievement, with the remaining 15% reported obstructed; the alternative-outcome experiment also approached that ceiling. Printed p.7 visually confirmed the ceiling and imposed error scenario; printed p.9 visually confirmed the increasing matching and search cost curves. No raw trial data, seeds or runnable implementation acquired; no E2 full-method adjudication or E3 reproduction claimed.

The paper reports two different approximation tradeoffs (printed pp.11–12, text extraction, not visually checked in this batch):

| Approximation | Goal achievement (full → reduced model) | Cost (full → reduced model) |
| --- | --- | --- |
| Selected precondition omission | 85% → 67% | 780 → 660 matching calls/problem |
| Pruning alternative action outcomes | 85% → 43% | about 100 → 72 search nodes/problem |

The first is an 18 percentage-point drop and about 15% less matching work; the second is a 42-point drop and about 28% less search work. These are distinct experiments and metrics, not a single pooled cost-benefit curve. A designer-supplied success criterion and cost proxy are not a metabolism. The authors describe a dynamic performance monitor as future implementation, not a validated autonomous controller. Positive learning and negative resource utility can coexist.

Ora crosswalk (research interpretation only): retained information, prediction, action success, cost and viability are distinct. Improvement in one must not be silently treated as improvement in all. Historical approximation experiments are prior art for accuracy/cost tradeoffs; no novelty claim. No new engineering recommendation, runtime change or experiment authorized here.

## Frontier

51/84 initial profiles; 33 pending, next ARCH-037 FORR, ARCH-038 GLAIR, ARCH-040 Homer, ARCH-042 ICARUS, ARCH-044 IMPRINT. Bibliography remains 34/2,983 initially dispositioned (five unresolved at primary level; next physical row 36 ACT-R); 2,949 not yet examined. Government years partially examined 4/17, none comprehensively audited. E2 full-method audits 1, E3 independently reproduced experiments 0. Bibliography and FOIA coverage remain priority backlogs. Closure not reached. No candidate imported or executed, no approved file modified, no runtime, grants, STOP/PARKED or production changes, no merge.
