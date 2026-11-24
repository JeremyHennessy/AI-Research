# Historical cognition research — Pass 2: dataset audit and BICA outcome trace

**Date:** 2026-11-24  
**Status:** Research-only, initial acquisition and selective source review complete; comprehensive literature reconciliation remains open.  
**Preserved base:** `18f37bebca2f650aff8ab844ddb1ab9c8896158b`  
**Predecessor:** [Pass 1 dossier](2026-11-24-ora-prior-art-and-archive-dossier.md).  
**Review submission:** [AI-Research PR #70](https://github.com/JeremyHennessy/AI-Research/pull/70).

## 1. Actual acquisition and processing

Recovered all 12 ODS workbooks from the exact public [upstream commit 88b5605b96cbd61e3e5409dadd92503b9eb7784c](https://github.com/ykotseruba/cog_arch_data/tree/88b5605b96cbd61e3e5409dadd92503b9eb7784c). This is the data associated with [Kotseruba and Tsotsos, 2018/2020](https://doi.org/10.1007/s10462-018-9646-y). The files were fetched as base64 via GitHub, decoded in memory, and the declared uncompressed length and ZIP CRC32 for each content.xml member were verified. No upstream code was executed. No ODS or full bibliography was republished: a separate dataset license was not visible in the inspected root listing. The paper's CC BY license must not be assumed to apply to separate files.

The [machine-readable audit](../../data/historical-cognition/2026-11-24-architecture-dataset-audit.json) records exact Git blob IDs, file lengths, member CRCs, sheet counts, bibliography identity diagnostics, and the prior repository catalog used for reconciliation. The XML extraction respected repeated rows and columns and omitted empty formatted rows. This is a first-pass structural audit, not independent validation of the underlying scholarship. CRC32 verifies the ZIP member against the stored checksum; it is not cryptographic source authentication.

| File family | Nonempty rows, including headers and ancillary rows |
| --- | ---: |
| Abilities | 85 |
| Action selection | 296 |
| Applications | 965 |
| Attention | 1,038 |
| Bibliography | 2,984 |
| Learning | 77 |
| Memory | 149 |
| Metacognition | 85 |
| Perception | 334 |
| Software | 87 |
| Timeline | 85 |
| Vision | 86 |

The timeline has 84 distinct architecture entries: 40 hybrid, 32 symbolic and 12 emergent, according to the historical survey classification. These are historical labels, not conclusions about the current field. All 84 architecture identifiers are now in the [review queue](../../data/historical-cognition/2026-11-24-architecture-review-queue.jsonl), at E0 until primary architecture records are checked. Priority is an Ora relevance triage, not a performance ranking.

The bibliography has 2,983 complete architecture/key/reference rows, 2,954 distinct reference keys, 2,938 distinct exact citation texts and 88 architecture/category labels (including non-architecture bibliography categories). None of these counts is a verified number of unique publications. The source catalog contains no extracted DOI strings under the current pattern. Comparison against the pinned 269-record `data/papers.jsonl` catalog produced zero DOI or normalized exact quoted-title row matches. This does **not** establish disjoint literature: the bibliography's citation formatting, title variants, conference/journal versions, absent DOIs and existing research notes outside the canonical paper catalog may conceal overlaps.

No E1 source was automatically created from the 2,983 entries; no E2 reading or replication was inferred. The entire range Sheet1 rows 2–2984 is the unresolved bibliography reconciliation queue. In future passes identify a stable upstream row number, reference key and resolved primary identifier; mark alias/duplicate, unrelated, E0 lead, E1 verified, E2 separately reviewed, or unavailable with reason. Do not store an unnecessary complete copy of the upstream citation table.

The current source manifest and queue are metadata and derived observations; exact reproduction requires the upstream files and a parser that respects ODF row/column repeat attributes. No independently runnable acquisition script is claimed in this pass.

## 2. From funding to documented outputs

The earlier FY2005 funding sample is retained. A [five-row FY2006 continuity sample](../../data/historical-cognition/2006-bica-continuity-sample.tsv) now traces exact award identifiers across years. Both sources are indexed government table extractions; the target FY2006 page image returned HTTP 403. Do not sum these samples into programme totals or assume completeness. On the FY2005 alternative URL the screenshot returned a nonmatching printed page, so the specific rows remain text-extraction evidence rather than image-authenticated rows.

The [additional source register](../../data/historical-cognition/2026-11-24-bica-output-sources.jsonl) contains 12 E1 records, with original dates, authors, source URLs, document numbers, evidence type and relevance. Four documents identify two awards exactly in their first-page acknowledgements, verified visually:

| Award | Technical document | Date | Evidence boundary |
| --- | --- | --- | --- |
| FA87500520272, University of Maryland | [A Behavior-to-Brain Map v1.0](https://api.drum.lib.umd.edu/server/api/core/bitstreams/76968b5f-15dc-476c-a152-fc31a31643bd/content), CS-TR-4803 | May 2006 | Preliminary functional-anatomical mapping; not a complete model. |
| FA87500520272 | [Large-Scale Integrated Neurocognitive Architecture, Part 1](https://api.drum.lib.umd.edu/server/api/core/bitstreams/74f6f331-b2e0-4548-892b-22a7f87f8513/content), TR-CS-4814 | June 2006 | Component prototypes, conceptual framework; not a human-level architecture. |
| FA87500520272 | [Large-Scale Integrated Neurocognitive Architecture, Part 2](https://api.drum.lib.umd.edu/server/api/core/bitstreams/f3d6ee44-9687-489c-932e-7d01bc16891a/content), TR-CS-4827 | October 2006 | Architecture proposal and exploratory component work, not validated general cognition. |
| FA865005C7257, Klein Associates | [Adapting the Turing Test for Embodied Neurocognitive Evaluation](https://cdn.aaai.org/Symposia/Fall/2008/FS-08-04/FS08-04-031.pdf) | 2008 | Evaluation design; not evidence of an agent passing the tests. |

The three Maryland reports are a single funded research lineage, not independent corroborations of a general result. Matching an acknowledgement to an award establishes a funding/output relationship, not proof of final contractual acceptance, expenditure totals, scientific success or comprehensive reporting.

### Maryland: a particularly relevant prior-art constraint

The researchers proposed an architecture integrating neural, symbolic and artificial-life-inspired components. Their October report describes a prototype with simplified perceptions and some learning conducted outside the running agent. This is directly relevant to distinguishing authored infrastructure from acquired cognition. If environmental objects are already coded as semantic categories, or relevant behavior is learned outside the measured lifetime, the resulting performance does not establish that an organism developed those competencies under its own constraints.

The team's conceptual and pilot contributions are useful historical comparators; their long-term objective is not an observed achievement. For Ora, the appropriate action is to record the source of each functional competency and the causal intervention demonstrating it, not to integrate a large hybrid architecture on the strength of the report.

### Other technical and methodological comparators

- [MIT CHIP report, September 29, 2006](https://courses.csail.mit.edu/6.803/pdf/bica.pdf): architectural design combining perception, action and higher control; relevant to prior-art analysis. PDF image unavailable because of size; exact award identifier not established.
- [Laird, Extending the Soar Cognitive Architecture, 2008](https://web.eecs.umich.edu/~soar/sitemaker/docs/pubs/Laird%20-%202008%20-%20Extending%20the%20Soar%20Cognitive%20Architecture.pdf): expansion of explicitly designed learning and memory infrastructure. The first page was visually checked; no exact award acknowledgement was found. Treat the funding link as unverified.
- [Samsonovich, Schema formalism, 2018](https://doi.org/10.1016/j.bica.2018.10.008): participant account of continuing GMU cognitive architecture work and a simulation proof-of-concept. Full methods and controls not reviewed.
- [Kotseruba and Tsotsos, 2025 online book](https://doi.org/10.1093/oso/9780192844835.001.0001): expanded synthesis based on 3,000+ publications, 80+ architectures. Its abstract and chapter descriptions are checked, but full book and any additional dataset remain unaccessed. Same research lineage as the 2018 survey, not an independent replication.

## 3. A significant negative finding: programme completion is not capability completion

The [2007 evaluation team's paper](https://citeseerx.ist.psu.edu/document?doi=66b3cec215b4aed5198abc4e80f032be97e01af0&repid=rep1&type=pdf) states that the proposed Phase II had not received funding at the time. Its authors designed independent evaluation of integrated cognitive agents, including component tests, broader tasks and biological comparison. The test plan was not a record of successful performance. PDF image retrieval failed; indexed text is retained as E1.

The [2009 AGI conference participant paper](https://agi-conf.org/2009/papers/paper_62.pdf) by Alexei V. Samsonovich explicitly reports cancellation of Phase II (visually confirmed on p. 1). It also proposes a theoretical threshold for sustained developmental growth. The threshold is a prior hypothesis, not a measured law or a new Ora hypothesis. The exact cancellation date, official decision memorandum and administrative rationale have not been recovered.

The February 2007 [DARPA budget justification](https://comptroller.defense.gov/Portals/45/documents/defbudget/fy2008/budget_justification/pdfs/03_RDT_and_E/Vol_1_DARPA/DARPA.pdf), COG-02, describes architectures and a test battery. This supports the existence of development and evaluation work, not attainment of the originally intended capability. Target page screenshot failed. It is compatible with the participant reports that the intended follow-on phase did not proceed.

This convergence is evidence against treating the public Phase I work as a documented successful completion of the intended programme. It does not prove what every participant or undisclosed organization did elsewhere. No hidden-general-intelligence conclusion is established.

## 4. Implications for Ora without altering the experimental baseline

1. **Independent testing before capability labels.** The BICA evaluation precedent distinguishes broad performance, component skills and biological plausibility. Ora must keep validated substrate, behavior, learning, transfer, inheritance and generality distinct.
2. **Scaffold accounting.** Record which abilities are provided by the designer, environment, initialization, inherited state, interaction or externally defined reward. Do not interpret an externally supplied label or task solution as independently acquired cognition.
3. **Historical growth hypotheses are not novelty.** Self-sustained development and threshold concepts were already proposed in the BICA literature. Any Ora novelty claim must specify a distinct mechanism, boundary and counterexample, and survive a primary literature search. No novelty claim is made here.
4. **Negative evidence is first-class.** Programme cancellation, abandoned methods, insufficient integration, unavailable results and unrun evaluations must remain discoverable. Lack of access is UNKNOWN, not failure.
5. **Current experimental governance remains unchanged.** Nothing in the new references authorizes modifying Ora, executing candidate code, changing scientific STOP or director PARKED, issuing new grants, or deploying anything.

## 5. Bounded comprehensive research completion criteria

This project is not literally capable of collecting every public or private record ever created. The tractable completion target is the following explicitly bounded coverage and gap report.

| Workstream | Completion criterion | State at end of this pass |
| --- | --- | --- |
| Dataset structural audit | All 12 pinned ODS files processed with member integrity and row counts | COMPLETE |
| Architecture queue | All 84 distinct timeline labels recorded with traceable locators | COMPLETE |
| Architecture profiles | Each of 84 queued IDs receives a primary-source profile, scope of learned vs designed abilities, evidence level, limitations and relevance or a documented access boundary | OPEN |
| Bibliography triage | All 2,983 rows at pinned source identity dispositioned with deduplicated metadata, relevance, access status and explicit unresolved cases | OPEN; initial exact match diagnostic only |
| Historical funding | Review accessible 1996–2012 DARPA FOIA annual lists for relevant cognition programme names; retain fiscal-year coverage, page and extraction status | OPEN; FY2005 sample and FY2006 continuity sample |
| Contract outcomes | Trace each relevant award to primary outputs, reports and evaluation where obtainable; document unsuccessful searches and unknowns | OPEN; exact 2-award/4-document sample |
| Modern follow-up | Locate public technical results for relevant cognition, developmental robotics, lifelong learning and alternative computing programmes, preserving positive and negative outcomes | OPEN |
| Critical methods review | Review the highest-value primary studies in full when lawfully accessible; tie every proposed Ora-relevant mechanism to a control, limitation and existing Ora evidence | OPEN |
| Closure | Deduplicated evidence inventory, source coverage, prioritized crosswalk, contrary evidence and remaining legal/access gaps; independent review of factual claims and Git diff | OPEN |

Use one incremental, non-overlapping batch at a time. Treat upstream bibliographic rows as E0 pointers until resolved, then check dates, authors and source IDs against the canonical research catalog and prior Ora literature notes before adding records. Each batch must record start/end source locators, input commit, disposition counts, new document paths and remaining backlog. No automatic E2 elevation on text access; no invented facts, rights claims or successful-run claims. Research-only changes may be proposed on this branch without modifying other approved work or merging unreviewed results. Do not circumvent access controls or reproduce copyrighted material beyond permission.

**Pass 2 conclusion:** authentic data acquisition and structural processing are complete for the pinned dataset. The literature and archive investigation is not complete. The central scientific lesson is that integration and general cognition must be measured separately, with clear provenance of the capabilities being evaluated. Preserve the two exact contract-output links and the negative BICA phase evidence; advance the explicit backlog rather than collecting speculative claims.
