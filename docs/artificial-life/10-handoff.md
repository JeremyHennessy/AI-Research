# Artificial Life Research Initiative — handoff for the next pass
**Initiated:** 2026-10-08. Explicit authorization **research only**, confined to JeremyHennessy/AI-Research. Do not modify Ora, AgentTest or other repositories. No organism creation/deployment.

## Purpose and non-goals
Study computational systems that *might* self-maintain, reproduce with heritable variation, adapt, develop independent organizational complexity and perhaps later cognition **without predefined human tasks**. Not a chatbot, assistant, simulated personality, task-performing RL agent or visually convincing toy creature.

## Third literature pass: primary full-method reviews verified 2026-10-08
**Status:** still **research-only**, without digital organisms, virtual worlds, agent runs, copied confidential materials, training, or modification to Ora/AgentTest.

**New E2 reviews:** [Flow-Lenia 2025 v1](16-flow-lenia-2025-full-review.md), [PBT-NCA 2026 v2](17-pbt-nca-2026-full-review.md), and [ToLSim 2026 v1](18-tolsim-2026-full-review.md). Each main paper's methods, results, discussion/limits (plus ToLSim appendix) was examined using public HTML; no paper figure or code was independently reproduced. Their [E2 metadata receipts](../../data/alife/method-audits.jsonl) list sections and versions; the [source claim ledger](../../data/claims.jsonl) now has **43** records, including nine new explicit ALife claims.

**Central comparison:** [resource-normalized Flow-Lenia evolutionary activity reverses raw ranking; PBT-NCA's novelty is directly optimized; ToLSim's normalized 20-run tests fail despite raw cumulative trends](19-three-paper-methodology-comparison.md). These findings are *not* a proof that artificial life is impossible: all methods use finite simulations and operational choices.

**Numbers:** unchanged **183 papers / 30 tracks / 37 ALife papers**; total full-public-paper reviews **6** (ALife 5 + separate formal-verifier 1). No E3 reproduction in the repository. Existing **12 original hypotheses** and **8 planned ALife experiments** remain `not_tested` and `not_authorized`.

**Verification checkpoint:** GitHub `47dd59bf4de997e5d0e6508fee305973679bac3b` returned success in run `37778996123`: catalog validated, **46 offline unit tests** passed. Any subsequent navigation-only commits must also pass CI; the exact final head should be reported by the custodian in its completion receipt.

**Next most informative:** (1) Outlier cellular self-reproduction 2025 full methods and published corrections; (2) full ALIFE 2026 conference search and negative-results ledger; (3) verify Flow-Lenia 2025 exact code beyond older 2023 JAX precursor; (4) investigate neutral-shadow and mass-normalization methods on *existing published data only* after permission, without running an artificial organism; (5) reproduce *published results* only after separate explicit experimental authorization, if an organism/simulator would run.

## Second-pass research checkpoint (October 8, 2026)
**Scope remains research only; no organism/simulator/world built or deployed.** Expanded curated collection to **183** primary research records across **30** tracks, with **37** records linked to ALife source notes (30 initial, seven added here). Overall E2 source reviews now **three**: existing DeepSeek-Prover-V2; Taylor's 2015 OEE theory; newly deep-read [Liu & Sumpter 2018](12-chemical-replication-full-review.md). **No** independent E3 replication.

**New results:** [2026 counterevidence](14-negative-results-and-measurement-disagreements.md) on ToLSim partial open-endedness failure and NCA attractor-scale complexity; [public author-code audit](13-implementation-source-audit.md) pinned FlowLenia, PBT-NCA and chemical MATLAB releases with exact observed GitHub SHA/license status; [future-only verdict protocol](15-experimental-verdicts-and-separation.md). The original **12** hypotheses and **8** experimental designs retain status `not_tested` / `not_authorized`.

**Verified intermediate GitHub checkpoint:** code/content SHA `08272a10977be5e3e23d266ed9b9c402d2218579`, GitHub Actions run `37777425259` reported success for syntax, catalog and tests. Subsequent navigation/handoff changes require their own final CI run. The previous full Pass 1 baseline and approved evidence conventions remain preserved.

**Remaining blockers before E2 for other papers:** Flow-Lenia 2025 journal article's complete method/results unavailable in this inspection despite access to primary abstract and older JAX code; PBT–NCA README/config does not constitute full-text review; ALIFE 2026 proceedings not exhaustively audited. Zero live collection/API crawling, training or ALife execution was performed.

## First integration checkpoint
The main catalog was expanded from **146 to 176** records across **30** research tracks, with 30 ALife entries linked to original source records. The hypothesis and future-study machine-readable registries contain **12** and **8** proposed items respectively; their status remains `not_tested` / `not_authorized`. Read the main [README](../../README.md) and inspect the latest GitHub Actions run for a confirmed deployment-free documentation baseline. The previous pre-initiative commit `6cdecdaa79879be028c7b53d19b067c0b6cb4d54` and its passing workflow `37773603738` remain reference checkpoints, not a rollback instruction.

## Initial work and materials
- Dedicated [artificial-life atlas](README.md) linking scientific foundations, systems, five architecture families, emergent bottlenecks, cross-system evaluation, twelve original hypotheses, future staged experiments, literature and contrary cases.
- Main catalog holds one record per unique paper; the ALife notes table connects to canonical paper IDs, **not copied second publication records**.
- One ALife source, [Taylor (2015)](https://www.tim-taylor.com/papers/taylor2015requirements.web.html), was read as a complete theoretical text and may be tagged E2 after the catalog method/caveat review is preserved. Others at E1 unless full methods verified.
- Important recent primary sources: [Flow-Lenia 2025](https://arxiv.org/abs/2506.08569), [Outlier binary CA 2025](https://doi.org/10.1162/artl_a_00449), [PBT–NCA 2026](https://arxiv.org/abs/2604.11248), [MSPD 2026](https://arxiv.org/abs/2606.17091).
- Existing compendium still supplies related [world models](../13-memory-world.md), [continual learning](../22-ai-field-map.md), [causal representation](../23-interpretability-and-causality.md), [agent reliability](../34-multiagent-reliability.md), [evaluation](../06-evaluation.md) and [security](../24-alignment-and-security.md).

## What has **not** been done
- No new artificial organism, virtual environment, cellular dynamics, executable simulator, self-evolving agent or AI training weights.
- No experiment demonstrates autonomous life, open-ended indefinite evolution, self-awareness or new intelligence.
- No exhaustive OpenAlex/Crossref/Semantic Scholar or ALIFE 2026 proceedings crawl; current paper corpus is hand-screened primary sources.
- No comprehensive reproduction of Tierra, Avida, Lenia, Flow-Lenia, NCA, artificial chemistry or POET.
- Source licenses/availability recorded as *not yet assessed* unless specifically checked. Full texts not copied wholesale.

## High-value next source tasks
1. **Primary complete-paper methodology E2:** 2025 Flow-Lenia (mass conservation discretization; parameter embedding; survival resources; metrics and controls).
2. **Independent evaluation:** Outlier (2025) two-scale replication, lineage vs shape, source code and seed reproducibility.
3. **2026 PBT–NCA:** full search objective, its hand-designed "novelty" and "diversity", long-horizon behavior and failure modes; verify sample counts.
4. **Artificial chemistry:** Liu & Sumpter reaction-model assumptions, GARD composition inheritance, protocell organizational closure.
5. **Historical experimental baselines:** Tierra source/configs, Avida source and experimental ecology; do not run untrusted legacy code blindly.
6. **ALIFE 2026:** conference proceedings, independent negative/corrective papers, status of recent theory on computational agency.
7. **Cross-substrate metrics:** find neutral evolutionary activity tests, operational definition of individual and robustness under resource/inheritance ablations.
8. **Full source dedup:** arXiv 2506.08569 has journal DOI 10.1162/artl_a_00471; treat as one work with multiple manifestation IDs, not separate papers.

## Scientific review gates
- For each paper: authors, exact date/version, source link, original method, experiment type, results attributed to authors, known limitations and independent replications. E2 only after entire methods/results/limits reviewed.
- For any proposed self-maintenance: perturb+knockout vs inert attractor; for inherited evolution: parent/offspring fidelity vs randomized lineage; for OEE: multiple definitions and independent functional novelty.
- For any eventual experiment: pre-register hypotheses, null controls, rights, budget, exact run code/hash, environment source, evaluator and stop criteria. Research-only authorization prevents actual implementation.

## Maintainer and task custody
Read [main README](../../README.md), [project log](../../data/research-log.md), and [this index](README.md) before any consequential edit. Preserve existing approved work. Check main SHA, latest CI, and previous source review before adding papers. Do not create a second task/custodian without explicit user request—the existing daily AI Research Custodian covers research continuation.

**Status field:** update this file with exact final main SHA and GitHub Actions result once subsequent integration/catalog validation is complete; do not assume success from a git commit alone.
