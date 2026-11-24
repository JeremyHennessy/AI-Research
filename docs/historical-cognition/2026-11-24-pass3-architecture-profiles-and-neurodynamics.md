# Historical cognition research — Pass 3: architecture profiles and evolutionary cognition

**Date:** 2026-11-24  
**Input checkpoint:** `4aba733951be153f56508b718c8eb88c1f23c47c`  
**Review submission:** [PR #70](https://github.com/JeremyHennessy/AI-Research/pull/70).  
**Status:** Research only; nine initial primary-source profiles at E1, not full methods audits or reproduction. No change to Ora's experimental or deployment authority.

## 1. Coverage and preservation

[Pass 2](2026-11-24-pass2-dataset-and-bica-outcomes.md) established an 84-architecture queue and 2,983 unresolved bibliography rows. This pass adds [nine architecture profiles](../../data/historical-cognition/2026-11-24-pass3-architecture-profiles.jsonl) with 21 distinct source identifiers within the batch, including two already explicitly indexed in HC043 and HC044 and other historical relationships. Count them as source pointers, not 21 independently new publications. The exact prior 269-record paper catalog was inspected for nine selected DOI strings and relevant title keywords; no matches returned for that restricted query. Full duplicate reconciliation across research notes and all aliases remains open.

Profile IDs dispositioned at initial E1 level: ARCH-004, 014, 021, 039, 043, 053, 077, 079, 083. Their original E0 queue entries are preserved, not overwritten; the new JSONL is the subsequent disposition record. **9/84 have initial profiles; 75 remain unprofiled.** Full source-method audit remains pending even for these nine. No claim of bibliography row-level completion: 2,983 rows remain to be resolved.

## 2. What the nine systems actually contribute

| Architecture | Evidence distinction | Relevance |
| --- | --- | --- |
| ACT-R | Published model of cognitive modules, rules and memory; selected learning and human-task comparisons | Distinguish acquired knowledge from the mechanisms and task rules that are supplied. |
| BECCA | Author-reported robotics demonstrations with feature learning and reward-based control | Learned representation is a separate capability from learning how to act. |
| CLARION | Reported skill learning in a defined task, with procedural-to-explicit learning | A prior model of behavior preceding explicit knowledge; not evidence of consciousness. |
| GMU-BICA | Architecture and proposed self-regulated tutor; the 2008 application is explicitly a blueprint | Self-sustaining growth and metacognitive development are historical prior-art goals, not demonstrated outcomes in this source. |
| iCub | Documented robotic research platform; related RobotCub-funded learning study | Distinguish provided sensorimotor skills from competencies acquired through experience. |
| MicroPsi | Motivated-cognition framework, initially prototypic | Authored representations of needs and emotions cannot establish naturally developed motivation. |
| Soar | Production rules, chunking and reward-based operator preference learning | Separate learned rules and preferences from initial symbolic structure. |
| Subsumption | Layered reactive control demonstrated on a mobile robot | Strong comparator against an unwarranted interpretation of robust behavior as learning. |
| Darwinian Neurodynamics | Computational models of selection and evolution of informational patterns | Prior art for variation and retention of information within a cognitive system. |

Each row links through the structured profile to dated original records, distinguishes implemented/reported behavior from designed scaffolding, and states the specific evidence boundary. The 1985 Brooks report and 1986 paper are not independent experiments; the 2008 RobotCub-funded affordance paper is a related comparator, not authenticated here as an experiment on the exact iCub platform.

## 3. Darwinian neurodynamics: strongest new research lead

The [2010 neuronal replicator hypothesis](https://pubmed.ncbi.nlm.nih.gov/20804380/) proposes copying and variation of neural activity patterns. The [2012 critical appraisal](https://doi.org/10.3389/fncom.2012.00024) distinguishes selection among existing alternatives from evolutionary processes involving multiplication and heritable variation. The existence of the proposed biological replicators was not established by the reviewed record.

The European Commission [INSIGHT grant 308943](https://cordis.europa.eu/project/id/308943/reporting) ran March 2013–August 2016, with EUR 2,863,634 total reported project cost and EUR 2,219,079 EU contribution. Coordinator: Parmenides Stiftung. The official reporting page lists three documents concerning experimental methods, replicator models and evolutionary foundations. Their contents remain unreviewed.

A direct funding-to-publication relationship is established by the [2016 paper, revised version 2 published June 29, 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5130073/), DOI 10.12688/f1000research.9630.2. Its funding statement names INSIGHT 308943, EvoEvo 294332 and GINOP-2.3.2-15-2016-00057. This is one documented output, not an independent validation of the grant's whole objective.

### 3.1 Selected experiment and limitations

The authors simulate networks with recurrent memory, linked by a designer-specified evaluation and selection process. In their alternating-environment experiment, they change the optimum every 2,000 generations; after 12,000 generations they disable learning and randomize initial inputs at subsequent environmental transitions. Previously acquired patterns can still be retrieved, then amplified by the explicit fitness-based selection process. See methods, Figure 4 and results. This distinguishes retained information from mere persistence of the immediately preceding output. It does not establish autonomous inference of a new goal or unrestricted transfer. In their stable-landscape experiments memory is less beneficial and may impede exploration. The assumed fully connected network and external target evaluation limit the biological interpretation.

The public open peer review attached to version 2 asks how natural neural systems would establish optimality and how simulated generations correspond to neural processes. Author responses and referee acceptance do not constitute an independent reproduction.

Source and data pointers supplied by the authors: [Neurodynamics code](https://github.com/IstvanZachar/Neurodynamics), [second implementation](https://github.com/andszilagyi/darwinianneurodyn), [Zenodo 154113](https://doi.org/10.5281/zenodo.154113), [Zenodo 803989](https://doi.org/10.5281/zenodo.803989). These pointers were read in the article; their actual repository contents, versions, licenses and test results are not yet audited. No code imported or run. A [2021 follow-up](https://doi.org/10.1038/s41598-021-91489-5) was identified but only an indexed abstract excerpt was accessible. No detailed claim about its results is made.

### 3.2 Interpretive implications for Ora

The comparison does not justify implementing a new evolutionary cognitive engine or relaxing any existing gate. Its value is scientific: it helps distinguish organismal lineage, retained individual information, and variation/selection among candidate representations. If a future approved observation appears to demonstrate learning, plausible explanations include fixed reactions, carried-over state, retrieval of previously stored patterns, or genuinely acquired new function. These are separate interpretations; the best-supported explanation must survive comparisons and appropriate controls. Memory itself is neither inherently advantageous nor proof of intelligence. Avoid counting repeated activation of an old representation as independent discovery.

Existing Ora metabolic qualification, reproduction, inheritance, and ecology evidence remains unchanged. Scientific STOP and director PARKED remain as previously reported; their actual local state was not independently accessed in this research-only pass. No experiment, candidate, implementation or external action authorized.

## 4. Next bounded research batch

Continue non-overlapping E1 profiles for the remaining high-priority queue entries (e.g. HTM, NARS, LIDA, DAC, ART, SPA, Leabra). Resolve primary records and actual application evidence before claiming implementation outcomes. Separately examine the three INSIGHT deliverable pointers, the cited 2021 follow-up and the published methodological critiques using lawful public access; record failures as unknown. Retain negative and null findings as first-class results. Continue bibliography-row and historical archive coverage independently; this pass does not discharge either backlog.

**Decision:** nine architecture profiles are now documented. The strongest historical comparator is evolutionary cognition with explicitly supervised selection and memory; it is a useful constraint on interpreting Ora, not a reason to change the approved research substrate. No evidence of undisclosed general intelligence or consciousness is established.
