# Paper Group Meeting Slides

A Codex skill for creating Chinese paper-reading group-meeting PowerPoint decks with a four-part narrative, speaker notes, and a reusable academic template.

## Installation

Copy or clone this folder into your Codex skills directory:

```text
~/.codex/skills/paper-group-meeting-slides/
```

The skill is then available as `$paper-group-meeting-slides`.

## Structure

```text
paper-group-meeting-slides/
|-- SKILL.md
|-- agents/
|-- assets/
|   |-- paper-group-meeting-template.pptx
|   `-- README.md
|-- references/
|   |-- four-part-structure.md
|   |-- paper-answer-style.md
|   |-- ppt-production-workflow.md
|   `-- template-spec.md
`-- scripts/
    |-- prepare_template.py
    `-- reorder_slides.py
```

## Presentation structure

1. 研究背景
2. 主要内容
3. 方法与评价标准
4. 实验设计与我的理解

## Example invocation

```text
使用 $paper-group-meeting-slides 根据这篇论文制作四部分结构的组会汇报 PPT。
```


## Notes

- The template contains no institutional logo, personal name, advisor name, or private example paper content.
- `artifact_tool` is used for deck authoring; `python-pptx` is not used for slide generation.
- Verify that you have the right to distribute template background assets before publishing this repository.

## License

MIT License. See [LICENSE](LICENSE).
