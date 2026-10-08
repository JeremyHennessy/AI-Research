# Banzhaf et al. (2016) — complete theoretical review of open-ended novelty

**E2 original primary full-paper review, NOT experimental replication.** Wolfgang Banzhaf, Bert Baumgaertner, Guillaume Beslon, René Doursat, James A. Foster, Barry McMullin, Vinicius Veloso de Melo, Thomas Miconi, Lee Spector, Susan Stepney, Roger White. *Defining and Simulating Open-Ended Novelty: Requirements, Guidelines, and Challenges*, *Theory in Biosciences* 135(3):131–161. [DOI](https://doi.org/10.1007/s12064-016-0229-7) · [author-hosted complete 31-page PDF](https://www.cs.mun.ca/~banzhaf/papers/OEE_2016.pdf). Published online May 19, 2016. © Springer-Verlag 2016; linked for reading, **not copied or redistributed**. The PDF's full argument, examples, figures, computational limits and challenges were inspected.

## Research definitions — why endless running is not enough
The authors distinguish an **endlessly running attractor**, a **non-goal-directed but brief process**, and a potentially **open-ended creative process**. They review competing definitions: perpetual novelty, unbounded evolutionary activity, continuous complexity production, and open-endedness treated as the essence of life. They reject the assumption that any of these phrases has a universally settled measurement.

Their **model-relative** taxonomy:
- **Type 0 variation** changes values *inside* the existing model: mutations to known types, population sizes, altered numerical properties.
- **Type 1 innovation** changes a scientific or engineering **model** by introducing/removing types and relations already allowed by its **meta-model**.
- **Type 2 emergence** changes the *meta-model* itself; new levels and categories of organized entity may enter the explanatory picture.
- In their proposed terminology, type 1 and type 2 events are **open-ended events**; a system is open-ended if it can continue producing these. Finite observations do **not** prove unbounded continuation.

**Observer-dependence is explicit:** if the scientist already encoded a candidate network-level phenomenon into the model, observing it is not automatically a type-2 discovery. The same extinction may count as a numeric variation or ecosystem type-level innovation depending on chosen descriptions.

## Multilevel entities and domains
Level-0 entities are provided by a **generative chemistry/physics**: tokens/molecules/elements and interaction rules. The authors distinguish **aggregate populations** from higher-level coherent **system entities**. Boundaries can be spatial, informational or behavioral. Entities may participate in overlapping systems, and higher-level entities constrain lower-level interactions. The hierarchy is mostly **mereological** (parts form wholes); the authors explicitly note limitations for overlapping ecologies and dependencies that cannot fit a simple part-whole tree.

Scientific models describe observed systems and may be revised when new evidence arrives. Engineering models prescribe what the simulator implements. **Changing the scientist's model is not the same as changing the running simulator**.

## The central result for digital-organism research: "shortcuts"
To make high-level computation tractable, simulators pre-install **shortcuts**. The authors call **individuality** the **"mother of all shortcuts"**:
- **Individuality shortcut:** researcher already creates protected identities, boundaries or whole objects. The experiment therefore cannot claim to have discovered the *origin of individuality at that level* from the lower-level processes.
- **Replication shortcut:** a simulator API copies/spawns level-N objects. It may support heritable adaptation, but **does not demonstrate emergence of the reproduction mechanism**.
- **Fitness shortcut:** a precomputed task reward, special logic bonus, virtual resource score or externally trained novelty judge substitutes for endogenous differential reproduction. Its results can be useful but should not be credited with an intrinsically discovered *goal*.
- **Generative layer:** even absent these shortcuts the chosen elementary opcodes, reaction types, update cadence, resource supply and binding chemistry are the simulator's **designed baseline**.

These shortcuts can be **scientifically legitimate and necessary**. Their presence narrows which properties can be causally attributed to emergence; the authors do **not** argue every useful evolutionary model must simulate fundamental particle physics.

## How the authors distinguish five modes of capturing novelty
Their "Capturing the novelties" section separately considers:
1. An **external observer** discovers a new pattern post hoc; simulator engineering code unchanged.
2. Existing **prewritten recognizer** reports a predefined event.
3. Existing **structural shortcut** activates a prewritten representation after recognition.
4. System generates **new recognition code** to identify previously uncoded novelty.
5. System generates **new shortcut/structural code** to incorporate a newly recognized emergent level into subsequent simulator dynamics.

The last two are **conceptual design scenarios**, not verified open-ended implementations or proof that software can invent unrestricted physics. This helps distinguish the later [Stringmol 2020 extrinsic reaction-network model](30-stringmol-2020-novelty-full-review.md) from **actually changed executable interpreted meaning**.

## Constraints, negative observations and author qualifications
- Finite time/memory/matter constrain the number of hierarchical levels and entities. The authors distinguish **theoretically** versus **effectively** open-ended behavior under a finite observable horizon.
- The authors present CoSMoS-style separation of **domain scientific model**, **platform engineering model** and **results/observations model**. Don't precode the answer to an emergence question in the platform model.
- Fixed-goal GA, GP, Tierra-like virtual CPU ecologies and Avida's predefined task rewards can stagnate or plateau. A finite resource or preset niche space does not guarantee new levels of selection.
- Authors suggest evolving *new niches* and *individuation at higher levels* as possible major open problems, not as demonstrated solutions.
- The paper **does not** establish that its particular meta-model is applicable to all biology, sociology or computation; it identifies non-mereological organizations, metric generalization and genuinely endogenous simulation shortcuts as unresolved challenges.
- **No new experimental runs** or verified universal OEE theorem are presented by this theoretical article.

## Falsifiable operational deductions (our proposals ONLY)
1. Maintain a "shortcut ledger": identify which system properties are *primitive*, emergent internal interactions, or observer-imposed labels.
2. If the world creates a protected entity/membrane automatically, **reject** a spontaneous-individuality claim for that property.
3. If `replicate()` is an engine operation, **reject** an internally evolved replication-mechanism claim, while leaving open later heritable innovations.
4. If novelty score is a training target, use separate hidden tests for new ecological functions and their inherited viability.
5. Use two independent observer taxonomies to determine whether an apparent type-2 event is **scientific reclassification**.
6. Verify an additional proposed higher-level organization by causal dependencies, internal regulation and descendants, not mere pixel proximity.
7. Report finite horizons, resource costs and negative worlds; no empirical run proves indefinite novelty.

**E2 scope:** full 31-page source literature/theory and discussion, no code execution or E3 results. Compare [2021 spatial Stringmol](35-stringmol-spatial-parasitism-2021-full-review.md), [2020 observer-relative taxonomy](30-stringmol-2020-novelty-full-review.md) and [cross-study interpretation](37-parasite-and-shortcut-synthesis.md).
