# Pass 16 — acquired skill structures versus supplied objectives

Date: 2026-11-24. Input HEAD `f3005878621eb996d1cfde4bd2b681f3c827483a`. Data commit `2907cfa0db738892a3b970876731a21bd9bce320`. Original main baseline `18f37bebca2f650aff8ab844ddb1ab9c8896158b`. [Draft PR #70](https://github.com/JeremyHennessy/AI-Research/pull/70).

## Custody and coverage

Read branch HEAD, PR, Pass 2 and Pass 15, queue and all nine earlier profile ledgers. Initial comparison: 34 added files, 34 commits ahead, none behind, zero deletions. Reconstructed 51 unique profiled IDs and 33 pending. This batch dispositions ARCH-037 FORR, ARCH-038 GLAIR, ARCH-040 Homer, ARCH-042 ICARUS and ARCH-044 IMPRINT; five new E1 profiles, zero duplicate IDs, zero blocked profiles. [Structured profiles](../../data/historical-cognition/2026-11-24-pass16-architecture-profiles.jsonl) contain eight primary source records. Exact identifier and selected title-phrase screening against 410 JSONL records in 15 files (canonical catalog and historical registers) returned no hits for the selected identifiers/phrases; not exhaustive alias or prose deduplication. One restricted full chapter (FORR 2011) and one failed image retrieval (Homer p.42, DisabledError) recorded; other abstract-only sources not represented as methods reviews. No source text or complete bibliography copied. Data commit verified by exact readback and comparison: five added lines, no deletions.

## Evidence distinctions

FORR ([1994](https://doi.org/10.1207/s15516709cog1803_4), [2011](https://doi.org/10.7551/mitpress/9780262014809.003.0004)): specialization through practice and an expert model, plus learning-management procedures. Retain distinction between learned strategy preference and the supplied evaluation and heuristic machinery.

GLAIR ([2010](https://doi.org/10.4230/DagSemProc.10081.17)): layered embodied reasoning and symbolic grounding. The existence of a functional self-model or grounding interface does not establish consciousness or independent acquisition of grounding mechanisms.

Homer ([Vere and Bickmore, 1990](https://doi.org/10.1111/j.1467-8640.1990.tb00128.x), [university-hosted paper](https://www.cs.rochester.edu/users/faculty/schubert/191-291/lecture-notes/vere-and-bickmore-a-basic-agent.pdf)): Lockheed AI Center simulated submarine integrates planning, language, episodic recall and temporal reasoning. Printed p.42 text explicitly excludes inductive learning from the implemented integration; it was deferred. Screenshot unavailable. This is a particularly useful negative comparator: retaining life events and answering questions about them can coexist with no inductive learning machinery.

IMPRINT ([2009](https://doi.org/10.1177/154193120905301212), [2024](https://doi.org/10.1177/10711813241261280)): authored human task-network workload models. Do not confuse simulation of resource-constrained human performance with an artificial organism acquiring cognition. Predictions and empirical validation must be distinguished.

## ICARUS — positive evidence of acquired executable skill structure

[Langley and Choi, March 2006, JMLR 7:493–518](https://www.jmlr.org/papers/volume7/langley06a/langley06a.pdf), Stanford Computational Learning Laboratory. Selected sections 1, 5.1 and limitations reviewed; Fig.3 (printed p.509), Table 8 (p.510) and acknowledgements (p.516) visually checked. This remains E1 because full-method adjudication and raw data/code acquisition were not completed.

Blocks World starts with nine concepts and four primitive skills, plus four goal concepts. Authors compared learning enabled and disabled over 200 randomized task orders, each with six sets of ten problems spanning 5 to 30 blocks. Attempts and search were bounded (50 cycles per attempt, up to five attempts, goal stack depth eight). At 30 blocks Table 8 reports:

| Condition | Cycles | CPU seconds | Solution probability |
| --- | ---: | ---: | ---: |
| Learning | 11.67 | 40.85 | 0.995 |
| No learning | 95.89 | 344.49 | 0.826 |

The reported difference is 16.9 percentage points in solution probability, and the reported CPU ratio is about 8.43 (344.49/40.85). The contrast is conditional on the supplied primitives, goals and search limits; more search could improve the no-learning comparator at a resource cost. The learned procedures are structural, not merely parameter adjustments. The ability to solve larger instances of familiar tasks is distinct from discovering new goals, and the authors explicitly identify limitations on generalization across goals. These are author-reported results, not independently reproduced. No claims of novelty or replication by Ora.

## Funding and access

The p.516 acknowledgement visually establishes two DARPA agreement identifiers (HR0011-04-1-0008, FA8750-05-2-0283) and one NSF grant (IIS-0335353) linked to the same paper. One publication, three funding acknowledgements, not three independent demonstrations. Individual award administrative records and final contractual acceptance not recovered.

A targeted FY2006 official [FOIA list text lead](https://www.esd.whs.mil/Portals/54/Documents/FOID/Reading%20Room/DARPA/12-F-1039_2006-DARPA-Funding-List.pdf) associates normalized FA87500520283 with Institute for Study of Learning and Expertise, AFRL Information Directorate, Transfer Learning programme/IPTO. Indexed row lines 2531–2536; exact PDF page not established. The FY2006 image access limitation was already documented in Pass 2; no new page authentication claimed. Treat as an E0 administrative cross-check lead pending page recovery, not a verified new archive disposition; no amount or full-year coverage claim. Paper acknowledgement is a separate, stronger E1 funding/output observation and does not establish the formal award recipient by itself.

## Ora prior-art boundary and next frontier

The ability to construct new executable skills from initially supplied primitives is documented prior art. Memory alone need not enable induction; structural learning can improve success and cost even without changing the objective. Neither observation establishes a mechanism for metabolic inheritance, evolution of learning machinery or autonomous formation of objectives. A future claim about Ora should identify the exact acquired structure, its provenance and the relevant counterfactual, not merely report novel behaviour. Research interpretation only; no experimental or engineering change authorized.

56/84 profiles (28 pending); next ARCH-045 ISAC, ARCH-050 MAMID, ARCH-051 MAX, ARCH-052 MDB, ARCH-054 MIDAS. Bibliography 34/2,983 initially investigated (five unresolved at primary level; 2,949 not examined; next physical row 36 ACT-R). Government coverage 4/17 partial years, zero complete. E2 full-method audits 1, E3 independent reproductions 0. Recommend prioritizing the bibliography or government workstream in the next finite batch to reduce backlog imbalance. Closure not reached. No Ora candidates imported or executed, no runtime, STOP/PARKED, grants, qualification gates, approved baselines or production changes, no merge.
