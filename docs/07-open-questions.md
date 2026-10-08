# Open questions and hypotheses register
All entries below are questions or original synthesis, not established advances.

| ID | Question / hypothesis | What would count as evidence? | Ways it could fail | Priority |
|---|---|---|---|---|
| H01 | Adaptive controller decides when to retrieve, think, act, or abstain | Dominates fixed policies across success-vs-cost curves | Controller overhead and errors outweigh gains | High |
| H02 | Provenance-aware episodic memory improves long-horizon tasks | Better update/forget/recover success at matched tokens | False recall, privacy risks, wrong time scope | High |
| H03 | Verifier-guided search generalizes beyond teacher traces | Transfer to unseen task generators and rubrics | Reward hacking or verifier distribution shift | High |
| H04 | Repetition-aware high-quality mixtures beat homogeneous pretraining | Lower held-out loss and downstream gain at equal FLOPs | Overfitting small domains and hidden leakage | High |
| H05 | Small learned transition model improves sparse-reward planning | Out-of-distribution mechanics success over reactive control | Error compounding in imagined rollouts | Medium |
| H06 | Hybrid SSM+attention yields better context/latency tradeoff | Matched quality and better actual hardware throughput | Long-range retrieval failures / kernel confound | Medium |
| H07 | Differentiable memories help beyond timestamped external stores | Gains after equal parameter+token+compute budget | Unstable writes, catastrophic forgetting | Later |
| H08 | Joint predictive objectives build stronger causal representations | Intervention/transfer wins, not probe correlation only | Shortcut features | Later |
| H09 | World-model objectives strengthen text-centric agents | Novel interactive environment success | No transfer from pixels to language | Later |
| H10 | Uncertainty-calibrated abstention reduces severe failures | Risk-coverage curves on unseen domains | Bad self-confidence or costly verification | High |

## Research disagreements to track
1. Does chain-of-thought improve actual reasoning or primarily change search/distribution? Measure independent verification and counterfactual outcomes.
2. At what horizon do recurrent/SSM systems forget exact information compared with attention and RAG?
3. Can synthetic data improve pretraining long-term without decreasing diversity?
4. Do agents learn new reusable skills, or merely accumulate hand-written workflows?
5. Are higher benchmark scores attributable to training changes, evaluation leakage, larger inference budgets, or model-scale effects?
6. How can one evaluate capability gain while accounting for energy, accessibility and safety?
7. Which features of a learned world state are truly causal under intervention rather than predictive probes?
8. What are credible incremental paths from narrow skill learning to broad transfer without assuming general intelligence emerges?

## How to resolve one question
Choose a specific hypothesis; write a 1-page experimental design; reproduce the baseline; obtain a precommitted holdout; run an ablation; compute uncertainty; inspect failures; store result and compare against competing explanations. See [experiments](04-experiments.md).

## Next literature pass
Systematically add contrary papers, negative results, later 2026 publications, peer-review decisions, replications and open implementations. Search concept families, not just famous model brand names.
