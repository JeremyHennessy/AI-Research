# Embodied AI, automated scientific discovery, and hardware-aware systems
Pass 3 | 2026-10-08 | Sources: primary paper abstracts, official labs and independent benchmark organizations. No experiment reproduced here.

## A. Embodied models: language should lead to observed action
| Approach | Inputs → output | Best reason to study | Primary evidence |
|---|---|---|---|
| VLM/VLA | Image + goal + robot state → actions | Ground instructions in observable sensor state | [RT-2](https://arxiv.org/abs/2307.15818) |
| Cross-embodiment learning | Diverse robot demos → transferable policy | Overcome scarcity of one robot's data | [Open X-Embodiment](https://arxiv.org/abs/2310.08864) |
| Diffusion action policy | Visual context → denoised action horizon | Model multimodal / smooth action sequences | [Diffusion Policy](https://arxiv.org/abs/2303.04137) |
| World-model video encoder | Video → latent state → predicted outcomes | Plan from observed dynamics | [V-JEPA 2](https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/) |
| Interactive generated world | Text+controls → video state transition | Generate diverse training/eval environments | [Genie 3](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) |
| Virtual generalist agent | Instructions + observations → simulator actions | Hold out whole environments for transfer | [SIMA 2](https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/) |
| VLA robotics agent | Image + instruction → motor commands | Real-world manipulation and language grounding | [Gemini Robotics 1.5](https://deepmind.google/en/models/gemini-robotics/gemini-robotics/) |

**Research caveat:** virtual-world success isn't physical-world safety; real robot transfer needs hardware constraints, latency, uncertainty and real outcome feedback.

### E19: practical robotics study
Start with a simple physics simulator and logged action outcomes. Compare scripted control, imitation, VLA interface (if models/license available), state-space dynamics, and action diffusion. Hide entire mechanism combinations, not just new object colors. Grade collision/constraint violations, success on unseen goals, recovery, latency and changes in observed state. Human-in-the-loop only for physical hardware.

## B. AI for science: discovery needs *external verification*
Science generally follows **hypothesis → prediction → test → independent interpretation → reproducible result**, not “confident paragraph → discovery.”

### Research patterns
- [AlphaEvolve (May 2025)](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/): generate candidate programs, score them with mathematical/unit-test evaluators, select promising candidates evolutionarily. Such systems can discover efficient algorithms where the fitness function is trustworthy.
- [AlphaEvolve impact update (May 2026)](https://deepmind.google/blog/alphaevolve-impact/): additional cases from the developing organization; selection bias and independent cost-accounting remain important.
- [FrontierScience (2025)](https://openai.com/index/frontierscience/): academic/scientific reasoning benchmark; correct short answers are not proof of doing novel independent science.
- [OpenAI First Proof (2026)](https://openai.com/index/first-proof-submissions/): research-level proof attempts with author-described limitations and expert feedback.
- [OpenAI mathematical release (October 6 2026)](https://openai.com/index/sharing-ai-progress-in-mathematics/), [original repository](https://github.com/openai/math): organization reports 722 manuscripts in 372 families, with **different verification stages** and only a subset supplied with Lean formalizations. Until independent review, treat novelty/correctness as **unresolved per result**, not 372 universally confirmed breakthroughs.

**Two independent questions:** Does an automated verifier accept a formalized proof under correct assumptions? And is the theorem genuinely new and important? Formal proof checks help with the first and do not settle the second.

### E21: toy research automation experiment
Use an explicitly bounded program-optimization search space (e.g., dynamic-programming optimization or sorting network). Independent hidden checker validates semantic equivalence on randomized and adversarial inputs; cost grader times implementations on frozen hardware. Compare random search, mutation/evolution, rule-based optimization and model-proposed candidates **at same compute and tuning budgets**. Preserve every failed proposal to control publication bias.

Evaluation should report total generation/tuning/verification dollars, number of evaluator calls, novelty vs known baselines, independently verified accuracy and distribution-shift speedups. A one-off fast candidate is not a general algorithmic advance.

## C. Hardware-aware training and serving
**Bottlenecks depend on task stage:**
- **Training:** accelerator memory, interconnect, optimizer states, activation recomputation, expert all-to-all, data loading, numerical precision.
- **Prefill:** attention and matmul throughput, prompt length, concurrent batch.
- **Decode:** KV-cache bandwidth and memory allocation, batch/latency trade-offs, speculative acceptance.
- **Agent system:** tools, retrieval and verification can dominate base decode.

**Primary research:**
- [MLPerf Inference v6.0](https://mlcommons.org/2026/04/mlperf-inference-v6-0-results/) and [MLPerf Training v6.0](https://mlcommons.org/2026/06/mlperf-training-v6-0-results/): standardized suite changes that must be compared by exact workload, latency constraints, hardware and submitted methodology.
- [ICLR 2026 architecture-aware scaling](https://proceedings.iclr.cc/paper_files/paper/2026/hash/dd2eb5250696753ea37141bbd89bb569-Abstract-Conference.html): model shape, hidden width, GQA and attention-to-MLP balance influence inference efficiency (author-reported). Do not use a single architecture ratio for every hardware.
- [ICML 2026 MoE scaling](https://proceedings.mlr.press/v306/elango26a.html): compares MoE design and operational hardware bottlenecks.
- [PagedAttention and vLLM](https://arxiv.org/abs/2309.06180): noncontiguous KV cache management.
- [BitNet b1.58](https://arxiv.org/abs/2402.17764): low-bit architectures trade weights, precision and kernel support.
- [LoRA](https://arxiv.org/abs/2106.09685) and [QLoRA](https://arxiv.org/abs/2305.14314): efficient adaptation vs full training.
- [Distillation](https://arxiv.org/abs/1503.02531): transfer teacher behavior to a student with additional assumptions and biases.

### E20: cheap adaptation matrix
On one frozen licensed model, compare inference-only prompting, full fine-tuning (if feasible), LoRA ranks [4,16,64] and QLoRA rank [16] on **the same training set**, matched optimizer steps and best-practice tuning budget. Evaluate trainable params, GPU VRAM, wall clock, quality by task family, calibration, safety regressions and time to deploy. **No general claim** that a rank or quantization level wins.

### E22: serving benchmark
Test at context windows [1K,4K,16K] and batch sizes [1,8,32] as feasible; include prefill and decode p50/p95, throughput, OOM, peak memory, effective tokens/J and error rates. Compare kernel/backbone changes without altering eval set, device or concurrency. A benchmark result from one GPU is not a universal hardware ranking.

## D. Strategic synthesis
A practical research lab can contribute through better **tests, data, verification, efficient serving, memory, task decomposition and modest architecture ablations**, without necessarily training a frontier-scale foundation model. Use honest labels: **a measured system-level gain is valuable but not a new trained LLM**.
