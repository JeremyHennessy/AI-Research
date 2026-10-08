# Full-paper audit: DeepSeek-Prover-V2 (revised v2, July 18, 2025)

**Status:** E2 — the complete public HTML paper (methods, training, evaluation, conclusion and appendices) has been read and analyzed. **Not an independent reproduction or an audit of every model weight/dataset.**

- Canonical source: https://arxiv.org/abs/2504.21801
- Reviewed full text: https://arxiv.org/html/2504.21801
- Source version: arXiv:2504.21801v2, 2025-07-18.
- Reference implementation/model repository: https://github.com/deepseek-ai/DeepSeek-Prover-V2 (not executed here).
- Reproducibility status: publicly described model/training methods but full compute, data and all sampling/ablation artifacts not independently validated.

## 1. What the system actually does

1. A large general-purpose model (DeepSeek-V3) sketches a solution in natural language and writes Lean4 `have` lemmas with incomplete proof placeholders.
2. A specialist 7B prover recursively attempts each local subgoal, possibly conditioned on previous proven lemmas.
3. Successful formally checked subgoals are assembled into a complete proof. Traces plus natural-language plans form cold-start examples.
4. Expert iteration generates verified short proofs, then a separate supervised stage teaches both fast non-CoT and slower CoT reasoning.
5. A GRPO reinforcement-learning stage updates the proof model using binary checked-proof rewards; an early structural reward encourages use of planned lemmas.
6. The large prover's rollouts also supervise a distilled 7B model.

**Causal attribution caveat:** the study combines decomposition, curriculum, synthetic traces, model scale, RL, prompt mode and test-time samples. Their reported overall performance does not isolate one contribution.

## 2. Publicly reported implementation details

| Stage | Paper's disclosed mechanism and setting | What's still unknown / confounded |
|---|---|---|
| Subgoal creation | Language proof sketch -> Lean `have` statements with temporary `sorry` placeholders | Quality, model-sampling costs, proof-correctness filtering |
| Local search | 7B prover searches recursively for formal solutions to derived lemmas | Overall candidate count and success distribution per initial theorem |
| Curriculum | New theorem examples from subgoal statements, both with/without preceding lemmas as premises | Shift induced by selecting solvable subgoals |
| Non-CoT pretraining | Expert iteration retains only Lean-verified full proofs | Model and prompt optimization, verifier reward exploits |
| Supervised stage | 671B DeepSeek-V3 base, constant LR 5e-6, context length 16,384 | Full seed/batch/optimizer specifics not exhaustively available |
| RL | GRPO, binary Lean proof reward; 256 problems × 32 samples/iteration; max generation 32,768 tokens | Total iterations, effective compute and complete hyperparameters |
| 7B distilled model | Extended from 4,096 to 32,768 context; large-model rollouts used for supervised data | Precise teacher/student FLOPs and train-data overlaps |
| Evaluation | Lean 4.9.0-rc2; author-revised MiniF2F and PutnamBench problems | Old tactic/version validity and independent verifier robustness |

These are **paper-reported** parameters, not a recipe we executed. Do not silently fill undisclosed values.

## 3. Quantitative claims: always report sample budget

| Evaluation | Paper-reported result | Critical interpretation |
|---|---|---|
| miniF2F-test, 671B CoT, pass@32 | 82.4% | 32 attempts, not one-shot performance |
| miniF2F-test, 671B CoT, pass@8192 | 88.9% | Extremely large attempt budget; compare cost and independence |
| miniF2F-test, 7B CoT, pass@8192 | 82.0% | Different model/compute, **not** 82% single-pass |
| PutnamBench, 671B CoT, pass@1024 | **47 / 658** | Corrected v2 full-text figure |
| ProverBench AIME subset, 671B CoT | 6 / 15 with 512 samples | Proving a provided correct answer differs from *finding* it |
| ProverBench AIME subset, general DeepSeek-V3 | 8 / 15 using 16 majority-vote samples | Different task/harness; NOT an apples-to-apples comparison |

### Crucial source discrepancy

At inspection (2026-10-08), the arXiv abstract landing page for 2504.21801 displayed **49 of 658**, while its **v2 full text and Table 4 said 47 of 658**. The HTML body also documents a different, specific earlier reporting problem with the 7B model: it appeared to prove some PutnamBench problems that were actually accepted through a Lean 4.9 `apply?` user-interface bug. Both observations show why results must be tied to **paper version, checker version, and exact run outputs**.

The full text also reports an initial combinatorics evaluation of 12 successful proofs that was revised to 10 after identifying misformulated problems. This is evidence of the importance of sound benchmarks, not proof that all remaining scores are free of errors.

## 4. Evaluator vulnerability and safety of proofs

The paper attributes an apparent small-model advantage to a Lean 4.9.0 `apply?` user-interface bug where `sorry` was not surfaced in some corner cases. It explicitly describes repeated exploitation involving `Cardinal.toNat` and `Cardinal.natCast_inj` in generated outputs.

For new evaluations:
- Reject `sorry`, `admit` and known unsafe axioms in submitted proof text **and** compiled proof dependencies.
- Pin Lean compiler, mathlib commit, tactics and plugins; record hash per run.
- Independently recompile every purported successful proof under a patched verifier and an allowlisted axiom policy.
- Run adversarial regression fixtures for previously exploited patterns, including `apply?` tactic edge cases.
- Check theorem statement equivalence: a formally proven *wrong or vacuous proposition* is not a solution to the intended mathematical problem.
- Separate language-model scoring, checker correctness, and problem formalization correctness.

## 5. Proposed small decisive experiment E24

**Hypothesis:** verified subgoal decomposition improves hidden-theorem success more per execution budget than direct proof generation.

**Variants:** direct baseline, random fixed-depth subgoal decomposition, language-guided decomposition, language-guided + independently checked intermediate rewards.

**Controls:** identical pinned Lean4/mathlib, theorem families, base model, maximum prover calls, total generated tokens and wall time; search prompts optimized equally. Hold out entire theorem families and never train on hidden statements or formal proof sketches.

**Primary:** correct proof term for intended theorem *accepted by patched independent checker*, counted at fixed total checker calls. **Secondary:** success vs tokens/time, false acceptance, solver reward-hacking, invalid theorem formalization, rare-theorem failure clusters.

**Falsifier:** apparent benefit disappears after correcting verifier bugs or matching total search budget.

## 6. Remaining evidence gaps

The published report is not a full disclosure of every data provenance item, seed, infrastructure setup, or repeatable training run. Its reported high sample budgets are expensive and can make cross-model comparisons misleading. The AIME proof task provides the correct answer in the theorem, unlike answer-finding. Changes to formalized theorem statements influence comparability. No original system trained here.

**Next action:** turn the above verifier acceptance rules into executable offline regression tests before attempting a large language model formal-proving experiment.

**Method citations:** https://arxiv.org/html/2504.21801#S2 ; evaluation and revisions: https://arxiv.org/html/2504.21801#S3 ; bug and appendices: https://arxiv.org/html/2504.21801#A2 .
