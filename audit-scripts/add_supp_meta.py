#!/usr/bin/env python3
"""Add missing meta files for bare data_clinical_supp*.txt files.

Scans study directories under the given root (default: public/). For every
data_clinical_supp*.txt with no matching meta_clinical_supp*.txt, writes one:

    cancer_study_identifier: <from meta_study.txt>
    genetic_alteration_type: CLINICAL
    datatype: SAMPLE_ATTRIBUTES | PATIENT_ATTRIBUTES
    data_filename: <data file name>

datatype is SAMPLE_ATTRIBUTES when the data file's column header contains
SAMPLE_ID, else PATIENT_ATTRIBUTES.

Files with malformed attribute headers (fewer than 4 leading '#' rows, or a
missing '#' prefix on one of them) are still given a meta file but reported,
since the validator will likely complain about the data file itself.

Usage: add_supp_meta.py [root_dir] [--dry-run]
"""
import sys
from pathlib import Path

META_TEMPLATE = """\
cancer_study_identifier: {study_id}
genetic_alteration_type: CLINICAL
datatype: {datatype}
data_filename: {data_filename}
"""


def study_id_from_meta(study_dir: Path):
    meta_study = study_dir / "meta_study.txt"
    if not meta_study.exists():
        return None
    for line in meta_study.read_text().splitlines():
        if line.startswith("cancer_study_identifier:"):
            return line.split(":", 1)[1].strip()
    return None


def inspect_data_file(path: Path):
    """Return (datatype, warning). Reads the leading '#' rows and the column
    header line."""
    comment_rows = 0
    header = None
    with open(path) as f:
        for line in f:
            if line.startswith("#"):
                comment_rows += 1
                continue
            header = line.rstrip("\n").split("\t")
            break
    if header is None:
        return None, "empty file"
    warning = None
    if comment_rows < 4:
        warning = f"only {comment_rows} '#' header rows (validator expects 4+)"
    datatype = (
        "SAMPLE_ATTRIBUTES" if "SAMPLE_ID" in header else "PATIENT_ATTRIBUTES"
    )
    return datatype, warning


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry_run = "--dry-run" in sys.argv[1:]
    root = Path(args[0]) if args else Path("public")

    created, skipped, warnings = 0, [], []
    for data_file in sorted(root.glob("*/data_clinical_supp*.txt")):
        study_dir = data_file.parent
        meta_file = study_dir / ("meta_" + data_file.name[len("data_"):])
        if meta_file.exists():
            continue
        study_id = study_id_from_meta(study_dir)
        if study_id is None:
            skipped.append(f"{study_dir.name}: no meta_study.txt")
            continue
        datatype, warning = inspect_data_file(data_file)
        if datatype is None:
            skipped.append(f"{data_file}: {warning}")
            continue
        if warning:
            warnings.append(f"{data_file}: {warning}")
        content = META_TEMPLATE.format(
            study_id=study_id, datatype=datatype, data_filename=data_file.name
        )
        if dry_run:
            print(f"would write {meta_file} ({datatype})")
        else:
            meta_file.write_text(content)
            print(f"wrote {meta_file} ({datatype})")
        created += 1

    print(f"\n{created} meta files {'needed' if dry_run else 'written'}")
    for s in skipped:
        print(f"SKIPPED {s}")
    for w in warnings:
        print(f"WARNING {w}")


if __name__ == "__main__":
    main()
