# Comments & assumptions made during curation

## General

- Study is updated once every 3 months with latest data from [ISB-CGC BigQuery tables](https://isb-cgc.appspot.com/bq_meta_search/)
  - The ISB-CGC tables allow easy access to data collected from multiple NCI-CRDC repositories including the GDC, PDC, and others. The TCGA data in this study comes from the GDC and is accessed through these tables.
- Reference genome used: hg38
- TCGA started using the hg38 genome as of GDC release 32. For more information, refer to the [GDC release notes](https://docs.gdc.cancer.gov/Data/Release_Notes/Data_Release_Notes/#data-release-320).
- This is the primary difference between this study and the legacy TCGA studies (PanCan / provisional), which use the hg19 genome. See [here](https://broadinstitute.atlassian.net/wiki/spaces/GDAC/pages/844334036/FAQ#FAQ-EndOfTCGAQ%3AIunderstandthatTCGAdatahasmigratedtotheGDC%2CbutwhydoIseediscrepanciesbetweenGDCandFireBrowse%3F) for more information.
- Only tumor sample data is included (no normal samples)

## Clinical data

- **Patient data:** Retrieved from `isb-cgc-bq.TCGA_versioned.clinical_gdc_r39`. ISB-CGC data was created in December 2023.
- **Sample data:** Retrieved from `isb-cgc-bq.TCGA_versioned.biospecimen_gdc_2017_02`. ISB-CGC data was created in April 2017.

### Survival data

Survival fields are calculated from the clinical data and added as new columns in the clinical file.

- `OS_STATUS` is converted from `demo__vital_status`
- `OS_MONTHS` is converted from `demo__days_to_death`, falls back to `diag__days_to_last_follow_up`
- `DFS_STATUS` and `DFS_MONTHS` are unavailable from BigQuery, so instead they're pulled from existing TCGA studies in Datahub.
  - The corresponding PanCan study is checked first, then the legacy TCGA study


### Timeline data

- Timeline data is extracted from the clinical data and stored in a separate data file. After extraction, the corresponding BigQuery fields are removed from the clinical file. For example, a timeline status of `DEATH` corresponds to the BigQuery field `demo__days_to_death`.

- For TCGA, the "time 0" anchor point is always the date of diagnosis. Not all patients have timeline data available, as indicated by a null `diag__days_to_diagnosis` (TCGA) or `index_date` (CPTAC) field.

- Birth timeline events are removed, as they (1) push other events to the far right of the graph and (2) can potentially be used to identify the patient.

The following status values are supported in `data_timeline_status.txt`:

- `__time0__`
- `demo__days_to_death`
- `diag__days_to_last_follow_up`
### Other transformations

- `"not reported"` values are replaced with blanks.
- If a clinical field is missing for the entire study, the column is removed from the data file.
- `RACE`, `ETHNICITY`, and `SEX` are capitalized.
- `AGE` is clipped from 18 to 89 to protect patient confidentiality.

## CNA data

- Retrieved from `isb-cgc-bq.TCGA_versioned.copy_number_gene_level_hg38_gdc_r36`. ISB-CGC data was created in March 2023.
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

- Retrieved from `isb-cgc-bq.TCGA_versioned.RNAseq_hg38_gdc_r35`. ISB-CGC data was created in December 2022.
- The `unstranded`, `tpm_unstranded`, and `fpkm_uq_unstranded` columns are pulled and each mapped to their own data file.
  - The regular FPKM values are excluded because [FPKM-UQ provides a more stable metric](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/#upper-quartile-fpkm).
- Transformations: see [Genomic data transformations](#genomic-data-transformations)

## Segment data

- Retrieved from `isb-cgc-bq.TCGA_versioned.copy_number_segment_masked_hg38_gdc_r14`. ISB-CGC data was created in December 2018.

## Mutation data

- Retrieved from `isb-cgc-bq.TCGA_versioned.masked_somatic_mutation_hg38_gdc_r36`. ISB-CGC data was created in March 2023.
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
| case_id | OTHER_PATIENT_ID |
| submitter_id | PATIENT_ID |
| demo__ethnicity | ETHNICITY |
| demo__gender | SEX |
| demo__race | RACE |
| demo__vital_status | VITAL_STATUS |
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