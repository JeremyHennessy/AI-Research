# Pass 20 — MDB full-method review: evolutionary search, memory confounds and paid heredity

Date: 2026-11-24. Input HEAD `e20122718f5cea25001a428999aa83c913d526f7`. Baseline `18f37bebca2f650aff8ab844ddb1ab9c8896158b`. [Draft PR #70](https://github.com/JeremyHennessy/AI-Research/pull/70).

## Custody and bounded scope

Read Pass 2, Pass 19, ARCH-052 from Pass 18, branch and PR; main remains original baseline, compare shows 41 added files and no other changes. One new methodological review of an existing E1 publication, not a new architecture or bibliography disposition. Source identity duplicate intentionally reconciled to ARCH-052 (one existing DOI, zero new publication identities, one E2 text-level audit, zero E3). No other batch repeated.

Primary source: Francisco Bellas, Richard J. Duro, Andrés Faiña and Daniel Souto, University of Coruña, *Multilevel Darwinist Brain (MDB): Artificial Evolution in a Cognitive Architecture for Real Robots*, IEEE Transactions on Autonomous Mental Development 2(4), 340–354; received 2010-03-01, accepted 2010-09-30, published 2010-10-14, December 2010 issue. [DOI](https://doi.org/10.1109/TAMD.2010.2086453); [institutionally hosted indexed publisher text](https://www.ece.uvic.ca/~bctill/papers/ememcog/Bellas_etal_2010.pdf). Indexed full article text reviewed across sections I–V (pp.340–353); references p.354 checked for provenance. PDF page image requests for pp.340,348,352,353 returned 404; image/curve values not independently digitized. E2 is scoped to textual methods and reported outcomes, not visual authentication, executable reconstruction or replication. IEEE copyright, no article or figures redistributed. Funding acknowledgement p.340: Xunta de Galicia 09DPI012166PR and European Regional Development Funds; already recorded, no award-level uplift. Authors' institutional affiliation is public; legal recipient, award dates, amounts, acceptance and final reports not established. No original experiment code, random seeds, per-run histories or raw numerical results acquired in this batch.

## Textual method observations (author-reported)

| Locator | Observations |
| --- | --- |
| III A–C, pp.344–348 | Concurrent model and controller optimization; populations persist across interactions; authored sample retention, context detection and model reseeding. Deliberation can run on separate processors. |
| IV A, pp.348–350 | Gait search varied six phases with other motion parameters fixed; human resets; 300 iterations; 7-4-4-1 predictor, 700 candidates, controller 120 candidates, FIFO window 40; no LTM or internal sensing. Turning uses previous gait and a changed model/action specification. |
| IV B, pp.350–353 | Two platforms; seven predefined commands/actions, teacher feedback, supplied perception encodings, STM 10. About 20 iterations to follow commands. Pioneer 2 switches mapping at 70 and back at 160; reward reversal is a separate example. Error is measured against current STM. |
| V, p.353 | Social operation, internal modeling, endogenous motivation changes and higher-order memory generalization remain future work. |

## Independent analytic checks (not E3)

1. **Representation consistency.** A fully connected 7-4-4-1 network with biases has 7*4 + 4*4 + 4*1 = 48 weights and 4+4+1 = 9 biases, totaling 57 adjustable values, consistent with the stated genotype. This is a check of the representation, not of its training.
2. **Units of learning.** At the stated 24 seconds per gait action, 300 complete action intervals would nominally total 7,200 seconds (two hours), excluding resets and computation. This is conditional arithmetic, not measured elapsed time; no exact per-iteration timing log was obtained. The number of internal genetic generations is not the number of physical trials, and candidate population sizes alone do not identify total compute.
3. **Window confound.** In an initially full ten-item FIFO buffer, after k new insertions with one replacement per insertion, max(10-k,0) old items remain. Thus after ten new samples, zero old items remain. A decrease in current-buffer error following this purge can arise even without long-term recall, because the evaluation set has changed. The paper reports an error rise stopping after approximately ten interactions on the first language switch. That timing is consistent with buffer turnover, not unique evidence for LTM. On the return to the old language, faster adaptation is consistent with LTM reseeding, but also with persistent optimizer state, easier mapping or unequal experience. The textual report does not establish a matched ablation distinguishing these. This is a counterexplanation, not proof of LTM ineffectiveness.
4. **Task fidelity versus cognitive origin.** The gait is a learned parameter combination within supplied motor dynamics; learned semantic association in the command experiment occurs within an already enumerated action/command space. Neither proves invention of the representation, optimizer, goals or motor apparatus. The experiment with reversed reward is evidence of adaptation to an externally changed evaluation, not an internally generated objective.
5. **Fitness versus evaluation.** In-buffer prediction error and an external behavior efficiency metric answer different questions. A lower rolling prediction error is not a held-out generalization guarantee; physical behavior examples are positive evidence but not population-level statistical replication. No inference about uncertainty across independent initializations or long-horizon performance without interventions is made.

## Prior-art crosswalk to Ora (read-only, conceptual controls, no experiment authorization)

Pinned baseline records: [endogenous-learning decision, 2026-10-23](../artificial-life/ORA-ENDOGENOUS-LEARNING-EVOLUTION-DECISION-20261023.md) and [evolutionary-substrate evidence, 2026-11-13](../artificial-life/144-ora-evolutionary-substrates-evidence-20261113.md). These documents distinguish authored learning, resource economics and paid transmission; the November report explicitly labels local evidence owner-reported rather than remotely replicated. No claim about the current private runtime is made here.

| Question | MDB comparator | Existing Ora evidence boundary | Logical discriminator for eventual interpretation (not a run request) |
| --- | --- | --- | --- |
| Is knowledge acquired? | In-life prediction and action learning under designed objectives | October Learning81 cue acquisition; supplied learner and cost disadvantage | Distinguish novel information from supplied machinery |
| Is recall the cause? | Context recovery and archived model seeding | Context90 own-history retrieval, no full paid energy advantage | Separate stored-model access from rolling-window turnover and persistent optimizer state; matched observation history |
| Is learning economically beneficial? | External concurrent computation; no self-funded reproduction | November report records compact copier/guesser advantage over long authored memory | Require full resource and opportunity-cost comparison, not solely task accuracy |
| Is cognition heritable? | Model populations within one robot | Paid copying/inherited variation reported, natural useful functional accumulation not established in pinned reports | Distinguish actor inheritance from persistence of an external model archive |
| Are goals endogenous? | Externally supplied or changed satisfaction | Authored benchmark merits explicitly distinguished from spontaneous objectives | Trace causal origin of objective and selection criterion |

Strongest counterevidence to broad novelty: evolutionary predictive learning, behavior adaptation and reuse of archived models were already documented in physical robots by 2010. Strongest open distinction: whether organism-native variation can yield a useful information strategy that remains beneficial after its full execution, memory and reproduction costs and transmits through viable descendants. The distinct question is not a world-first claim; the pinned Ora documents already identify Avida and other evolutionary learning precedents.

## Counts and next frontier

Cumulative 61/84 architecture profiles (23 pending), 48/2,983 bibliography initial dispositions (39 new E1, 3 aliases, 6 E0; 2,935 untouched), five of 17 fiscal years partly examined (zero complete), two E2 methods audits including this text-only review, zero E3 experiments. One blocked image-access route (four page requests in one batch); no repeat retrieval needed until a lawful alternate source is found. Next bibliography row 50 (Anderson1996a); prioritize larger metadata reconciliation batches and unresolved government-year coverage. Closure not reached.

Research-only append. No Ora code import, execution, population changes, grants, runtime, STOP/PARKED, qualification, production, spending, outreach or merge.
