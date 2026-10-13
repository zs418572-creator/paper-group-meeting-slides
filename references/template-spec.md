# Template Specification

## Canvas

- 16:9.
- Artifact Tool size: `1280 × 720` CSS pixels.
- OOXML slide size: `12192000 × 6858000` EMU.

## Typography

- Primary font: `微软雅黑`.
- Page title: 30-34 px, bold, dark title color.
- Section divider title: 38-42 px, bold.
- Card heading: 21-23 px, bold.
- Body: 16-20 px.
- Table body: 14-16 px.
- Footer: 12 px.
- Avoid body text below 14 px.

## Core colors

| Role | Hex |
|---|---|
| Deep academic blue | `#1F4E78` |
| Main accent blue | `#2E75B6` |
| Light blue accent | `#5B9BD5` |
| Pale background | `#EAF3FA` |
| Alternate band | `#F4F8FC` |
| Border | `#BFD3E6` |
| Page title | `#333F48` |
| Body text | `#263442` |
| Muted text | `#66717B` |
| Warning / error | `#C00000` |
| Positive | `#548235` |
| Amber note | `#BF8F00` |

## Repeated elements

### Content pages

- Title: around `left=100, top=28, width=1030, height=58`.
- Content region begins near y=120 and ends before y=660.
- Footer bar: `0,688,1280,32`, deep blue.
- Footer left: paper title, white, 12 px.
- Footer right: page number, white, 12 px.
- Keep the three blue bars at the upper left when using the template layout.

### Section dividers

- Full-width pale band around `y=245` to `y=435`.
- Large section number at `x≈92`.
- Section title at `x≈280`.
- Subtitle below the title.
- Keep the background white and the inherited top bars.

### Cover

- Reuse the template background and university logo.
- Center the paper title.
- Keep advisor, presenter, and date centered.
- Update advisor name when the user supplies it.

## Visual rules

- Use pale cards with thin blue borders instead of heavy shadows.
- Use one accent strip per card.
- Use arrows only when direction matters.
- Use red only for warnings, failures, or important limitations.
- Use green for improvements or positive control.
- Keep tables editable and header rows dark blue.
- Charts must have their own explicit 微软雅黑 font settings.
- Preserve the template's repeated footer and page number style.
