#!/usr/bin/env python3
"""Add missing meta files for bare data_timeline*.txt files.

Scans study directories under the given root (default: public/). For every
data_timeline*.txt that has no matching meta_timeline*.txt, writes one:

    cancer_study_identifier: <from meta_study.txt>
    genetic_alteration_type: CLINICAL
    datatype: TIMELINE
    data_filename: <data file name>

Usage: add_timeline_meta.py [root_dir] [--dry-run]
"""
import sys
from pathlib import Path

META_TEMPLATE = """\
cancer_study_identifier: {study_id}
genetic_alteration_type: CLINICAL
datatype: TIMELINE
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


def main():
    args = [a for a in sys.argv[1:] if a != "--dry-run"]
    dry_run = "--dry-run" in sys.argv[1:]
    root = Path(args[0]) if args else Path("public")

    created, skipped = 0, []
    for data_file in sorted(root.glob("*/data_timeline*.txt")):
        study_dir = data_file.parent
        meta_file = study_dir / ("meta_" + data_file.name[len("data_"):])
        if meta_file.exists():
            continue
        study_id = study_id_from_meta(study_dir)
        if study_id is None:
            skipped.append(f"{study_dir.name}: no meta_study.txt")
            continue
        content = META_TEMPLATE.format(
            study_id=study_id, data_filename=data_file.name
        )
        if dry_run:
            print(f"would write {meta_file}")
        else:
            meta_file.write_text(content)
            print(f"wrote {meta_file}")
        created += 1

    print(f"\n{created} meta files {'needed' if dry_run else 'written'}")
    for s in skipped:
        print(f"SKIPPED {s}")


if __name__ == "__main__":
    main()
