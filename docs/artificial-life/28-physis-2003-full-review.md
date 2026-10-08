# E2 full-paper review — Physis: heritable processor and instruction-set architectures (2003)

**E2 primary review, no code executed.** **Source:** Attila Egri-Nagy and Chrystopher L. Nehaniv, *Evolvability of the Genotype-Phenotype Relation in Populations of Self-Replicating Digital Organisms in a Tierra-like System*, ECAL 2003, *Lecture Notes in Computer Science* 2801:238–247. [Springer DOI 10.1007/978-3-540-39432-7_26](https://doi.org/10.1007/978-3-540-39432-7_26) · [author-deposited entire paper PDF](https://uhra.herts.ac.uk/id/eprint/2526/1/101997.pdf). Published title sometimes appears with **'gentotype' typo in institutional metadata**; the paper's own text spells *Genotype*. Rights of Springer accepted manuscript require separate review, not copied here.

## I. What evolves: not only a program, but the processor
Earlier Tierra-like digital organisms execute heritable instructions on fixed interpreters. Physis divides an organism's circular genome into:
1. A **processor architecture description**, using structural primitives **register, stack, queue** (R,S,Q) and separators.
2. A **new instruction-set definition**, where each evolved instruction expands into sequences of a fixed lower-level **universal processor**'s primitive operations.
3. Executable instructions for the replicator's own survival/reproduction.

At each individual birth the universal processor first reads genotype and constructs an effective processor; that processor runs the remaining program until death. Offspring copy the structure definition and instruction interpretation code, allowing the mapping between genotype and runtime behavior to **vary heritably**.

**Major boundary:** the *universal processor and its primitive operations remain fixed and designed*, even when the organism's intermediate interpreter definition changes. No simulator can escape all of its own physical rules. Claiming "the laws of computation evolve" without this qualifier would overstate the paper.

## II. Initial conditions and controls
- The authors **handwrite two functional ancestral replicators** (one with **four registers**, another with **two registers and one stack**), rather than evolve the first from random blank chemistry.
- Genomes encode structural description, interpreter definition and executable program; the original 4-register example is **78** units long; the other begins at **81**.
- Two regimes:
  - **Simple ecology:** selection only for speedier replication, **no artificial task reward**.
  - **Evolutionary learning:** additional CPU rewards for solving programmer-defined arithmetic/input-output tasks with external "task-handler" subsystem (similar to Avida). Gains there must **not** be called goal-free intelligence.
- For each regime the paper reports **five trials**, up to **20,000 organisms**, **200,000 update cycles** and thousands of generations.
- The published evolutionary performance measure **fitness=m/γ** uses organism merit and gestation time. That is an observational statistic in the no-extra-reward case; in the task regime merit includes **explicit externally rewarded tasks**.

## III. Original paper results and negative findings
### Simple regime: replication gets faster, interpreter is conservative
The 4-register ancestral genotype takes **857** gestation cycles; evolved descendants' first/second copy times average about **498±85 / 414±52**. The 2-register+stack ancestor begins at **1369** cycles; evolved descendants average **732±44 / 662±35**. These are paper-reported sample summaries, not our replication.

The **processor structural layout** remained strongly conservative: the original structure **never dropped below 90%** of the population in studied experiments, though mutated variants were observed. Numbers and types of registers/stacks and instruction count did not undergo established domination.

### Task-reward regime: definitions change, but superior open-endedness is not established
The authors report that the instruction content/definitions (not necessarily the number of instruction slots) could change dramatically, including additions of input/output primitives needed to solve externally selected computational tasks. Some genomic sequence parts came to have multiple context-dependent meanings.

However, their own evaluation explicitly states that **there were no observed signs of different evolutionary potential** compared with fixed-processor systems for the tested task set/time horizon. This is a **negative or inconclusive comparison**, not a justification for "universal processors outperform previous AI architectures."

## IV. Scientific insight for future ALife
**Working hypothesis:** a substrate with mutable intermediate instruction semantics makes some new functions reachable while increasing risk from invalid interpretation and incompatibility. A fixed physics layer `P` and an evolved descriptive/interpreter layer `B` still coexist. This anticipates Stringmol's viable semantic-closure transitions (2017) and the exploratory 2026 Physis meta-chemistry abstract without making either synonymous.

**Critical comparator:** same organism/evolution/resource budgets under a frozen interpreter, mutable interpreter, and human-upgraded interpreter. Do not confuse successful outside-task rewards with internally selected survival strategy. Measure:
- Actual mutation/transmission of interpreter semantics;
- New useful **functional** actions absent in parent and viable in descendants;
- Error rate in replication and interpreter-expression separately;
- Resource/CPU costs and extinction across independent worlds;
- Capacity for dynamic repair/maintenance and ecology when substrate permits.

## V. Code/provenance audit — *source-only*
- Original project has historical documentation at [Physis SourceForge](https://physis.sourceforge.net/research.html), proposing a universal processor and acknowledging **free biological building blocks** as a limitation in then-current ecology.
- A public contemporary **Python port** by [alyssa-adams/physis_python](https://github.com/alyssa-adams/physis_python) @ `5b5b7f8d3763c0cdbdfb036893645021823ad6a6` (main, 2026-10-08) documents self-replication, CPU/merit-based scheduling, genetic evolution, and externally rewardable tasks. Its README and root file inventory were inspected. **No root LICENSE** was found; do not assume permission to redistribute its contents. No tests/programs/web server executed.
- The 2026 Adams et al. *Transformational Novelty with an Automata Meta-Chemistry* summary [author record](https://www-users.york.ac.uk/~ss44/bib/ss/nonstd/alife26-late.htm) reports a CPU→GPU Physis port. **The above Python port is not proved identical** to that GPU implementation or to the 2003 Java source. Do not assume source-code continuity.

## VI. Evidence limits
Strongest paper-demonstrated finding: in a bounded digital-evolution universe **heritable processor and instruction-definition variations can occur**, though large structural changes rarely dominate the studied short runs. It is **not** proof of genuine lifelong learning, autopoiesis, cognition, unlimited evolutionary innovation or conscious experience.

**Full read:** the public ten-page article sections 1–6 including figures/table of performance and its explicit negative observations. No supplementary source code or exact experiment seeds audited; E2, not E3.

**Cross-links:** [2016 Stringmol principles](26-stringmol-2016-full-review.md), [2017 semantic closure](27-semantic-closure-2017-full-review.md), [2025 Stepney synthesis](25-stepney-2025-complete-review.md).
