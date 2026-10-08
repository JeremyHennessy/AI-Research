# E2 full-paper review — Hickinbotham et al. (2016), automata-chemistry adjacent possible

**Evidence:** E2 complete accessible 29-page accepted author manuscript, research review only. **Article:** Simon Hickinbotham, Edward Clark, Adam Nellis, Susan Stepney, Tim Clarke, Peter Young, *Maximizing the Adjacent Possible in Automata Chemistries*, *Artificial Life* 22(1):49–75 (2016), DOI [10.1162/ARTL_a_00180](https://doi.org/10.1162/ARTL_a_00180). **Access:** [White Rose accepted author manuscript](https://eprints.whiterose.ac.uk/id/eprint/114475/1/alifej_16.pdf) and [journal source](https://direct.mit.edu/artl/article/22/1/49/2837/Maximizing-the-Adjacent-Possible-in-Automata). **Rights:** accepted manuscript institutional record states reuse/reproduction not automatically licensed. Only original scientific notes are stored; no PDF was copied to the repository. No Stringmol code was executed.

## I. The paper's crucial distinction: evolving biology B within fixed physics P
The authors distinguish a **physics/substrate** layer `P` from a mutable **molecular biological** layer `B`:
- `P` comprises the simulator's instruction semantics, scheduling, container and elementary operations; it is still **designed and fixed**.
- `B` comprises strings/program composition, including binding and copying sequences that can mutate, interact and be selected.
- A system allows more variation when many composite behaviors live in `B`, but it does **not** mean `P` itself is unrestrictedly evolvable.

Three design principles:
1. **Everything Evolves:** express as much function as feasible using evolvable molecular sequences, not nonheritable interpreter primitives.
2. **Everything's Soft:** binding and action selection can be stochastic/probabilistic instead of Boolean, allowing mutation pathways and reduced lethal overbinding.
3. **Everything Dies:** component destruction/decay means maintaining a population requires ongoing reproduction; otherwise static processes can persist forever.

These are author **engineering principles**, not empirically proven sufficient conditions for an autonomous living system.

## II. Stringmol execution and seed conditions
- Molecules are strings of opcodes, with templating/matching regions and pointers for reading/writing, execution flow, and partner binding.
- The seed **replicase is explicitly hand-designed**, about **65 opcodes** long, with separate binding/junk/reaction regions; its production of another molecule requires about **240 execution steps** under source's described configuration.
- Standard replication involves a `=` copy operation, moving pointers, programmatic cleavage and release. When copying, substitutions/insertions/deletions occur with assigned probabilities (example substitution rate `p_s=10^-5`), all external design choices.
- A random collision/binding policy and decay process are imposed by the simulated chemistry. The world is **not** a spontaneous origin-from-no-seed experiment.

## III. Controlled findings: three design choices and their unintended outcomes

### A. Replication and evolutionary interaction
The authors summarize **1,000 seed-replicase trials**, including parasitism, succession, drift and dependency. They report **eight** trials with emergent two-species hypercycles, six of those displaying extended sweeps; 15 labeled spontaneous and 14 multi-species hypercycles in the source's categorized experiments. **Do not sum these into a single nonoverlapping success percentage:** the categories and historical experiments need careful interpretation. A two-species codependence is interesting, but neither proves organism-level metabolic closure or expanding cognition.

### B. Stochastic molecular binding versus a deterministic sticky control
**Experiment:** 100 trials of each of two binding designs seeded with **300 replicase molecules** and **10 parasites**, terminated at extinction or 500,000 steps.
- Probabilistic Stringmol: **32 of 100** cases evade an otherwise potentially fatal parasite.
- "Sticky" deterministic-binding control: **0 of 100** evade.
- The paper reports Mann–Whitney **p≈5.34×10^-5** and **A effect-size≈0.638** for the distributions of QNN (quantitative non-neutral evolutionary activity), which is **not identical** to the discrete 32/100 parasite-evasion rate.
- **Interpretation:** stochastic binding can alter selective opportunities, including reduced parasite access and evolved resistant molecules in this specific setup. It does not follow that universally increasing randomness improves evolvability.

### C. Molecular decay policy selects exploitative behavior
Four decay designs tested with 100 trials each (some limited to one million steps):
1. Inversely length-based decay, unbound molecules only.
2. Fixed decay, unbound molecules only.
3. Inversely length-based decay, **all** molecules including bound pairs.
4. Fixed decay, **all** molecules.

**Results and adverse mechanisms:**
- Protect **bound** molecular pairs → a pathological endlessly looping complex can become effectively immortal while performing no useful replication.
- Reward **longer** molecules with slower decay → selection favors very long programs; population size and CPU workload can rise **quadratically**, making analysis impractical.
- A fixed uniform decay across all molecules is computationally tractable, but decay semantics are located wholly in **fixed physics P**: the organism cannot evolve a new relationship between its composition and its decay susceptibility.
- The authors note an overall **fitness/novelty-proxy dilemma**: external constraints intended to foster evolution are themselves subject to gaming by simulated replicators.

This is particularly important for the digital-life program: a paper-reported *survival advantage* can be a **selection loophole**, not increased organismal function.

### D. Making an opcode more granular
The researchers decomposed one compound copy instruction into finer-grained read/write pointer operations, testing **Granular Stringmol**. The original fixed `=` effectively becomes a sequence with separately mutable pointer increments (e.g. `=+A+B`).

This increases potential composability but can make each reproduction more expensive and alter mutation opportunity. QNN measures must be interpreted **at matched computational and evolutionary event budget**, not simply compared as if all encodings cost the same.

## IV. What this study actually proves, and what it doesn't
**Author-supported outcomes:** distinct mutation and parasitism dynamics under specific stochastic binding, hand-seeded replicases in a fixed virtual substrate, qualitative dependency/hypercycles, and dramatic behavior under different decay regimes.

**Unresolved:**
- Ability to evolve genuinely *new interpreter semantics* rather than recompose a limited predefined opcode set;
- Body/boundary self-production and metabolic energy transduction;
- Causal multi-generation inheritance of novel ecological capabilities under closed reward constraints;
- Continued open-ended functional innovation across many niches or arbitrary long horizons;
- Consciousness or human-like intelligence.

**Model limit:** interactions and QNN reflect only the author-selected Stringmol experimental conditions. Some figure examples are representative rather than blindly assessed multi-seed confidence bounds; computational collapse can censor runs.

## V. Three novel, falsifiable deductions (original research proposals only)
1. **Decay-selection loophole:** allowing externally imposed immunity when molecules are bound makes inert loops win selection; predicted removal of that immunity reduces pathological fixation, **but could also destroy valuable symbiosis**. Need pairwise matched resource/repair controls.
2. **Mutable primitives tradeoff:** moving more behavior from P into B increases possible heritable change but may raise mutational brittleness and replication cost; measure new *functional* phenotypes per viable mutation, not sheer genotype length.
3. **Stochasticity optimum:** binding uncertainty may improve escape from parasites until copying/binding fidelity collapses. The hypothesized curve is nonmonotonic. Compare narrow parameter sweeps against deterministic control with frozen environments.

**Bottom line:** "Everything Evolves/Soft/Dies" are fruitful hypotheses and experimentally explored principles, **not a guaranteed recipe to make life**.

**Review coverage:** accepted paper §1–8, methods/protocols, figures/tables, observed negative outcomes and discussion examined. No full code/figure independently reproduced; E2.
