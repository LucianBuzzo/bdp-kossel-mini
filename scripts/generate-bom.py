#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOM_DIR = ROOT / "bom"
OUTPUT_CSV = BOM_DIR / "combined.csv"
OUTPUT_MD = BOM_DIR / "README.md"
ASSEMBLY_NAMES = {
    "psu": "PSU",
}


def read_component_boms():
    rows = []
    component_rows = {}
    for path in sorted(BOM_DIR.glob("*.csv")):
        if path.name == "combined.csv":
            continue
        assembly = path.stem
        component_rows[assembly] = []
        with path.open(newline="") as handle:
            for row in csv.DictReader(handle):
                row = {key: value.strip() for key, value in row.items()}
                row["assembly"] = assembly
                row["quantity"] = float(row["quantity"])
                rows.append(row)
                component_rows[assembly].append(row)
    return rows, component_rows


def format_quantity(quantity):
    if quantity.is_integer():
        return str(int(quantity))
    return str(quantity)


def combine_rows(rows):
    combined = {}
    notes_by_key = defaultdict(lambda: defaultdict(set))
    assemblies_by_key = defaultdict(set)

    for row in rows:
        key = (row["part"], row["unit"], row["spec"])
        if key not in combined:
            combined[key] = {
                "part": row["part"],
                "quantity": 0.0,
                "unit": row["unit"],
                "spec": row["spec"],
            }
        combined[key]["quantity"] += row["quantity"]
        assemblies_by_key[key].add(row["assembly"])
        if row["notes"]:
            notes_by_key[key][row["assembly"]].add(row["notes"])

    output = []
    for key, row in combined.items():
        assemblies = sorted(assemblies_by_key[key])
        notes = []
        for assembly, assembly_notes in sorted(notes_by_key[key].items()):
            for note in sorted(assembly_notes):
                if len(assemblies) > 1:
                    notes.append(f"{assembly}: {note}")
                else:
                    notes.append(note)
        output.append(
            {
                "part": row["part"],
                "quantity": format_quantity(row["quantity"]),
                "unit": row["unit"],
                "spec": row["spec"],
                "used_in": ", ".join(assemblies),
                "notes": "; ".join(notes),
            }
        )
    return sorted(output, key=lambda row: (row["part"].lower(), row["spec"].lower()))


def write_combined_csv(rows):
    fieldnames = ["part", "quantity", "unit", "spec", "used_in", "notes"]
    with OUTPUT_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows, include_used_in=True):
    headers = ["Part", "Quantity", "Unit", "Spec"]
    if include_used_in:
        headers.append("Used in")
    headers.append("Notes")

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    for row in rows:
        values = [row["part"], row["quantity"], row["unit"], row["spec"]]
        if include_used_in:
            values.append(row["used_in"])
        values.append(row["notes"])
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def write_markdown(combined_rows, component_rows):
    component_sections = []
    for assembly, rows in sorted(component_rows.items()):
        display_rows = []
        for row in rows:
            display_rows.append(
                {
                    "part": row["part"],
                    "quantity": format_quantity(row["quantity"]),
                    "unit": row["unit"],
                    "spec": row["spec"],
                    "notes": row["notes"],
                }
            )
        component_sections.append(
            "### {name}\n\n{table}".format(
                name=ASSEMBLY_NAMES.get(assembly, assembly.title()),
                table=markdown_table(display_rows, include_used_in=False),
            )
        )
    component_content = "\n\n".join(component_sections)

    content = f"""# Bill of Materials

This BOM is generated from the component CSV files in this directory. Do not edit it directly.

To update it, edit the relevant component CSV and run:

```sh
python3 scripts/generate-bom.py
```

The generated combined CSV is available at [`combined.csv`](./combined.csv).

## Combined BOM

{markdown_table(combined_rows)}

## Component BOMs

{component_content}
"""
    OUTPUT_MD.write_text(content)


def main():
    source_rows, component_rows = read_component_boms()
    rows = combine_rows(source_rows)
    write_combined_csv(rows)
    write_markdown(rows, component_rows)


if __name__ == "__main__":
    main()
