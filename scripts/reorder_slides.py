#!/usr/bin/env python3
"""Persist PPTX slide order using unique text markers.

The order file is a JSON list of strings. Each string must match exactly one
slide. Matching uses all <a:t> text nodes in each slide XML.

Example order.json:
  [
    "Paper title",
    "汇报结构",
    "研究背景",
    "论文核心内容"
  ]

Example command:
  python reorder_slides.py in.pptx out.pptx --order-file order.json
"""
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def relationship_map(rels_xml: str) -> dict[str, str]:
    rels: dict[str, str] = {}
    for attrs in re.findall(r"<Relationship\b([^>]+)>", rels_xml):
        id_match = re.search(r'Id="([^"]+)"', attrs)
        target_match = re.search(r'Target="([^"]+)"', attrs)
        if id_match and target_match:
            rels[id_match.group(1)] = target_match.group(1)
    return rels


def slide_text(xml: str) -> str:
    return "\n".join(html.unescape(value) for value in re.findall(r"<a:t>(.*?)</a:t>", xml, re.S))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--order-file", required=True)
    args = parser.parse_args()

    source = Path(args.input)
    target = Path(args.output)
    if source.resolve() == target.resolve():
        raise SystemExit("Refusing to overwrite the source file. Choose a new output path.")
    markers = json.loads(Path(args.order_file).read_text(encoding="utf-8"))
    if not isinstance(markers, list) or not all(isinstance(x, str) and x for x in markers):
        raise SystemExit("order file must be a JSON list of non-empty strings")

    with ZipFile(source, "r") as z:
        names = z.namelist()
        presentation_xml = z.read("ppt/presentation.xml").decode("utf-8")
        rels_xml = z.read("ppt/_rels/presentation.xml.rels").decode("utf-8")
        rels = relationship_map(rels_xml)
        slide_texts: dict[str, str] = {}
        for name in names:
            if re.fullmatch(r"ppt/slides/slide\d+\.xml", name):
                slide_texts[name] = slide_text(z.read(name).decode("utf-8", "replace"))

        ordered: list[str] = []
        used: set[str] = set()
        for marker in markers:
            hits = [name for name, text in slide_texts.items() if marker in text and name not in used]
            if len(hits) != 1:
                raise SystemExit(f"marker {marker!r} matched {len(hits)} slides: {hits}")
            ordered.append(hits[0])
            used.add(hits[0])
        if len(used) != len(slide_texts):
            raise SystemExit(f"ordered {len(used)} of {len(slide_texts)} slides; leftovers: {sorted(set(slide_texts) - used)}")

        block_match = re.search(r"<p:sldIdLst>(.*?)</p:sldIdLst>", presentation_xml, re.S)
        if not block_match:
            raise SystemExit("ppt/presentation.xml has no p:sldIdLst")
        block = block_match.group(0)
        inner = block_match.group(1)
        entries = re.findall(r"<p:sldId\b[^>]*/>", inner)
        by_slide: dict[str, str] = {}
        for entry in entries:
            rid_match = re.search(r'r:id="([^"]+)"', entry)
            if not rid_match or rid_match.group(1) not in rels:
                raise SystemExit(f"cannot resolve slide relationship: {entry}")
            rel_target = rels[rid_match.group(1)].lstrip("/")
            if not rel_target.startswith("ppt/"):
                rel_target = "ppt/" + rel_target
            by_slide[rel_target] = entry
        new_inner = "".join(by_slide[name] for name in ordered)
        new_block = block.replace(inner, new_inner)
        new_presentation = presentation_xml[:block_match.start()] + new_block + presentation_xml[block_match.end():]

    with ZipFile(source, "r") as zin, ZipFile(target, "w", ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "ppt/presentation.xml":
                data = new_presentation.encode("utf-8")
            zout.writestr(item, data)

    print(f"wrote reordered deck: {target}")


if __name__ == "__main__":
    main()
