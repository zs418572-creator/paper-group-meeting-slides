# PPT Production Workflow

## 1. Verify the request

Check whether the request is reasonable and feasible. Identify the paper, audience, time limit, language, and whether the user wants a new deck or an edit.

Do not start authoring until the paper text, required figures, and target template are available.

## 2. Read the paper

Extract:

- title, year, task, input, output;
- research background and exact gap;
- method pipeline and important equations;
- datasets, simulation setup, and comparison arms;
- metrics and test sets;
- main results and limitations;
- relation to the user's research direction.

Keep paper evidence separate from your own interpretation.

## 3. Build the content outline

Map the paper into the four-part structure in `four-part-structure.md`.

Split dense topics:

- `评价标准` must be separate from `实验设计`.
- `方法总览` should be separate from `模块 / 参数细节`.
- `主要结果` should be separate from `补充实验 / scaling`.

## 4. Prepare the template

Use `assets/paper-group-meeting-template.pptx` or a user-supplied template.

If import fails because a chart uses negative `axId` values, run:

```bash
python scripts/prepare_template.py input.pptx output.pptx --fix-negative-axis-ids
```

If the theme contains an unused or unwanted font, normalize a copy:

```bash
python scripts/prepare_template.py input.pptx output.pptx --replace-font "等线=微软雅黑"
```

Do not edit the source template in place.

## 5. Author the deck

Use the `presentations` skill and `artifact_tool`.

Recommended order:

1. Copy the template to a private build directory.
2. Create or reset all content slides.
3. Add the contents page and section dividers.
4. Rebuild dense pages into separate slides.
5. Add editable tables and charts from complete, traceable data.
6. Put the spoken script into speaker notes.
7. Export a new draft filename.

## 6. Preserve slide order

If display order must be written into the PPTX, create an order JSON containing one unique text marker per slide and run:

```bash
python scripts/reorder_slides.py input.pptx output.pptx --order-file order.json
```

Example:

```json
[
  "Paper title",
  "汇报结构",
  "研究背景",
  "论文核心内容"
]
```

## 7. Validate and render

Use the `presentations` skill finalizer and render every slide.

Check:

- 16:9 size and expected page count;
- footer page numbers after reordering;
- no text clipping or unintended overlap;
- font policy passes with approved fonts;
- native tables and charts are editable;
- embedded chart workbook exists when quantitative charts are required;
- speaker notes exist;
- cover placeholders are intentional.

## 8. Deliver

Write a new file with a descriptive name. Do not overwrite the supplied template or a previous deck.

Mention placeholders explicitly, and provide the final file path with a file citation.
