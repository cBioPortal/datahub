# Bladder Cancer (AUBMC, 2026)

Targeted sequencing (IMPACT505) of 13 bladder tumors from the American University
of Beirut Medical Center (AUBMC), characterizing the genomic landscape of bladder
cancer in patients from Lebanon with a history of hookah (waterpipe) smoking.

## Why the CNA data includes only 5 of the 13 samples

All 13 samples were profiled with the IMPACT505 panel for both mutations and copy
number. However, only **5 samples** carry CNA calls in `data_cna.txt`:

- `s_C_0DJMJU_P001_d`
- `s_C_3LPVY1_P001_d`
- `s_C_4R4R0T_P001_d`
- `s_C_CDW3P7_P001_d`
- `s_C_JWWJAW_P001_d`

The remaining 8 samples were excluded from the CNA profile after QC:

- **Low sequencing coverage.** Coverage in these samples was too low to reliably
  estimate copy number, producing noisy log-ratio segmentation.
- **Whole-arm losses.** The noise manifested as entire chromosome arms being
  called as lost — a signature of poor-quality CNA data rather than true biology.
- **Implausible alteration types.** Genes were called with alteration directions
  that don't occur for them (e.g. `ERBB2` **loss**, when `ERBB2` is a canonical
  amplification target), further indicating unreliable calls.

Because of this, arm-level and low-confidence calls were dropped. The 5 retained
samples legitimately had focal CNA events **spanning less than 5 Mb**, which pass
QC as real copy-number alterations.

## Gene panel matrix

`data_gene_panel_matrix.txt` records IMPACT505 as the panel for all 13 samples in
the `mutations` column. In the `gistic` (CNA) column, only the 5 CNA-profiled
samples are set to `IMPACT505`; the other 8 are `NA` since they have no CNA data.

## Case lists

- `case_lists/cases_all.txt` — all 13 samples
- `case_lists/cases_sequenced.txt` — all 13 sequenced (mutation) samples
- `case_lists/cases_cna.txt` — the 5 samples with CNA data
