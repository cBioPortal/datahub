# Comments & assumptions made during curation

## General

- Study is updated once every 3 months with latest data from [ISB-CGC BigQuery tables](https://isb-cgc.appspot.com/bq_meta_search/)
  - The ISB-CGC tables allow easy access to data collected from multiple NCI-CRDC repositories including the GDC, PDC, and others. The TARGET data in this study comes from the GDC and is accessed through these tables.
- Reference genome used: hg38
- TARGET started using the hg38 genome as of GDC release 32. For more information, refer to the [GDC release notes](https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/#data-release-320).

- Only tumor sample data is included (no normal samples)
- [GDC project webpage](https://portal.gdc.cancer.gov/projects/TARGET-ALL-P3)

## Clinical data

- **Patient data:** Retrieved from `isb-cgc-bq.TARGET_versioned.clinical_gdc_r40`. ISB-CGC data was created in April 2024.
- **Sample data:** Retrieved from `isb-cgc-bq.TARGET_versioned.per_sample_file_metadata_hg38_gdc_r40`. ISB-CGC data was created in April 2024.

### Survival data

Survival fields are calculated from the clinical data and added as new columns in the clinical file.

- `OS_STATUS` is converted from `demo__vital_status`
- `OS_MONTHS` is converted from `demo__days_to_death`, falls back to `diag__days_to_last_follow_up`




### Timeline data

- Timeline data is extracted from the clinical data and stored in a separate data file. After extraction, the corresponding BigQuery fields are removed from the clinical file. For example, a timeline status of `DEATH` corresponds to the BigQuery field `demo__days_to_death`.

- For TARGET, the "time 0" anchor point is always the date of diagnosis. Not all patients have timeline data available, as indicated by a null `diag__days_to_diagnosis` (TCGA) or `index_date` (CPTAC, TARGET) field.

- Birth timeline events are removed, as they (1) push other events to the far right of the graph and (2) can potentially be used to identify the patient.

The following status values are supported in `data_timeline_status.txt`:

- `__time0__`
- `demo__days_to_death`
- `diag__days_to_last_follow_up`
### Other transformations

- `"not reported"` values are replaced with blanks.
- If a clinical field is missing for the entire study, the column is removed from the data file.
- `RACE`, `ETHNICITY`, and `SEX` are capitalized.
- `AGE` is converted from days to years. 

## CNA data

- Retrieved from `isb-cgc-bq.TARGET_versioned.copy_number_gene_level_hg38_gdc_r36`. ISB-CGC data was created in March 2023.
- Transformations
  - Copy number values from the BigQuery tables are converted from [ASCAT](https://www.pnas.org/doi/10.1073/pnas.1009843107https://www.pnas.org/doi/10.1073/pnas.1009843107) to GISTIC 2.0 using the following thresholds:

| ASCAT Value | GISTIC Value | Meaning |
|---|---|---|
| X = 0 | -2 | Deep loss |
| X = 1 | -1 | Single-copy loss |
| X = 2 | 0 | Diploid |
| 2 &lt; X &lt; 7 | 1 | Low-level gain |
| 7 &le; X | 2 | Amplification |

Only amplifications (GISTIC = 2) and deep deletions (GISTIC = -2) are shown on the cBioPortal website. As a result these conversion thresholds affect how many samples show up in the CNA chart, which can be inconsistent with legacy versions of this study. We chose ASCAT &ge; 7 as the amplification threshold because it resulted in the least deviation from our legacy studies.



## mRNA Expression data

- Retrieved from `isb-cgc-bq.TARGET_versioned.RNAseq_hg38_gdc_r35`. ISB-CGC data was created in December 2022.
- The `unstranded`, `tpm_unstranded`, and `fpkm_uq_unstranded` columns are pulled and each mapped to their own data file.
  - The regular FPKM values are excluded because [FPKM-UQ provides a more stable metric](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/#upper-quartile-fpkm).
- Transformations: see [Genomic data transformations](#genomic-data-transformations)



## Mutation data

- Retrieved from `isb-cgc-bq.TARGET_versioned.masked_somatic_mutation_hg38_gdc_r40`. ISB-CGC data was created in July 2024.
- The MAF is annotated with Genome Nexus in order to avoid issues with the isoform mapping. Parameters used:
  - Endpoint: https://grch38.genomenexus.org/
  - Isoform override: mskcc
  - Replace gene symbols and Entrez IDs
  - Post interval size: 500
- Mutation data may be missing for some samples-- this reflects a lack of data availability in ISB-CGC.

## Expression data transformations (CNA / mRNA)

- Ensembl gene IDs are mapped to Entrez IDs using the [Genome Nexus hg38 canonical transcript file](https://github.com/genome-nexus/genome-nexus-importer/blob/master/data/grch38_ensembl95/export/ensembl_biomart_canonical_transcripts_per_hgnc.txt). Any genes that cannot be converted using this file are dropped.
  - Prior to conversion, we also filter out a small number of duplicate Ensembl genes. These genes have copies containing data for both the X and the Y chromosomes.
- If a sample has multiple aliquots, it has to be condensed to 1 before it can imported into cBioPortal. This is done by choosing the aliquot ID with the highest sort value (eg. highest plate number), following [the same policy](https://broadinstitute.atlassian.net/wiki/spaces/GDAC/pages/844334036/FAQ#FAQ-replicateFilteringQ%3AWhatdoyoudowhenmultiplealiquotbarcodesexistforagivensample%2Fportion%2Fanalytecombination%3F) used by GDAC used to condense aliquot data in their studies.

## Post-processing steps

  - Samples that lack any genomic data are removed from the clinical sample file.
  - Metadata headers are added to the clinical patient and sample files using a curation-provided script.
  - Case lists are generated under `case_lists/` using a curation-provided script.
  - The validator script is run and the HTML report is saved under `validation_reports/`.

## List of remapped columns

### Clinical patient

| Original | cBioPortal |
|---|---|
| submitter_id | PATIENT_ID |
| case_id | OTHER_PATIENT_ID |
| demo__ethnicity | ETHNICITY |
| demo__gender | SEX |
| demo__race | RACE |
| demo__vital_status | VITAL_STATUS |
| diag__age_at_diagnosis | AGE |
| diag__classification_of_tumor | TUMOR_CLASSIFICATION |
| diag__cog_neuroblastoma_risk_group | COG_NEUROBLASTOMA_RISK_GROUP |
| diag__icd_10_code | ICD_10 |
| diag__inss_stage | INSS_STAGE |
| diag__last_known_disease_status | DISEASE_STATUS |
| diag__metastasis_at_diagnosis | METASTASIS_AT_DIAGNOSIS |
| diag__morphology | MORPHOLOGY |
| diag__path__necrosis_percent | PATHOLOGY_NECROSIS_PERCENT |
| diag__primary_diagnosis | PRIMARY_DIAGNOSIS |
| diag__site_of_resection_or_biopsy | BIOPSY_SITE |
| diag__year_of_diagnosis | YEAR_OF_DIAGNOSIS |
| disease_type | DISEASE_TYPE |
| index_date | INDEX_DATE |
| primary_site | PRIMARY_SITE_PATIENT |
| proj__name | PROJECT_NAME |
| proj__project_id | PROJECT_ID |


### Clinical sample

| Original | cBioPortal |
|---|---|
| case_barcode | PATIENT_ID |
| sample_barcode | SAMPLE_ID |
| sample_gdc_id | OTHER_SAMPLE_ID |
| sample_type_name | SAMPLE_TYPE |
| primary_site | PRIMARY_SITE |
| days_to_collection | DAYS_TO_COLLECTION |
| days_to_sample_procurement | DAYS_TO_SPECIMEN_COLLECTION |
| is_ffpe | IS_FFPE |



### Mutation

| Original | cBioPortal |
|---|---|
| sample_barcode_tumor | Tumor_Sample_Barcode |
| sample_barcode_normal | Matched_Norm_Sample_Barcode |