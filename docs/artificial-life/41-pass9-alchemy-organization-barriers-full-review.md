# Pass 9 — AlChemy: what self-organizes, what stalls, and why (full primary-manuscript review)

**Reviewed 2026-10-08. Research only.** This is an **E2 manuscript/methods review** of the publicly accessible complete HTML text, **not** independent reproduction, peer-review verification, or a demonstrated digital organism. No third-party software or dataset was run. Do not inflate the catalog E2 counts until the source record and ledger are reconciled.

**Primary source:** Cole Mathis, Devansh Patel, Westley Weimer and Stephanie Forrest, *Self-Organization in Computation & Chemistry: Return to AlChemy*, arXiv:2408.12137 **v2**, 23 August 2024, [full article](https://arxiv.org/html/2408.12137v2), [version history](https://arxiv.org/abs/2408.12137). The HTML body carries a later auto-generated 'Date: August 24, 2026' field, conflicting with the arXiv version banner. Cite the immutable arXiv v2 date, not the HTML template date. Original historical AlChemy is Fontana and Buss 1990s; this paper is a **modern reanalysis/extension**, not an independent different substrate.

## What was actually implemented by the study's authors
- A virtual soup of **lambda-calculus expressions**, whose collision composes two expressions and attempts beta reduction into a normal form.
- Simulation fixes a total expression population by adding collision product and removing a randomly chosen expression; the resulting abundances are not a physically derived energy/stoichiometry ledger.
- No general halting test exists; the **pragmatic reduction cutoff** treats nonterminating reactions as elastic (no product). A **syntactic filter** may explicitly ban direct copy reactions. Both are installed simulator physics.
- Initial expression generators and **free-variable standardization** constrain accessible expression structure. The original generator favors distinctive long chains of abstractions; a permutation-tree generator creates different expression distributions.
- Authors modified legacy C software to compile: alternate camllight, includes, function name `select` -> `peep`, and one memory-allocation replacement. The linked code/container is author-provided and **was not checked for exact commit, runtime equivalence, or license in this pass**.

## Methods and positive/negative outcomes (author-reported, not reproduced)

### A. Robustness within one organization
In 'L0 simulation' conditions, authors initialized **1,000 expressions**, operated for **1 million collisions**, added **100 random expressions**, then continued through five perturbations of one million collisions each. A 1,000-run survey at that condition showed not every ecosystem fell into a single copying identity function; some stabilized with tens or hundreds of expression types. A highlighted example reported about **380 distinct expressions** at its stable state (Figure 2).

The follow-up perturbation took **50 end states**, formed **four** variant populations per state (200 trials), replaced some fraction of expressions with the identity function, and evolved each for **1 million additional collisions**. Authors report surprising resilience. Importantly, the survival assay here is defined as *any non-identity expression remaining*, **not unchanged organizational identity, new function, autonomous repair or a living lineage**. High perturbation can transform one organization into another.

**Text consistency warning:** section 4.1 contains an apparently inconsistent phrase claiming that 'Even replacing 50%' causes collapse, immediately followed by 90% replacement destroying only some and not most organizations. Interpret only the broad pattern and verify Figure 2D/source data before quoting an exact 50% threshold. Do not silently correct the source.

### B. Robustness is not guaranteed
Authors also studied 'L1' conditions with direct-copy syntactic filtering. They removed **10 random expressions and inserted 10 new random expressions**, or changed the **collision RNG seed**, followed by **100,000 further collisions**. For sampled organizations they repeated each comparison **seven times**. Outcomes varied from convergence back toward the original to lasting divergence. Hence apparent macroscopic stationarity (entropy/number of types) can hide underlying replacement and fragility (Figure 3).

### C. Higher organization is a bottleneck
Authors took pairs of separately matured L1 organizations (1,000 expressions per source), combined them into a larger 2,500-expression world, ran another **1 million collisions**, and classified **455 paired outcomes** as **dominance**, **coexistence**, or **mutual destruction** using a **Jaccard set overlap threshold of 0.1**. Coexistence was uncommon. Crucially, **coexistence under an observer's set-similarity threshold is not inherited higher-level individuality, and the authors did not exhaustively search for spontaneous L2 organization within a single soup** (Figure 4). Do not claim a numerical success percentage from a figure graphic without table inspection.

### D. Initial-condition generator drastically changes behavior
Authors compared original probabilistic generator with their permutation-tree generator, using **5 independent initial conditions × 5 RNG seeds** per generator, **1,000 starting expressions** and **100,000 collisions** per run, with direct copying disallowed. Permutation-generated worlds tended toward an **inert identity-function fixed point**, while original-generator worlds more often formed diverse organizations (Figure 5). They attribute the difference partly to expression accessibility and standardization choices, but the exact mechanism **is a hypothesis, not isolated causally**.

### E. Representation theorem is not evolutionary discovery
Their constructive proof maps an arbitrary **chemical reaction network (CRN)** to a typed-lambda expression system with preconstructed terms for reaction rules. It proves that a sequence of transitions is **possible** in the constructed correspondence, **not** that random reactions are likely to find it, that rates/energy are modeled, or that the reaction rules emerge internally. The typed-language and handcrafted terms are installed scaffolding (section 6).

## Scientific lessons for living-organization research

| Author-reported result | What it does **not** demonstrate | Future discriminator (NOT RUN) |
|---|---|---|
| Random expression mixtures create stable interacting ensembles | New organism with causal, heritable daughters | Lineage reconstruction and split/reseed of component ensembles, tracking necessary causal dependencies |
| Some ensembles survive large copy-function perturbations | Self-repair maintaining identical organization | Internal mechanism knockout plus maintenance of *same functions* and viable independent descendants |
| L1 pairs rarely coexist after mixing | Universal impossibility of higher-level individuality | Test coadapted versus independent pairs; frozen coexistence AND group-level heredity criteria |
| Generator choice strongly changes outcomes | Fundamental law that one syntax generator is life-like | Matched structural statistics, varied standardization, reaction accessibility, null generator |
| Typed-lambda formally encodes CRNs | Spontaneously discovered metabolism | Resource-conserving stochastic CRN comparator; measure rates, costs and resource influx |

**Critical original insight (hypothesis):** an *organizational permeability window* may be necessary. If interactions collapse too easily into inert sinks, no exploration is possible; if every partner reacts indiscriminately, no stable lineage boundary persists; if interaction between successful organizations is mostly destructive, major transitions cannot accumulate. This is a **prospective parameter/control hypothesis**, not evidence of a universal law or optimal threshold.

### Distinguish external 'life assistance'
- **Designer-supplied:** total-population clamp, reaction reducer, nontermination cutoff, syntactic no-copy ban, random-object distribution, choice of similarity metric, prewritten chemical rules in theorem.
- **Self-organized within these constraints:** emergent assemblage of mutually reproducing lambda expressions, robustness under some perturbations, drift to alternate stable organizations.
- **Unknown/unshown:** endogenous physical/resource maintenance, daughters inheriting effective functions, new metabolic niche generation, independent group-selection, sensorimotor learning, conscious experience, indefinite openness.

## Evidence and rights boundaries
- **Reading status:** E2 complete publicly available HTML manuscript sections 1–8 and Figure 1–5 captions/results + formal construction examined; this is an *evidence review*, not an external replication.
- **Code provenance:** paper links [author GitHub](https://arxiv.org/html/2408.12137v2) from reference 24; exact repository commit and license **not checked**. Do not claim code was reproduced here.
- **Rights:** arXiv page indicates perpetual non-exclusive distribution license; link to text instead of redistributing it.
- **No computation:** no software, experiments or datasets executed. Author outcomes are appropriately labeled. No implementation permission is implied.
- **Further work:** inspect figure 2/4 numerators and paper code revision; validate ambiguous 50%-perturbation sentence; critically review chemistry energy/resources vs formal mapping; integrate catalog E2 receipt only after schema inspection.
