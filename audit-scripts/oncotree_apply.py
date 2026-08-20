#!/usr/bin/env python3
"""Apply the pipelines JAR's Oncotree cancer-type transformation to cBioPortal
clinical staging files, replicating ImporterImpl.convertCancerTypesFromOncotree
(pipelines/importer/.../internal/ImporterImpl.java:803).

JAR behavior replicated exactly:
  - File without an ONCOTREE_CODE column: left unchanged.
  - Missing CANCER_TYPE / CANCER_TYPE_DETAILED columns are appended (with
    metadata header lines "Cancer Type"/"Cancer Type Detailed", STRING,
    priority 1, SAMPLE when the file carries an attribute-types line), rows
    padded with "NA".
  - Rows are rewritten from Oncotree ONLY when forceCancerTypeFromOncotree is
    true OR a column was just added. IMPORTANT: for datahub imports the JAR
    sets force=false (ImporterImpl.java:459 `rootDirectory.contains("datahub")`),
    so files that already have both columns pass through UNCHANGED. That is
    the default here; pass --force to emulate the non-datahub behavior.
  - When rewriting: code found -> CANCER_TYPE = mainType (or "NA" if mainType
    blank), CANCER_TYPE_DETAILED = name; code missing from Oncotree or blank
    -> both set to "NA" (warning printed).
  - Lookup is exact string match against the tumorTypes API for the given
    version (JAR OncotreeUtilImpl builds a plain code->node map).

Files that would crash the Java importer (blank lines, short data rows) are
reported as ERROR and left untouched. A header-only file without ONCOTREE_CODE
still gets the columns appended (Java's bail-out check sits inside the
data-row loop). Note the Java importer writes a whitespace-normalized temp
file even when it changes nothing; this script only rewrites on real change.

Usage:
  oncotree_apply.py [--force] [--check] [--version oncotree_latest_stable] \
                    file1 [file2 ...]
  --check: dry run; report what would change, write nothing.
Output per file: CHANGED / UNCHANGED / SKIPPED / ERROR, with a summary of rewrites.
"""
import argparse
import json
import sys
import urllib.request

DELIM = "\t"


def fetch_oncotree(version):
    url = "https://oncotree.mskcc.org/api/tumorTypes"
    if version:
        url += "?version=" + version
    with urllib.request.urlopen(url, timeout=60) as r:
        tumor_types = json.load(r)
    if not tumor_types:
        # Java OncotreeUtil throws on an empty tumorTypes response; without
        # this guard every code would be "not found" and rewritten to NA.
        raise SystemExit(f"oncotree API returned no tumor types ({url}) — refusing to run")
    return {t["code"]: (t.get("mainType") or "", t.get("name") or "") for t in tumor_types}


def process_file(path, onco, force, check_only):
    """Returns (status, message)."""
    with open(path, newline="") as f:
        raw_lines = [line.rstrip("\r\n") for line in f]
    if not raw_lines or all(l == "" for l in raw_lines):
        return "skipped", "empty file"
    if "" in raw_lines:
        # Java iterates every line and calls clinLine.get(oncotreeCodeIndex) on
        # it; a blank line (including a trailing one) throws IndexOutOfBounds
        # and aborts the import run. Refuse rather than silently differ.
        return "error", "file contains a blank line — the Java importer would crash on it"

    # --- header block (mirrors the Java comment-line parsing; Java trims each
    # header/comment line before splitting) ---
    i = 0
    display_names, descriptions, datatypes, attribute_types, priorities = [], [], [], [], []
    header = raw_lines[i].strip()
    if header.startswith("#"):
        display_names = raw_lines[i].strip().split(DELIM)
        descriptions = raw_lines[i + 1].strip().split(DELIM)
        datatypes = raw_lines[i + 2].strip().split(DELIM)
        priorities = raw_lines[i + 3].strip().split(DELIM)
        header = raw_lines[i + 4].strip()
        i += 4
        if header.startswith("#"):
            # attribute-types line present (mixed-attribute file)
            attribute_types = priorities
            priorities = header.split(DELIM)
            header = raw_lines[i + 1].strip()
            i += 1
    column_headers = header.split(DELIM)
    data_start = i + 1

    def col(name):
        return column_headers.index(name) if name in column_headers else -1

    n_original_cols = len(column_headers)
    oncotree_idx = col("ONCOTREE_CODE")
    if oncotree_idx < 0 and data_start < len(raw_lines):
        # Java bails out ("return the file as is") from inside the data-row
        # loop, so a file with data rows and no ONCOTREE_CODE is untouched —
        # but a header-only file never reaches that check and still gets the
        # columns appended below.
        return "skipped", "no ONCOTREE_CODE column, file left as is"
    sample_idx = col("SAMPLE_ID")
    ct_idx = col("CANCER_TYPE")
    ctd_idx = col("CANCER_TYPE_DETAILED")

    add_ct = ct_idx < 0
    add_ctd = ctd_idx < 0
    if add_ct:
        column_headers.append("CANCER_TYPE")
        ct_idx = len(column_headers) - 1
        if display_names:
            display_names.append("Cancer Type")
            descriptions.append("Cancer Type")
            datatypes.append("STRING")
            priorities.append("1")
            if attribute_types:
                attribute_types.append("SAMPLE")
    if add_ctd:
        column_headers.append("CANCER_TYPE_DETAILED")
        ctd_idx = len(column_headers) - 1
        if display_names:
            display_names.append("Cancer Type Detailed")
            descriptions.append("Cancer Type Detailed")
            datatypes.append("STRING")
            priorities.append("1")
            if attribute_types:
                attribute_types.append("SAMPLE")

    rewriting = force or add_ct or add_ctd
    out_lines = []
    if display_names:
        out_lines.append(DELIM.join(display_names))
        out_lines.append(DELIM.join(descriptions))
        out_lines.append(DELIM.join(datatypes))
        if attribute_types:
            out_lines.append(DELIM.join(attribute_types))
        out_lines.append(DELIM.join(priorities))
    out_lines.append(DELIM.join(column_headers))

    rows_changed = 0
    na_warnings = []
    for line in raw_lines[data_start:]:
        clin = line.split(DELIM)
        if len(clin) < n_original_cols:
            # Java calls clinLine.get()/set() at header-based indexes with no
            # bounds check; a short row throws and aborts the import run.
            return "error", (f"data row has {len(clin)} columns, header has "
                             f"{n_original_cols} — the Java importer would crash on it")
        code = clin[oncotree_idx] if 0 <= oncotree_idx < len(clin) else ""
        node = onco.get(code) if code else None
        if add_ct:
            clin.append("NA")
        if add_ctd:
            clin.append("NA")
        if rewriting:
            before = (clin[ct_idx], clin[ctd_idx])
            if node is not None:
                main_type, name = node
                if not main_type.strip():
                    clin[ct_idx] = "NA"
                elif force or add_ct:
                    clin[ct_idx] = main_type
                if force or add_ctd:
                    clin[ctd_idx] = name
            else:
                clin[ct_idx] = "NA"
                clin[ctd_idx] = "NA"
                sample = clin[sample_idx] if 0 <= sample_idx < len(clin) else "?"
                na_warnings.append(f"({sample}, {code!r})")
            if (clin[ct_idx], clin[ctd_idx]) != before or add_ct or add_ctd:
                rows_changed += 1
        out_lines.append(DELIM.join(clin))

    original = "\n".join(raw_lines) + "\n"
    rewritten = "\n".join(out_lines) + "\n"
    if rewritten == original:
        return "unchanged", "no differences" + ("" if rewriting else " (datahub mode: existing columns kept verbatim)")

    if not check_only:
        with open(path, "w", newline="") as f:
            f.write(rewritten)
    parts = []
    if add_ct:
        parts.append("added CANCER_TYPE column")
    if add_ctd:
        parts.append("added CANCER_TYPE_DETAILED column")
    parts.append(f"{rows_changed} rows rewritten")
    if na_warnings:
        parts.append(f"{len(na_warnings)} rows NA'd, no oncotree data for: "
                     + ", ".join(na_warnings[:5])
                     + (f", ... {len(na_warnings) - 5} more" if len(na_warnings) > 5 else ""))
    return "changed", "; ".join(parts)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default="oncotree_latest_stable")
    ap.add_argument("--force", action="store_true",
                    help="overwrite existing CANCER_TYPE/CANCER_TYPE_DETAILED from Oncotree "
                         "(the JAR's non-datahub behavior); default replicates the datahub path")
    ap.add_argument("--check", action="store_true", help="dry run, write nothing")
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()

    onco = fetch_oncotree(args.version)
    print(f"loaded {len(onco)} oncotree codes (version {args.version})", flush=True)

    any_error = False
    for path in args.files:
        try:
            status, message = process_file(path, onco, args.force, args.check)
        except Exception as e:
            status, message = "error", str(e)
            any_error = True
        print(f"{status.upper()}\t{path}\t{message}", flush=True)
    sys.exit(1 if any_error else 0)


if __name__ == "__main__":
    main()
