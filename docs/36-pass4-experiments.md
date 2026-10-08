# Pass 4 — experiment plans E23–E28
**2026-10-08** · Planning only. The repo's runnable Python tools are **deterministic/synthetic methodology fixtures**, not experiments showing an improved LLM. See [evaluation standards](06-evaluation.md) for task isolation, paired statistics, and cost matching.

## First, run the offline methodology checks
```bash
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
python experiments/calibration_metrics.py --bins 5
python experiments/ensemble_correlation.py --agents 5 --p 0.70 --rho 0.80 --override 0.15
```
The synthetic calibration fixture computes Brier score, log loss, classifier ECE, risk-versus-coverage and a **development-set-only** temperature selection. It does not use any model weights. The analytic group-voting fixture computes probabilities from explicit assumptions rather than simulating LLM behavior. **Neither output may be cited as empirical AI capability evidence.**

## E23 — probabilistic calibration and justified abstention
**Hypothesis:** separately calibrating evidence reliability and answer correctness reduces high-confidence factual errors at fixed answer coverage versus a model's self-reported confidence.

**Data:** synthetic contradictory source records with hidden binary ground truth, then licensed held-out real question-answer tasks. Source quality, evidence age and answer difficulty vary independently. **Comparators:** raw model confidence, held-out temperature scaling, multi-sample/ensemble disagreement, retrieval-source calibration, two-stage source+reasoning calibration. Match inference/verification time. **Primary:** Brier and risk at a prespecified 80% coverage; **secondary:** NLL, ECE sensitivity to bins, severe false-assertion rate, abstention rate, latency. **Falsifier:** apparent gains vanish under source shift or with an equal-cost baseline. **Current runnable code:** `experiments/calibration_metrics.py` validates only metric calculations.

## E24 — verified formal reasoning and subgoal search
**Hypothesis:** independently checked intermediate lemmas improve final proof success per total verification budget more than final-only proof checking.

**Prerequisite:** freeze permitted Lean version and mathlib SHA; no untrusted `sorry`, `admit`, nonallowed axioms or theorem changes. Independently recompile accepted proofs. **Comparators:** direct candidate generation, final-only Lean check, random fixed-depth decomposition, model-guided decomposition, interleaved check with repair. **Hidden data:** fresh theorem families and source-disjoint proof statements, with formalization reviewed separately. **Primary:** correct proof of the intended original theorem per total checker calls and wall clock; **secondary:** invalid acceptances, formalization error and sample cost. **Falsifier:** gains disappear after repairing verifier exploits. **Case study:** [DeepSeek-Prover-V2 full paper and corrections](30-deepseek-prover-v2-review.md).

## E25 — graph representation vs symbolic and language baselines
**Hypothesis:** appropriate relational inductive bias lowers data requirements for unseen graph compositions, while explicit graph solvers may still dominate exact tasks.

**Tasks:** reachability, typed path, changed node labels, edge direction, counterfactual edge removal, hidden graph-size and topology shifts. **Comparators:** deterministic exact graph solver; flat features/MLP; plain text LM; GCN/GAT/GIN; graph-to-LM. Keep graph/data supervision equal, freeze training/test generator seeds, and verify graph correctness independently. **Primary:** exact task success on unseen graph families per compute; **secondary:** label efficiency, OOD size transfer, inference latency and unreachable-case false positives. **Falsifier:** graph learning only memorizes labels or cannot improve on a strong symbolic baseline.

## E26 — audio-native vs transcript-cascade learning
**Hypothesis:** models that retain acoustic evidence outperform strong ASR→language cascades on tasks where prosody, timing, speaker shifts, and environmental sounds determine the answer.

**Tasks:** audio event classification, speech translation, overlapping speakers, acoustically disambiguated questions, clean and noisy ASR. **Comparators:** frozen ASR/text model; audio encoder+LM; end-to-end audio-language model with similar total training/serving budget when possible. **Split:** held-out microphones, people, recordings and languages; do not use voices without rights. **Primary:** correct grounded decision on audio-dependent tasks; **secondary:** WER, transcription hallucination during silence, worst-group accuracy, p95 streaming latency and compute. **Falsifier:** benefit disappears for matched ASR quality or costs overwhelm improvement.

## E27 — information-seeking agents and brain-inspired objectives
**Hypothesis:** active state-disambiguating probes improve future task completion more than reflexive novelty or reward-only exploration at equal environment interaction budget.

**Environment:** procedural 8×8 object/door/timer mechanics with partial observations and deterministic ground-truth transition logging. Withhold **combinations** of physical rules. **Comparators:** random exploration, greedy reward, novelty/curiosity, expected information gain, and information gain with duplicate-probe penalty. **Primary:** hidden task completion at fixed action budget; **secondary:** newly learned state transitions, uncertainty calibration, loops, redundant probes and wall-clock. **Falsifier:** more surprise measured but no improved transfer or reward. Do not equate biological analogy with demonstrated superior general intelligence.

## E28 — collaboration, error correlation and verifiers
**Hypothesis:** debate only improves objective correctness beyond best-of-N when participants bring genuinely independent information or tool capabilities and can avoid persuasive error propagation.

**Initial control:** one frozen model + candidate search at matched total tokens. **Variants:** independent repeated samples, heterogeneous agent/model samples, fixed-budget debate, role-specialist tools, evidence-only critique, consensus-free arbitration, incorrect but persuasive nonprivileged participant. **Primary:** objective correct hidden-task success vs total cost; **secondary:** correct-minority reversals, group-confidence miscalibration, answer correlation and tool/retrieval failures. **Falsifier:** debate gains disappear when equal-budget independent samples and verified tools are provided.

**Current runnable code:** `experiments/ensemble_correlation.py` illustrates the *mathematical* effect of shared failures on voting; not a trained multi-agent result.

## Every experiment requires a run contract
- Research question, independent variable, matched baselines, task family;
- Exact source model/data revision and rights; independent verifier / grader revision;
- Frozen hidden test generator hash, seed and implementation commit;
- Precommitted primary metric, uncertainty method, meaningful effect threshold;
- Output-level logs, resource cost (tokens, wall-clock, power if available), and risk events;
- Failure analysis including negative results; reproducible artifacts and reversion point;
- Clear label **proposed**, **executed**, **reproduced**, or **inconclusive**.

**Suggested order:** complete E01 true open-model baseline first. E23 can follow with frozen model output probabilities; E28 with frozen LLM agents; E24 requires a working trusted prover setup. E25/E26/E27 need appropriate data/simulators before making strong claims.
