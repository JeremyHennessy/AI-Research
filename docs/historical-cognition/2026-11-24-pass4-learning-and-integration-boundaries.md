# Historical cognition research — Pass 4: learning, attention and the limits of integrated architectures

**Date:** 2026-11-24  
**Input checkpoint:** `8c6d95bf98fe3365d9cae264b335919a67329b0e`  
**Profile commit:** `3f74ead020824f8b5b4712cc79c7fd1f920854d4`  
**Review:** [draft PR #70](https://github.com/JeremyHennessy/AI-Research/pull/70)  
**Mode:** research only.

## Coverage and reconciliation

The current draft and its main base were checked before writing. The base remains the original `18f37bebca2f650aff8ab844ddb1ab9c8896158b`. Pass 2 and Pass 3 reports were read. The seven selected IDs were checked against the pinned queue and previous nine-profile batch. This pass covers ARCH-011, 029, 041, 047, 048, 058, 078 only; no overlap with Pass 3.

[Structured profiles](../../data/historical-cognition/2026-11-24-pass4-architecture-profiles.jsonl) contain seven initial E1 dispositions and eleven distinct source identifiers. Exact DOI and dissertation title/path searches across the 269-record canonical catalog, 35-source and 12-source registers, nine-profile file, and three existing historical reports found no exact matches. This is a limited duplicate screen; title variants and other research notes have not been exhaustively reconciled. Eleven new pointers within the screened records, zero known exact duplicates, zero completely blocked architecture profiles. No raw article content or upstream tables reproduced. The DAC III record was available in indexed NLM metadata but not on the subsequent direct page. The original NARS thesis and the Spaun correction/supplement are unreviewed leads. No E2 or E3 promotion.

**16 of 84 architecture profiles now have initial dispositions; 68 remain.** All 2,983 bibliography rows still await row-specific dispositions. Archive FY coverage is unchanged.

## Principal comparative evidence

| ID | Architecture | Verified source boundary | What this contributes |
|---|---|---|---|
| 011 | ART | Carpenter and Grossberg 1987, author abstract | A defined approach to incremental category formation and retention. |
| 029 | DAC | Verschure 2003, publisher abstract; 1998 DAC III metadata | Author-reported controlled comparison in real and simulated foraging robots. |
| 041 | HTM | Hawkins/Ahmad and Cui et al. 2016, abstracts | Online sequence learning with comparable predictive accuracy to other methods; not universally superior. |
| 047 | Leabra | O'Reilly 1996 dissertation title/abstract and related 1996/2006 abstracts | Associative and error-driven learning and related learned working-memory gating. |
| 048 | LIDA | Franklin et al. 2014 author manuscript, selected sections | Separates implemented cognitive behavior from intended architecture. |
| 058 | NARS | Johansson 2024 publisher article, selected methods/results | Reported adaptation to explicit changes in feedback and retention in no-feedback test blocks. |
| 078 | SPA | Eliasmith et al. 2012 first article page, selected results/limitations | Demonstrates that broad predefined task execution is distinct from developing entirely new tasks. |

### 1. LIDA: a useful caution against architecture diagrams as evidence

[Franklin, Madl, D'Mello and Snaider (2014)](https://doi.org/10.1109/TAMD.2013.2277589), [author manuscript](https://ccrg.cs.memphis.edu/assets/papers/2013/franklin-ieee-tamd11.pdf), explicitly separates the conceptual architecture from its computational realization. Selected agents reproduce reaction-time and attention effects, including the attentional blink. Sections V–VII discuss components not fully realized; section XI distinguishes the episodic learning implementation from procedural learning in a predecessor and notes that neither had yet been validated against human data. A selected perceptual task used authored nodes and schemes. The article does not equate functional access to information with subjective experience.

These are limitations of the 2014 paper's implementation, not a claim about all later LIDA versions. The paper's first page acknowledges five support identifiers (four for Sidney D'Mello, one for Tamas Madl). The profile records the exact attribution. Acknowledgements are evidence of author support; they are not acceptance certificates or evidence of funding for every architectural module.

### 2. NARS: separate a changed behavior from its supplied problem

[Johansson, August 14, 2024](https://doi.org/10.3389/frobt.2024.1440631), sections 7–8, reports three controlled learning tasks. In simple and conditional discrimination, the author reports 36 correct choices out of 36 in the respective feedback-free test phases. A reversal task measures adaptation after a change in the rewarded action. Inference operates over explicitly encoded temporal statements, with two supplied actions, an assigned goal, and feedback during training. Declarative inference is disabled in this particular configuration.

This is evidence of reported learning within the task, not spontaneous symbol grounding or general reasoning. The design illustrates why training exposure, test feedback, pre-existing representation and task constraints must be separately documented. It is not evidence for the origin of an autonomous goal. No software acquired or executed.

### 3. SPA: a large simulation with a documented developmental boundary

[Eliasmith et al., November 30, 2012](https://doi.org/10.1126/science.1225266) describes Spaun, using 2.5 million simulated neurons to carry out eight assigned task classes through a common model. It demonstrates limited learning in its reinforcement task, but its discussion expressly identifies inability to acquire wholly new task types and restricted inputs and representations. The model's eye and attentional orientation are fixed. This distinction survives the impressive scale of the system. The publicly accessible copy notes a subsequent correction; correction text and supplementary methods were not examined. Findings remain E1 and provisional at that boundary.

### 4. Mechanism-specific evidence, not a unified success claim

[ART 2 (1987)](https://doi.org/10.1364/AO.26.004919) offers a defined category learning framework. [HTM (2016)](https://doi.org/10.1162/neco_a_00893) reports comparable streaming prediction against established alternatives and properties useful for continuous temporal learning. [Leabra's 1996 dissertation](https://ccnlab.org/papers/OReilly96phd.pdf) and [related 2006 working-memory model](https://doi.org/10.1162/089976606775093909) illustrate local learning and learned control over working memory. [DAC (2003)](https://doi.org/10.1207/s15516709cog2704_1) reports controlled task-specific improvement. None of the reviewed evidence demonstrates self-originating intelligence merely by combining these mechanisms.

## Interpretation for Ora (research only)

The central constraint is to keep observed performance, its acquisition history, and the source of its objectives separate. An artifact can be capable of several tasks because the designer supplied the relevant architecture or problem decomposition, even if some internal parameters change with experience. A learned representation is not identical to a learned goal; matching human behavior does not by itself demonstrate human-like development. This is a literature interpretation, not a newly validated Ora capability or a recommendation to alter the experimental substrate.

No candidate was imported or executed. The local runtime was not inspected. Nothing changes scientific STOP, director PARKED, qualification or release authority.

## Next bounded frontier

Architecture queue: remaining P0 entries include MACSi, MIDCA, Kismet, CogPrime, Copycat/Metacat. Separately continue the bibliography-row reconciliation and the fiscal-year archive coverage in future bounded passes. Retain source locators, access limits, negative evidence and exact duplicate diagnostics. The prior INSIGHT deliverable backlog remains open. No completion claim.
