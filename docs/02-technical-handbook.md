# Technical handbook: mechanisms, math and engineering choices
Scope: compact engineering reference. Equations are simplified and depend on training regime; read original papers for derivations.

## A. Foundation: predictive modeling
A decoder-only autoregressive LM parameterizes P(x_1,...,x_T) = product over t of P(x_t | x_<t). Minimize token cross entropy:
L = -sum_t log P_theta(x_t | x_<t) / T.
This loss trains next-token prediction, not a guarantee of truth, grounded causality, long-term planning, or calibrated uncertainty.

**Tokenization:** BPE/unigram/byte-level approaches trade vocabulary size, sequence length, multilingual coverage, numeric representation and robustness. Compare tokenizer-fixed experiments unless tokenization itself is the independent variable.

**Transformer decoder layer:** self-attention uses A = softmax(QK^T / sqrt(d_k) + causal mask); Y = A V. Attention captures content-addressable interactions but grows quadratically with context length for vanilla full attention. Modern variants use grouped-query attention, rotary positions, normalization, gated feed-forward blocks and efficient kernels. Details differ by family.

**Training mechanics:** embedding / attention / FFN / residual / normalization / causal objective; AdamW or alternatives; schedules; warm-up; weight decay; gradient clipping; mixed precision; activation checkpointing; sharding; parallelism. At scale, data quality and system stability are as important as model topology.

**Compute approximation:** for conventional dense Transformer pretraining in regimes dominated by matrix multiplies, training FLOPs are often estimated as roughly 6 x N_active x D_tokens. It is a back-of-envelope estimate, not a law; context attention, optimizers, embeddings, MoE routing, recomputation and hardware overhead alter actual cost. Chinchilla studies how parameter and token choices depend on compute. [Vaswani 2017](https://arxiv.org/abs/1706.03762), [Hoffmann 2022](https://arxiv.org/abs/2203.15556).

## B. Architecture alternatives
| Family | Mechanism | Strength | Important caveat |
|---|---|---|---|
| Dense Transformer | Full/selective attention over tokens | Versatility, mature tooling | KV memory and long-sequence compute |
| Sparse MoE | Router selects subset of FFN experts | Higher total capacity per active FLOP | Communication, load balance, routing collapse |
| State-space / Mamba | Learned latent recurrence and selective dynamics | Linear-ish sequence processing and bounded per-layer state | Quality/recall tradeoffs and kernel dependence |
| Hybrid attention+SSM | Mix sparse/global attention with recurrence | Potentially good context/speed balance | Complex attribution and implementation |
| Recurrent memory | Compress history into evolving state | Constant-size memory | Can forget precise details |
| Retrieval-augmented | External store supplies relevant context | Freshness, provenance, editable memory | Missing/wrong retrieval and injection risk |
| Latent/diffusion generation | Iterative denoising / parallel token refinement | Potential generation tradeoffs | Training/inference maturity, discrete text handling |

Sparse MoE total parameters **are not** comparable directly to dense active parameters. Evaluate actual throughput and quality. [Switch](https://arxiv.org/abs/2101.03961), [DeepSeek-V3](https://arxiv.org/abs/2412.19437), [Mamba-2](https://arxiv.org/abs/2405.21060).

## C. Scaling and data
- **Compute optimality:** fit empirical learning curves to choose parameters, tokens and mixture; don't take a single famous ratio as universal across architectures, domains or inference demand.
- **Data pipeline:** source -> license/provenance -> parse -> deduplicate -> quality score -> safety/privacy filter -> mixture sampler -> train/validation/test isolation.
- **Contamination:** exact and near-duplicate content, solutions, translations, benchmark prompts and generated answer traces can all leak into training. Use timestamped holdouts and provenance lineage.
- **Synthetic data:** self-generated rephrasing, question synthesis and tool-verified traces can add diversity, but recursive low-diversity synthesis may amplify errors or distribution narrowing. Compare synthetic/natural mixtures and model-size interaction rather than assuming synthetic data is universally good.
- **Curriculum:** random / difficulty-stratified / reward-aligned; measure whether improved loss translates to independent capabilities.
[2025 synthetic data study](https://arxiv.org/abs/2510.01631), [2026 constrained mixtures](https://arxiv.org/abs/2605.12715).

## D. Post-training
**SFT:** supervised imitation of chosen demonstrations. It can improve usability but also distort calibration, induce verbosity or narrow behavior.
**Preference learning:** RLHF trains rewards from preferences followed by RL; DPO optimizes a preference objective against a reference model without an explicit reward-model training loop. The DPO loss for winning vs losing response differences includes beta-weighted differences of policy/reference log probability ratios inside a logistic objective; see derivation in [DPO](https://arxiv.org/abs/2305.18290).
**RL with verifiable rewards:** obtain rewards from reliable external judges (e.g., tests, exact arithmetic). It can improve math/coding; watch for reward hacking and verifier gaps. [DeepSeek-R1](https://arxiv.org/abs/2501.12948), [Scaling Up RL](https://arxiv.org/abs/2507.12507).
**Process supervision:** training verifiers against intermediate steps potentially reduces ungrounded outcomes, but steps and rubrics may be gamed. Distinguish an independent grader from a model grading itself.

## E. Reasoning and inference-time compute
- **Single pass**: baseline model answer at fixed decoding parameters.
- **Best-of-N**: sample N candidates; use an external verifier or ranker.
- **Self-consistency**: aggregate answers from independent traces.
- **Search / tree expansion**: evaluate branches under a compute budget; cost may dominate benefit.
- **Adaptive compute**: spend tokens only when problem uncertainty warrants it.
- **Verifier-guided stopping**: stop after a high-confidence independently verified answer.
- **Abstention**: better to say unknown than invent unsupported claims.

**Critical measurement:** plot pass@1 or verified-task-success vs wall-clock, dollars, total generated+scored tokens, and verifier calls. Extra thinking tokens do not automatically mean better reasoning. [s1](https://arxiv.org/abs/2501.19393), [Quiet-STaR](https://arxiv.org/abs/2403.09629).

## F. Memory and retrieval
Separate:
1. **Context:** transient tokens presently attended.
2. **Parametric knowledge:** patterns encoded in model weights.
3. **Episodic memory:** timestamped interactions, observations, causal outcomes.
4. **Semantic memory:** consolidated verified facts with provenance and supersession.
5. **Procedural memory:** policies, skills and tool affordances.
6. **Working memory:** task-local, short-lived summaries / plans.
External memory can be edited, revoked, evaluated and time-filtered. A memory system needs duplicate detection, TTL, confidence, contradiction handling, privacy, selective recall, auditing and deletion.

An experiment should compare no-memory, full-context (when feasible), naive RAG, chronological memory, and policy-selected structured memory at matched token budgets. Use future fact updates and false memories to test correction. [RAG](https://arxiv.org/abs/2005.11401).

## G. Agents, action and world models
An agent loop: observe O_t -> maintain state S_t -> choose action A_t -> execute in bounded environment -> record O_(t+1), success/failure -> update belief/plan. ReAct interleaves reasoning and acting [paper](https://arxiv.org/abs/2210.03629). **A tool wrapper is not an improvement to the base model weights.**

World model: predict transition P(s_(t+1), r_t | s_t, a_t) or a learned latent equivalent. Plan by imagined rollouts; compare to model-free or reactive agent. Train on many procedurally varied environments and evaluate transfer to rules and objects excluded from training. Prediction error alone is not intelligence: test action utility and calibration. [DreamerV3](https://arxiv.org/abs/2301.04104), [Genie](https://proceedings.mlr.press/v235/bruce24a.html).

## H. Multimodal & embodiment
Vision, audio, video, text, spatial tokens and actions require encoders, synchronized data and suitable objectives. Crossmodal training must test visual grounding rather than caption memorization. Self-supervised vision pretraining [DINOv2](https://arxiv.org/abs/2304.07193), vision-language-action [OpenVLA](https://arxiv.org/abs/2406.09246). Build multimodal experiments only after dataset/compute/licensing checks.

## I. Systems and inference
- Attention kernels reduce memory traffic; FlashAttention offers exact tiled attention, while follow-on work improves GPU work partitioning. Measure full-model time, not kernel microbenchmarks only. [FlashAttention](https://arxiv.org/abs/2205.14135), [FlashAttention-2](https://arxiv.org/abs/2307.08691).
- KV caching, grouped-query attention, prefix caching and paged allocation improve serving under some workloads.
- Quantization (int8, 4-bit and variants) lowers memory/compute but may degrade reliability on edge cases; calibrate per task.
- Distillation and adapters/LoRA reduce deployment or training costs but inherit teacher biases and often fail at transfer.
- Optimize for actual available hardware, context lengths, batch sizes, concurrent users, tool-call waits, precision and safety constraints.

## J. Security and governance
Prompt injection in retrieved documents, tool result forgery, malicious dataset samples, untrusted weights, personally identifying data and answer leakage require threat modeling. Disable arbitrary shell/network in experimental agents by default; apply least privilege and record immutable action traces. Do not train on or exfiltrate private data without a legitimate basis. Science requires replicability and human oversight, not unconstrained autonomy.

## K. Fundamental unresolved questions
How to learn robust abstract causal models? How much persistent memory should be differentiable vs external? What representations support compositional novelty? Can agents improve from sparse verified feedback without reward exploitation? Does recurrence offer global reasoning benefits beyond throughput? What are valid generalization measures across genuinely unseen environments? These remain open questions, not settled recipes.
