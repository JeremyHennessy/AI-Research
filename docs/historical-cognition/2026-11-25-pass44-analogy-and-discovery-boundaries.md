# Pass 44 — Analogy, abstraction and mathematical discovery: bounded method audit

2026-11-25; research only. Input HEAD `99804b73f8e726c796a9a6b65c4d68c481bc6e47`; original main `18f37bebca2f650aff8ab844ddb1ab9c8896158b`; draft [PR #70](https://github.com/JeremyHennessy/AI-Research/pull/70). Read Pass 2 and latest Pass 43. Input branch 60 commits ahead of pass-2, zero behind; 72 added files, zero deletions versus original main. This batch deepens existing bibliography row 251 (Guhe2009c), not a new row.

## Primary source and scope

Markus Guhe, Alison Pease, Alan Smaill, University of Edinburgh School of Informatics, *A Cognitive Model of Discovering Commutativity*, CogSci 2009, pp.727–732, ISBN 9780976831853; [publisher version in Edinburgh repository](https://www.pure.ed.ac.uk/ws/portalfiles/portal/24467573/guhe_css09.pdf), [Dundee institutional metadata](https://discovery.dundee.ac.uk/en/publications/a-cognitive-model-of-discovering-commutativity/). All six printed pages visually inspected, including Table 1 and Figures 1–3, and all sections reviewed in text. Public read access; repository cover reserves copyright; no source text, figures, model code or datasets redistributed. Dundee event metadata contains a conflicting 2008 event date despite 2009 publication; retain publication year, not the inconsistent event dates. No independently runnable model or raw trace obtained in this bounded review.

## Method and capability provenance

| Location | Evidence and boundary |
|---|---|
| p.729 | Cardinality, physical collection commutativity, cross-domain metaphor, ordered arguments, mapping procedure and specialized symmetry detector are prerequisites, not independently acquired results. |
| p.730, Figs.1–2 | ACT-R 6 reimplementation maps explicitly encoded equations 1+2=3 and 2+1=3; goal and typed roles supplied; retrieved correspondences stored during processing. |
| p.730, Fig.3 p.732 | Transfer depends on stored source knowledge and a permitted cross-domain relationship. The authors report another analogy example, not broad benchmark validation. |
| p.731 | Filtering false conjectures, proving/integrating results, perceptual acquisition and broader task testing are outstanding; concept formation was outside the model's scope. |

The paper is E2 for its published method, not E3 or a demonstration of independent discovery of the reasoning machinery. No run count, held-out test battery, quantitative generalization result or cost benchmark is established in the six pages. Treat the result as conditional transfer of structured knowledge, rather than proof of a universally valid new rule.

## Independent analytical checks (not a replication)

1. **Finite evidence is insufficient.** On positive integers define two operations A(x,y)=x+y and B(x,y)=x+y+(x-1)(x-2). Both yield 3 on (1,2) and (2,1); B yields 6 at (3,1) but 4 at (1,3). Thus matching the paper's displayed equation pair and symmetry pattern does not uniquely identify a globally commutative operation. This is a counterexample to an inference from observations alone, not a claim that the actual ACT-R implementation accepts B.
2. **Exact sufficient condition.** Let a source operation s be commutative and let a map h into the target satisfy h(s(x,y))=t(h(x),h(y)) for every source pair. For any u=h(x), v=h(y), t(u,v)=h(s(x,y))=h(s(y,x))=t(v,u). Hence commutativity transfers on the image; surjectivity makes it global. A similarity of roles, even with a bijection of objects, is not by itself the operation-preservation assumption. Identity between A and B above is a counterexample.
3. **General finite-sample obstruction.** For any finite nonempty set S of observed first and second arguments, let P(x)=product over a in S of (x-a)^2. Operation C(x,y)=x+y+P(x) on positive integers agrees with addition on S×S. For a in S and positive b outside S, C(b,a)-C(a,b)=P(b)>0. Consequently even all observed swaps in any finite collection leave an unconstrained noncommutative alternative. This does not deny sound inference under separately justified structural assumptions.

These elementary proofs are original analysis in this report, not a claim of mathematical novelty. Numerical check of A and B on (1,2),(2,1),(3,1),(1,3): A=(3,3,4,4), B=(3,3,6,4). No historical or Ora code executed.

## Ora crosswalk and provenance

Separate (i) acquisition of representations, (ii) acquisition or authored availability of a candidate-generating operation, (iii) transfer under independently justified invariants, and (iv) checking a candidate in the target domain. A repeated useful behavior or symmetric outcome is evidence of neither general abstraction nor a proof of a rule. A future *research-only evaluation concept* would contrast cases where a shared relation genuinely preserves resource outcomes against cases with similar observed patterns but different held-out outcomes; evaluate whether a candidate representation is necessary and useful under matched costs. No runtime change or experiment is authorized here.

Funding acknowledgement p.731 visually confirms UK EPSRC Wheelbarrow grant EP/F035594/1, publication by Edinburgh researchers. Search of public UKRI/award records did not resolve the exact administrative award page in this batch; recipient designation, award value and dates remain unverified, and no funding success is inferred. One exact award identifier recovered from primary text; unique-award reconciliation outstanding. [2001 path-mapping predecessor](https://doi.org/10.1207/s15516709cog2501_4) and [2009 related formal model](https://doi.org/10.1007/978-3-642-04617-9_41) are linked context, not new catalog entries or separately audited papers.

## Counts and frontier

One existing source deepened E1→E2, zero new bibliography dispositions, zero new unique publications credited, zero new alias dispositions, zero E3, one unresolved administrative award locator, no page-image failures. The source code/trace was not acquired or tested. Cumulative initial bibliography dispositions 264/2983 (161 primary metadata records including reviewed subset, 7 aliases including provisional, 96 E0), 2719 untouched; nine E2 and zero E3; 84 initial architecture dispositions (not a closure audit); 10 fiscal years partially examined and zero fully audited. Resume physical row 266; remaining bibliography and archive coverage take precedence over repeated deepening of this paper. No closure, worldwide novelty or hidden AGI claim. No spending, outreach, Ora candidate imports/execution, population experiments, runtime, STOP/PARKED, grants, qualification, approved-file modifications or merge.
