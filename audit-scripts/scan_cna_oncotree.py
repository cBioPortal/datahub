#!/usr/bin/env python3
"""Scan datahub public studies for:
1. Duplicate Entrez/Hugo rows in data_cna*.txt (JAR fuses nonzero-wins; metaImport takes first)
2. ONCOTREE_CODE / CANCER_TYPE / CANCER_TYPE_DETAILED mismatches vs latest Oncotree API
Skips LFS pointer files (reports them separately).
"""
import os, sys, json, urllib.request, collections

ROOT = os.path.expanduser("~/Code/datahub/public")

def is_pointer(path):
    try:
        with open(path, "rb") as f:
            return f.read(30).startswith(b"version https://git-lfs")
    except OSError:
        return True

def read_header(line):
    return line.rstrip("\n").split("\t")

# ---------- Oncotree ----------
print("== Fetching Oncotree API ==", flush=True)
url = "https://oncotree.mskcc.org/api/tumorTypes?version=oncotree_latest_stable"
with urllib.request.urlopen(url, timeout=60) as r:
    tumor_types = json.load(r)
onco = {}  # code -> (mainType, name)
for t in tumor_types:
    onco[t["code"]] = (t.get("mainType") or "", t.get("name") or "")
print(f"Loaded {len(onco)} oncotree codes", flush=True)

cna_results = []
onco_results = []
pointer_cna = []
pointer_clin = []

studies = sorted(d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)))
for s in studies:
    sdir = os.path.join(ROOT, s)
    # ----- CNA duplicates -----
    for fn in sorted(os.listdir(sdir)):
        if not (fn.startswith("data_cna") or fn.startswith("data_log2_cna")) or not fn.endswith(".txt"):
            continue
        path = os.path.join(sdir, fn)
        if is_pointer(path):
            pointer_cna.append(f"{s}/{fn}")
            continue
        try:
            with open(path, errors="replace") as f:
                hdr = None
                for line in f:
                    if line.startswith("#"):
                        continue
                    hdr = read_header(line)
                    break
                if not hdr:
                    continue
                key_idx = None
                for cand in ("Entrez_Gene_Id", "Hugo_Symbol"):
                    if cand in hdr:
                        key_idx = hdr.index(cand); key_name = cand; break
                if key_idx is None:
                    continue
                gene_cols = [i for i, h in enumerate(hdr)
                             if h in ("Hugo_Symbol", "Entrez_Gene_Id", "Cytoband")]
                val_start = max(gene_cols) + 1
                seen = {}
                dups = 0
                conflicts = 0
                dup_keys = set()
                for line in f:
                    parts = line.rstrip("\n").split("\t")
                    if key_idx >= len(parts):
                        continue
                    k = parts[key_idx].strip()
                    if not k or k in ("", "NA", "0"):
                        continue
                    if k in seen:
                        dups += 1
                        dup_keys.add(k)
                        if parts[val_start:] != seen[k][val_start:]:
                            conflicts += 1
                    else:
                        seen[k] = parts
                if dups:
                    cna_results.append((s, fn, key_name, dups, conflicts, sorted(dup_keys)[:10]))
        except Exception as e:
            print(f"ERR {s}/{fn}: {e}", flush=True)

    # ----- Oncotree mismatches -----
    clin = os.path.join(sdir, "data_clinical_sample.txt")
    if not os.path.exists(clin):
        continue
    if is_pointer(clin):
        pointer_clin.append(s)
        continue
    try:
        with open(clin, errors="replace") as f:
            hdr = None
            for line in f:
                if line.startswith("#"):
                    continue
                hdr = read_header(line)
                break
            if not hdr or "ONCOTREE_CODE" not in hdr:
                continue
            oc_i = hdr.index("ONCOTREE_CODE")
            ct_i = hdr.index("CANCER_TYPE") if "CANCER_TYPE" in hdr else None
            ctd_i = hdr.index("CANCER_TYPE_DETAILED") if "CANCER_TYPE_DETAILED" in hdr else None
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
                main, name = onco[code]
                if ct_i is not None and ct_i < len(parts):
                    v = parts[ct_i].strip()
                    if v and v != "NA" and v != main:
                        ct_mismatch[(code, v, main)] += 1
                if ctd_i is not None and ctd_i < len(parts):
                    v = parts[ctd_i].strip()
                    if v and v != "NA" and v != name:
                        ctd_mismatch[(code, v, name)] += 1
            if stale or ct_mismatch or ctd_mismatch:
                onco_results.append((s, dict(stale),
                                     {f"{c}|{a}=>{b}": n for (c, a, b), n in ct_mismatch.items()},
                                     {f"{c}|{a}=>{b}": n for (c, a, b), n in ctd_mismatch.items()}))
    except Exception as e:
        print(f"ERR {s}/clin: {e}", flush=True)

out = {
    "cna_duplicates": [
        {"study": s, "file": f, "key": k, "dup_rows": d, "conflicting": c, "sample_keys": keys}
        for s, f, k, d, c, keys in cna_results
    ],
    "oncotree_issues": [
        {"study": s, "stale_codes": st, "cancer_type_mismatch": ct, "cancer_type_detailed_mismatch": ctd}
        for s, st, ct, ctd in onco_results
    ],
    "lfs_pointer_cna_files": pointer_cna,
    "lfs_pointer_clinical_sample": pointer_clin,
}
with open(os.path.expanduser("~/scan_results.json"), "w") as f:
    json.dump(out, f, indent=1)
print(f"DONE. CNA-dup studies: {len(cna_results)}; oncotree-issue studies: {len(onco_results)}; "
      f"pointer CNA files: {len(pointer_cna)}; pointer clinical: {len(pointer_clin)}", flush=True)
