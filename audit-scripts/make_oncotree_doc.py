#!/usr/bin/env python3
"""Render datahub-oncotree-audit.md (companion to datahub-behavioral-differences)
from an oncotree_audit.json produced by oncotree_audit.py.

Usage: make_oncotree_doc.py [audit.json] [out.md]
"""
import json
import sys
from datetime import date

audit_path = sys.argv[1] if len(sys.argv) > 1 else "oncotree_audit.json"
out_path = sys.argv[2] if len(sys.argv) > 2 else "datahub-oncotree-audit.md"
d = json.load(open(audit_path))

def split_key(k):
    code, rest = k.split("|", 1)
    old, new = rest.split("=>", 1)
    return code, old, new

def is_quote_artifact(old, new):
    return old.strip('"') == new

stale, ct, ctd = {}, {}, {}
quote_ct = quote_ctd = 0
for study, r in d.items():
    for code, n in r["stale_codes"].items():
        e = stale.setdefault(code, [0, set()]); e[0] += n; e[1].add(study)
    for k, n in r["cancer_type_mismatch"].items():
        code, old, new = split_key(k)
        if is_quote_artifact(old, new):
            quote_ct += n
            continue
        e = ct.setdefault((code, old, new), [0, set()]); e[0] += n; e[1].add(study)
    for k, n in r["cancer_type_detailed_mismatch"].items():
        code, old, new = split_key(k)
        if is_quote_artifact(old, new):
            quote_ctd += n
            continue
        e = ctd.setdefault((code, old, new), [0, set()]); e[0] += n; e[1].add(study)

stale_total = sum(e[0] for e in stale.values())
ct_total = sum(e[0] for e in ct.values())
ctd_total = sum(e[0] for e in ctd.values())

L = []
L.append("# Datahub Studies with Oncotree Drift")
L.append("")
L.append(f"Companion to *Datahub Studies with Behavioral Import Differences*. "
         f"Studies in `/Code/datahub/public` whose `data_clinical_sample.txt` "
         f"ONCOTREE_CODE / CANCER_TYPE / CANCER_TYPE_DETAILED values are out of date "
         f"with the latest stable Oncotree (oncotree.info / oncotree.mskcc.org API, "
         f"897 codes). Scanned {date.today().isoformat()}.")
L.append("")
L.append("**Correction to the original doc (section 7):** the JAR only overwrites "
         "CANCER_TYPE / CANCER_TYPE_DETAILED from the Oncotree API for non-datahub roots. "
         "For datahub imports, `ImporterImpl` sets `forceCancerTypeFromOncotree = false` "
         "(`rootDirectory.contains(\"datahub\")`, ImporterImpl.java:459), so existing "
         "columns pass through verbatim — the JAR and metaImport agree on datahub. The "
         "drift below is therefore data staleness in the files themselves, not an "
         "importer behavioral difference. The rewrite only happens when a column is "
         "missing entirely (added and filled from Oncotree; unknown codes become `NA`).")
L.append("")
L.append(f"**Summary:** {len(d)} studies affected — {stale_total:,} samples with stale codes, "
         f"{ct_total:,} with outdated CANCER_TYPE, {ctd_total:,} with outdated "
         f"CANCER_TYPE_DETAILED (quote-only artifacts excluded, see section 4).")
L.append("")
L.append("---")
L.append("")

L.append(f"## 1. Stale ONCOTREE_CODEs ({len(stale)} distinct codes, {stale_total:,} samples)")
L.append("")
L.append("Codes no longer present in Oncotree. A `--force` Oncotree rewrite would set these "
         "samples' CANCER_TYPE and CANCER_TYPE_DETAILED to `NA`; they need manual remapping "
         "(e.g. `GBM`/`AASTR`/`AODG` glioma codes were restructured in Oncotree).")
L.append("")
L.append("| Code | Samples | Studies |")
L.append("|---|---|---|")
for code, (n, studies) in sorted(stale.items(), key=lambda x: -x[1][0]):
    L.append(f"| `{code}` | {n:,} | {len(studies)} |")
L.append("")
L.append("---")
L.append("")

L.append(f"## 2. CANCER_TYPE Out of Date ({len(ct)} distinct mappings, {ct_total:,} samples)")
L.append("")
L.append("File value differs from the code's current Oncotree mainType. Top 20 by sample count:")
L.append("")
L.append("| Code | File value | Current Oncotree mainType | Samples | Studies |")
L.append("|---|---|---|---|---|")
for (code, old, new), (n, studies) in sorted(ct.items(), key=lambda x: -x[1][0])[:20]:
    L.append(f"| `{code}` | {old} | {new} | {n:,} | {len(studies)} |")
L.append("")
L.append("---")
L.append("")

L.append(f"## 3. CANCER_TYPE_DETAILED Out of Date ({len(ctd)} distinct mappings, {ctd_total:,} samples)")
L.append("")
L.append("File value differs from the code's current Oncotree name. Some are renames "
         "(`GB`: Glioblastoma → Glioblastoma, IDH-Wildtype); others look like genuine data "
         "errors (`LUSC` samples labeled Lung Adenocarcinoma, `READ` labeled Colon "
         "Adenocarcinoma). Top 20 by sample count:")
L.append("")
L.append("| Code | File value | Current Oncotree name | Samples | Studies |")
L.append("|---|---|---|---|---|")
for (code, old, new), (n, studies) in sorted(ctd.items(), key=lambda x: -x[1][0])[:20]:
    L.append(f"| `{code}` | {old} | {new} | {n:,} | {len(studies)} |")
L.append("")
L.append("---")
L.append("")

L.append("## 4. Quoting Artifacts")
L.append("")
L.append(f"{quote_ct:,} CANCER_TYPE and {quote_ctd:,} CANCER_TYPE_DETAILED sample values "
         "differ from Oncotree only by surrounding double quotes (e.g. "
         "`\"Biliary Tract Cancer, NOS\"` vs `Biliary Tract Cancer, NOS`) — CSV-style "
         "quoting inside TSV files. Not real drift, but worth normalizing; excluded from "
         "the counts in sections 2 and 3.")
L.append("")
L.append("---")
L.append("")

def weight(r):
    return (sum(r["stale_codes"].values())
            + sum(r["cancer_type_mismatch"].values())
            + sum(r["cancer_type_detailed_mismatch"].values()))

L.append(f"## 5. Per-Study Breakdown ({len(d)} studies)")
L.append("")
L.append("Distinct issue kinds per study; affected samples counts every sample-level hit "
         "(quote artifacts included here).")
L.append("")
L.append("| Study | Stale codes | CANCER_TYPE mismatches | CANCER_TYPE_DETAILED mismatches | Affected samples |")
L.append("|---|---|---|---|---|")
for study, r in sorted(d.items(), key=lambda kv: -weight(kv[1])):
    L.append(f"| `{study}` | {len(r['stale_codes'])} | {len(r['cancer_type_mismatch'])} "
             f"| {len(r['cancer_type_detailed_mismatch'])} | {weight(r):,} |")
L.append("")
L.append("---")
L.append("")

L.append("## Tooling")
L.append("")
L.append("- `oncotree_audit.py` — read-only; regenerates this data "
         "(`oncotree_audit.md` per-study detail + `oncotree_audit.json`).")
L.append("- `oncotree_apply.py` — applies the JAR transformation "
         "(`convertCancerTypesFromOncotree`). Default replicates the datahub path "
         "(only adds missing columns); `--force` replicates the non-datahub overwrite. "
         "`--check` for dry runs.")
L.append("- Full mapping detail per study: `oncotree_audit.md` / `oncotree_audit.json`.")
L.append("")

open(out_path, "w").write("\n".join(L))
print(f"wrote {out_path} ({len(L)} lines)")
