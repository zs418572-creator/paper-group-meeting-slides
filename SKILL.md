---
name: paper-group-meeting-slides
description: Create or revise Chinese paper-reading group-meeting PowerPoint decks with a reusable academic template, four-part narrative, speaker notes, and validated production scripts.
---

# Paper Group Meeting Slides

## Purpose

Use this skill when the user asks to:

- Create a Chinese 组会汇报 PPT from a research paper.
- Revise the narrative, layout, metrics, or experiments of an existing paper deck.
- Produce a spoken presentation script or speaker notes.
- Reuse a general academic slide template with a four-part paper-reading structure.
- Answer follow-up paper-reading questions in the same teaching style.

## Core defaults

- Reply in Chinese; keep standard technical terms in English and explain them at first use.
- Separate paper evidence from reasonable inference.
- Preserve the user's own takeaway unless it is factually wrong.
- Before executing a paper, code, or experiment task, perform a brief reasonableness and feasibility check.
- Connect speech/audio papers to relevant directions such as world models, AVSE, AVSS, spatial audio, self-supervised speech representation, or embodied hearing when appropriate.
- Every paper discussion or deck must include a research-connection module. State the direct connection, transferable mechanism, one concrete experiment, and what does not transfer. If the connection is weak, say so instead of forcing it.

## Four-part narrative

Use this structure unless the user requests another one:

1. 研究背景
2. 主要内容
3. 方法与评价标准
4. 实验设计与我的理解

See `references/four-part-structure.md` for the slide-by-slide map.

## Research connection module

Read `references/research-connections.md` before answering research-relevance questions or creating the final section of a deck.

The module must cover:

1. Direct connection to the configured research directions.
2. Transferable mechanism or model component.
3. One concrete experiment or ablation.
4. Boundary, risk, or non-transferable assumption.
5. Optional next step.

Use the connection levels `Direct`, `Transferable`, or `Weak`. A weak connection is allowed; a fabricated connection is not.

## Deck production

- Read and use the `presentations` skill.
- Start from `assets/paper-group-meeting-template.pptx` or a user-supplied template.
- Use `artifact_tool` for authoring. Do not use `python-pptx` to build or edit the deck.
- Keep the 16:9 canvas, blue header bars, footer, page numbers, and a Chinese-friendly font.
- Prefer editable shapes, native tables, and native charts.
- Put the full spoken script in speaker notes; keep slide text concise.
- Keep `评价标准` separate from `实验设计`.
- Render and inspect every slide before delivery.
- Write a new output file; never overwrite the supplied template.

## Template repair and ordering

- If template import fails due to negative chart axis IDs, run `scripts/prepare_template.py`.
- If slide order must be persisted after reordering, use `scripts/reorder_slides.py`.
- Follow `references/ppt-production-workflow.md` for the full build and validation sequence.

## Answer and script style

Read `references/paper-answer-style.md` when explaining concepts or writing speaker notes.

Core behavior:

- Start with a one-sentence answer.
- Move from intuition to mechanism, then to a concrete example or calculation.
- For comparisons, state both what is similar and what is different.
- Avoid generic filler and marketing language.
- Preserve the user's original meaning when polishing a personal takeaway.

## Resources

- `references/four-part-structure.md`
- `references/ppt-production-workflow.md`
- `references/template-spec.md`
- `references/paper-answer-style.md`
- `references/research-connections.md`
- `scripts/prepare_template.py`
- `scripts/reorder_slides.py`
- `assets/paper-group-meeting-template.pptx`
