# Pass 8: critical peer-review audit and cross-substrate operational test specification

**2026-10-08 | Research only.** No simulator, organism, training, or third-party experiment was executed. This is a primary-publication/peer-review research note; no change to Ora or AgentTest.

## Primary sources and provenance

- Stepney & Hickinbotham (2024), *On the Open-Endedness of Detecting Open-Endedness*, Artificial Life 30(3), 390–416: https://doi.org/10.1162/artl_a_00399 ; author abstract https://www-users.york.ac.uk/~ss44/bib/ss/nonstd/artl23.htm ; official special issue editorial https://direct.mit.edu/artl/article/30/3/300/123431/
- York supplementary methods: https://pure-research.york.ac.uk/ws/portalfiles/portal/76644523/Measuring_Stringmol_code_and_data_documentation.pdf (search-indexed extract; direct browser access redirects to authentication). It identifies the input data as 2021 Stringmol material, not fresh independent experimental worlds.
- Furubayashi et al. (2020), *Emergence and diversification of a host-parasite RNA ecosystem through Darwinian evolution*: https://elifesciences.org/articles/56038 ; figure/data record https://elifesciences.org/articles/56038/figures ; **published editor/reviewer exchanges and author responses** https://elifesciences.org/articles/56038/peer-reviews (read).
- The RNA experiment extends **43 prior rounds by 77 rounds** to **120 rounds** total; repeated samples from the same evolving experiment are not automatically independent replication trials.

## 2024 novelty metrics: evidence-bound conclusion

The paper's accessible author abstract says eight spatial Stringmol runs originally made for a parasite-defense hypothesis were reexamined. Authors use system-generic evolutionary measures followed by phenomenon-specific analyses. The 2024 special-issue editorial identifies Droop–Hickinbotham non-neutral evolutionary activity among these measures. **Neither an independently accessible complete paper nor individual figure values have been verified here.** Therefore **E1** remains appropriate; no fabricated claims about metric 'success' or rank order.

Critical methodological boundary: reanalysis of eight runs = additional interpretation, **not** eight independent validation experiments. A metric can miss an evolved interaction, but a post hoc tuned metric may overfit those same worlds; require held-out behaviors and frozen detection code for predictive claims.

## RNA peer-review audit: what criticism was actually raised

Published editorial correspondence specifically raised:
1. **Lineage causality:** need time-resolved joint sequence/lineage maps; simple Hamming-distance ordinations alone do not fully resolve the history of beta/gamma parasite emergence. Later review still found temporal-lineage reconstruction incomplete.
2. **Measurement asymmetry:** host population concentration by RT-qPCR, parasite population by gel band intensity. Authors explained population-level parasite primers could not target diverse host-derived deletion mutants; band sensitivity caused missing observations around **<30 nM**. For **known isolated parasite clones** in competition assays, specific RT-qPCR *was* possible. Do not treat missing gel signal as true ecological absence.
3. **Mechanism:** reviewer queried copy-choice recombination. The authors screened selected sequences with **RDP4** and reported **no detected signal**, which is not proof that recombination is impossible.
4. **Claims of diversity:** reviewers asked for quantitative distinctions between increased lineage diversity, changed mutation spectra, and larger apparent RNA genome length. Longer later parasite species can be deletion derivatives retaining more host sequence, not de novo construction of all their component information.
5. **Sequencing uncertainty:** late review queried singletons and how read/consensus thresholds handled potential sequence errors. Do not claim singleton variants are independent adaptive innovations.
6. **Replication and controls:** Figure 4 uses competitive evolved-clone assays (figure caption: 3 independent assays for error bars). Those assay repeats **are not** three independently evolved 120-round ecosystems.

Sources: https://elifesciences.org/articles/56038/peer-reviews and https://elifesciences.org/articles/56038/figures ; reviewer statements are criticism/requests, not independently demonstrated experimental failures.

## Cross-substrate evidence rubric (research proposal, NOT validated assay)

Each prospective substrate is scored on **separate descriptive axes**, not a summed 'life' grade:

| Axis | Required evidence | Null/confound control |
|---|---|---|
| L — lineage | Parent–descendant causality and transmitted variation | shuffle lineage labels; seeded copy baseline |
| F — blind functionality | Previously unseen interaction challenge, no retrospective fitness shaping | preregister perturbations and score hidden test set |
| R — repair/maintenance | Endogenous restoration following resource/structural disruption | passive decay, external repair, inert analog |
| B — boundary origin | System-built/rebuilt persistent boundary | externally supplied compartments vs boundary-free control |
| E — ecological niche creation | New, usable resource/interaction opportunity generated by inhabitants | static resource graph vs evolved graph, matched resource input |
| C — resource accounting | Costs of copying, defense, repair, and interaction measured | equal energy/compute budget, extinct-run inclusion |
| S — simulator shortcut inventory | Which replication, fitness, identity, physics, mutation and compartment operations are supplied | remove/ablate installed primitives only where system remains comparable |
| G — generalization | Capabilities transfer to unseen disturbances/environments | holdout settings and lineages; fixed scoring code |

**Intervention hierarchy:** historical observation -> within-world knockout -> causal rescue -> blinded held-out ecological challenge -> independently reseeded validation. Cross-paper analogy is not substitute for matched experiments. RNA droplets, Stringmol spatial grids, and processor inheritance are non-equivalent infrastructure; report raw units and available interventions instead of converting to a universal novelty index.

## Preliminary assessment for future research (unverified hypotheses)

- New strategies **inside** existing resource/interaction rules may be evolutionarily meaningful without constituting **new ecological niches**.
- Reconstructing lineages across time is necessary but insufficient for proving new capabilities; causally disable putative new mechanisms and measure consequence.
- Apparent abundance dips can be measurement censoring rather than actual extinction. Method-specific detection limits must accompany time series.
- An adaptive complexity metric trained from observed runs risks becoming the observer's invention; preregister functions and independently challenge outcomes.

## Next review actions

1. Obtain legally accessible complete 2024 text, read all plots/tables and exact metric definitions; only then consider E2 promotion.
2. Inspect RNA article supplementary genotype workbook, full Figure 2/4 data, and author's final handling of singleton sequencing; verify experimental denominators. E2 status not asserted by this note.
3. Compare the 2021 Stringmol and 2020 RNA papers using the eight-axis matrix, marking **not measured** separately from **failed**.
4. Research theories and experiments of **niche construction**, with priority to direct interventions distinguishing environmental change caused by inhabitants versus designer-supplied new resources.
5. If experiments are ever authorized in a separate project, preregister metrics, budget, negative controls, extinction handling, and validation seeds. No experiment is authorized by this note.

**Evidence state:** document and reviewer correspondence checked; no figure dataset downloaded or calculations repeated. This note is source-backed interpretive research, **not independent replication**.
