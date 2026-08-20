#!/usr/bin/env python3
"""Fuse duplicate-gene rows in cBioPortal CNA staging files, replicating the
pipelines JAR logic in CopyNumberAlterationUtilImpl.unifyDuplicatedGeneIdsByName
(pipelines/importer/.../internal/CopyNumberAlterationUtilImpl.java) and
CopyNumberAlterationUtilDao.getHugoToEntrezMap.

Behavior matches the JAR pipeline end-to-end. The merge util throws on
conflicting event codes (UnexpectedCNAEventCodeDifferenceException), but the
caller CATCHES every exception and falls back to the original file, which the
downstream importer (ImportTabDelimData) dedupes first-row-wins per resolved
gene ("Duplicated row will be ignored!"). This script reproduces that:
  - file merges cleanly -> fused rows written (status MERGED)
  - any conflict or Entrez parse error -> whole file falls back to
    first-row-wins dedup: keep the first row per resolved gene, drop later
    duplicates (status FALLBACK)

Deliberate deviations (documented):
  - Output row order: merged/resolved groups keep first-occurrence input order
    (Java iterates a HashMap keySet, i.e. arbitrary order). Unresolvable rows
    are appended at the end, as in Java.
  - gene_alias rows are sorted by entrez_gene_id ascending before first-wins
    insertion, implementing the DAO comment "select the first entrez id
    returned (lowest integer)". The Java SQL has no ORDER BY.
  - fallback dedup replicates ImportTabDelimData line handling: gene columns
    untrimmed, non-digit Entrez cells drop the whole line (no Hugo fallback),
    Hugo truncated at the first '|', blank lines skipped. Remaining known gap:
    the real importer uses DaoGeneOptimized, which SKIPS lines whose symbol is
    ambiguous (maps to multiple genes) or is '///'/'---', and duplicates rows
    for miRNA aliases; this script resolves through a flat symbol->entrez map
    instead, so such rows may claim a gene or survive where Java drops them.
  - rows whose gene cannot be resolved at all are kept in both modes (the
    downstream importer reports-then-drops them at import time; we leave the
    data in the file).

Usage:
  cna_merge.py --gene-table gene_table.tsv --gene-alias gene_alias_table.tsv \
               [--check] file1 [file2 ...]
  --check: dry run; report what would happen, write nothing.
Exit code: 0 unless a file could not be processed at all (ERROR status).
"""
import argparse
import re
import sys

ENTREZ_HEADER = "Entrez_Gene_Id"
HUGO_HEADER = "Hugo_Symbol"
DELIM = "\t"
NO_EVENT_CODE = "0"
UNRESOLVABLE = None  # group key for rows with no resolvable entrez id

GENE_SYMBOL_DISAMBIGUATION = {"MLL2": 8085, "MLL4": 9757, "CDC2": 983}


def missing_event_string_set():
    primary = ["Not Applicable", "Not Available", "Pending", "Discrepancy",
               "Completed", "Null", "NA", ""]
    secondary = []
    for p in primary:
        secondary.append(p)
        secondary.append("[" + p + "]")
        if " " in p:
            for repl in ("_", "-"):
                q = p.replace(" ", repl)
                secondary.append(q)
                secondary.append("[" + q + "]")
    out = set()
    for s in secondary:
        out.add(s)
        out.add(s.upper())
        out.add(s.lower())
    return out


MISSING_EVENT_STRINGS = missing_event_string_set()


class ConflictError(Exception):
    pass


def load_gene_maps(gene_table_path, gene_alias_path):
    gene_table_symbols = set()
    gene_records = []
    with open(gene_table_path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            entrez_s, hugo = line.split("\t")[:2]
            gene_table_symbols.add(hugo)
            gene_records.append((hugo, int(entrez_s)))
    hugo_to_entrez = {}
    for hugo, entrez in gene_records:
        if hugo not in hugo_to_entrez:
            hugo_to_entrez[hugo] = entrez
    alias_records = []
    with open(gene_alias_path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                continue
            entrez_s, alias = line.split("\t")[:2]
            alias_records.append((int(entrez_s), alias))
    alias_records.sort(key=lambda r: r[0])  # "lowest integer" wins
    for entrez, alias in alias_records:
        if alias not in hugo_to_entrez:
            hugo_to_entrez[alias] = entrez
    hugo_to_entrez.update(GENE_SYMBOL_DISAMBIGUATION)
    if not gene_table_symbols or not alias_records:
        # Java DAO throws on an empty gene or gene_alias table and the merge
        # never runs; refuse rather than silently resolving nothing.
        sys.exit("gene table or alias table is empty — refusing to run")
    return gene_table_symbols, hugo_to_entrez


def equivalent_to_missing_event(s):
    return s in MISSING_EVENT_STRINGS


def additional_cna_event_is_better(additional, merged):
    additional = additional.strip()
    if len(additional) == 0:
        return False  # never overwrite something with nothing
    merged = merged.strip()
    if len(merged) == 0:
        return True  # any value is better than none
    if equivalent_to_missing_event(additional):
        return False
    if equivalent_to_missing_event(merged):
        return True
    if additional == NO_EVENT_CODE:
        return False
    if merged == NO_EVENT_CODE:
        return True
    if additional != merged:
        raise ConflictError(f"conflicting event codes {additional!r} vs {merged!r}")
    return False  # matching code is not better


def additional_hugo_is_better(additional, merged, gene_table_symbols):
    additional = additional.strip()
    if len(additional) == 0:
        return False
    merged = merged.strip()
    if len(merged) == 0:
        return True
    if merged in gene_table_symbols:
        return False
    return additional in gene_table_symbols


class MergeAbort(Exception):
    """Any condition that makes the Java merge util give up on the file
    (conflicting event codes, unparseable Entrez, ragged rows). The JAR then
    imports the original file, deduped first-row-wins downstream."""


JAVA_INT_MIN = -2**31
JAVA_INT_MAX = 2**31 - 1
_JAVA_INT_RE = re.compile(r"^[+-]?[0-9]+$")
_DIGITS_ONLY_RE = re.compile(r"^[0-9]+$")  # DataValidator.isValidNumericSequence


def java_parse_int(s):
    """Integer.parseInt: ASCII sign+digits only, 32-bit range. Raises ValueError
    on anything Python's int() would be laxer about (underscores, unicode
    digits/whitespace, arbitrary magnitude)."""
    if not _JAVA_INT_RE.match(s):
        raise ValueError(s)
    v = int(s)
    if not (JAVA_INT_MIN <= v <= JAVA_INT_MAX):
        raise ValueError(s)
    return v


def resolve_entrez_strict(columns, entrez_idx, hugo_idx, hugo_to_entrez):
    """Java groupCNARecordsByEntrezId: Integer.parseInt, so a non-integer
    Entrez entry raises -> whole-file merge abort. Integer.MIN_VALUE collides
    with the Java unresolvable-group sentinel, so such rows are unresolvable."""
    if entrez_idx != -1:
        entry = columns[entrez_idx].strip()
        if entry:
            try:
                entrez = java_parse_int(entry)
            except ValueError:
                raise MergeAbort(f"unparseable Entrez value {entry!r}")
            if entrez == JAVA_INT_MIN:
                return UNRESOLVABLE
            if entrez != 0:
                return entrez
    if hugo_idx != -1:
        hugo = columns[hugo_idx].strip()
        if hugo:
            return hugo_to_entrez.get(hugo, UNRESOLVABLE)
    return UNRESOLVABLE


DROP_LINE = object()  # fallback: downstream would ignore this line entirely


def resolve_entrez_fallback(columns, entrez_idx, hugo_idx, hugo_to_entrez):
    """Downstream ImportTabDelimData semantics (first-wins dedup happens there):
    - gene columns are NOT trimmed
    - a non-empty Entrez cell that is not all-digits ([0-9]+, so negatives and
      whitespace included) means the WHOLE LINE is ignored ("Ignoring line with
      invalid Entrez_Id") — no Hugo fallback
    - empty Entrez -> resolve by Hugo symbol; symbol is truncated at the first
      '|' before lookup
    Returns an entrez id, UNRESOLVABLE (row kept, claims no gene), or DROP_LINE.
    """
    entrez = None
    if entrez_idx != -1 and entrez_idx < len(columns):
        cell = columns[entrez_idx]
        if cell:
            if not _DIGITS_ONLY_RE.match(cell):
                return DROP_LINE
            entrez = int(cell)
    if entrez is not None and entrez != 0:
        return entrez
    if hugo_idx != -1 and hugo_idx < len(columns):
        hugo = columns[hugo_idx]
        if "|" in hugo:
            hugo = hugo.split("|", 1)[0]
        if hugo:
            return hugo_to_entrez.get(hugo, UNRESOLVABLE)
    return UNRESOLVABLE


def parse_file(path):
    # No trailing-blank-line trimming: Java's LineIterator hands a trailing
    # blank line to the merge util as a record, whose column count mismatches
    # the header -> merge abort -> fallback. Keep that behavior.
    with open(path, newline="") as f:
        records = [line.rstrip("\r\n") for line in f]
    if not records or all(r == "" for r in records):
        raise ValueError("empty file")
    header = records[0]
    columns = header.split(DELIM)
    entrez_idx = columns.index(ENTREZ_HEADER) if ENTREZ_HEADER in columns else -1
    hugo_idx = columns.index(HUGO_HEADER) if HUGO_HEADER in columns else -1
    if entrez_idx == -1 and hugo_idx == -1:
        raise ValueError(f"no {ENTREZ_HEADER} or {HUGO_HEADER} column")
    return records, header, columns, entrez_idx, hugo_idx


def try_merge(records, columns, entrez_idx, hugo_idx, gene_table_symbols, hugo_to_entrez):
    """The merge util. Returns (out_lines, merge_count, messages) or raises MergeAbort."""
    ncols = len(columns)
    group_order = []  # entrez ids in first-occurrence order
    groups = {}       # entrez id -> list of row column-lists
    unresolvable = []
    for record in records[1:]:
        cols = record.split(DELIM)
        if len(cols) != ncols:
            raise MergeAbort(f"record with {len(cols)} columns, header has {ncols}: {record[:80]}")
        entrez = resolve_entrez_strict(cols, entrez_idx, hugo_idx, hugo_to_entrez)
        if entrez is UNRESOLVABLE:
            unresolvable.append(cols)
            continue
        if entrez not in groups:
            groups[entrez] = []
            group_order.append(entrez)
        groups[entrez].append(cols)

    merge_count = 0
    messages = []
    for entrez in group_order:
        group = groups[entrez]
        if len(group) <= 1:
            continue
        merged = list(group[0])
        if entrez_idx >= 0:
            merged[entrez_idx] = str(entrez)
        for cols in group[1:]:
            for col in range(ncols):
                if col == entrez_idx:
                    entry = cols[col].strip()
                    if entry and int(entry) != 0 and int(entry) != entrez:
                        raise MergeAbort(f"differing entrez ids grouped together (internal error): {cols[:3]}")
                elif col == hugo_idx:
                    if additional_hugo_is_better(cols[col], merged[col], gene_table_symbols):
                        merged[col] = cols[col]
                else:
                    try:
                        if additional_cna_event_is_better(cols[col], merged[col]):
                            merged[col] = cols[col]
                    except ConflictError as e:
                        raise MergeAbort(f"gene entrez={entrez} sample column {columns[col]}: {e}")
        gene_labels = ", ".join(g[hugo_idx] if hugo_idx >= 0 else g[entrez_idx] for g in group)
        messages.append(f"merged {len(group)} rows for entrez {entrez} ({gene_labels})")
        groups[entrez] = [merged]
        merge_count += 1

    out_lines = []
    for entrez in group_order:
        for cols in groups[entrez]:
            out_lines.append(DELIM.join(cols))
    for cols in unresolvable:
        out_lines.append(DELIM.join(cols))
    return out_lines, merge_count, messages


def fallback_dedup(records, entrez_idx, hugo_idx, hugo_to_entrez):
    """First-row-wins per resolved gene, preserving input order — what
    ImportTabDelimData effectively keeps when the merge util backed off.
    Blank lines are skipped (downstream isDataLine skips them) and lines with
    an invalid Entrez cell are dropped (downstream ignores them outright).
    Returns (out_lines, dropped, invalid_dropped)."""
    seen = set()
    out_lines = []
    dropped = []
    invalid_dropped = 0
    for record in records[1:]:
        if not record.strip():
            continue
        cols = record.split(DELIM)
        entrez = resolve_entrez_fallback(cols, entrez_idx, hugo_idx, hugo_to_entrez)
        if entrez is DROP_LINE:
            invalid_dropped += 1
            continue
        if entrez is not UNRESOLVABLE:
            if entrez in seen:
                label = cols[hugo_idx] if 0 <= hugo_idx < len(cols) else str(entrez)
                dropped.append((entrez, label))
                continue
            seen.add(entrez)
        out_lines.append(record)
    return out_lines, dropped, invalid_dropped


def merge_file(path, gene_table_symbols, hugo_to_entrez, check_only):
    """Returns (status, message). status in {'clean','merged','fallback','error'}."""
    try:
        records, header, columns, entrez_idx, hugo_idx = parse_file(path)
    except ValueError as e:
        return "error", str(e)

    try:
        out_lines, merge_count, messages = try_merge(
            records, columns, entrez_idx, hugo_idx, gene_table_symbols, hugo_to_entrez)
        if merge_count == 0:
            return "clean", "no duplicate gene groups"
        status = "merged"
        message = f"{merge_count} groups fused; " + "; ".join(messages[:5]) + (
            f"; ... {len(messages) - 5} more" if len(messages) > 5 else "")
    except MergeAbort as e:
        out_lines, dropped, invalid_dropped = fallback_dedup(records, entrez_idx, hugo_idx, hugo_to_entrez)
        if not dropped and not invalid_dropped:
            return "clean", f"merge abandoned ({e}) but no rows to drop"
        drop_summary = ", ".join(f"{label}(entrez {entrez})" for entrez, label in dropped[:5])
        status = "fallback"
        message = (f"merge abandoned ({e}); first-row-wins dedup dropped {len(dropped)} duplicate rows"
                   + (f" and {invalid_dropped} invalid-Entrez rows" if invalid_dropped else "")
                   + (": " + drop_summary if dropped else "")
                   + (f", ... {len(dropped) - 5} more" if len(dropped) > 5 else ""))

    if not check_only:
        with open(path, "w", newline="") as f:
            f.write(header + "\n")
            for line in out_lines:
                f.write(line + "\n")
    return status, message


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gene-table", required=True)
    ap.add_argument("--gene-alias", required=True)
    ap.add_argument("--check", action="store_true", help="dry run, write nothing")
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()

    gene_table_symbols, hugo_to_entrez = load_gene_maps(args.gene_table, args.gene_alias)
    print(f"gene map: {len(gene_table_symbols)} gene-table symbols, "
          f"{len(hugo_to_entrez)} symbol->entrez entries", flush=True)

    any_error = False
    for path in args.files:
        try:
            status, message = merge_file(path, gene_table_symbols, hugo_to_entrez, args.check)
        except Exception as e:
            status, message = "error", str(e)
        if status == "error":
            any_error = True
        print(f"{status.upper()}\t{path}\t{message}", flush=True)
    sys.exit(1 if any_error else 0)


if __name__ == "__main__":
    main()
