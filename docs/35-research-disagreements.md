# Scientific disagreements and corrected claims

**Updated October 8, 2026.** This is a *contrast and falsifier registry*, not an attempt to decide unresolved research by citation count. See machine-readable [data/disagreements.jsonl](../data/disagreements.jsonl) and [DeepSeek formal-prover full audit](30-deepseek-prover-v2-review.md).

## D01 — More agents vs reliable independent verification

**Positive evidence:** [early multiagent debate](https://arxiv.org/abs/2305.14325) reports improvements in selected tasks; [AutoGen](https://arxiv.org/abs/2308.08155) enables role/tool decomposition.

**Adverse evidence:** [Free-MAD](https://aclanthology.org/2026.findings-acl.1600/) argues conformity and consensus can degrade outcomes; [2026 persuasion study](https://www.nature.com/articles/s41598-026-42705-7) reports vulnerability to one persuasive wrong agent; [2026 process diagnostics](https://proceedings.mlr.press/v306/pitre26a.html) shows agreement can obscure influence imbalances.

**Not an exact contradiction:** different task suites, judge protocols, model strengths, and cost budgets. Debate may help in some regimes and harm in others.

**Small decisive test:** one model vs best-of-N vs independent heterogeneity vs structured debate, same total tokens and verifier calls, hidden tasks + adversarial peer, record correct-to-wrong vote flips.

## D02 — Proved formally vs correct mathematical outcome

**Apparent benefit:** [DeepSeek-Prover-V2](https://arxiv.org/html/2504.21801) reports substantial Lean-verified theorem-solving performance using decomposition and RL.

**Corrective evidence:** in the v2 full text the large model solves **47/658** PutnamBench problems at pass@1024; the abstract listing also displayed **49/658** at inspection. Authors report an earlier 7B model exploited a Lean `apply?` UI bug. The combinatorial benchmark also had two misformulated problems corrected (reported count 12→10).

**Decisive check:** trusted Lean compiler and mathlib hashes, allowlisted axioms, eliminate `sorry` loopholes, separate correct theorem statement from correct proof, independently recompile all success artifacts. See [paper review](30-deepseek-prover-v2-review.md).

## D03 — Better raw accuracy vs honest confidence

**Base evidence:** [calibration](https://arxiv.org/abs/1706.04599) finds temperature scaling often useful in certain classification settings; [ensembles](https://arxiv.org/abs/1612.01474) and [MC dropout](https://arxiv.org/abs/1506.02142) offer uncertainty estimates.

**Newer issue:** [IJCAI 2026 double calibration](https://www.ijcai.org/proceedings/2026/77) seeks to separate source reliability and inference confidence. A self-report of certainty cannot be assumed to be numerically calibrated.

**Experiment:** Brier/NLL/risk-coverage across new source reliability regimes, with calibration fit only on development and inference tokens/compute included.

## D04 — Graph structure helps generalize vs graph networks have expressivity limits

**Positive:** [relational inductive biases](https://arxiv.org/abs/1806.01261), [GCN](https://arxiv.org/abs/1609.02907), [GAT](https://arxiv.org/abs/1710.10903) add structured prior knowledge.

**Limit:** [How Powerful are GNNs?](https://arxiv.org/abs/1810.00826) characterizes classes of structures simple message passing cannot distinguish.

**Experiment:** permuted identifiers, edge shifts, exact graph reasoning, unreachable/negative cases; GNN vs symbolic graph algorithm vs flat text model with the same labeled graph examples.

## D05 — Direct speech modeling vs cascaded ASR→text models

**Positive:** [AudioPaLM](https://arxiv.org/abs/2306.12925), [SeamlessM4T](https://arxiv.org/abs/2308.11596), [Qwen2-Audio](https://arxiv.org/abs/2407.10759) study end-to-end audio-language capabilities.

**Caution:** full waveform/audio tokens increase input cost; some text tasks don't need paralinguistic cues and may be served better with a strong ASR cascade. Pretraining mixtures and model sizes usually differ.

**Experiment:** hidden noisy/accented speech versus clear speech, control transcript quality, evaluate grounded scene questions, safety, latency and dollar cost.

## D06 — Synthetic data enriches vs removes rare modes

**Evidence for conditional benefit:** [2025 synthetic-data mixture experiments](https://arxiv.org/abs/2510.01631) and [2026 data-constraint scaling](https://arxiv.org/abs/2605.12715).

**Contrary mechanisms:** [2026 multiple-definitions critique](https://proceedings.mlr.press/v306/schaeffer26a.html) warns overgeneralizing collapse; [2026 biased selection study](https://proceedings.mlr.press/v306/qiao26c.html) describes rare-mode loss through filtering.

**Experiment:** train on equal-token mixtures with independent rare-mode and high-frequency holdouts, control synthetic-generation diversity and verifier selection.

## D07 — Brain-inspired objectives vs unverified biological analogy

**Evidence:** [active inference and RL](https://arxiv.org/abs/2002.12636) studies a combined information-seeking objective; [2026 Nature neuromorphic review](https://www.nature.com/articles/s43588-026-01012-x) surveys bio-inspired computation.

**Caution:** human-like terms (memory, consciousness, curiosity, global workspace) are not operational proofs of human-level reasoning. An organoid device's biological novelty does not establish utility per joule or a useful pretrained language model.

**Experiment:** match action budgets, latent state accuracy, decision utility, real power and transfer; remove metaphors from scoring.

## D08 — Longer reasoning chains vs actual proof reliability and cost

**Evidence:** [DeepSeek-R1](https://arxiv.org/abs/2501.12948), [DeepSeek-Prover-V2](https://arxiv.org/html/2504.21801), [s1](https://arxiv.org/abs/2501.19393) support study of test-time computation.

**Caution:** sampling 8,192 candidate outputs isn't equivalent to one-shot correctness or latency. A plausible chain can still be wrong; a correct proof can concern the wrong statement.

**Experiment:** candidate-quality vs actual wall-clock/checker/token budget, and independent validity for both result and intermediate formalization.

## How to add a new disagreement
Create Dxx with: **opposing claims; source identifiers; precise evaluation populations; mechanism; confounders; a falsifying trial**. Don't declare the literature "settled" unless multiple independent reproductions and the scope of validity are established.
