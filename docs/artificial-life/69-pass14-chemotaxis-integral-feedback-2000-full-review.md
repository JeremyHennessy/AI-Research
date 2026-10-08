# Pass 14 — Yi, Huang, Simon & Doyle (2000): integral feedback can mimic memory without learning

**2026-10-08 | E2 complete five-page primary PNAS theoretical paper inspected; no new experiments replicated.** Tau-Mu Yi, Yun Huang, Melvin I. Simon and John Doyle, **Robust perfect adaptation in bacterial chemotaxis through integral feedback control**, *PNAS* 97(9):4649–4653 (2000), DOI [10.1073/pnas.97.9.4649](https://doi.org/10.1073/pnas.97.9.4649), [public 5-page primary PDF](https://groups.csail.mit.edu/mac/projects/amorphous/6.978/papers/doyle-PNAS-2000.pdf), [author repository record](https://authors.library.caltech.edu/records/sa6bx-35q11). Public paper read; no source MATLAB simulation, experimental E. coli culture or analytic independent proof run.

## The actual scientific result

Bacterial chemotaxis momentarily alters run/tumble behavior when encountering attractants. Its sensory transduction later **adapts** toward the previous baseline even while the stimulus remains. The proposed mechanism is a **negative/integral feedback loop** implemented with receptor methylation/demethylation, especially **CheR**, **CheB**, kinase **CheA**, response regulator **CheY-P** and its dephosphorylation via **CheZ**.

The authors analytically connect a model of the methylation cycle to an **integral feedback representation**, explaining why **perfect adaptation** can be robust to substantial parameter changes, subject to specific assumptions about receptor kinetics and viable operating ranges.

**This is a control-theory derivation and analysis of a pre-existing genetic/molecular circuit**, supported by earlier independent experimental chemotaxis findings. It does **not** evolve a circuit from scratch, prove cells learn a new association, or identify subjective experience.

## Process and evidence distinctions

- Receptor binding and signaling are rapid, while receptor methylation/demethylation is a **slower internal state** that accumulates a history of encountered attractant relative to a feedback reference.
- Integral adaptation seeks to **remove the long-run output error**, not maximize a memory score; the organism's sensor output returns toward baseline after a step input. A permanent state may exist internally despite apparently no change in the externally measured output.
- The authors compare and translate **Barkai & Leibler** two-state active/inactive receptor assumptions and relate robust adaptation to feedback laws. This study is **theory plus reported consistency with existing experiments**, not an independent new evolved-population replication.
- Model correctness depends on network topology, saturating kinetics and operating conditions; integral-feedback behavior can break outside assumptions or under biochemical perturbations. The exact molecular implementation is not proven uniquely by a system-level transfer-function equivalence.
- Matching bacteria's past-stimulus response with **an engineered fixed integrator** is an especially strong counterexample to the assertion that any history-conditioned behavior necessarily means *learning*.

## What the result suggests but does not establish for EERC

Even if the system's causal state remembers past chemical concentrations:
- **Fixed design**: a developer can install the feedback controller in a digital world as a generic sensing primitive.
- **Transient adaptation**: current output can look memoryless after integral compensation even when internal methylation state retains history. Treat low measured output correlation as **not sufficient to conclude zero internal memory**.
- **Fitness and ecological transfer**: robust restoration of output does not automatically show new functional competence under changing unseen resources or that memory controllers evolve naturally.
- **Memory costs**: a feedback mechanism consumes protein/molecular resource budgets; biochemical control cannot be assumed free and infinite.
- **Confound**: observed long-horizon stability may be homeostatic control rather than an evolving high-level individual, a moral conscience, or general intelligence.

## Future-only comparison to falsify a novel digital-memory claim

1. Measure output under a step disturbance and under **reversal/aperiodic** stimulus sequences at matched total energy.
2. Compare no history, **preinstalled integrator**, fitted passive low-pass filter, and genuinely evolving/state-modifiable chemistry as separate arms.
3. Scramble memory state without altering sensor/motor pathways; test whether unseen adaptive survival differs and whether the state was formed/maintained internally.
4. Preserve all failed worlds and alternative parameter ranges, not only ideal robust-adaptation curves.
5. Distinguish **state retention, adaptive use, and heritable endogenous development** before declaring any new life-like intelligence.

**E2 source audit only.** Theoretical integral-control equivalence does not justify invoking a real artificial learning system.
