# Pass 12 E2 full-primary review — Physarum habituation transferred through cell fusion

**2026-10-08 | Complete original public main-text methods, numerical results, figure captions and discussion inspected, E2.** No independent reproduction; original supplementary statistical tables, videos, archived data and biological materials not independently downloaded/analysed.

**Primary:** David Vogel and Audrey Dussutour (2016), **Direct transfer of learned behaviour via cell fusion in non-neural organisms**, Proceedings of the Royal Society B 283:20162382. [DOI 10.1098/rspb.2016.2382](https://doi.org/10.1098/rspb.2016.2382), [complete PMC HTML](https://pmc.ncbi.nlm.nih.gov/articles/PMC5204175/).

## Study question

Can a **habituated cell** transmit its altered behavioral response to an initially unhabituated cell, **without offspring or a nervous system**, via temporary cytoplasmic fusion?

The study concerns *Physarum polycephalum*, a giant **multinucleate single-cell plasmodium**. Fusion can combine two or more plasmodia into **one larger continuing cell**. This is **horizontal state transfer**, not a vertical germline inheritance event; the two prior individuals do not become two independent daughter lineages.

## Study methods and denominators

- Cultures derived from **8 sclerotia**, not thousands of independently founded genetic lineages. At 24°C, slime moulds navigated agar bridges toward food. Experimentalists manually handled and moved them each day.
- **Habituation phase**: n=240 plasmodia, split **120 habituated** vs **120 unhabituated**. Exposed to **150 mM NaCl** (or no NaCl) for five consecutive days; all crossed NaCl on day 6; recovery days 7–8 used plain agar; final retest on day 9.
- **Fusion transfer**: n=4,380 initial individual plasmodia across **19 configurations** of two-to-four participants and zero-to-four prehabituated cells. Each final fused entity was measured after components made contact; *n=4,380 inputs is NOT 4,380 independent fused entities or separate evolutionary origins*.
- **Time-dependence**: 500 original plasmodia used in UU, UH, HH pairwise fusion; cells were **separated after 1 hour or 3 hours**, then retested individually on NaCl bridge.
- Main response: **time to cross an aversive bridge** and derived habituation index normalized against unhabituated matched-configuration controls. The behavior might partly reflect movement/metabolic condition; authors used controls, recovery and composition tests.
- Statistical machinery: generalized linear models and exact binomial tests, with nonlinear fits to habituation dynamics using R 3.2.3.

## Results from main text, author-reported

1. **Habituation and recovery:** initially NaCl bridge slowed crossing markedly; repeated daily NaCl made crossing progressively faster (inverse-power fit R²≈0.93). On day 6, trained cells crossed faster than untrained under NaCl (F(1,214)=131.80, p<0.001). After two no-salt recovery days, previously trained and untrained groups were statistically indistinguishable on final NaCl test (F(1,238)=0.14, p=0.714): **recoverable habituation**, not permanent salt tolerance.
2. **Merged cells:** any habituated contributor lowered the merged entity's salt aversion vs all-naïve controls (p<0.001 across configurations). The response depended **nonlinearly** on the fraction of habituated members (fit R²≈0.97), arguing against simple passive cytoplasm dilution. It still does not identify which molecules transmit the state.
3. **Which component navigated:** in composite entities the pseudopod that first arrived at food often originated from a **previously naïve cell** (reported probability 0.72±0.03), a key behavioral argument for transfer rather than merely retaining a habituated driver's motor output.
4. **Separation after contact:** after **1h fusion**, previously naïve separated cells behaved as naïve (p=0.999). After **3h fusion**, those cells showed behavior statistically indistinguishable from habituated ones (p=0.991). This demonstrates time-dependent **transfer of behavioral adaptation**, not proof of any particular biochemical molecule or neural-like representation.

## Critical boundaries

- **No reproduction measured**: cytoplasmic mixing by fusion is not daughter inheritance, reproduction of a combined collective, or an emerging evolutionary individual.
- **No endogenous learning from fully natural ecology**: repeated repellent exposure was imposed by the researchers; no direct demonstration of viability in a new ecological niche.
- **No specific material carrier**: nonlinearity is evidence against the simplest dilution model but does not distinguish proteins, RNA, membrane remodeling, exchange of signaling factors or physical transport. The authors expressly suggest multiple possible physiological causes without direct molecular identification.
- **Behavioral criterion**: shorter bridge crossing can be influenced by movement speed/size, learned aversion, effort/energy costs and experimenter timing. Authors matched culture histories and used multiple controls, but not every possible sensor/motor counterfactual.
- **Statistical independence**: a coalesced entity is the acute behavioral test unit, not the number of original cells or nuclei; multiple source cultures and assay conditions share experimental design/genetics.
- **Not independently reproduced**: study's original Dryad data and supplements not recalculated, and findings do not imply indefinite adaptive memory or consciousness.

## Relevance to Endogenous Ecological–Reproductive Closure (EERC)

This study suggests a fourth, **non-genetic** route for transporting information **between living components**, in addition to (a) vertical daughter state, (b) inherited interpreter instructions, and (c) morphology/structure. For EERC, a separate future-only experiment would require:

- Track **one individually history-trained donor** and **separate recipient**, with matched naive-naive, trained-trained, 1h/3h fusion, re-separation and viability controls.
- After a successful state transfer, assess **functional benefit** on a blinded novel test *without experimenter re-creating the learned state*.
- If any new collective is claimed, demand **independent daughter collectives that inherit a function**, after any external fusion/propagule aid is decreased. This is **not** tested in the paper.
- Use component-specific causality and time-lag/flow interventions to distinguish actual state transfer from group-average behavior and transferred toxic-substance exposure.
- Do not count repellent-tolerant cells, merged structures or nuclei as independent learned new organisms.

**Rights receipt:** source paper publicly accessible at PMC, with author/publisher rights statement checked; linked material only, no full text or images copied here. Source is E2 only for full main text reviewed; no E3 scientific replication. **No execution or organism experiment performed.**
