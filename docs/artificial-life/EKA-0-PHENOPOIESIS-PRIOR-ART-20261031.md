# EKA-0 selective prior-art note — supplied heritable patterns versus naturally evolved information processing

**Reviewed:** 2026-10-31; **corrected against the actual v2 HTML on 2026-11-01**. **Evidence level:** direct reading of public preprint methodology and result tables; no independent rerun, code reproduction, peer-review certification or Ora experiment. **Decision:** EKA feasibility **UNKNOWN**; new scientific population **NO-GO**.

## Exact primary source

Nam H. Le, *Organisms Write Their Own Evolution: Direct Epigenomic Inheritance Accelerates Learning on Compositional Tasks*, arXiv:2602.00978 **v2**, revised **2026-10-09**, https://arxiv.org/html/2602.00978v2 (source §§3.1–3.4, 4.1–4.3, 5.3). This is a **preprint**. The former note's "post-switch recovery of 28.4/14.7/8.3 generations", "genetic-weight write-back" and §§4.2/5.2.2 attributions were **incorrect for v2** and are withdrawn; do not use them.

## What the v2 model actually supplies and reports

The developer supplies three fixed algorithms and a 10×10 binary pattern task, rather than evolving the ability to learn. Gene-only (GENE) mutates a 100-bit genome without learning. BALDWIN and Phenopoiesis (PHENO) each perform **20 within-life learning trials** using the same random-activation rule and both pass mutated genetic genomes to offspring; only PHENO additionally **inherits its learned 100-bit epigenome unchanged** (100% fidelity). PHENO writes learned activations into the epigenome, **not** into genetic weights (§3.2, Table 1). There are six fixed tasks, 50 organisms and 150 generations per run, 30 replicates per algorithm/task (§3.3). Do not describe these runs as environment-switch recovery.

The author reports final-fitness comparisons (§4, Tables 2–3): on individual patterns, BALDWIN and PHENO both score 1.0, while GENE averages 0.56–0.59. On L+T, BALDWIN 0.254±0.196 versus PHENO 0.772±0.075; on T+Plus, 0.086±0.123 versus 0.517±0.000; on L+Plus, 0.177±0.149 versus 0.189±0.156 (reported p=0.789, no significant difference). These are **author-reported model fitness results**, not measurements of adaptation, energy or survival in Ora. The paper's PHENO–BALDWIN contrast **does** deliberately vary inherited learned epigenomic state while keeping the specified genetic mutation and learning-trial counts aligned; the earlier claim that only PHENO updates genes was false.

## Direct source-level falsifiers and limits

1. **Task/scoring loophole (new deterministic observation).** The paper defines fitness as `|P ∩ T| / |T|` and explicitly does **not** penalize non-target cells (§3.1, Eq. 1). Any phenotype activating all 100 cells therefore scores **1.0 on every task**, including every composition, under the stated metric. The 100-bit cell-activation representation and union phenotype allow that bitmask (§§3.1–3.2). This is a **mathematical reference**, not proof that random mutation/learning reaches it cheaply. At minimum, the paper's §4.3 assertion that L+Plus is *geometrically impossible to satisfy* does not follow from its described union-plus-recall task. A fixed/all-on, cost-aware or precision-penalized comparator is needed before treating the reported fitness gaps as a strong novelty claim.
2. **Engineering is supplied, not naturally originated.** PHENO's within-life learning rule, 100-bit inherited epigenome, deterministic read/write semantics and perfect-fidelity copying are **designed into the model**; no ordinary mutation path evolves those capabilities. Author-reported gains consequently do not demonstrate mutation-originated learning in Ora.
3. **No Ora-style resource accounting or causal decomposition.** Matching 20 learning trials is not matching memory storage/lookup, copy, reproduction, energy/material, survival or compute cost. This comparison does not include separately cost-matched inherited-fixed patterns or ablations that isolate which retained bits matter under unseen tasks. No native Ora VM, COPY/division or live descendant fitness was measured.
4. **Source internal consistency.** The v2 abstract says all three algorithms are equivalent on simple tasks, while §4.1/Table 2 reports that only **BALDWIN and PHENO** are equal and GENE is substantially lower. Interpret the actual table and specified pairwise contrast, not the broader abstract sentence.

The paper is relevant prior art for **developer-provided vertical transmission of acquired patterns**; it is not evidence that such a transmission rule can emerge unaided or pay its full lifetime price. These are **source-level criticisms only**, not a replication, allegation of misconduct or global refutation of heritable learning.

## Smallest discriminating Ora question

Can ordinary mutations in the existing compact VM produce an information-read/write rule absent from the founder; express it before death; acquire an **actual personally observed** older target; afford every action and ordinary paid offspring; transmit effective code or information; and beat equally cheap **stay-put, fixed-port, latest-successful-port, finite-state and sham/erasure** controls on preregistered unseen histories? Require prefix-funding, mutation reachability, all attempted births/deaths as denominator, and no privileged founder, selected seed or artificially required travel. Distinguish genetic learning capacity, acquired individual state, effective SELFWRITE and cultural transmission.

**Boundary:** No new ecology, VM/ancestor change, re-costing, seed bank, Context90 rerun, PILOT74 build, native admission, assistant change or Observatory claim. Preserve sealed failures and EKA **UNKNOWN / NO-GO**.

**Related owned work:** [Ora scientific issue #313](https://github.com/JeremyHennessy/Ora2.0/issues/313), [AI-Research issue #62](https://github.com/JeremyHennessy/AI-Research/issues/62), [Codex-owned critique PR #63](https://github.com/JeremyHennessy/AI-Research/pull/63). Only this custodian-owned document is revised.
