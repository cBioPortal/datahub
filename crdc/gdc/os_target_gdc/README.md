# Comments & assumptions made during curation

## General

- This study is sourced from the Genomic Data Commons (GDC) through the Cancer Data Aggregator library provided by the NCI.
- Reference genome used: hg38

## Clinical data

For CDA studies, TARGET clinical data was gathered through the CDA `subject` and `researchsubject` tables.

Only tumor sample data is included -- no normal samples. Samples lacking any genomic data are also dropped. This follows the same convention that was used by the ISB-CGC pipeline.

### Survival data

Survival fields are calculated from the clinical data and added as new columns in the clinical file.

- `OS_STATUS` is converted from `VITAL_STATUS`.
- `OS_MONTHS` is converted from `DAYS_TO_DEATH`, falls back to `DAYS_TO_LAST_FOLLOW_UP` if `DAYS_TO_DEATH` is not available.


### Timeline data

Timeline data is procured from the CDA `diagnosis` and `treatment` tables and stored in `data_timeline_diagnosis.txt` / `data_timeline_treatment.txt`, respectively.

### Other clinical transformations

- If a clinical field is missing for the entire study, the column is removed from the data file.
- If a patient / sample identifier is too large to fit in the cBioPortal database (the limits are 50 and 63 characters, respectively), then that patient / sample is removed.
- The `SEX`, `PRIMARY_SITE_PATIENT`, and `VITAL_STATUS` attributes are title-cased.
- `AGE` is calculated from the `DAYS_TO_BIRTH` attribute.
- `AGE` is clipped from 18 to 89 to protect patient confidentiality.

## CNA data

CNA data was downloaded through the CDA file table. We searched for files with the `Gene Level Copy Number` data type and with a filename matching `*.gene_level_copy_number.v36.tsv`. This coincides with the file IDs used by ISB-CGC BigQuery. Data for any samples not in the clinical sample file is dropped. Only the "primary" aliquot is used to represent a given sample, and data for all other aliquots for that sample is dropped.

Copy number values from the BigQuery tables are converted from [ASCAT](https://www.pnas.org/doi/10.1073/pnas.1009843107) to GISTIC 2.0 using the following thresholds:

| ASCAT Value | GISTIC Value | Meaning |
|---|---|---|
| X = 0 | -2 | Deep loss |
| X = 1 | -1 | Single-copy loss |
| X = 2 | 0 | Diploid |
| 2 &lt; X &lt; 7 | 1 | Low-level gain |
| 7 &le; X | 2 | Amplification |

Only amplifications (GISTIC = 2) and deep deletions (GISTIC = -2) are shown on the cBioPortal website. As a result these conversion thresholds affect how many samples show up in the CNA chart, which can be inconsistent with legacy versions of this study. We chose ASCAT &ge; 7 as the amplification threshold because it resulted in the least deviation from our legacy studies.

## mRNA Expression data

mRNA data was downloaded through the CDA file table. We searched for files with the `Gene Expression Quantification` data type and with a filename matching `*.rna_seq.augmented_star_gene_counts.tsv`. This coincides with the file IDs that ISB-CGC BigQuery uses. Data for any samples not in the clinical sample file is dropped. Only the "primary" aliquot is used to represent a given sample, and data for all other aliquots for that sample is dropped.

The `unstranded`, `tpm_unstranded`, and `fpkm_uq_unstranded` columns are pulled and each mapped to their own data file. The regular FPKM values are excluded because [FPKM-UQ provides a more stable metric](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/#upper-quartile-fpkm).

Z-score files are generated and added for each of the mRNA data types using a curation-provided script.



## Mutation data

Mutation data was downloaded through the CDA file table. We searched for files with the `Masked Somatic Mutation` data type. This coincides with the file IDs that ISB-CGC BigQuery uses. Data for any samples not in the clinical sample file is dropped. Only the "primary" aliquot is used to represent a given sample, and data for all other aliquots for that sample is dropped.

The MAF is annotated with Genome Nexus in order to avoid issues with the isoform mapping. Parameters used:
- Endpoint: https://grch38.genomenexus.org/
- Isoform override: `mskcc`
- Replace gene symbols and Entrez IDs
- Post interval size: 500

## Expression data transformations (CNA / mRNA)

- Ensembl gene IDs are mapped to Entrez IDs using the [Genome Nexus hg38 canonical transcript file](https://github.com/genome-nexus/genome-nexus-importer/blob/master/data/grch38_ensembl95/export/ensembl_biomart_canonical_transcripts_per_hgnc.txt). Any genes that cannot be converted using this file are dropped.
  - Prior to conversion, we also filter out a small number of duplicate Ensembl genes. These genes have copies containing data for both the X and the Y chromosomes.
- If a sample has multiple aliquots, it has to be condensed to 1 before it can imported into cBioPortal. This is done by choosing the aliquot ID with the highest sort value (eg. highest plate number), following [the same policy](https://broadinstitute.atlassian.net/wiki/spaces/GDAC/pages/844334036/FAQ#FAQ-replicateFilteringQ%3AWhatdoyoudowhenmultiplealiquotbarcodesexistforagivensample%2Fportion%2Fanalytecombination%3F) used by GDAC used to condense aliquot data in their studies.

## Post-processing steps

- Metadata headers are added to the clinical patient and sample files.
- `TMB_NONSYNONYMOUS` is calculated and added to the clinical sample file using a curation-provided script and gene panels from the Datahub repository.
- Samples that lack any genomic data are removed from the clinical sample file.
- Case lists are generated under `case_lists/`.
- A gene panel matrix / associated meta file is generated via the `generate_gene_panel_matrix.py` script.
- The validator script is run and the HTML report is saved under `validation_reports/`.