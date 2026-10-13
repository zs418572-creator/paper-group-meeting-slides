# Research Direction Connections

This skill must connect every paper discussion or deck to the configured research profile when a meaningful connection exists. Do not force a connection when the paper is genuinely distant.

## Target research profile

### Primary direction 1: World Models × Speech/Audio

- audio world models;
- speech and audio generation;
- temporal prediction and latent dynamics;
- neural audio codecs and discrete audio tokens;
- self-supervised speech representation;
- generative modeling with diffusion, flow matching, autoregressive, or SSM-based backbones.

### Primary direction 2: Embodied Auditory AI

- audio-visual speech enhancement and separation, especially AVSE and AVSS;
- sound source localization and spatial hearing;
- room impulse response, HRTF, binaural and multichannel audio;
- audio-visual fusion, synchronization, and alignment;
- robot or agent auditory perception;
- multimodal large models for embodied perception.

### Existing research foundation

- speech separation: TF-GridNet, Conv-TasNet, SepFormer, Mamba/SSM models;
- microphone-array processing: beamforming, MVDR, SDW-MWF;
- audio-visual modeling and cross-modal attention;
- Universal Speech Enhancement tasks and URGENT-style data simulation;
- data curation, non-intrusive quality metrics, and reproducible experiment design.

## Required connection output

For every paper, answer these four questions:

1. **Direct connection**  
   Is the task, dataset, metric, or model directly related to the research profile?

2. **Transferable mechanism**  
   Which component could be reused, adapted, or combined with existing work?

3. **New experiment**  
   What is one concrete experiment, ablation, or research hypothesis that follows from the paper?

4. **Boundary or risk**  
   What assumptions, data conditions, or evaluation choices would prevent direct transfer?

A fifth optional item is a short next step:

5. **Next step**  
   What should be read, implemented, or tested first?

## Connection levels

Use one of these levels explicitly:

| Level | Meaning | Typical evidence |
|---|---|---|
| Direct | Same or nearly same task, data, or model family | AVSE/AVSS, spatial audio, world-model sequence prediction |
| Transferable | Different task but reusable mechanism | RIR simulation, SSM block, data filtering, representation learning |
| Weak | Conceptual relation only | Generic scaling laws, unrelated image tasks, distant application domains |

If the connection is weak, state it clearly. Do not invent a research opportunity merely to satisfy the format.

## Connection map

| Paper topic | World model × speech/audio | AVSE / AVSS | Embodied auditory AI | Model / SSM relevance | Data and evaluation relevance |
|---|---|---|---|---|---|
| Speech enhancement | predictive clean-state modeling | audio branch or front end | noisy robot hearing | causal or non-causal sequence modeling | simulation, metrics, real-room generalization |
| Audio-visual separation | multimodal latent state | direct AVSS connection | audio-visual scene understanding | cross-modal fusion and temporal alignment | synchronization and speaker consistency |
| Sound source localization | spatial state estimation | spatial prior for enhancement | direct connection | sequence model and causal updating | array calibration and room variation |
| Neural audio codec | discrete audio state/tokenizer | reconstruction and generation branch | sensor-to-action representation | token sequence modeling | codec robustness and real recordings |
| RIR / room acoustics | acoustic world state | reverberation simulation or dereverberation | direct spatial-hearing connection | temporal convolution and state estimation | simulated-to-real gap |
| Data curation | training distribution control | training-data filtering | sensor-quality control | scaling and curriculum learning | metric bias and held-out evaluation |
| Self-supervised representation | latent speech state | representation prior | robust perception under noise | pretraining and fine-tuning | label efficiency and transfer |

## PPT placement

In a four-part paper deck, add one dedicated page or one clearly separated block:

```text
实验设计与我的理解
├── 实验设计
├── 主要结果
├── 补充实验
├── 与我研究方向的联系
└── 我的理解与后续研究
```

The connection page should contain:

- one direct connection;
- one transferable idea;
- one concrete experiment;
- one limitation or non-transferable part.

If the talk is short, combine this with the final personal-understanding slide, but keep the four connection elements visible.

## Answer template

```text
直接联系：
- ...

可迁移方法：
- ...

可设计的新实验：
- ...

不能直接照搬的地方：
- ...

下一步：
- ...
```

Use technical English terms when they are standard, while keeping the explanation in Chinese.
