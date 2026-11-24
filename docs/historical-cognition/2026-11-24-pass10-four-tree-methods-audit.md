# Pass 10 — Darwinian neurodynamics: independent paper-level methods audit

Date: 2026-11-24. Input: `a5bcd74b2e06c145edd13d3fa56d36635fdfe979`. Baseline: `18f37bebca2f650aff8ab844ddb1ab9c8896158b`. Research-only, draft PR [#70](https://github.com/JeremyHennessy/AI-Research/pull/70). Pass 2 and Pass 9 read; branch and PR verified open, draft, unmerged, all 23 previous files additive. This bounded batch advances the critical methods workstream, not the contiguous bibliography queue.

## Evidence register

- **E2, paper-level full methods/results review (not implementation audit or reproduction):** Anna Fedor, István Zachar, András Szilágyi, Michael Öllinger, Harold P. de Vladar, Eörs Szathmáry. *Cognitive Architecture with Evolutionary Dynamics Solves Insight Problem*. Frontiers in Psychology 8:427, published 2017-03-29; DOI [10.3389/fpsyg.2017.00427](https://doi.org/10.3389/fpsyg.2017.00427), PMID 28405191, PMCID PMC5370243. [Publisher HTML](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00427/full), [publisher PDF](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00427/pdf). Methods and all three experiments, analysis and conclusions reviewed in publisher text; printed pp.4–6,8–11 visually inspected. CC BY confirmed by publisher. Only original analysis and bibliographic/factual metadata retained. Exact acknowledgments: EU INSIGHT 308943 and ERC EvoEvo 294332. This is another output from the same grant/research lineage as Pass 3, not independent replication.
- **E1 comparator:** Trina C. Kershaw, Christopher K. Flynn, Leamarie T. Gordon. *Multiple paths to transfer and constraint relaxation in insight problem solving*, Thinking & Reasoning 19(1), 96–136, online 2012-11-27, issue 2013. DOI [10.1080/13546783.2012.742852](https://doi.org/10.1080/13546783.2012.742852). Publisher abstract and metadata accessed; no full methods or rights audit. Human experiment uses instruction/analogy training; do not infer individual trial results or verify personal-communication counts from this abstract.
- **E0 implementation-access gap:** [OSF vjfv9](https://osf.io/vjfv9/), code, parameters and analysis scripts cited by Fedor et al., returned HTTP 403 on this access route. PMC article route also returned a browser challenge; lawful publisher HTML/PDF sufficed for paper review. No attempt to circumvent either. Code, exact initial conditions and raw paired outcome data not inspected.

Duplicate screen: 269 canonical paper records and all nine historical JSONL registers/profile files existing at input (101 top-level historical records) checked for exact DOI or complete title (case-insensitive substring). Neither paper matched. This is a limited screen, not all repository notes or fuzzy aliases. Two new publication pointers, one newly E2-reviewed paper, one E1 comparator, one unresolved implementation pointer; zero E3. No new architecture or bibliography-row dispositions. No external outreach.

## What is established and what is not

The published simulation finds a position for one missing tree given three fixed positions. Its numerical encoding already represents all three spatial dimensions, and the evaluation rule already defines successful geometry. The authors compare different pretraining and priming conditions and parameter interventions. The model is a limited example of candidate search, not a demonstration of acquiring a previously nonexistent representational dimension or an underlying goal. No actual neuronal process or autonomous organism was observed. The reported human comparison uses a different task formulation and a control-derived timing alignment, not a validated conversion between simulation generations and human minutes.

The following table records the author-reported solver counts (30 simulations per condition), not newly executed experiments. See printed pp.9–13.

| Contrast | Early count | Count at 200 generations |
|---|---:|---:|
| Experiment 1 control | 1 | 28 |
| Experiment 1 combined training/priming | 22 | 29 |
| Experiment 2 2D training, derived 2D initialization (2DD) | 2 | 25 |
| Experiment 2 2D training, random 3D initialization (2DR) | 26 | 29 |
| Experiment 2 3D training, derived 2D initialization (3DD) | 17 | 26 |
| Experiment 2 3D training, random 3D initialization (3DR) | 11 | 23 |

Early cutoffs are generation 33 for experiment 1 and 35 for experiment 2, chosen using the observed controls. They are not independently prespecified evaluation horizons. Experiment 2's reported final omnibus comparison was nonsignificant (p=.1618, under its published test). Descriptive evidence supports a speed difference more clearly than a new end-state capability; nonsignificance is not proof of equal performance.

## Independent arithmetic and methods checks

All checks below were calculations on published aggregate facts, not execution of the original research software or any Ora candidate.

**A. The target representation is already complete.** Using the paper's three integer coordinates (15,10,0), (15,90,0), (84,50,0), the 0–100 inclusive coordinate grid, and its rounded-distance criterion, I enumerated all 101^3 = 1,030,301 possible integer positions. For every candidate and each fixed tree, the test was 79.5^2 <= squared Euclidean distance < 80.5^2. Exactly one point passed all three tests: (38,50,65), as expected from the article. No floating rounding ambiguity at half integers can arise for these integer squared distances. This independently checks the numerical task definition only. Every candidate is already expressible in the authored coordinate map, so transition to a nonzero third coordinate is an expansion of the explored subset rather than creation of a new dimension. The target space is finite, and this enumeration is not a cost-matched performance benchmark or replication of the agent.

**B. Paired-design sensitivity.** The authors explicitly describe shared random seeds across conditions and treat time outcomes as repeated measures (p.9). Their solver-count comparisons use ordinary chi-square contingency tests. If the seed-level outcomes are genuinely paired, a paired binary-outcome analysis is appropriate. Raw seed-level pairings were not retrieved. For two marginal success counts a,b in 30 paired runs, the number t of joint successes lies in [max(0,a+b-30),min(a,b)]. For every integer t in that range I calculated the exact two-sided McNemar p-value by the binomial tail on discordant outcomes (a-t,b-t). These are attainable marginal bounds, not reconstructed individual outcomes.

| Published contrast | Exact paired p-value interval |
|---|---:|
| Experiment 1 early, 1 vs 22 | 9.5367e-7 to 5.7221e-6 |
| Experiment 2 early, 2 vs 26 | 1.1921e-7 to 3.0324e-6 |
| Experiment 2 early, 11 vs 26 | 6.1035e-5 to .0025995 |
| Experiment 2 early, 2 vs 17 | 6.1035e-5 to .00072861 |
| Experiment 3 final, 26 vs 2 | 1.1921e-7 to 3.0324e-6 |
| Experiment 3 final, 26 vs 17 | .00390625 to .04904175 |
| Experiment 3 final, 26 vs 25 | 1 to 1 |

The large early differences remain below .00833 under all feasible pairings in the displayed experiment 2 contrasts, conditional on the chosen cutoff. This does not correct outcome-dependent cutoff selection, confirm actual pairing, or validate the global test. The smaller experiment 3 memory contrast is sensitive to multiplicity and pairing. That intervention also changes population size, hence evaluations per generation and total resources; attributing the effect solely to memory capacity is not isolated.

**C. Confirmed reporting discrepancy.** On printed p.11 (also in publisher HTML), the Friedman statistic for selection-phase duration is 8.883 with printed p=.309, yet the text describes significance. For four conditions, the standard asymptotic chi-square(3) survival probability at 8.883 is approximately .0308877 (computed from the half-integer gamma survival formula). The printed p and significance wording conflict; a decimal typo is plausible, not established. Raw ranks and the original analysis script are needed to resolve the exact test. Do not silently correct the paper or treat the proposed mechanism as statistically isolated.

**D. Switching-law boundary.** Printed p.6 specifies a probability involving the reciprocal of the count of previous repetitions, which is undefined when that count is zero under the literal equation. A convention such as an offset or special case may exist in code, but the inaccessible implementation prevents confirmation. The mode transition is explicitly authored and one-way. The study's surprise result cannot by itself establish discovered metacognition. The repetition-to-switch relationship is partly imposed by construction, rather than an independent finding about human minds.

## Interpretation and falsification boundary

The strongest retained finding is narrower than a claim of independent cognition: in one engineered problem, altering initial bias and search dynamics changes the rate at which a known evaluation criterion is met. The evidence is consistent with memory/search interactions and does not discriminate uniquely among all optimization mechanisms.

For interpretation of existing Ora evidence, separate availability of an authored action/representation, transient exploration, retained acquired information, and genuinely new function. Also keep efficiency and eventual success separate. Pass 8's GILA result is an independent historical example of an efficiency-versus-quality distinction; the Fedor study is not a replication of GILA. This audit proposes no Ora implementation, experiment, parameter change, or authorization; it identifies interpretive controls and missing evidence only. No Ora local state accessed; STOP/PARKED and all approved boundaries remain untouched by this work.

## Remaining work

31/84 initial architecture profiles (21/21 priority), 14/2,983 bibliography rows initially dispositioned (four unresolved; 2,969 not yet investigated), four of 17 fiscal years partially examined, zero fully validated annual audits. One new E2 paper-level methods review in this pass, zero E3. The original 2,983-row corpus reconciliation and comprehensive closure remain open. Next bounded batch: CAPS bibliography from row 16, or retrieve INSIGHT deliverables through a distinct lawful public route; avoid repeating the OSF/PMC failure route without new evidence.
