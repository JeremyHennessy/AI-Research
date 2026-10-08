# Pass 2: build-ready experiments and gate checklists
**Status:** prepared experiments (none trained or independently benchmarked by this document). Add actual measurements only with run receipts.

## E03b — temporal memory and action grounding (CPU first)
**Pre-registered hypothesis:** an explicitly timestamped event ledger yields fewer stale or future-leaked facts than naive first-match retrieval, and its memory improves tool-argument selection without granting more context tokens.

**Training data:** none; synthetic event records with fictional entity IDs and tasks. **Grader:** authoritative fixture state. **Test families:**
1. Current vs historical state after change;
2. Multiple contradictory update events;
3. Revoke/erase memory; ensure no recall after deletion;
4. Vague query requiring disambiguation or abstention;
5. Tool-argument selection based on current state; validation of chosen tool and arguments;
6. Distractor context with similar names;
7. Cross-session action outcomes and causal dependencies;
8. Attempts to inject instructions through retrieved documents.

**Baselines:** first mention; last mention; BM25+timestamp post-filter; chronological event ledger; ledger+planning/controller. **Controls:** same available sources, privacy rules, token budget; time-scoped query intent must be identical. **Primary:** exact temporal fact accuracy; **secondary:** wrong tool parameter rate, stale-memory rate, total storage, retrieval latency. Separate the trivial time-ledger smoke test from real LLM-agent evaluation.

**Reproducible fixture prototype:** `python3 experiments/temporal_memory.py --trials 100 --seed 41`. This simulates deterministic source retrieval *without any LLM*. Its purpose is testing scoring/temporal semantics, not claiming a model improved.

**Production gate:** don't graduate a learned memory module without permission audits, forgetting semantics, externally verified updates and stress on unknown schemas.

## E07b — retaining useful attention heads
**Hypothesis:** preserve heads critical to associative recall while replacing less important attention computation with recurrence, producing better accuracy at lower actual inference cost.

**Setup:** begin with accessible open small Transformer+recurrent/hybrid implementation. Dev task generator emits key-value pairs, repeated keys, distractors, missing keys and long distances. Score head importance by ablation on *development only*. Freeze top-k selection, then evaluate held-out random seeds and task generators.

**Variants:** all attention; pure recurrent; uniform retained attention fraction; importance-selected retained fraction; random retained fraction (control). **Budget axes:** active FLOPs, retained heads, KV bytes and end-to-end p95 latency. **Acceptance:** hidden retrieval accuracy no worse than a prespecified acceptable tolerance *plus* actual speed/VRAM gain; report errors separately. **Falsifier:** importance map doesn't transfer or dense baseline is faster after optimized kernels.

**Related paper:** [ICML 2026 retrieval-aware distillation](https://proceedings.mlr.press/v306/bick26a.html).

## E10 — byte tokenizer architecture
**Hypothesis:** byte-patched models generalize better to rare strings, character transforms and multilingual edge cases at tolerable bits/byte and latency.

**Input families:** arbitrary SHA-like strings, source code identifiers, malformed Unicode/escaped bytes, multilingual text, whitespace-sensitive syntax, case changes, cipher toy rules. All synthetic identifiers generated after evaluation freeze.
**Variants:** unchanged BPE reference; pure byte baseline; published Bolmo if licensed and compute permits; modified byte boundary threshold.
**Metric:** exact character-level correctness, **bits/byte**, generation bytes/s, worst-case context fragmentation, task-level calibration. **Important:** BPE per-token perplexity is incomparable to byte per-token perplexity; use common-byte normalization.

**Falsifier:** no meaningful edge-case gain, high latency or regressions in reasoning/math/code; reported training gains depend on proprietary data or incomparable parameter count.

**Source:** [Nature 2026 Bolmo paper](https://www.nature.com/articles/s41586-026-11111-4).

## E11 — autoregressive vs diffusion/flow LM
**Hypothesis:** for particular editing, structured or parallelizable outputs, diffusion may provide an improved verified quality × time frontier relative to tuned autoregressive generation.

**Grid:** AR baseline with KV+optional speculation; discrete masked DLM with (steps × block size × remasking policy); continuous DLM with NFE × guidance. Use model-weight/data-matched conditions where available; otherwise clearly label architecture/model confounds.
**Primary:** verified pass@1 vs milliseconds per generated output; **secondary:** VRAM, tail latency, length correctness, effective samples per second, quality-vs-energy.

**Caveat:** a “single parallel step” is not a single AR token. Compare real device runtime rather than raw NFE count alone. **Falsifier:** diffusion needs too many denoiser passes to beat AR at acceptable quality.

**Sources:** [DLM experimental analysis](https://arxiv.org/abs/2606.19475), [Sigma](https://arxiv.org/abs/2610.02665), [Clock Diffusion](https://arxiv.org/abs/2610.00894).

## E12 — ability deconvolution / benchmark interpretation
**Hypothesis:** a single aggregate benchmark score conceals skill-specific improvements and regressions.

**Design:** synthetic task clusters with controlled latent requirements (retrieval, planning depth, character manipulation, calculation, conflicting evidence, tool schema comprehension), then real held-out problems. Collect results from fixed models, create cluster-level scorecard and inspect correlations; optionally fit item-response models with adequate sample size and held-out calibration.

**Primary:** predictive ability of skill-specific scores on unseen composed tasks; **secondary:** stability of cluster assignments, fairness across varied demographic/language phrasing, calibration. **Falsifier:** inferred factors unstable across seeds/models and fail to predict unseen task performance.

**Source:** [BenchMIRT](https://allenai.org/blog/benchmirt).

## E13 — cooperative supervision with RL
**Hypothesis:** learning *when* demonstrations are beneficial to RL outperforms indiscriminate SFT/RL loss mixing.
**Variants:** SFT then RL; RL only; joint constant-weight; scheduled joint; cooperative gain estimator. **Controls:** same starting model, training compute and verifier.
**Primary:** hidden exact reward and independently verified transfer accuracy; **secondary:** training variance, false confident answers, reward exploit frequency. **Falsifier:** cooperative method fails transfer or depends on extra hyperparameter search.

**Sources:** [BRIDGE](https://proceedings.mlr.press/v306/chen26an.html) and [DAPO](https://arxiv.org/abs/2503.14476).

## One-page run manifest
```yaml
experiment_id: E03b
status: proposed # or executed / failed / verified / inconclusive
hypothesis: "..."
baseline_commit: null
variant_commit: null
source_model_revision: null
dataset_provenance: null
data_rights: null
train_data_sha256: null
test_data_sha256: null
evaluation_sealed_at: null
seed: 41
hardware: null
python_version: null
primary_metric: exact_temporal_accuracy
effect_threshold: null  # decide BEFORE hidden test
confidence_method: paired_cluster_bootstrap
evidence_level: E0
artifact_uri: null
failure_report: null
```
For any learned agent or source copy, include authorized tool permissions and original rights. Never mark tests "passed" without execution logs. Expected metrics here are proposals, **not results**.
