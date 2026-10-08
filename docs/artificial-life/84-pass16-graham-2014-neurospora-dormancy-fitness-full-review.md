# Pass 16 — Graham, Smith & Simons (2014): selection for long-horizon survival, with real extinctions

**Reviewed 2026-10-08 | E2 complete original public Proceedings of the Royal Society B main article, figures, tables, Methods, negative outcomes and Discussion inspected via [full PMC paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4071552/), DOI [10.1098/rspb.2014.0706](https://doi.org/10.1098/rspb.2014.0706).** Under the original author/publisher rights statement; raw [Dryad doi:10.5061/dryad.8qc20](https://datadryad.org/dataset/doi:10.5061/dryad.8qc20) and supplemental tables NOT downloaded/replicated. No biological experiment in AI-Research.

**Primary:** Jeffrey K. Graham, Myron L. Smith & Andrew M. Simons, *Experimental evolution of bet hedging under manipulated environmental uncertainty in Neurospora crassa*. Proc. R. Soc. B **281**:20140706 (2014).

## An independent substrate/selection result, with valuable failures

- The study used **12 founding genetic lineages** of the fungus *Neurospora crassa*, with **88 independently evolved samples** across different environmental schedules. Experimentalists defined **five probabilities of an adverse year**; the offspring trait of interest was the fraction of dormant fungal propagules.
- After about **10–14 full rounds of selection**, the observed final dormancy fraction generally increased with probability of an adverse period. Cohort mean dormancy fractions roughly **0.16 at 0% adversity**, **0.22 at 25%**, **0.29 at 30%**, **0.33 at 40%** and **0.30 at 50%**. The small decline at 50% is a **counter-trend**, not perfect monotonic adaptation.
- Evolutionary change could be upward or downward from source-specific starting dormancy. Authors found a significant association with adverse-year frequency (ANCOVA F=8.430, p=0.0051) and reported a geometric-mean fitness interpretation with relative likelihood **2.4×** an arithmetic-mean comparison under their Akaike information criterion.
- **Strong important caveat:** experimenters prohibited **two consecutive adverse years** to avoid rapid extinction. At 50%, the sequence therefore **necessarily alternated** rather than being unpredictable at every opportunity. The very environmental stochasticity under study was partly structured by researchers.
- Many lines were subject to **stochastic extinction** during repeated small-sample transfers. The 88 evolving samples are the analyzed cohorts, not proof that all initially established lineages survived. No full raw extinction genealogy was independently reconstructed here. Including failures is essential when comparing actual long-horizon robustness.
- The study does **not** demonstrate which genetic changes caused altered dormancy, that the trait reached a stable evolutionary optimum, or that any continuing fungus used learned memory to forecast the next year. The **natural fungal sporulation/dormancy apparatus** and researcher-chosen lab phases are pre-existing.

## Scientific insight relevant to our research

The distinction between **higher mean instantaneous growth** and **higher geometric-mean success across several environmental episodes** is real biological experimental evidence: populations may sacrifice immediate expression for improved long-term lineage survival. A good EERC evaluation therefore needs two separate denominators—within-episode productivity and **surviving independently reproducing lineages**—rather than one averaged score.

This is a genuinely **independent physical study cohort/substrate** from Acar 2008 engineered yeast and Beaumont 2009 evolving bacteria. It still tests a **mature organism's existing life cycle**, not origin of a new collective reproduction mechanism.

## Nulls and remaining checks

- Require explicit extinction record; the geometry of researcher-imposed intervals can affect viability even at identical adverse-event fraction.
- Compare change in selected dormancy between cohorts to inherited molecular mechanism (not shown by current study).
- An EERC experimental model must measure extinction alongside mean returns and must **not** hard-code the bet-hedging controller into its agents then call the resulting competition a discovery of adaptive cognition.
- Keep environment schedule generation, founder identities, durations and alternative adaptation mechanisms visible; no claim of digital organism life or consciousness.
