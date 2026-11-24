# Historical artificial cognition: archive and prior-art investigation for Ora

**Date:** 2026-11-24  
**Status:** Initial source-indexed research pass, no new scientific experiment; no implementation or execution authority.  
**Repository baseline:** `18f37bebca2f650aff8ab844ddb1ab9c8896158b`  
**Scope:** Publicly available scholarly records, released internal government records, official funding records, and public disclosures by privately operated research organizations. No classified, restricted, confidential or unauthorized material was accessed. A search of public records cannot establish the contents of inaccessible records.

## Read this first

- [35 source records (JSONL)](../../data/historical-cognition/2026-11-24-sources.jsonl): stable identifiers, authors/issuers, dates, URLs, access scope, observation, Ora relevance and evidence boundary.
- [17 BICA contract rows (TSV)](../../data/historical-cognition/2005-bica-contract-extract.tsv): directly associated contract identifiers, recipients, fiscal year, contracting agents, obligations and scan-verification caveat.
- [Existing Ora evolutionary-substrate synthesis, November 13](../artificial-life/144-ora-evolutionary-substrates-evidence-20261113.md): preserved. The present collection is complementary, not a replacement for the existing biological and digital-evolution investigations.
- [Repository evidence standard](../05-evidence-standards.md): E1 for the records in this pass. No full-paper E2 promotion, E3 reproduction, new organism, experiment, runtime action or deployment.

All URLs below are source pointers, not evidence of permission to redistribute full documents or datasets. The repository was observed to be public. Store original summaries and metadata, not restricted copies or private communications. Exact original document hashes and scan authentication remain outstanding. No automation, download or execution of upstream software was performed.

## 1. Scientific adjudication of the historical hypothesis

The hypothesis that important non-LLM cognitive work predates present-day chatbots is well supported. The stronger hypothesis that an undisclosed organization already achieved a generally intelligent, genuinely self-directed or conscious artificial mind is not substantiated by this collection. That hypothesis also cannot be ruled out by absence of public documentation.

| Proposition | Finding |
| --- | --- |
| Non-language cognitive architectures and artificial organisms existed decades ago | Supported by published work, including 1974 autopoiesis, 1991 embodied robotics, and 2003–2004 digital evolution. |
| Some government AI discussion was classified | Supported specifically by an archived 1983 CIA symposium schedule labeling a session Secret. |
| Governments and private performers invested in brain-inspired cognition | Supported by FY2005 BICA contract rows and additional programme records. |
| Prior programmes achieved their full stated humanlike-cognition objectives | Not established; the Strategic Computing history explicitly reports failure to achieve its overarching machine-intelligence goal. |
| A secret machine mind more capable than public systems exists | UNKNOWN; no authenticated outcome, benchmark, primary technical report or independently reproducible result in this pass. |
| Consciousness follows from self-modeling, neuronal scale, self-reproduction or broad task performance | Unsupported; those are different observations. |

Distinguish five kinds of evidence: **objective** (what a programme proposed), **resource commitment** (what was funded), **artifact** (what was built), **measured result** (what a documented protocol observed), **independent reproduction** (what a genuinely independent implementation/run established). A record may be strong evidence for the first two and say nothing about the last three.

The research question for Ora is not whether secrecy is real. It is which documented mechanisms and failures constrain a credible alternative account of the emergence of cognition.

## 2. Historical records with provenance

### CIA symposium — December 1983 (HC002)

Original date: December 1, 1983. Sender: Executive Secretary, ISB, from the CIA Planning Staff. The memorandum was addressed to the Executive Director, Executive Assistant/Executive Director, ISB members, C/IHC/ICS, P&PS/ICS and O/Compt. The attached December 6–8 symposium was sponsored by the US intelligence community and coordinated by SMART SYSTEMS TECHNOLOGY, Inc. The extracted programme names Philip K. Eckman (CIA), Richard D. DeLauer (Defense), Patrick H. Winston (MIT), Rodney Brooks (listed as Stanford), and Raj Reddy (Carnegie Mellon), alongside industry representatives. The Wednesday morning schedule identifies a classified Secret session. The document is stamped as a sanitized copy approved for release May 18, 2010.

Record identity: [CIA-RDP85-00142R000100030008-2](https://www.cia.gov/readingroom/docs/CIA-RDP85-00142R000100030008-2.pdf). Indexed text reviewed; page-image attempts redirected to the reading room. The named participants and classifications are reported from the extracted text, not independently authenticated scan images. This is an agenda/memorandum, not a transcript or proof of an undisclosed technical success. Speaker names are discovery keys for their published research, not evidence of personal knowledge of a secret AGI.

### Strategic Computing and Fifth Generation Computing (HC003–HC004)

The Japanese MITI/ICOT project (1982–1992) pursued knowledge-based computation using parallel inference architectures. The IPSJ Computer Museum records prototypes and approximately JPY 54 billion spent over eleven years. The US Strategic Computing Initiative (1983–1993) invested approximately USD 1 billion in additional research, according to Roland and Shiman's 2002 historical account. The latter identifies meaningful advances but reports that its overall machine-intelligence goal was not achieved. These are different national programmes; neither is evidence of the other programme's outcome.

Source pointers: [IPSJ history](https://museum.ipsj.or.jp/en/computer/other/0002.html), [MIT Press historical assessment](https://mitpress.mit.edu/9780262529266/strategic-computing/). Next read: original programme goals, contemporaneous evaluations, final programme reports, surviving implementation artifacts and termination rationale. Book full text not reviewed.

### DARPA biologically inspired cognitive architectures — FY2005 (HC010, HC033)

The WHS FOIA directory exposes annual DARPA funding lists for FY1996–2012 under request 12-F-1039. The retrieved FY2005 indexed table includes identifiable IPTO BICA obligations through the Air Force Research Laboratory, Office of Naval Research, Naval Surface Warfare Center and Army contracting agents. Seventeen rows in the accompanying extract connect contract identity to performer and amount. Examples:

| Contract | Performer | FY2005 obligation (USD) |
| --- | --- | ---: |
| FA865005C7253 | University of Michigan | 427,465 |
| FA865005C7254 | Carnegie Mellon University | 276,560 |
| FA865005C7255 | MIT Media Lab | 121,580 |
| FA87500520274 | Massachusetts Institute of Technology | 397,164 |
| FA87500520278 | George Mason University | 133,213 |
| FA87500520272 | University of Maryland | 174,213 |
| FA87500520273 | Rutgers University | 66,243 |
| N0001405C0510 | HRL Laboratories | 428,068 |
| FA87500620004 | Numenta, Inc. | 47,000 |

**Correction to earlier conversational summary:** the indexed table does not support the earlier mappings of $427,465 to Carnegie Mellon, $428,068 to Stanford, $397,164 to George Mason, $276,560 to MIT Media Lab, or $174,213 to Rutgers for these identified rows. Preserve the corrected associations above; do not silently treat the earlier mappings as verified. Stanford may have other awards; the present excerpt is not a full recipient audit. Exact annual totals, cumulative expenditures, contract deliverables and all-year coverage are unverified. The FY2005 PDF page-image fetch returned HTTP 403; retain E1 and do not assert visual authentication.

[Official FY2005 record](https://www.esd.whs.mil/Portals/54/Documents/FOID/Reading%20Room/Science_and_Technology/12-F-1039_2005-DARPA-Funding-List.pdf) · [FOIA index](https://www.esd.whs.mil/Records-Declass/FOIA/Reading-Room/Reading-Room-List_2/DARPA/).

The most useful connection is the ability to trace BICA funding from programme title to contract identifier to published investigator work and (if available) final deliverables. Do not infer a successful brain-like architecture from an award.

### CALO / PAL (HC008–HC009)

SRI's records describe CALO as part of a five-year DARPA effort beginning in 2003: a reported $150 million programme, 300+ researchers and 22 institutions. Objectives included adaptive reasoning and assistance. Its documented approach integrated multiple components supporting everyday information and task management. The relationship to the later Siri product demonstrates technological transfer, not an artificial organism or independent mind.

[Programme history](https://www.sri.com/hoi/artificial-intelligence-calo/) · [SRI retrospective](https://www.sri.com/75-years-of-innovation/75-years-of-innovation-calo-cognitive-assistant-that-learns-and-organizes/).

### Other government and multinational programmes

| Programme | Evidence and next question |
| --- | --- |
| DARPA Lifelong Learning Machines (HC023) | Official completed-programme page describes continual acquisition, retention, transfer and safety as goals. Find technical final reports and quantify retention under changed tasks; do not classify goals as verified outcomes. |
| DARPA Machine Common Sense (HC024) | Official completed-programme page distinguishes experiential developmental learning from knowledge acquisition from documents. Seek outcome papers and intervention tests. |
| EU IM-CLeVeR (HC014) | CORDIS grant 231722, 2009-01-01 through 2013-04-30, coordinated by CNR in Italy. EU contribution EUR 5,899,884. Its explicit cumulative skill acquisition and reuse objectives make it relevant prior art. Fact sheet is not final performance evidence. |
| IARPA MICrONS (HC025, HC031–HC032) | Official account reports cortical-network-informed pattern-recognition improvement. 2025 Nature records describe co-registered mouse visual cortex functional/connectomic data and analyses. The dataset and associated wiring paper are linked, not independent replicated results. |
| EU Human Brain Project (HC028, HC035) | Consortium closing statement reports EUR 607m over 2013–2023 with research outputs and EBRAINS infrastructure. A brain simulation infrastructure is not equivalent to an artificial mind. |

## 3. The highest-value new discovery: an existing large cognitive-architecture index

Kotseruba and Tsotsos published [40 years of cognitive architectures](https://doi.org/10.1007/s10462-018-9646-y) online July 28, 2018 (2020 journal issue). Their inclusion criteria selected 84 implemented architectures with publications and at least one practical use. Their review reports 900+ application projects and a bibliography of over 2,500 publications. The review is open access CC BY 4.0; the separate dataset's reuse terms must be checked independently. Counts refer to the authors' collection, not new records imported here.

[Upstream research data](https://github.com/ykotseruba/cog_arch_data) exposes tables for perception, vision, attention, action selection, memory, learning, applications, abilities, metacognition, architecture timelines, software references and bibliography. The repository README and listing were checked; individual spreadsheet rows have **not** been extracted or ingested. Retain this as a high-leverage, explicit acquisition frontier.

The 2010 survey [Goertzel et al.](https://doi.org/10.1016/j.neucom.2010.08.012) provides a complementary crosswalk. Its categories include symbolic systems (ACT-R), emergent approaches (DeSTIN), developmental robotics (IM-CLeVeR), and hybrids (LIDA, CLARION, 4D/RCS, DUAL, MicroPsi, OpenCog). This list is a survey-level index, not a verified current inventory of implementations. The survey explicitly leaves unresolved whether architecture-level brain emulation suffices.

For each architecture, recover original design papers, artifacts, learning mechanism, control rules, environment interface, state/memory provenance, externally supplied objectives, evaluation scope, comparisons, transfer limits, known failures, maintenance history and authors' stated limitations. Do not equate designed modules with spontaneously acquired function.

## 4. Mechanism crosswalk to Ora

| Comparator | What it contributes | Critical limit for Ora |
| --- | --- | --- |
| Varela, Maturana & Uribe, 1974 (HC001) | Self-producing organization as a distinct conceptual target. | A persistent pattern or self-copying genome is insufficient to establish self-maintaining organization or cognition. |
| Brooks, 1991 (HC005) | Embodied reactive behavior without requiring rich internal representations. | Behavioral success may admit simple reactive explanations; compare these before attributing a model or memory. |
| Avida, 2003–2004 (HC006–HC007) | Evolved complex computation and a mature digital-evolution instrument. | Existing Ora archive review already covers this prior art. No new original archive recovery here. Task-based selection, historical lineage uncertainty and the precise cost rules matter. |
| Bongard, Zykov & Lipson, 2006 (HC011) | Reported physical robot self-modeling and adaptation after damage. | Infer a causal model only through interventions and alternatives; self-modeling is not subjective self-awareness. |
| Oudeyer et al., 2007 (HC012–HC013); IM-CLeVeR (HC014) | Developmental exploration, learning-progress incentives, cumulative skill hypotheses. | Engineered intrinsic reward remains externally specified in origin. Do not equate it with viability-selected or emergent purpose. |
| Lehman & Stanley, 2011 (HC016) | Novelty-guided search as alternative to deceptive objectives. | Novelty descriptors/search criteria are still designed. Novelty without retained useful function is not cumulative cognition. |
| TrueNorth (HC017); Blue Brain (HC018); Hala Point (HC029–HC030) | Alternative computing substrates and biologically inspired reconstruction. | Hardware scale, cell count and physiological fidelity are not demonstrated intelligence. Same Hala Point event is corroborated by two organizations, not two experiments. |
| OEE workshop review (HC019); Soros (HC022) | Open-endedness criteria and observed stagnation alternatives. | Unbounded novelty is not established by finite traces; distinguish neutral drift, externally introduced novelty and retained functional gains. |
| XLand, 2021 (HC026) | Lab-reported generalization across held-out games under extensive interactive training. | Authored environments, goals and training curricula remain important scaffolds. Cross-task success within a family is not arbitrary generality. |
| Butlin et al., 2023 (HC027) | Theory-grounded computational indicators for evaluating possible machine consciousness. | Indicator satisfaction is not proof; a finite assessment of selected systems is not an exclusion theorem about undisclosed systems. |
| MICrONS, 2025 (HC031–HC032) | Empirical cortical data and measurable structure/function relationships. | A measured biological circuit or reconstruction is not by itself an autonomous artificial cognitive system. |

### What should change in the research strategy?

The documented comparisons strengthen an existing distinction in Ora's November 13 synthesis: substrate expressiveness, authored control, useful learned behavior, heritable innovation and retained cumulative function are separate scientific claims. Do not replace existing metabolic or ecological mechanisms with a cognitive architecture merely because a historical programme used one.

For the present research programme, preserve all earlier positive and negative evidence. Examine the **lowest-cost causal explanation** of any observed adaptive behavior. The scientific progression should be explicit:

1. Valid accounting and independently reconstructible histories.
2. Independently verified behavior beyond an equally resourced fixed/reactive control.
3. Evidence of learning or history dependence with appropriate ablations.
4. Evidence of heritable functional acquisition, distinct from inherited authored solutions or post-selection artifacts.
5. Retention and transfer across held-out conditions, including failed and incomplete outcomes.
6. Cumulative innovation only after function, lineage and transfer are demonstrated separately.
7. Separate, theory-dependent consciousness assessment if and when evidence warrants it.

This is a research interpretation ladder, **not** a new experiment design, permission to execute an evolving population or revised project policy. The current synthetic qualification and safety governance remain independent; no experimental settings, STOP state, director, grants, production assets or protected code are changed by this document.

## 5. Evidence collection roadmap and unresolved acquisition frontier

This is a finite first pass, not an exhaustive archive. The following are **unprocessed discovery queues**, not claims of completed collection.

| Priority | Source family / route | Required acquisition and closure |
| --- | --- | --- |
| P0 | [Cognitive architecture data](https://github.com/ykotseruba/cog_arch_data) | Pin upstream commit; establish data license; enumerate all ODS sheets and row counts; normalize architecture names and DOI/other identifiers; reconcile existing repository catalog; retain distinct aliases, missing records and disagreements. Review source papers only after deduplication. |
| P0 | [WHS DARPA FOIA archive](https://www.esd.whs.mil/Records-Declass/FOIA/Reading-Room/Reading-Room-List_2/DARPA/) | Acquire accessible 1996–2012 records with hashes and page references; crosscheck BICA, PAL/CALO, cognitive information processing and lifelong-learning awards; trace grant/contract IDs to actual published reports; retain non-matches and extraction errors. Do not treat annual obligations as total programme expenditures. |
| P0 | [CIA FOIA reading room](https://www.cia.gov/readingroom/) | Search for AI steering group, AI symposium, machine intelligence, cognitive systems and related research; retain origin, date, sender/recipient, document identity, classification markings, declassification date and redactions. Separate briefing, proposal, report, evaluation and transcript. No unauthorized access. |
| P1 | DARPA programme archives and [IARPA programme records](https://www.iarpa.gov/research-programs/microns) | Locate completed programme technical deliverables, peer-reviewed publications, contracts and actual task benchmarks. Verify dates against original records. |
| P1 | [CORDIS](https://cordis.europa.eu/project/id/231722), [EBRAINS](https://ebrains.eu/about/at-a-glance), Japanese ICOT/AIST archives | Trace developmental robotics, neural modelling, cognitive architecture and parallel logic projects; identify programme completion evidence and technical negative results. Expand to other countries as lawful records become available. |
| P1 | [NASA NTRS](https://ntrs.nasa.gov/) and other public technical-report repositories | Search public autonomy, artificial cognition, adaptive learning and self-modeling reports. Registered NTRS material is not included; never use unauthorized access. |
| P1 | Private-lab publications, patents and public code/data | Search IBM, SRI, Numenta, Intel, Sony CSL, DeepMind, neuroscience labs and historical corporate archives. Patents establish disclosure/claims, not performance. Cross-link patent family, priority date, assignee, technical papers, demonstrations and independent evaluations. |
| P1 | Existing ALife catalog | Reconcile Avida, Tierra, autopoiesis, open-ended evolution, artificial chemistry, ecological organization and cost-sensitive memory studies with the November 13 record and earlier research passes. Avoid reopening completed archive searches without a specific evidence gap. |
| P2 | Theories of cognition and consciousness | Compare operational indicators across models, review critiques and counterexamples, record disagreement rather than assuming one theory is correct. |

Additional discovery portals (not reviewed here): DTIC public catalogue, US National Archives, NSF award search, USAspending, EU grant records, national archival institutions, bibliographic databases (Crossref/OpenAlex), patents via USPTO/EPO/WIPO, and institutional repositories. Use exact record IDs, legal access routes and original source metadata.

### Acquisition integrity checklist

For each new record store original date, publication date, release/declassification date if distinct, issuer/author, public institutional recipients where applicable, identifier, canonical URL, retrieval time, access class, rights, checksum of lawfully stored bytes, extraction version, page/section, redactions, claim scope and independent evidence status. Unknown values remain null or explicitly UNKNOWN. A citation found in a secondary source is not automatically a checked primary source.

Deduplicate by DOI, archive identifier, patent family, grant/contract ID, upstream artifact identity and publication version. Map dependencies: a company's announcement and its recipient's announcement can corroborate delivery without providing two independent intelligence tests. A programme proposal must never be promoted as a completed experiment. Negative, abandoned and failed research should be indexed with the same diligence as successes.

Do not download or publish classified/restricted records, confidential correspondence, leaks of uncertain authorization, personal identifiers, trade secrets or copyrighted works outside applicable permission. Publicly released internal documents can be linked and summarized with provenance. The research repository is public.

### High-information next reading sequence (research only)

1. Read and reconcile the architecture dataset metadata and full cognitive-architecture survey; then triage the highest-value actual implementations for methods-level reading.
2. Reconstruct a verified BICA contract-to-output map for a bounded sample before expanding fiscal years. Retrieve original public award documents and final results where possible; record inaccessible or absent records as unknown.
3. Prioritize full-method comparator reviews of developmental cumulative learning, causal self-modeling, lifelong retention and reactive behavior. Map each positive claim to the cheapest alternative explanation and to the exact experimental intervention that distinguished it.
4. Cross-check against existing Ora research and negative results. Promote only genuinely new, traceable mechanisms or constraints; write a brief reviewer-facing discrepancy report and retain contrary evidence.

**Completion condition of this pass:** the initial source inventory, funding-row correction and research crosswalk are published in an isolated documentation branch. This does not certify every source or complete the larger collection. No new hypothesis about secret AI is elevated above UNKNOWN, and no scientific experiment is authorized.

## 6. Source audit notes

Search strategy: targeted public-source discovery across declassified AI records, funding and contracting, cognitive architecture surveys, artificial life, developmental robotics, continuous learning, neural hardware, brain simulations, interactive generalization and consciousness assessments. Access date 2026-11-24. Indexed abstracts, official records and public project/lab pages support the E1 records. The two analyzed government PDFs had unsuccessful screenshot retrieval; no PDF scan verification or downloaded-byte checks were accomplished.

Document IDs and stable DOI/URLs are retained in the source inventory rather than copying papers. Where the date of a programme page is not stated, the catalog distinguishes it from a dated reported event. No claim that this collection is exhaustive or that a classified achievement exists is made.

**Decision:** Continue prior-art research using the explicit acquisition queue; preserve existing scientific decisions and qualification gates. Review any proposed experimental change separately under existing authority.
