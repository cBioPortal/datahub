#!/usr/bin/env python3
"""Audit datahub studies against the latest stable Oncotree.

Reads each public/*/data_clinical_sample.txt, resolves every ONCOTREE_CODE
against https://oncotree.mskcc.org/api/tumorTypes?version=oncotree_latest_stable
(the API behind oncotree.info), and reports per study:
  - stale codes (no longer present in Oncotree)
  - CANCER_TYPE values that differ from the code's current mainType
  - CANCER_TYPE_DETAILED values that differ from the code's current name

Writes a markdown report and a JSON file with the raw findings.

Usage: oncotree_audit.py [--root ~/Code/datahub/public]
                         [--out-md ~/oncotree_audit.md]
                         [--out-json ~/oncotree_audit.json]
"""
import argparse
import collections
import json
import os
import urllib.request

ONCOTREE_URL = "https://oncotree.mskcc.org/api/tumorTypes?version=oncotree_latest_stable"


def fetch_oncotree():
    with urllib.request.urlopen(ONCOTREE_URL, timeout=60) as r:
        tumor_types = json.load(r)
    return {t["code"]: (t.get("mainType") or "", t.get("name") or "") for t in tumor_types}


def is_lfs_pointer(path):
    try:
        with open(path, "rb") as f:
            return f.read(30).startswith(b"version https://git-lfs")
    except OSError:
        return True


def audit_study(clin_path, onco):
    """Returns dict with stale/ct/ctd counters, or None if no ONCOTREE_CODE column."""
    with open(clin_path, errors="replace") as f:
        header = None
        for line in f:
            if line.startswith("#"):
                continue
            header = line.rstrip("\n").split("\t")
            break
        if not header or "ONCOTREE_CODE" not in header:
            return None
        oc_i = header.index("ONCOTREE_CODE")
        ct_i = header.index("CANCER_TYPE") if "CANCER_TYPE" in header else None
        ctd_i = header.index("CANCER_TYPE_DETAILED") if "CANCER_TYPE_DETAILED" in header else None
        stale = collections.Counter()
        ct_mismatch = collections.Counter()
        ctd_mismatch = collections.Counter()
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if oc_i >= len(parts):
                continue
            code = parts[oc_i].strip()
            if not code or code == "NA":
                continue
            if code not in onco:
                stale[code] += 1
                continue
            main_type, name = onco[code]
            if ct_i is not None and ct_i < len(parts):
                v = parts[ct_i].strip()
                if v and v != "NA" and v != main_type:
                    ct_mismatch[(code, v, main_type)] += 1
            if ctd_i is not None and ctd_i < len(parts):
                v = parts[ctd_i].strip()
                if v and v != "NA" and v != name:
                    ctd_mismatch[(code, v, name)] += 1
        if not (stale or ct_mismatch or ctd_mismatch):
            return {}
        return {"stale": stale, "ct": ct_mismatch, "ctd": ctd_mismatch}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.expanduser("~/Code/datahub/public"))
    ap.add_argument("--out-md", default=os.path.expanduser("~/oncotree_audit.md"))
    ap.add_argument("--out-json", default=os.path.expanduser("~/oncotree_audit.json"))
    args = ap.parse_args()

    onco = fetch_oncotree()
    print(f"loaded {len(onco)} oncotree codes", flush=True)

    results = {}
    skipped_pointer = []
    no_code_column = []
    for study in sorted(os.listdir(args.root)):
        clin = os.path.join(args.root, study, "data_clinical_sample.txt")
        if not os.path.isfile(clin):
            continue
        if is_lfs_pointer(clin):
            skipped_pointer.append(study)
            continue
        r = audit_study(clin, onco)
        if r is None:
            no_code_column.append(study)
        elif r:
            results[study] = r

    # ---- markdown report ----
    def issue_weight(r):
        return sum(r["stale"].values()) + sum(r["ct"].values()) + sum(r["ctd"].values())

    lines = ["# Oncotree audit — datahub `public/` vs Oncotree latest stable", ""]
    lines.append(f"Studies with issues: **{len(results)}**. "
                 f"Studies lacking ONCOTREE_CODE column: {len(no_code_column)}. "
                 f"Skipped (LFS pointer): {len(skipped_pointer)}.")
    lines.append("")
    lines.append("| Study | Stale codes | CANCER_TYPE mismatches | CANCER_TYPE_DETAILED mismatches | Affected samples |")
    lines.append("|---|---|---|---|---|")
    for study, r in sorted(results.items(), key=lambda kv: -issue_weight(kv[1])):
        lines.append(f"| {study} | {len(r['stale'])} | {len(r['ct'])} | {len(r['ctd'])} | {issue_weight(r)} |")
    lines.append("")
    for study, r in sorted(results.items(), key=lambda kv: -issue_weight(kv[1])):
        lines.append(f"## {study}")
        if r["stale"]:
            lines.append("**Stale ONCOTREE_CODEs** (absent from latest Oncotree):")
            for code, n in r["stale"].most_common():
                lines.append(f"- `{code}` — {n} samples")
        if r["ct"]:
            lines.append("**CANCER_TYPE out of date** (file value → current mainType):")
            for (code, old, new), n in r["ct"].most_common():
                lines.append(f"- `{code}`: \"{old}\" → \"{new}\" — {n} samples")
        if r["ctd"]:
            lines.append("**CANCER_TYPE_DETAILED out of date** (file value → current name):")
            for (code, old, new), n in r["ctd"].most_common():
                lines.append(f"- `{code}`: \"{old}\" → \"{new}\" — {n} samples")
        lines.append("")
    with open(args.out_md, "w") as f:
        f.write("\n".join(lines))

    # ---- json ----
    out = {
        study: {
            "stale_codes": dict(r["stale"]),
            "cancer_type_mismatch": {f"{c}|{a}=>{b}": n for (c, a, b), n in r["ct"].items()},
            "cancer_type_detailed_mismatch": {f"{c}|{a}=>{b}": n for (c, a, b), n in r["ctd"].items()},
        } for study, r in results.items()
    }
    with open(args.out_json, "w") as f:
        json.dump(out, f, indent=1)

    total_stale = sum(sum(r["stale"].values()) for r in results.values())
    total_ct = sum(sum(r["ct"].values()) for r in results.values())
    total_ctd = sum(sum(r["ctd"].values()) for r in results.values())
    print(f"studies with issues: {len(results)}")
    print(f"samples with stale codes: {total_stale}")
    print(f"samples with CANCER_TYPE mismatch: {total_ct}")
    print(f"samples with CANCER_TYPE_DETAILED mismatch: {total_ctd}")
    print(f"wrote {args.out_md} and {args.out_json}")


if __name__ == "__main__":
    main()
