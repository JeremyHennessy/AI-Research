# Pass 15 — Kratz et al. (2026): multi-timescale cellular history, limits of an RNN analogy

**2026-10-08 | E2 complete 14-page public original PRX Life main paper and experimental Appendix reviewed; NOT source-code or model reproduction.** Josiah C. Kratz, Huijing Wang, Fangwei Si, Shiladitya Banerjee, **Multi-Timescale Adaptation and Emergent Learning in Single Bacterial Cells**, *PRX Life* 4:023015, May 15 2026, DOI [10.1103/5zbg-8vll](https://doi.org/10.1103/5zbg-8vll), [full primary 14-page PDF](https://journals.aps.org/prxlife/pdf/10.1103/5zbg-8vll), CC BY 4.0. **Journal supplemental Figures S1–S10, numerical source code, data archives and author repos were not independently executed or reanalyzed.**

## Research question and what was actually observed

Bacterial growth under alternating nutrient quality appears conditioned by **past pulse timing**, in a way poorly captured by a one-timescale ordinary proteome-allocation equation. The authors contrast a fixed Markovian baseline with a fractional-order/history-kernel model. They further propose that differently relaxing ribosomal subpopulations could implement these dynamics. This **does not establish a new genetic evolution event or a self-created artificial brain**.

## Direct observations and study units

- Paper Figure 1(a) **reuses published E. coli K12 NCM3722 growth data from an earlier study** (Nguyen et al., 2021): it is not an extra independent fresh experiment in this paper.
- New experiments used **E. coli MG1655** in an externally controlled, custom microfluidic mother-machine device, switching between nutrient-poor and nutrient-rich defined media over selected pulse intervals. The authors recorded **~30,000 tracked cells per experimental time series** (exact condition denominators are in unreviewed supplementary Table S3); repeated timepoints/descendant cells are nested, not 30,000 independent evolution studies.
- Single-cell size/growth trajectories were processed and **averaged across the population in short time bins**. The effective adaptation time constant tau was obtained by **fitting a population-average growth-rate curve** to an exponential after nutrient upshifts. Claiming every individual directly demonstrated the fitted power law would overstate the sample unit.
- Increasing nutrient pulse frequency was associated with **shorter fitted adaptation times**, while sustained rich-medium growth performance was generally lower than in continuously rich conditions; the authors also reported repeated pulses gradually speeding the response.
- A local-in-time ordinary proteome-allocation model matched some single shifts but failed several multi-pulse dynamics. A **fractional-order, power-law-history model** better captured fitted time constants and held-aside qualitative trajectories.
- Both growth rate and adaptation rate are experimentally investigated; the interpretation that these are under active “learning” control is the authors' **theoretical framing**, not a unique molecular intervention demonstrating environmental belief or anticipation.

## What the authors *installed* in their mathematical model

1. Three coarse-grained proteome sectors, fixed nutrient uptake/conversion laws, ribosomal translation and housekeeping fraction; a researcher-chosen structure of state variables.
2. A phenomenological **fractional derivative with a power-law memory kernel**. The fixed model's 'memory strength' is an explicitly defined mathematical parameter. The adaptive version connects a researcher-defined **exponential moving average of past nutrient-downshift cost** to memory strength through a **sigmoid function**.
3. An alternative finite **ribosomal-subsector ODE model**, with a chosen distribution of relaxation constants and variable flux allocations, can approximate the power-law kernel. This is a **mechanistic explanation candidate**, not a direct isolation of distinct ribosomal subsector populations in the experiment.
4. A mapping from ribosomal sector dynamics to continuous-time recurrent neural network state equations, described as a functional analogy. The bacteria were **not engineered to have an LSTM, trained by gradient descent on hidden tasks, or observed evolving digital memory code**.

**Paper's explicit crucial limitation:** Direct experimental demonstration of its proposed heterogeneous ribosomal subsector dynamics was left as future work. Figures model such subsectors and connect them to known biological regulators, but do not isolate the unique memory-storage carrier causally in each bacterium.

## Counterfactual and replication problems

- A simpler **distributed linear relaxation** or fixed pre-existing resource regulator might produce the same input-output curves; mechanistic comparisons require a model with **equal parameter count/fit freedom**, nested preparations and new pulse schedule holdouts.
- The authors compare their invented adjustable history model against an earlier Markovian baseline; outperforming that baseline **does not prove the cell discovered the kernel** or that nonlinear inference is literally carried out as in the fitted equations.
- Fitting tau to growth averages and model parameters to one set of pulsing conditions can overstate generalization to arbitrarily changed ecological statistics or entirely different resources.
- No demonstration that a new memory mechanism appeared during experimental evolution, that daughter collectives acquired novel inheritance, or that a self-maintaining artificial organism emerged.
- Financial/time/resource constraints of a living bacterium include protein turnover and inactivated ribosomes; laboratory pump medium is exogenous, and authors do not prove every optimization is globally fitness-optimal after accounting for stochastic extinction.

## Original EERC-S scientific bridge — still untested

**Separate two clocks:** (i) an individual's already-present **physical relaxation spectrum** can adapt within hours; (ii) an inherited regulatory structure may evolve over many generations to alter the **distribution of available relaxation/switching behaviors**. These are distinct observable processes.

An emergent digital-system hypothesis would demand **proof that mutable interactions alter the relaxation spectrum** and that the altered phenotype improves an unfamiliar ecological outcome relative to **researcher-installed fractional filters, integrators and stochastic switching**, at matched material/compute cost. A functional RNN analogy alone is no special evidence for digital organismhood or subjective consciousness.

**Source receipt:** Main PRX Life full PDF sections I–III and Appendix read through the publisher; full Supplemental Material and both public author code/data repositories listed in its references **not cloned or executed**. E2 source reading only. No code, living agent, trained AI or experimental world was produced by AI-Research.
