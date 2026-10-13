#!/usr/bin/env python3
"""Repair a PPTX copy for artifact-tool import.

This script uses only the Python standard library and changes the package copy,
never the source file.

Supported repairs:
  * Replace one or more font families in theme, slide master, layout, and slide XML.
  * Convert negative chart axis IDs to positive IDs and update matching crossAx refs.

Examples:
  python prepare_template.py in.pptx out.pptx --fix-negative-axis-ids
  python prepare_template.py in.pptx out.pptx --replace-font "等线=微软雅黑"
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def parse_font_map(values: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for value in values:
        if "=" not in value:
            raise SystemExit(f"font replacement must be OLD=NEW, got: {value}")
        old, new = value.split("=", 1)
        old, new = old.strip(), new.strip()
        if not old or not new:
            raise SystemExit(f"font replacement must be OLD=NEW, got: {value}")
        result[old] = new
    return result


def repair_chart_axis_ids(xml: str) -> tuple[str, int]:
    negative_ids = sorted(set(re.findall(r'<c:axId val="(-\d+)"', xml)), key=lambda s: int(s))
    if not negative_ids:
        return xml, 0
    mapping: dict[str, str] = {}
    for idx, value in enumerate(negative_ids, start=1):
        positive = str(2_000_000_000 + idx)
        mapping[value] = positive
    for old, new in mapping.items():
        xml = xml.replace(f'<c:axId val="{old}"', f'<c:axId val="{new}"')
        xml = xml.replace(f'<c:crossAx val="{old}"', f'<c:crossAx val="{new}"')
    return xml, len(mapping)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--replace-font", action="append", default=[])
    parser.add_argument("--fix-negative-axis-ids", action="store_true")
    args = parser.parse_args()

    source = Path(args.input)
    target = Path(args.output)
    if source.resolve() == target.resolve():
        raise SystemExit("Refusing to overwrite the source file. Choose a new output path.")
    fonts = parse_font_map(args.replace_font)

    with ZipFile(source, "r") as zin, ZipFile(target, "w", ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            name = item.filename
            if fonts and name.startswith(("ppt/theme/", "ppt/slideMasters/", "ppt/slideLayouts/", "ppt/slides/")):
                text = data.decode("utf-8", "replace")
                for old, new in fonts.items():
                    text = text.replace(old, new)
                data = text.encode("utf-8")
            if args.fix_negative_axis_ids and name.startswith("ppt/charts/") and name.endswith(".xml"):
                text = data.decode("utf-8", "replace")
                text, changed = repair_chart_axis_ids(text)
                if changed:
                    print(f"fixed {changed} negative axis ID(s) in {name}")
                data = text.encode("utf-8")
            zout.writestr(item, data)

    print(f"wrote {target}")


if __name__ == "__main__":
    main()
