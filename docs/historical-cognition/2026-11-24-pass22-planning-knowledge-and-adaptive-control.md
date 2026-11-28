# Pass 22 — Planning knowledge, adaptive control and capability provenance

Date: 2026-11-24 (Halifax). Input HEAD `61e40fd478134417a080a150c7c9fda0268df1b5`. Preserved main `18f37bebca2f650aff8ab844ddb1ab9c8896158b`. [Draft PR #70](https://github.com/JeremyHennessy/AI-Research/pull/70).

## Custody and batch

Read current branch ref, PR metadata and file list, Pass 2, Pass 21, queue and all 19 scoped JSONL registers (including data/papers.jsonl; excluding queue). At input, PR open/draft/unmerged; base unchanged; 44 files added, no deletions; branch descends from Pass 2. Counted 66 existing architecture profile rows; zero contain the five selected pending IDs ARCH-063 through ARCH-067. Screened 439 records for literal case-insensitive substrings of seven new document titles; zero hits. This does not establish exhaustive identifier, fuzzy or prose deduplication. The [five structured profiles](../../data/historical-cognition/2026-11-24-pass22-architecture-profiles.jsonl) contain seven source identities at E1. No new bibliography disposition, E2 or E3.

## Primary findings

**PRODIGY**: Veloso et al., [1995 author-hosted paper](https://www.cs.cmu.edu/~jgc/publication/Integrating_Planning_Learning_PRODIGY_JETAI_1995.pdf), sections 2 and 4.1–4.4, printed p.26 (PDF index 27, visually verified). HAMLET trained on 400 simple generated logistics problems and acquired 17 search-control rules. On 500 generated test problems, the reported unsolved counts were 218 without learned rules and 135 with rules. Thus solved counts are 282 and 365, or 56.4% and 73.0%, a net 83 additional solved cases / 16.6 percentage points. Aggregate counts do not establish how many individual tasks changed outcome in either direction. For problems solved in both conditions the reported quality improvement count is 72; avoid mixing that denominator with 500. Runtime decreased but not significantly; the authors explicitly left rule-matching efficiency as a utility issue. The goal metric, operators and learning machinery were supplied, not evolved. QUALITY can learn from human-supplied alternatives or further search; its selected-result table is not a population-wide effect estimate. No full-method audit or reproduction performed.

**PRS**: Georgeff and Lansky, [1987](https://cdn.aaai.org/AAAI/1987/AAAI87-121.pdf), printed p.677 image and section 3 selected text: flexible plan revision, goal switching and inferred beliefs are possible using supplied procedure specifications. The [1989 follow-up](https://ijcai.org/proceedings/1989/156) describes resource-bounded reasoning; abstract only. Task prioritization is not autonomous origin of fundamental objectives.

**PolyScheme**: Cassimatis, [2006](https://doi.org/10.1609/aimag.v27i2.1879), publisher abstract, and Cassimatis et al., [2007](https://cdn.aaai.org/AAAI/2007/AAAI07-241.pdf), selected text and printed p.1525 visual check: supplied specialists jointly solve problems and update plans. Reuse of shared mechanisms in language and physical reasoning is different from experience-driven transfer of acquired competencies.

**Pogamut**: Gemrot et al., [AGS 2009](https://doi.org/10.1007/978-3-642-11198-3_1), publisher abstract. A virtual-agent research platform with extensions does not by itself establish autonomous learning or cognition. Chapter restricted at the publisher; no alternative full text acquired in this batch.

**R-CAST**: Fan and Yen, [July 2007](https://cdn.aaai.org/AAAI/2007/AAAI07-243.pdf), printed pp.1540–1541 visually checked. Reports better human-agent team performance in a simulated context-switching study with 30 participants; comparison also changes team composition. Some metrics in a separate study were not clearly improved. These are task-specific author-reported evaluations, not isolated evidence of a learned coordination mechanism.

## Institutional crosswalk

Four numbered acknowledgements visually confirmed: PRODIGY F33615-93-1-1330 (Wright Laboratory/USAF and ARPA); PRS N00014-85-C-0251 (ONR), NAS2-12521 (NASA Ames), FMC-147466 (FMC, private). R-CAST acknowledges an FY06 task under ARL Advanced Decision Architectures Collaborative Technology Alliance without a contract number. Additional unnumbered Spanish fellowships and System Development Foundation gift documented. PolyScheme includes AFRL author affiliation, not a funding award. Exact administrative awards, acceptance and final reports remain unverified; no new DARPA year or complete-year coverage. These public acknowledgements establish claimed funding relationships only.

## Ora comparison and next frontier

A useful acquired rule can increase success rate while still imposing matching costs. A resource-accounted evolutionary result would have to establish net benefit and causal inheritance rather than assume that successful search, belief revision, or teamwork proves the emergence of cognitive mechanisms. No new novelty claim or execution recommendation. Rights: metadata, original analysis and small factual derived counts only; no spreadsheet, source PDF or proprietary code redistributed.

Cumulative: 71/84 profiles, 13 pending; P0 21/21; 48/2,983 bibliography rows initially dispositioned (39 E1 new, 3 aliases, 6 unresolved E0; 2,935 untouched); five of 17 DARPA years partial, zero complete; two E2 audits, zero E3. Five new profiles, seven primary document pointers, zero scoped title matches, one publisher full-text restriction and two further abstract-only method gaps (PolyScheme 2006 and PRS 1989). The next architecture IDs are 068–072; bibliography row 50 remains the priority for a larger reconciliation batch. Closure not reached.

Research-only append. No Ora imports, execution, population changes, runtime, STOP/PARKED, grants, qualification, production, spending, outreach or merge.
