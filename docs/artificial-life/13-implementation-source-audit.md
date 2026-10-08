# Implementation and reproducibility audit: Flow-Lenia / PBT–NCA / artificial chemistry

**2026-10-08.** We inspected publication abstracts and public implementation READMEs/configuration files. This is **NOT** a reproduction, full-method audit of Flow-Lenia/PBT papers, or authorization to execute a self-evolving world.

## Frozen source inventory (GitHub public repository metadata inspected)
| Related paper | Author code link | Branch head inspected | What's observable | Rights and execution |
|---|---|---|---|---|
| [Flow-Lenia](https://arxiv.org/abs/2212.07906) | [erwanplantec/FlowLenia](https://github.com/erwanplantec/FlowLenia) | `dce428c6b0c5079a06e5606fb7b5ac1fe1323bc5` (main) | JAX source `flowlenia.py`, `flowlenia_params.py`, examples and state `A` or `A+P` | No root LICENSE found at inspection; **do not assume a license**. Not executed |
| [PBT-NCA, 2026](https://arxiv.org/abs/2604.11248) | [arberzela/pbt-nca](https://github.com/arberzela/pbt-nca) | `7eb61b6a240db6ae53fd044d8906c2633af0503c` (main) | Population training loops, configs, source, SLURM scripts and method-aligned controls | Root `LICENSE` is **MIT**, ©2026 Arber Zela. Repo includes optional trained external model/data dependencies; not executed |
| [Liu–Sumpter chemistry 2018](https://doi.org/10.1074/jbc.RA118.003795) | [yuernestliu/Self-replication-simulator](https://github.com/yuernestliu/Self-replication-simulator) | `0cbebf18e3d632a5d5349bf270b32e8f7abdec1a` (master) | MATLAB ZIP; README names `sim_general.m`, `SpecificSys.m`, `recordT`, `recordN` and MATLAB R2017b+ | Paper CC BY; associated code license unknown. No archive extracted or executed |

**Immutable SHA** documents which version of the public code we *inspected* from metadata, not that these source repositories were cloned, executed or fully reviewed for vulnerabilities.

## Flow-Lenia: concrete source file map
The author README discloses:
- `flowlenia/flowlenia.py` contains `Config`, `State(A)`, `FlowLenia` update/kernel/rule space;
- `flowlenia/flowlenia_params.py` has `Config_P`, `State(A,P)` and parameter-embedding dynamics;
- `examples/FlowLenia.ipynb`, `examples/example_1C.py`, `examples/example_2C.py`, `examples/parameter_embedding.py` demonstrate variations.
- Repo is **JAX** and uses GPU acceleration when available.

**Scientific issue:** "parameter embedding" lets local rule parameters coexist and move/affect flow, but it does not by itself establish a **genetic lineage** or robust inherited functional innovation. Determine how `P` evolves, diffuses/advects and is transmitted through physically detected splits; no true heredity proof exists in the read README.

**Outstanding review items:** check exact discretized mass conservation, conservation residual under boundary conditions, movement/advection numerical error, phenotype segmentation and evolutionary activity metric definition. The 2025 [journal article](https://doi.org/10.1162/artl_a_00471) and [preprint](https://arxiv.org/abs/2506.08569) are one scientific work with multiple manifestations, not two independent replications.

## PBT–NCA: what is selected externally
Official README describes:
1. Train and score populations of competitive NCA worlds;
2. Archive behavior descriptors with FIFO historical novelty;
3. DINOv2-based visual diversity;
4. Exploit/explore: replace weaker worlds with mutated/crossed descendants.

**Public `configs/slurm_h100_pbt_scale_small.json` (inspected blob SHA `3091cd31731c9809e93d41d21a80cf6c8fd8ccd4`):** `grid_size=[128,128]`, `n_ncas=3`, `cell_state_dim=4`, `hidden_dim=64`, Adam `learning_rate=0.0003`, `batch_size=8`, `pbt_population_size=30`, `pbt_meta_iterations=500`, `pbt_world_horizon=12`, `pbt_exploit_interval=5`, `pbt_replace_fraction=0.25`, `pbt_archive_size=512`, `pbt_novelty_k=8`, `pbt_inheritance_mode="lamarck"`, `pbt_complexity_weight=0.5`. These are **snapshot parameters**, not confirmed runtime behavior for each paper figure. Many other knobs and scripts choose different options.

**Crucial reproducibility detail:** the config lists `n_seeds=4` (likely distinct from experiment repetitions); the author README says the paper's SLURM arrays run **three independent seeds** `--array=0-2`. Do not conflate the two. The published README names:
- combined history novelty + DINOv2 selection;
- DINOv2-only selection;
- VLM prompt-based selection;
- handcrafted-descriptor selection;
- random-resampling control **without selection**;
- single PD-NCA baseline at matched total training compute.

In the observed small config `pbt_vlm_enabled=false`, although other experiments enable VLM-based criteria. The overall architecture is **outer-loop designed novelty selection and resource/world training**, not a demonstration that a virtual organism internally chooses to stay viable without externally optimized signals.

**Priority checks before E2:** inspect actual `src/train.py` objective, descriptor code and seed scripts; reconcile paper version, selection weights and table values; verify control compute matching beyond README; independently validate whether "spore-like" and "amoeboid" visuals correspond to reproduction/heredity, functional adaptation or merely appearance. No experiment here ran that code.

## Replication/readiness comparison
| Study | Source access | Actual data/model artifact reviewed? | Primary blocker | Best *future* discriminator |
|---|---|---|---|---|
| Liu 2018 chemical chemistry | Full public paper + MATLAB ZIP link | Read main article and README; **not** ZIP | No independent reproduction; infinite reservoir and simplified species | Finite resources/feedback knockout + organizational lineage |
| Flow-Lenia 2025 | Published abstract + older public JAX code | README and file map, not full paper/code executions | Conservation/heritability measurements not audited | Mass residual, true functional inheritance after splitting |
| PBT–NCA 2026 | Preprint abstract + MIT-licensed public code and config | README and JSON only; no training | Outer novelty selection and effects not separated | No-reward and nonvisual functional-innovation controls |

**Important:** A public GitHub repository with executable code is not an empirical claim until the specific revision reproduces a result, with identical hardware, data, seeds, dependencies and trusted graders. Legacy scientific code is untrusted; do not run it automatically.

## Next scholarly/reproduction pass (research only)
- Collect published **negative** Flow-Lenia inheritance findings or explicitly record if none identified.
- Verify equation/figure details in Flow-Lenia 2025 and PBT–NCA paper beyond author abstract.
- Check exact repo LICENSE and model asset rights at pinned commits before legal archival.
- Design no-visual-fitness evaluation protocol using independent function assays and lineage tracking.
- Review reported three seed runs statistically; rare emergent events may require much more sampling.
- Record **research receipts**, not unverified claims of an implemented digital creature.

Source citations: [Flow-Lenia public JAX repo](https://github.com/erwanplantec/FlowLenia), [PBT–NCA MIT code](https://github.com/arberzela/pbt-nca), [chemistry simulator MATLAB archive](https://github.com/yuernestliu/Self-replication-simulator).
