# AI Research Atlas — start here
Updated: 2026-10-08 | Pass: 2 | Status: **curated and CI-validated research foundation; not a systematic full-text survey or trained model**

## In 60 seconds
**Objective:** discover a measurable improvement in intelligence per dollar, per token, per joule, or per interaction; do not confuse a bigger benchmark score with general intelligence.

**Five working bets (hypotheses, not findings):**
1. Better verified data and curricula can outperform naive increases in tokens.
2. Adaptive inference and external verification improve difficult reasoning at controlled cost.
3. Structured persistent memory and retrieval outperform infinitely growing conversation context for some long-horizon tasks.
4. Learning environment dynamics and actions helps transfer better than text-only imitation on interactive tasks.
5. Hybrid architectures may offer useful latency/context/quality tradeoffs, but must beat strong attention baselines.

## Pass 2 additions
Start at the [Pass 2 decision atlas](10-pass2-index.md) for recent 2026 alternatives, the [63-record catalog](19-paper-index.md), [lab recipes](11-open-training-recipes.md), [source claim ledger](../data/claims.jsonl), and [metadata collection pipeline](20-collection-pipeline.md). Reproduction candidates and the next research stages are indexed in the [backlog](21-pass3-backlog.md).

## Navigation by the question you are asking

| Question | Read first | Next action |
|---|---|---|
| How does an LLM actually work? | [Technical handbook](02-technical-handbook.md) | Implement a tiny autoregressive transformer and measure loss |
| Which idea should we pursue? | [Strategy](01-research-strategy.md) | Pick a benchmark, budget and falsifiable hypothesis |
| What does published research say? | [Primary sources](03-source-map.md) | Check paper + code, record caveats |
| What should we build first? | [Experiments](04-experiments.md) | Run experiment E01 with a frozen holdout |
| How do we avoid false discoveries? | [Evaluation](06-evaluation.md) | Pre-register acceptance criteria |
| What are the unknowns? | [Open questions](07-open-questions.md) | Mark evidence gaps |
| What machinery and data are needed? | [Systems and data](08-systems-and-data.md) | Profile hardware and audit data licenses |
| How do we reproduce results? | [Build playbook](09-implementation-playbook.md) | Capture seed, versions, hardware and samples |
| Can we trust a claim? | [Evidence standards](05-evidence-standards.md) | Check evidence tier and provenance |

## Research map

| Track | Core problem | Strong baseline | Cheap decisive test | Failure warning |
|---|---|---|---|---|
| T01 Data | Quality, diversity and repetition | Identical-size pretraining on fixed corpus | Replace 10% with quality-selected examples | Improvement only on train distribution |
| T02 Architectures | Compute/context scaling | Dense decoder Transformer | Dense vs SSM/hybrid at matched tokens/FLOPs | Kernel optimization masquerades as architecture gain |
| T03 Post-training | Steerability and correctness | SFT and DPO | Same dataset, isolated ablation | Preference score improves while calibration worsens |
| T04 Reasoning | Test-time search & verification | Direct answer and best-of-N | Same time/token budget, independent verifier | Reward model overfitting |
| T05 Memory | Useful knowledge across sessions | Sliding context / simple RAG | Long-horizon fact updates and distractor tests | Leakage, stale recalls, unbounded storage |
| T06 Agents | Reliable actions and recovery | ReAct with tools | Sandbox multi-step tasks with failure injection | Success only in scripted trajectories |
| T07 World models | Predictive, actionable state | Model-free or reactive control | New obstacles, compositional transfer | Only memorizes trajectories |
| T08 Multimodal | Ground language in sensors/actions | Separate encoders + projector | Held-out crossmodal tasks | Data leakage from vision-text pairs |
| T09 Efficiency | Quality under resource budget | FlashAttention + quantization | Latency/throughput/VRAM/energy sweep | Benchmark ignores quality or prefill |
| T10 Safety & eval | Know when systems fail | Frozen test + human audit | Shift, deception, adversarial, misuse tests | Judge leakage and overly narrow task distribution |

## Hypothesis-to-evidence-to-experiment chain
**Paper → claim → caveat → hypothesis → baseline → frozen test → result → decision.**

No stage is implied by the next: reading a paper is not validating it; building an agent is not training a model; an idea is not a breakthrough.

## Priority ladder
- **Now:** E01 baseline and reproducibility, E02 adaptive test-time computation, E03 memory freshness, E04 data mixture.
- **Next:** E05 tool-action recovery, E06 verifier training, E07 hybrid architecture profiling.
- **Later:** E08 learnable world dynamics and causal transfer, E09 multimodal action grounding.
- **Do not attempt yet:** frontier-scale pretraining, uncontrolled autonomous self-modification, benchmark-driven leaderboard chasing.

## How to use multiple research passes
Pass 1 = map, fundamentals, cited foundations, experiments, collection code. Pass 2 = extend current papers and full-text claim verification. Pass 3 = reproducibility packages and compute-matched experiments. Pass 4 = evidence-based design revision. Maintain [research log](../data/research-log.md) and never overwrite a recorded negative result.

## Evidence language
- **Source-backed:** the linked publication *reports* the claim, not a fact independently reproduced here.
- **Synthesis:** reasoned integration of multiple published findings.
- **Hypothesis:** unverified proposal.
- **Verified in this repo:** requires reproducible experiment artifacts and tests; none yet.
