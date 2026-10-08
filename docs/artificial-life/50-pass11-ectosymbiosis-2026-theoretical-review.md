# Pass 11 E2 — Krishnan et al. (2026): metabolic self-inhibition and host-initiated ectosymbiosis

**2026-10-08 | Complete original accessible PLOS Computational Biology main-text method/theory audit, E2, no numerical replication.** Source: Nandakishor Krishnan, István Zachar, Ádám Kun, Chaitanya S. Gokhale & József Garay, *Host-initiated microbial association leads to stable ectosymbiosis in an ecological model*, *PLOS Computational Biology* **22**(9):e1014699, published **September 2, 2026**. [DOI](https://doi.org/10.1371/journal.pcbi.1014699) · [publisher HTML](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1014699). Publisher says **CC BY 4.0**, Mathematica v14.3 notebook is in Supporting Information; supporting notebook/equations as image renderings were not independently executed/verified.

## Authors' actual causal argument

Starting with **already existing** free-living syntrophy:
1. Host species **X** consumes externally replenished resource **W** and emits metabolite **U** that inhibits **X** at high concentrations.
2. Another species **Y** consumes U, reducing local inhibition; Y also emits inhibitory metabolite **V**. Interacting as free-living populations is assumed to work at a stable resident state.
3. A mutant host **Z** with a cell surface that **already can bind Y** arises (the existence of this mutant and its binding function are **assumed**, not spontaneously discovered during a simulation).
4. Bound ectosymbionts shield the host from its own waste U, providing a *private inhibition-reduction* advantage that may offset the extra surface-binding/reproductive costs and reduced uptake.
5. By analyzing equilibrium stability and invasion fitness of a system of differential equations, the paper identifies ecological regimes in which the consortial form displaces free-living hosts.

The proposed innovation is not an externally assigned reward for cooperation, but a possible **consequence of resource and self-inhibition dynamics within the authors' chosen model**. It is still a heavily specified ecological model with selected assumptions.

## Explicit supplied operations vs demonstrated outcome

| Supplied in model | What is mathematically analyzed | What remains open |
|---|---|---|
| Fixed species X,Y; linear resource-use growth; constant external W concentration | Feasible resident equilibrium | Chemical origin of metabolism/resources |
| Two preassigned self-inhibiting metabolites U,V, decay and concentrations | Whether Y consumption reduces X's inhibition | Whether these particular conditions occur frequently naturally |
| A **pre-existing Z mutant** that inherently binds Y to its surface | Invasion conditions for Z into X+Y | The actual origin of binding structure |
| Consortial host already assumed to reproduce with random assortment of attached Y | Stable consortial mutant replacement | Co-transmission mechanism and causally viable daughters |
| Higher-level population entity defined as Z-bound Y | Potential ecological stability of association | Reproductive cohesion, higher-level heredity and organelle formation |

Direct from main paper's discussion: **"this transition remains to be seen either in the lab or in simulations"** with regard to vertically inheriting ectosymbionts and a new higher-level unit of selection. Interpret their stable ecological coexistence/invasion result as **not** an observed multi-generation emergent individual.

## Method-level details checked
- Hosts acquire replenished food W and excrete waste U. Growth inhibition is nonlinear/Monod-like; equations follow population densities and metabolite levels in continuous time.
- Resident one-species, then two-species ecological equilibria precede analysis of rare Z mutants; authors assume their mutant appears when the resident ecosystem is at stable equilibrium, with negligible back mutation.
- Y metabolites dilute in available habitat volume; attached-Y benefit incorporates **local exposure reduction** to U and **host resource-surface loss** as an explicit cost; attached symbionts' own reproduction/dissociation are **not modeled explicitly**.
- Population-level selection and evolutionary stability are checked analytically plus Mathematica numerical plots. Published notebook is not independently executed. The authors evaluate possible nonlinear parameter sensitivity, but do not empirically sample biological genotypes or claim a universal positive rate of transition.

## Comparison with actual induced fungal study and biological failures

- [Giger et al. 2024](49-pass11-induced-endosymbiosis-2024-full-review.md): *physical* paired cells were produced through deliberate injection and selected inheritance, but **the association still washed out in 4–5 rounds after selection withdrawal**. Not evidence this theoretical ectosymbiotic route necessarily persists physically.
- [Rose 2020](45-pass10-pseudomonas-life-cycle-2020-full-review.md): separated or mixed propagules affect group reproduction independently of component fitness. A model of Z invasion cannot substitute for that reproductive evidence.
- [Pauli 2022](https://doi.org/10.1038/s41467-021-27630-9) and [Melero-Jiménez et al. 2025](https://doi.org/10.1038/s41467-025-58742-1): mutualistic cross-feeding can lower adaptive robustness and select a partner to become autonomous, respectively. These studies have materially different biological substrates and stressors; they are **contrary evidence** against a simplistic 'dependence always stabilizes' conclusion.

## New experimentally falsifiable proposal (UNTESTED, not authorized)

**Tension:** contact can improve local metabolic economics without securing reliable collective offspring.

A high-value future comparison would separate **ecological adhesion advantage** from **reproductive co-transmission**:
- Hypothesis E: selecting for local toxic-product buffering increases Z occupancy but does not necessarily improve child groups' retention of Y.
- Hypothesis H: if a lineage evolves active **partner distribution to its offspring** (not assigned by externally imposed random assortments), mutual dependence can become more reliably heritable.
- Control: preinstalled daughter-pair copy API vs unchanged metabolite ecology without co-delivery; measure offspring survival and change under withdrawal of external enrichment.
- Negative: Z dominates ecologically but next-generation Y distribution is random, short-lived, or externally reconstructed, yielding no novel organismal inheritance.

**Claim boundary:** No living/computational system or artificial intelligence was trained, deployed or demonstrated by this theoretical study or by AI-Research. E2 denotes complete main-paper reading, not validation of the Mathematica results or scientific guarantee.
