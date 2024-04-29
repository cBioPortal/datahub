# Comments & assumptions made during curation

## General

- Study is updated once every 3 months with latest data from [ISB-CGC BigQuery tables](https://isb-cgc.appspot.com/bq_meta_search/)
  - The ISB-CGC tables allow easy access to data collected from multiple NCI-CRDC repositories including the GDC, PDC, and others. The TCGA data in this study comes from the GDC and is accessed through these tables.
- Reference genome used: hg38
- This is the primary difference between this study and the legacy TCGA studies (PanCan / provisional), which use the hg19 genome. See [here](https://broadinstitute.atlassian.net/wiki/spaces/GDAC/pages/844334036/FAQ#FAQ-EndOfTCGAQ%3AIunderstandthatTCGAdatahasmigratedtotheGDC%2CbutwhydoIseediscrepanciesbetweenGDCandFireBrowse%3F) for more information.
- Only tumor sample data is included (no normal samples)

## Clinical data

- **Patient data:** Retrieved from `isb-cgc-bq.TCGA.clinical_gdc_current`
- **Sample data:** Retrieved from `isb-cgc-bq.TCGA.per_sample_file_metadata_hg38_gdc_current`

### Survival data

- `OS_STATUS` is converted from `demo__vital_status`
- `OS_MONTHS` is converted from `demo__days_to_death`, falls back to `diag__days_to_last_follow_up`
- `DFS_STATUS` and `DFS_MONTHS` are unavailable from BigQuery, so instead they're pulled from existing TCGA studies in Datahub.
  - The corresponding PanCan study is checked first, then the legacy TCGA study


### Other transformations

- `RACE` and `ETHNICITY` are capitalized.
- `AGE` is clipped from 18 to 89.


## CNA data

- Retrieved from `isb-cgc-bq.TCGA.copy_number_gene_level_hg38_gdc_current`
- Transformations
  - Copy number values from the BigQuery tables are converted from [ASCAT](https://www.pnas.org/doi/10.1073/pnas.1009843107https://www.pnas.org/doi/10.1073/pnas.1009843107) to GISTIC 2.0 using the following thresholds:

| ASCAT Value | GISTIC Value |
|---|---|
| X = 0 | -2 |
| X = 1 | -1 |
| X = 2 | 0 |
| 2 &lt; X &le; 8 | 1 |
| 8 &lt; X | 2 |



## mRNA Expression data

- Retrieved from `isb-cgc-bq.TCGA.RNAseq_hg38_gdc_current`
- The `unstranded`, `tpm_unstranded`, and `fpkm_uq_unstranded` columns are pulled and each mapped to their own data file.
  - The regular FPKM values are excluded because [FPKM-UQ provides a more stable metric](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/#upper-quartile-fpkm).
- Transformations: see [Genomic data transformations](#genomic-data-transformations)



## Segment data

- Retrieved from `isb-cgc-bq.TCGA.copy_number_segment_masked_hg38_gdc_current`


## Mutation data

- Retrieved from `isb-cgc-bq.TCGA.masked_somatic_mutation_hg38_gdc_current`
- The MAF is annotated with Genome Nexus in order to avoid issues with the isoform mapping. Parameters used:
  - Endpoint: https://grch38.genomenexus.org/
  - Isoform override: mskcc
  - Replace gene symbols and Entrez IDs
  - Post interval size: 500

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
| case_id | OTHER_PATIENT_ID |
| submitter_id | PATIENT_ID |
| demo__days_to_birth | DAYS_TO_BIRTH |
| demo__days_to_death | DAYS_TO_DEATH |
| demo__ethnicity | ETHNICITY |
| demo__gender | GENDER |
| demo__race | RACE |
| demo__vital_status | VITAL_STATUS |
| demo__year_of_birth | BIRTH_YEAR |
| demo__year_of_death | YEAR_OF_DEATH |
| diag__age_at_diagnosis | AGE |
| diag__ajcc_clinical_m | CLIN_M_STAGE |
| diag__ajcc_clinical_n | CLIN_N_STAGE |
| diag__ajcc_clinical_stage | CLINICAL_STAGE |
| diag__ajcc_clinical_t | CLIN_T_STAGE |
| diag__ajcc_pathologic_m | PATH_M_STAGE |
| diag__ajcc_pathologic_n | PATH_N_STAGE |
| diag__ajcc_pathologic_stage | PATH_STAGE |
| diag__ajcc_pathologic_t | PATH_T_STAGE |
| diag__ajcc_staging_system_edition | AJCC_STAGING_EDITION |
| diag__ann_arbor_b_symptoms | LYMPH_B_SYMPTOMS |
| diag__ann_arbor_clinical_stage | CLIN_STAGE_ANN_ARBOR |
| diag__ann_arbor_extranodal_involvement | EXTRANODAL_INVOLVEMENT |
| diag__days_to_last_follow_up | DAYS_LAST_FOLLOWUP |
| diag__figo_stage | FIGO_GRADE |
| diag__icd_10_code | ICD_10 |
| diag__igcccg_stage | IGCCCG_STAGE |
| diag__masaoka_stage | MASAOKA_STAGE |
| diag__morphology | MORPHOLOGY |
| diag__primary_diagnosis | PRIMARY_DIAGNOSIS |
| diag__primary_gleason_grade | PRIMARY_GLEASON_SCORE |
| diag__prior_malignancy | PRIOR_MALIGNANCY |
| diag__prior_treatment | PRIOR_TREATMENT |
| diag__site_of_resection_or_biopsy | BIOPSY_SITE |
| diag__year_of_diagnosis | YEAR_OF_DIAGNOSIS |
| disease_type | DISEASE_TYPE |
| exp__alcohol_history | ALCOHOL_HISTORY_DOCUMENTED |
| exp__pack_years_smoked | SMOKING_PACK_YEARS |
| exp__years_smoked | SMOKER_YEARS |
| primary_site | PRIMARY_SITE_PATIENT |
| proj__name | PROJECT_NAME |
| proj__project_id | PROJECT_ID |
| state | PROJECT_STATE |


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


### Segment

| Original | cBioPortal |
|---|---|
| sample_barcode | ID |
| chromosome | chrom |
| start_pos | loc.start |
| end_pos | loc.end |
| num_probes | num.mark |
| segment_mean | seg.mean |


### Mutation

| Original | cBioPortal |
|---|---|
| sample_barcode_tumor | Tumor_Sample_Barcode |
| sample_barcode_normal | Matched_Norm_Sample_Barcode |