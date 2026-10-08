# Future ALife study protocol: detect what *causes* survival and novelty

**Research design only.** This is a preregistration and interpretation guide, not a simulator, new evolutionary rule or autonomous agent.

## 1. Avoid one monolithic score
For each independently tested substrate, produce *separate* verdicts:

| Claimed property | Minimal positive observation | Required negative control | Explicit failure label |
|---|---|---|---|
| Self-maintenance | Structural process turns over constituents and restores function after damage | Remove internal regeneration link; compare engine-reset pattern | STATIC_STABILITY_ONLY / ENGINE_REPAIR |
| Energy/resource regulation | Resource uptake, use and waste causally determine persistence | Remove inflow vs fake energy counter; match initial stores | RESOURCE_COUNTER_DECORATIVE |
| Reproduction | Distinct viable descendant forms through local operation | Engine copy/respawn disabled, parent assignments shuffled | DUPLICATION_BY_ENGINE |
| Inheritance | Descendant functional trait depends on parent organization | Environmental baseline, shuffled lineage, fixed genotype | RESEMBLANCE_NOT_INHERITANCE |
| Adaptation | Perturbation-specific compensatory change improves viability | Cue shuffle and behavior freeze, equal resources | SCRIPTED_REFLEX_ONLY |
| Ecological novelty | New stable resource/interaction affordance persists in lineage | Neutral selection, shuffled interaction network | DRIFT_OR_VISUAL_ONLY |
| Lifetime learning | A *single individual's* later behavior improves from experience | Reset state, history shuffle, non-plastic counterfactual | EVOLUTION_NOT_LEARNING |
| Open-ended hallmarks | Continued **independent** functional innovation across preregistered windows | Size/time-matched null, function-holdout transfer, no novelty scorer | NONFUNCTIONAL_OEE_METRIC |

An "alive" or "intelligent" score is intentionally not defined; evidence must be interpreted at the level it directly tests.

## 2. Factorial study of organizer versus environment
**Variables recorded as design constraints, not instructions to build:**
- Externally scheduled source of new resource; total input mass and control signal time;
- Spatial dimensionality/grid topology and boundary conditions;
- Local update law, allowed reaction templates and conservation;
- Resource/energy cost for state and action, degradation/decay rules;
- Protected memory and built-in reproduction API;
- Mutation distribution, whether heritable, timing and scope;
- Outer loop / image metric / foundation-model evaluator / novelty archive;
- Initial seed (random soup vs **viable organism intentionally supplied**).

**Core matrix:** controls differing along one relevant axis at equal total resource and compute. Precommit null expectations, then estimate world-level uncertainty (not thousands of correlated individual frames).

## 3. The source-specific null that researchers tend to forget
**Artificial chemistry:** distinguish reaction topology being "self-driven" from actual **molecular overproduction**; distinguish exponential replication with unlimited replenishment from genuine self-maintained compartment.

**Digital instruction ecology:** remove artificial rewards for logic functions; check viable descendants and new capabilities from *ecological* selection. Compare when CPU/memory protection is weakened while avoiding catastrophic interpreter bugs.

**Flow-Lenia:** probe passive mass conservation vs active repair, track *parameter-map* `P` across splits, and measure whether new functional interaction strategies are inherited.

**Neural cellular automata:** evaluate across unseen damage and body targets, and ablate pretrained target-image/visual novelty objectives. Visual diversity is not a surrogate for inherited function.

**Open-ended-evolution metrics:** inspect raw distributions: total accumulated activity, normalized cumulative activity, **new activity**, novel function and time-window slopes. This directly guards against the ToLSim 2026 partial failure pattern.

## 4. Preregistered lineage audits
A descendant should be identified by **observable causality**:
- Parent formation that contributes parts, programs, reaction components, or dynamically transcribed local parameters;
- A continuing daughter distinct from parent after separation;
- Demonstrable inherited information under controlled removal/shuffling;
- Functional phenotype repeatable over more than one descendant and environment.

Splitting a fluid wave into two visually similar pieces is not enough. In a spatial model, arbitrary component tracking may fragment a continuous material lineage; report ambiguity and validate against multiple segmentation thresholds.

## 5. Reasonable result categories
- **SUPPORTED_AT_THIS_HORIZON:** predeclared hypothesis met on tests and independent null controls at horizon H, with uncertainty and cost.
- **INCONCLUSIVE:** effect sign/size uncertain or tests inadequate.
- **REFUTED_UNDER_TESTED_CONDITIONS:** null controls match/exceed variant or mechanism knockout does not affect outcome.
- **INVALID_EVALUATION:** violated sampling, resource accounting, model provenance or measurement assumptions.
- **UNREPLICATED_PUBLICATION:** result reported by source but not reproduced by our experimental project.

These tags are future reporting vocabulary only. None is applied to an organism in this research repository.

## 6. Cross-substrate fairness
Equal GPU-seconds does not imply equivalent accessible phenotype complexity; equal cell count does not imply equal computational expressivity. Compare:
1. **Within-substrate** causal ablations first.
2. Across substrates, matched **wall-clock/resource** and common independent function tests when meaningful.
3. Statistical sensitivity to world size, seed, perturbation severity and hidden rules.
4. A Pareto map of evidence-supported capabilities and cost; **not** a ranking of life status.

No actual research world has been run, and no approval to do so exists. Revisit [evaluation framework](05-evaluation-framework.md), [hypotheses](06-hypotheses-and-open-questions.md), [future plan](07-experimental-roadmap.md) and [counterexamples](09-counterevidence.md) before creating a future separate project.
