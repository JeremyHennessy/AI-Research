# Experiment portfolio — build, test, falsify
Pass 1 proposals, **no outcomes claimed**. Dates, sizes, thresholds and costs below are *design parameters* to preregister and may be adapted before the run. Holdout must remain sealed thereafter.

## Common experiment contract
Every trial requires: parent baseline run; single intervention; dataset + license; exact model revision; frozen prompt; hidden test; fixed compute and tool rights; seed; reliability/latency/cost; confidence interval; per-example failures; stop/rollback criteria. Optimizations and comparisons must get equal tuning budgets.

### Shared metrics
- **Primary:** exact task success or objective graded correctness on unseen instances.
- **Secondary:** wall-clock p50/p95, model and verifier tokens, API/hardware dollars, VRAM, tool calls, unsafe tool attempts, false confident answers, human review.
- **Calibration:** selective accuracy vs abstention rate (risk-coverage curve).
- **Long horizon:** success and error recovery by step count.
- **Generalization:** newly generated tasks, changed terminology, unseen mechanics.
- **Statistical:** paired bootstrap 95% interval for delta, multiple seeds as applicable. A result is inconclusive if its uncertainty spans practically irrelevant or negative outcomes.

## E01 — reproducible baseline and dataset audit [P0]
**Question:** can we reliably measure an open model before building new machinery?
**Setup:** lock model/tokenizer revision, decoder, evaluation harness, random seed, hardware and 100-500 development examples. Separately create hidden test; source must be legal and contamination-audited. Use one reasoning set, one code set, one interactive task family if licenses permit.
**Compare:** same model across two repeated inference runs, with environment snapshots.
**Success:** deterministic grading where expected, reproducible metrics and logs; robust error handling.
**Failure:** missing model hash, changing dependency version, missing per-example traces, inconsistent baseline.
**Deliverable:** /runs/E01/... manifest + scores.json + predictions.jsonl. Do not label model quality improvement.

## E02 — adaptive test-time computation [P0]
**Hypothesis:** decide per question whether to answer directly, sample extra candidates, run a verifier, or abstain.
**Conditions:** fixed model direct pass; fixed 4-sample best-of-N; fixed budget deliberation; proposed adaptive controller.
**Controls:** equal *average* and *tail* compute budgets; identical independent verifier and prompts; untouched novel templates.
**Metric:** accuracy-vs-cost area and severe incorrect high-confidence answers; report per-difficulty buckets.
**Falsifiers:** best-of-N dominates controller across compute curve; additional deliberation increases confident errors; gains vanish on future tasks.
**Proposed acceptance gate:** statistically supported positive gain in prespecified area metric at comparable p95 latency, without severe error increase.
**Source:** [s1](https://arxiv.org/abs/2501.19393), [DeepSeek-R1](https://arxiv.org/abs/2501.12948).

## E03 — explicit memory and correction [P0]
**Hypothesis:** provenance-aware, timestamped external memory supports accurate recall and correction across sessions.
**Task generator:** random entities/facts; new events revise earlier facts; delayed unrelated distractors; user asks "what is true now" vs "what was true then". Use withheld entity names and action sequences.
**Variants:** no memory; last-N conversation; all-context when feasible; BM25 retrieval; embedding retrieval; structured episodic+semantic memory with supersession.
**Measures:** exact answer with time scope; fabricated memory rate; stale fact rate; latency, storage, token cost; delete/correction correctness.
**Falsifiers:** structured store cannot beat naive retrieval at equal budget or propagates stale information.
**Source:** [RAG](https://arxiv.org/abs/2005.11401), agent-system synthesis.

## E04 — data quality and mixture [P0 or P1, depends on compute]
**Hypothesis:** better selection and mixing of natural/synthetic/task data improves quality per training FLOP.
**Setup:** same tokenizer/architecture/optimizer/total tokens/compute; simple 50M-300M parameter scratch model *only if resources allow*, otherwise controlled adapter fine-tuning on a small open model. Separate these regimes clearly.
**Variants:** raw mixture; near-duplicate filtered; quality-selected; 10/30% verified synthetic; target-domain mixtures with controlled repetitions.
**Measures:** out-of-domain loss, task transfer, memorization, performance by language/topic, duplicate overlap, training stability.
**Falsifiers:** gains from contaminated splits, narrow-domain gains hiding general losses, expensive preprocessing more than offsets accuracy.
**Sources:** [Compute-optimal scaling](https://arxiv.org/abs/2203.15556), [synthetic study](https://arxiv.org/abs/2510.01631), [data-constrained mixtures](https://arxiv.org/abs/2605.12715).

## E05 — tool recovery and persistent plans [P1]
**Hypothesis:** structured state, bounded actions and independent outcome checks outperform prompting-only ReAct on unseen long tasks.
**Sandbox:** procedurally generate file/logic/puzzle tasks with reversible actions, changed tool descriptions, injected failures, stale observations, and blocked actions.
**Compare:** reactive tool loop; fixed hand-written planning; plan+verify/replan; state ledger + verify/replan.
**Measure:** success vs horizon; recovery rate; irreversible error count; wasted actions; tool instruction injection incidents.
**Falsifiers:** improvement only when train/eval tool schema matches, excessive action count, tool leakage.
**Sources:** [ReAct](https://arxiv.org/abs/2210.03629), [AgentBench](https://arxiv.org/abs/2308.03688).

## E06 — verifier training [P1]
**Question:** does a learned verifier improve search beyond rule-based or independent unit tests?
**Setup:** correctness-labeled traces on development tasks; held-out generators, corrupted proofs and partial solutions. Split by problem families, not just rows.
**Compare:** random candidate; LM self-judge; rules-based judge; independent learned verifier.
**Measures:** precision/recall on wrong answers, calibration, final correct selections, susceptibility to reward hacking.
**Falsifiers:** self-judges flatter their own outputs; learned verifier fails distribution shift or penalizes valid unfamiliar strategies.

## E07 — dense vs hybrid SSM [P1]
**Question:** does state-space mixing provide a better quality/latency frontier on target hardware?
**Compare:** dense decoder-only; Mamba-like selective state space; hybrid attention-SSM with matched active parameters and FLOPs plus matched training data. Measure short and long context.
**Primary:** quality at equal wall-clock budget; **secondary:** throughput, prefill, decode, long-range exact recall, VRAM, power.
**Falsifiers:** memory compression breaks exact recall; advantage disappears when dense baseline gets equal kernel optimization.
**Sources:** [Mamba-2](https://arxiv.org/abs/2405.21060), [FlashAttention](https://arxiv.org/abs/2205.14135).

## E08 — learned dynamics / world-model planning [P2]
**Question:** can a latent dynamics model and bounded model-predictive controller beat reactive policies on unseen rule combinations?
**Environment:** procedural grid/crafting tasks with movable objects, resources, obstacles, hidden rules, partial observation. Train/test split by mechanism combinations.
**Baseline:** random, heuristic shortest path, model-free RL, recurrent policy. **Variant:** learned transition model + imagined rollouts, with uncertainty gating.
**Metrics:** task success, transfer, cost per interaction, transition calibration, model exploitation, loop detection.
**Falsifier:** planning accuracy high on seen states but catastrophic under unseen dynamics.
**Sources:** [DreamerV3](https://arxiv.org/abs/2301.04104), [Genie](https://proceedings.mlr.press/v235/bruce24a.html).

## E09 — multimodal grounded action [P2]
**Question:** do grounded observations support generalization over text descriptions alone?
**Baseline:** captions+actions. **Variants:** image features+language+actions; temporal visual prediction; explicitly supervised spatial state.
**Measures:** grounding under counterfactual scene changes, unseen object configurations, real vs simulated robustness, safety.
**Dependencies:** lawful video/robot demos, data provenance and substantial compute.
**Sources:** [DINOv2](https://arxiv.org/abs/2304.07193), [OpenVLA](https://arxiv.org/abs/2406.09246).

## How to choose the next experiment
Choose **E01 first**. Advance to E02 or E03 only after a frozen measured baseline exists. Favor low-cost experiments with an objective grader and high information gain. Do not start a costly architecture training run without confirming a baseline and available hardware.

## Template: preregistration
- Run ID / git SHA / timestamp:
- Research question:
- Intervention and mechanism:
- Baseline and matching rules:
- Data source, rights, split hashes and contamination checks:
- Primary metric and meaningful effect size:
- Secondary/safety metrics:
- Seeds, sample size and analysis method:
- Stopping rule and rollback:
- Interpretations for positive, null and negative results:
- Link to immutable artifacts:
