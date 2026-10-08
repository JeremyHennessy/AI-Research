# AI Research Atlas — start here
Updated: 2026-10-08 | ALife research addition | Status: **197 research records across 30 tracks, fifteen full-paper/theory reviews; no artificial organism or trained model**

## New ecological evidence: costly inherited defenses versus engineered simulation shortcuts
The [2021 spatial Stringmol full-paper audit](artificial-life/35-stringmol-spatial-parasitism-2021-full-review.md) examines **20 author-run virtual worlds, 12 extinctions and 8 surviving trajectories** with new parasite defenses that often slow copying. The [2016 Banzhaf full theoretical audit](artificial-life/36-banzhaf-2016-open-ended-novelty-full-review.md) separates those **within-world evolved behaviors** from platform-supplied individuality, replication and fitness. The [paired synthesis](artificial-life/37-parasite-and-shortcut-synthesis.md) and [current handoff](artificial-life/38-pass7-research-handoff.md) preserve alternative explanations and future-only falsifiers. Neither paper proves a self-maintaining digital organism.

## Latest: when evolutionary novelty is only in the observer's model
The [Stringmol 2020 complete eight-page study](artificial-life/30-stringmol-2020-novelty-full-review.md) distinguishes internally available code modifications from **extrinsic** scientific reclassification, including its reaction-network type-2 example. This becomes central to the [12-case failure mechanism ledger](../data/alife/failure-modes.jsonl), [three competing research-only candidate architectures](artificial-life/33-three-pathway-critical-experiments.md), and [ALIFE 2026 Physis evidence-boundary review](artificial-life/31-physis-2026-source-boundaries.md) (full booklet not inspected, remains E1).

## Deep research: evolving the interpreter rather than only the program
The [four new E2 technical reviews](artificial-life/29-evolvable-semantics-cross-study.md) trace a key artificial-life challenge from **Physis (2003)** through **Stringmol (2016–2017)** to Stepney's **2025 requirements/design/implementation** framework. Heritable changes to an intermediate instruction interpreter and viable molecular expressor/copy machinery have been reported, **but no independently verified continued functional innovation or self-maintaining organism is demonstrated**. The 2026 Physis meta-chemistry late abstract and 2020 novelty conference abstract remain **E1**. Research-only; no simulator or organism executed.

## New causal-replication and organization research
The [original Outlier paper](artificial-life/20-outlier-original-2025-full-review.md) and [2026 independent causal-lineage study](artificial-life/21-outlier-causal-selfhood-2026.md) now receive E2 evidence reviews; the latter documents multi-generation branching causal replication without proving heritable functional innovation. [Stepney and changing-language research](artificial-life/22-engineering-life-and-transformational-novelty.md) remain E1 where only author abstracts were inspected. The [10-criterion evidence standard](artificial-life/23-unified-organism-evidence-standard.md) distinguishes repeatable motion, branching offspring, functional heredity, self-maintenance, agency and open-endedness, with no single "life score". See [next research priorities](artificial-life/24-research-priorities-after-outlier.md).

## New research direction: digital living systems
[Artificial Life, Emergent Intelligence, and Digital Organisms](artificial-life/README.md) investigates whether computational processes can originate and sustain life-like organization, adaptation, heredity and ecological evolution without being another human-targeted LLM or assistant. It distinguishes real maintenance and lineage innovation from convincing animation. Five competing research-only substrates, [criteria](artificial-life/05-evaluation-framework.md), [12 falsifiable hypotheses](../data/alife/hypotheses.jsonl) and [future study designs](artificial-life/07-experimental-roadmap.md) are documented; **none is implemented**.

The [three-paper comparison](artificial-life/19-three-paper-methodology-comparison.md) now contrasts **resource confounding in Flow-Lenia**, **designed novelty objectives in PBT-NCA**, and **neutral-shadow correction in ToLSim**. Full source-method reviews: [Flow-Lenia 2025](artificial-life/16-flow-lenia-2025-full-review.md), [PBT-NCA 2026](artificial-life/17-pbt-nca-2026-full-review.md), [ToLSim 2026](artificial-life/18-tolsim-2026-full-review.md). No scientific experiment was run by this literature review.

## In 60 seconds
**Objective:** discover a measurable improvement in intelligence per dollar, per token, per joule, or per interaction; do not confuse a bigger benchmark score with general intelligence.

**Five working bets (hypotheses, not findings):**
1. Better verified data and curricula can outperform naive increases in tokens.
2. Adaptive inference and external verification improve difficult reasoning at controlled cost.
3. Structured persistent memory and retrieval outperform infinitely growing conversation context for some long-horizon tasks.
4. Learning environment dynamics and actions helps transfer better than text-only imitation on interactive tasks.
5. Hybrid architectures may offer useful latency/context/quality tradeoffs, but must beat strong attention baselines.

## Updated reading map
Start with the [Pass 4 research atlas](29-pass4-index.md) → the [25-track AI field map](22-ai-field-map.md) → the [197-record primary-source catalog](19-paper-index.md) → [lab training recipes](11-open-training-recipes.md) and [cross-domain dossiers](23-interpretability-and-causality.md) → [experiment plans](26-experiments-cross-domain.md). The [source claim ledger](../data/claims.jsonl) preserves exactly what is claimed, by whom, and with what caveat. The [discovery pipeline](20-collection-pipeline.md) identifies source metadata across three services and deduplicates by stable identifiers. See [research disagreements](35-research-disagreements.md), [proposed experiments E23–E28](36-pass4-experiments.md) and the [Pass 5 plan](37-pass5-handoff.md).

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
