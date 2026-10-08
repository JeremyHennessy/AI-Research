# Audio-native AI, continual learning, and brain-inspired computation

**Evidence:** public foundational paper abstracts and current 2026 conference/journal descriptions. The 2026 results below are author-reported; no speech model or biological computing system was trained here.

## A. Why audio isn't just text in another container
Speech carries linguistic content but also prosody, timing, speaker turn-taking, noise, acoustic scene, and emotion-related cues. A system that transcribes speech to text may lose information. An end-to-end audio-language system potentially retains those cues, at the expense of harder sequence alignment, larger data and real-time streaming constraints.

| Approach | Modeling objective / data | Advantage to test | Pitfalls |
|---|---|---|---|
| [wav2vec 2.0](https://arxiv.org/abs/2006.11477) | Masked latent audio contrastive representation, discrete targets | Reduced transcript-label demand | Dependence on acoustic domain and pretext loss |
| [Whisper](https://arxiv.org/abs/2212.04356) | Large multilingual weakly supervised audio/transcript data | Zero-shot ASR robustness | Silence hallucinations, accents and recording shift |
| [AudioPaLM](https://arxiv.org/abs/2306.12925) | Speech tokens combined with powerful text LM | Speech understanding/generation, translation, voice cues | Speaker safety and multi-stage architecture confounds |
| [SeamlessM4T](https://arxiv.org/abs/2308.11596) | Unified speech/text translation and speech recognition | Direct crossmodal translation | Low-resource bias, noise, compute, cascade comparator |
| [Qwen2-Audio](https://arxiv.org/abs/2407.10759) | Audio-language instruction training with different interaction modes | Acoustic event understanding beyond transcripts | Dataset and prompt artifact |
| [ICLR 2026 speech-data study](https://proceedings.iclr.cc/paper_files/paper/2026/hash/63b96ace3e28465aff61918e77de2a00-Abstract-Conference.html) | Processing and synthetic/interleaved training data | Architecture-independent data improvements | Tricky data matching and leakage |
| [PACE audio continual learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/26cce1e512793f2072fd27c391e04652-Abstract-Conference.html) | Audio representations adapted sequentially | Long-term adaptation without losing earlier abilities | Representation saturation and fine-grained drift |

## B. E26: a controlled audio research matrix
**Task groups:** speech-to-text, background event Q&A, speaker turn tracking, command following, speech translation. **Holdouts:** microphone/device, speaker, language, ambient noise, recording date, overlapping sound events. **Baselines:** ASR→text LM cascade; frozen audio encoder + LM; direct audio model. Keep compute and data rights aligned.

**Metrics:**
- **ASR:** word error rate (WER) per language/accent/noise stratum, and insertion of unsupported speech in silence.
- **Audio QA:** grounded answer accuracy under contradictory transcript vs waveform.
- **Translation:** semantic adequacy and error severity by human review, not BLEU alone.
- **Streaming:** end-to-end delay, p95 latency, chunk consistency and interruptions.
- **Privacy:** speaker identification/reproduction risks, rights to training audio, consent and deletion.
- **Continual adaptation:** new-task gain vs old-task retention after each incremental audio session.

**Do not conclude:** a multimodal decoder is universally better just because it sees more inputs, or a low transcript WER implies it understands the environment's non-speech context.

## C. Brain-inspired methods: mechanism over metaphor

What neuroscience can contribute:
- **Spatial/predictive memory:** learn states that forecast future transitions and reflect action consequences.
- **Selective attention/working memory:** allocate finite resources to relevant information, and forget or suppress irrelevant data.
- **Active inference:** use predictions and uncertainty to select informative actions.
- **Continual learning:** adapt new tasks without catastrophic loss of old competence.
- **Energy-efficient computation:** asynchronous/spiking or sparse signals may reduce some hardware work.

[Reinforcement Learning through Active Inference (2020)](https://arxiv.org/abs/2002.12636) develops an exploration/exploitation objective inspired by expected free energy. Simplifying greatly, actions can be chosen based on both **expected task value** and **expected information gain** about the state/mechanisms. This is not universally more efficient than carefully tuned RL.

[2026 Nature Computational Science brain-computing review](https://www.nature.com/articles/s43588-026-01012-x) surveys neuromorphic and organoid approaches. Current organoid computing is a highly exploratory biological research area with major ethics and reproducibility challenges; a biological analogy is **not** a demonstrated blueprint for a superior text LLM.

## D. E27: active exploration vs reflexive curiosity
In a small deterministic procedural world, compare:
1. Random exploration;
2. Reward-seeking policy;
3. Prediction-error/novelty policy;
4. Expected information gain about hidden transitions;
5. Information-gain policy that is penalized for duplicate probes.

Hold out mechanism combinations and evaluate **realized task success**, not just movement or how surprising a state appeared. Report model prediction calibration, action cost and unresolved unknowns. An agent that generates endless novelty without solving new tasks did not become more capable.

## E. Opportunity for the next AI
An integrated system may learn grounded observations, update explicit temporally scoped state, build a compact world-transition model and act to resolve uncertainty. Whether that helps language and other domains is **an experimental question**. Compare it to strong supervised multimodal and agent baselines, and distinguish new representation learning from a better tool interface.
