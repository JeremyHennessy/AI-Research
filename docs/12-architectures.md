# Architecture directions beyond a standard Transformer
**Engineering reading notes — 2026-10-08.** Claims below refer to cited paper abstracts and public author releases. No new architecture implemented or proven here.

## 1. Dense attention, sparse experts and recurrence solve different costs
A decoder model computes conditional token distribution p(x_t | x_<t). Full attention creates a content-addressable workspace but attention score work grows approximately O(L²d) for sequence length L in naive prefill. Optimized exact attention improves IO and kernels but not the mathematical pairwise interactions. KV caches let decoding reuse past values, at a growing memory cost. Sparse MoEs increase **total** capacity without activating every expert; route and network bandwidth become critical. Recurrent/SSM layers compress history into state, improving some context/memory costs but can lose exact token retrieval.

**Synthesis:** no single metric “parameters” or “context window” is adequate. Compare train FLOPs, active params, KV state, HBM bytes moved, network all-to-all, prefill, decode, and task-specific recall.

## 2. ICML 2026 retrieval-aware Transformer→SSM distillation
**Primary:** [Retrieval-Aware Distillation for Transformer-SSM Hybrids](https://proceedings.mlr.press/v306/bick26a.html), [Expressivity-Efficiency Tradeoffs for Hybrid Sequence Models](https://proceedings.mlr.press/v306/cooper26a.html).

**Mechanism (author reports):** identify Transformer attention heads especially important to **gather-and-aggregate**, use ablation on synthetic associative retrieval, preserve only those heads while converting the remainder to recurrent heads. The ICML paper reports that keeping ~2% of heads retained over 95% of teacher performance **on its retrieval-heavy evaluation**; this is not a universal ratio or an independent reproduction. Separate theory identifies tasks where hybrid recurrence+attention can be more efficient than either alone under particular theoretical resource models.

**Design space:** dense attention every layer; attention at layers [0,4,8,...]; retrieval-preserving selected heads; pure SSM; hybrid + external RAG. Build retrieval probes with exact keys, repeated distractor keys, negative queries, long dependencies and hidden reassociations. Head importance may change after re-training, task domain or length shift. Test **head retention selection on development tasks only**, freeze before hidden test.

## 3. Byte-level models: Bolmo 2025→Nature 2026
**Primary:** [Ai2 byteifying details](https://allenai.org/blog/bolmo), [October 7, 2026 Nature release](https://allenai.org/blog/bolmo-nature).

Subword tokenizers trade sequence length and vocabulary rigidity against throughput. Byte models avoid fixed subword boundaries, but naïve bytes create long sequences. Bolmo's **latent tokenizer**:
```
UTF-8 bytes -> local mLSTM byte encoder -> boundary predictor -> variable-length patch pooling
            -> existing global Transformer -> patch depooling -> local byte decoder
            -> next byte / boundary predictions
```
Ai2 reports a **two-stage retrofit**: (1) freeze global Transformer and fit byte-local components using ~9.8B original-token-equivalent text tokens (~43B bytes), (2) unfreeze global and continue ~39.3B tokens (~173B bytes). The report describes the local boundary mechanism, and also transferring post-training updates via weight-space differences. Its October 2026 release describes adapting the technique to Qwen3 8B and Llama3 8B models as well.

**What this does *not* prove:** a byte model is always superior for general tasks, multilingual text, or latency. Source numbers are trained on specific GPUs and compression targets; “byte-level” has an additional patching policy not present in ordinary BPE models.

**E10 proposed ablation:** tokenizer BPE vs naive byte vs adaptive byte patching (when a suitable open implementation and hardware exist). Test spelling edits, arbitrary identifiers, Unicode normalization, mixed-script sequences, bytes/sec, NLL/bits-per-byte, tokenizer failure cases and compute. **Never** compare perplexity directly across different tokenizers; normalize by bits/byte or common downstream tasks.

## 4. Diffusion language models (DLMs) and flow models
**Sources:** [LangFlow](https://arxiv.org/abs/2604.11748), [Consistent Diffusion Language Models](https://arxiv.org/abs/2605.00161), [DLM Experimental Analysis](https://arxiv.org/abs/2606.19475), [Clock Diffusion, Oct 1 2026](https://arxiv.org/abs/2610.00894), [Sigma: Large Language Continuous Diffusion Models, Oct 2 2026](https://arxiv.org/abs/2610.02665), [PRISM](https://proceedings.mlr.press/v306/bai26f.html).

**Autoregressive (AR):** predict one next token from a prefix; sample sequentially but reuse KV and use speculative decoding.
**Masked discrete DLM:** mask/corrupt sequences; train denoising prediction conditional on corrupted context/time; generate by iterative token updates, sometimes in parallel blocks.
**Continuous DLM:** noise latent embeddings and use an ODE/SDE/flow-like denoising path; decoding quality depends on numerical steps, guidance, length and embedding geometry.

**Public findings from 2026:** newer work reports improvements in denoiser consistency and few-step text sampling; Clock Diffusion proposes semi-autoregressive windows and caching ideas; Sigma warm-starts from AR weights and steers continuous trajectories. A separate systematic comparison finds that block size, denoising steps and unmasking have major effects. **Caveat:** doing full-sequence parallel computation per step can be expensive; many denoising evaluations (NFEs) may negate the apparent throughput benefit. Some reports emphasize quality parity on individual benchmarks; do not mistake that for uniform lower latency.

**E11 required comparison:**
- Freeze matching model sizes/data where possible and document when unmatched.
- For AR: tokens/sec, prefill, decode, speculative options and total output quality.
- For DLM: block size, parallel unmasking schedule, **network function evaluations**, guidance strength, steps-per-block, time, VRAM, accuracy and quality at equal end-to-end budget.
- Use synthetic exact-format tasks, independent reasoning/code tests and human quality review. Include valid-length/stop handling, a key practical weakness in non-AR generation.
- Report quality-vs-time Pareto curves; **no blanket claims** based on parameter counts.

## 5. Language as latent computation vs explicit search
Options for reasoning:
1. More tokens with same model (fixed deliberation).
2. Adaptive stopping (uncertainty / verifier confidence).
3. Candidate search with independent reward/verifier.
4. Train an internal value/verification representation.
5. Differentiable predictive state or external memory.
6. RL training with valid rewards.

Beware mixing more capable base models with better controllers; if the model's weights change, isolate their contribution. Benchmarked long chains may be overoptimized to public math problems.

## 6. Architecture decision matrix

| Option | Attractive when | Likely limiting factor | First discriminator |
|---|---|---|---|
| Dense AR Transformer | Broad generality and tooling maturity | KV/prefill cost | Baseline E01 |
| Sparse expert MoE | Capacity at modest active FLOPs | Training infra/communication | E07 router profiling |
| Hybrid SSM+attention | Long sequences + exact retrieval | Head selection and recurrent forgetting | E07b hidden recall |
| Byte-patch model | Rare characters / variable granularity | Boundary prediction and training cost | E10 byte/Unicode tests |
| Discrete DLM | Flexible remasking / block parallelism | NFE, quality consistency | E11 quality/time curve |
| Continuous DLM | Steerable latent trajectories | Expensive solver steps | E11 NFE curve |
| AR + external memory | Fresh facts, provenance and correction | Retrieval staleness / injection | E03 memory tasks |
| World-model agent | Actions, partial state and long horizons | Dynamics compounding | E08 hidden mechanics |

## 7. Practical next step
Do **not** jump to writing a 1T model. Start from an openly reproducible 50M–1B baseline and build a common benchmark harness. All alternatives must beat a tuned AR baseline on a *specific, preregistered* problem at comparable cost before becoming architecture candidates.
