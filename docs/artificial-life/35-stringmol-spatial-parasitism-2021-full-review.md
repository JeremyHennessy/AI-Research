# Spatial Stringmol and parasite-driven replicator complexity (2021) — E2 primary paper review

**Reviewed 2026-10-08. E2 means main published article methods/results/discussion inspected, not independently reproduced.** Simon J. Hickinbotham, Susan Stepney, Paulien Hogeweg, *Nothing in evolution makes sense except in the light of parasitism: evolution of complex replication strategies*, **Royal Society Open Science** 8:210441 (2021). [Published article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8334846/), [DOI](https://doi.org/10.1098/rsos.210441); journal article CC BY 4.0. [Study dataset](https://doi.org/10.15124/305dfdb6-9483-4c5b-8a01-c030570b9c31) and supplementary PDF **not independently reviewed**, and no scientific code was executed.

## Experimental provenance
- **20 independently seeded runs**, 12 extinct, eight active at **2,000,000 timesteps**. Authors' world-level results, not an estimated universal extinction probability.
- Toroidal **12,500-cell grids**: 10 trials at `100×125`, 10 at `250×50`; initial locations either contiguous 10×10 block or paired seeds at 50 random sites (10 trials per placement). The combined **2×2 design has five trials per cell**.
- **100 hand-coded ancestor replicators**, so this experiment is **not** origin from an unseeded soup.
- Copying uses Stringmol with **33 opcodes (seven functional, 26 no-ops)**. Binding uses probabilistic sequence matching; only Moore-neighborhood binding allowed. Products must land in local empty cells or are discarded. Decay, mutation and virtual-machine instruction semantics are supplied by the simulator.
- Authors name **Stringmol 0.2.3.4** and Rstringmol **0.3.1**. Tagged [Stringmol source](https://github.com/uoy-research/stringmol/tree/0.2.3.4) resolves to commit `aa6c7301822a93b74ad60b46437515ef6804784f` and has a root **GPL v2** license. The tag's old README still calls itself 0.2.2: preserve that inconsistent prose, use exact tagged SHA.
- [Rstringmol](https://github.com/uoy-research/Rstringmol) inspected source head `8d059beaf3ed4ca17c2edddda9ad56efb6f28118`: root README identifies an R analysis package; currently inspected DESCRIPTION says version **0.1.0**, contains an unfinished license field and there is **no verified v0.3.1 tag**. Thus the published analysis version is **not pinned for independent replay**.

## Causal mechanisms actually reported
1. **Parasite emergence:** a short non-copying string gains a replication advantage when copied by a longer active replicator. Spatial host wavefronts can persist as hosts colonize empty space while parasites follow behind; early collapse occurs in 12/20 worlds.
2. **Non-complementary binding:** short parasites bind one another instead of exclusively seeking host copies, reducing their competitive advantage. This is change to string sequence/binding, **not to the interpreter's base opcode semantics**.
3. **Self-scan:** an evolved replicator writes over its own instructions before copying a partner. This slows both host and parasitic replication, reducing the benefits of very short parasite genomes. Its extra use of the copy operator roughly **doubles mutation opportunities** on some paths—an evolved behavior causing altered mutational effects without explicitly changing the base mutation engine.
4. **Partner checks/execution toggles:** replicators redirect execution between paired molecules and demand complementary partner behavior before exposing the copying loop. New parasites tend to arise repeatedly from mutated replicator lineages and may temporarily evade defenses.
5. **Emergent large rearrangements:** incorrectly positioned copy/cleave commands can rearrange long strings in one reproduction event even when the primitive mutation operator makes only small changes.

The authors additionally describe occasional **hypercycles**, where A copies B and B copies A. "Replicator" and "parasite" are **relational**, not immutable labels attached to single genome strings.

## Methodological limitations and needed future falsifiers
- **Survivor bias:** most dynamics plots focus on the eight surviving worlds; twelve extinctions must remain visible in every comparison. Grid geometry and initial placement alter opportunities for protective spatial waves.
- **Fixed code physics:** VM operations, decay, collision, local capacity and mutational primitives were designed; the experiments do not show new executable *primitive* semantics, autopoietic membranes or emergent intelligence.
- **Detection versus runtime:** formal reaction-category analysis disables mutation to classify deterministic pairwise outcomes; this does **not** represent every stochastic process during the runs.
- **Causal interpretation:** source includes mechanistic traces and comparisons, but the full 20-run published configuration does not include a separately preregistered matched 20-run **no-parasite knockout arm**.
- **Wet-lab transfer:** authors observe that parasites repeatedly originate from replicators rather than as long independent parasite lineages in their model. Real [Furubayashi et al. eLife 2020](https://doi.org/10.7554/eLife.56038) RNA experiments display both lineages and interactions. Mechanisms should not be generalized to biology without independent evidence.
- **Time bound:** 2m steps is a finite experimental cutoff; continuous pattern generation cannot establish indefinite new functional innovation.

**Future-only controls (NOT IMPLEMENTED):** parasite-present versus parasite-blocked equal-resource ecology; self-scan/toggle/binding ablations; unseen parasite variants as independent challenge; copy fidelity/interpretation fidelity separated; viable daughters/granddaughters and process-based lineage; full trial-level extinction and resource/time distributions. A defense that only recognizes ancestral parasites or fails environmental transfer refutes the broad functional-innovation hypothesis.

**Evidence level E2:** original main paper fully read, tagged author source/readmes inspected as metadata. Raw experimental logs, supplementary methods and actual program outputs not independently checked. [2016 theory and shortcut audit](36-banzhaf-2016-open-ended-novelty-full-review.md); [cross-study synthesis](37-parasite-and-shortcut-synthesis.md). No artificial organisms were created or run by this research repository.
