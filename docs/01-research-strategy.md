# Strategy: how to develop a better AI without fooling ourselves

## 1. Define what "better" means
"Next best AI" is not a single axis. Measure a Pareto frontier:
- **Capability:** exact-match / pass@1 / task success and transfer to unseen task families.
- **Reliability:** error severity, uncertainty calibration, abstention, recovery after tool errors.
- **Learning efficiency:** gain per new labeled example or environment interaction.
- **Runtime efficiency:** actual dollars/energy/latency/VRAM; report prefill and decode separately.
- **Long-horizon behavior:** success vs task length, memory updates, goal persistence and correction.
- **Safety & human control:** bounded authority, auditability, red-team resistance.
Rank systems only when they are evaluated at comparable budgets and on independently held-out tasks. Different applications need different trade-offs.

## 2. Working system decomposition
Observation -> tokenizer/encoders -> backbone -> inference controller -> retriever/memory -> tool/action executor -> external verifier -> feedback store -> trainer. Each layer must be independently replaceable and measurable. First isolate whether improvement comes from weights, retrieval, search, reward, execution harness, or evaluation artifact.

### Training vs inference
**Pretraining** learns general representations from predictive objectives; **post-training** shifts behavior; **inference-time compute** explores candidate solutions without updating weights; **memory/retrieval** stores external state; **agents** execute actions and observe consequences; **world models** learn transition/reward dynamics. Avoid crediting "model intelligence" for improvements supplied by tools, data leakage, or scaffolding.

## 3. Direction portfolio
| Direction | Evidence | Key uncertainty | First test |
|---|---|---|---|
| High-quality token mixture | Compute/data scaling and data-mixture studies | Optimal mixture changes by scale/domain | 3 seeds, matched token budget |
| Adaptive compute with verification | Reasoning and test-time scaling studies | Extra thinking can become circular | Accuracy-vs-tokens curve |
| Explicit memory | RAG and agent systems literature | Retrieval errors/staleness create regressions | Contradictory updates and distractors |
| Agentic feedback | ReAct, interactive benchmark literature | Overfitting to tool schema | Hidden tools / injected tool failures |
| Dynamics-aware planning | DreamerV3, Genie research | Visual-world findings may not transfer to language agents | Unseen mechanics with hidden transitions |
| Sparse/hybrid backbone | MoE, Mamba-2, FlashAttention | Speed/quality depends on kernels and workload | Equal hardware, parameters and FLOPs |
| Multimodal representation | DINOv2, OpenVLA | Dataset/licensing and embodied transfer | Crossmodal OOD split |
| Mechanistic interpretability | Feature/probing and intervention studies | Probes don't establish causality | Causal patching with held-out prompts |

**Synthesis:** no single architecture choice guarantees a superior general model. Data, losses, training stability, compute allocation, post-training and evaluation interact; improvements must be attributed with ablations.

## 4. Research program with phase gates
### Phase A: establish facts
Build deduplicated metadata index, manual shortlist and evidence trail. Capture availability of weights/code, licenses, limitations, corrections. A short paper summary is not a completed replication.

### Phase B: baseline
Pick an accessible *open-weight, licensed* small model and public dataset; record model revision/hash, dataset revision, exact split, tokenizer, hardware, inference parameters and evaluation harness. Choose a task family with objective graders and novel distribution splits.

### Phase C: minimal controlled experiments
Only one independent variable per trial. Three or more seeds where feasible; identical budgets, tuning rights, data access and tool privileges across baseline/variant; keep separate development and untouched tests. Record negative results.

### Phase D: stress and transfer
Test paraphrases, domain shift, length extension, decoy retrievals, contradictory facts, tool failures, hidden rule changes and distribution-shifted problem templates. Include serious-failure review.

### Phase E: graduation
Promote a hypothesis only when it improves a predeclared primary metric with uncertainty estimates, does not materially degrade safety or held-out generalization, and is reproducible by a second run.

## 5. Suggested first implementation
A strong small language model, frozen by revision, combined with:
1. Retrieval baseline (BM25, then embedding-based).
2. Structured event memory with timestamps and provenance, plus an explicit retrieval policy.
3. Optional bounded search (best-of-N or verifier-guided) for tasks with objective checks.
4. Sandboxed tools (read-only or mocked at first), deterministic fixture environments.
5. Metrics tracked at comparable wall-clock and output-token budgets.

**Original unverified hypothesis H01:** an adaptive controller deciding **retrieve / deliberate / act / ask / abstain** will outperform always-deliberate or always-retrieve policies for latency-constrained, long-horizon tasks. **Falsifier:** at equal budget it does not improve success on hidden tasks or worsens calibration. **Do not mistake this hypothesis for a demonstrated model.**

## 6. Explicitly avoided traps
- Bigger test set scores after repeated tuning on the same test split.
- Benchmark names used as proxies for general intelligence.
- Training on unlicensed or private data because it was publicly findable.
- Self-rewarding agents that create their own success labels without an independent outcome signal.
- Deploying autonomous agents to production during method exploration.
- Comparing sparse and dense models by parameter count alone.
- Ignoring power, batch size, context length, compiler and hardware variants.
- Copying unpublished proprietary model recipes without verified access.

Sources: [Chinchilla](https://arxiv.org/abs/2203.15556), [DeepSeek-R1](https://arxiv.org/abs/2501.12948), [ReAct](https://arxiv.org/abs/2210.03629), [Mamba-2](https://arxiv.org/abs/2405.21060), [HELM](https://arxiv.org/abs/2211.09110). Claim-specific links and limitations in [source map](03-source-map.md).
