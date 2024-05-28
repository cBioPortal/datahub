# Comments & assumptions made during curation

## General

- Study is updated once every 3 months with latest data from [ISB-CGC BigQuery tables](https://isb-cgc.appspot.com/bq_meta_search/)
  - The ISB-CGC tables allow easy access to data collected from multiple NCI-CRDC repositories including the GDC, PDC, and others. The CPTAC data in this study comes from the GDC and is accessed through these tables.
- Reference genome used: hg38

- Only tumor sample data is included (no normal samples)

## Clinical data

- **Patient data:** Retrieved from `isb-cgc-bq.CPTAC_versioned.clinical_gdc_r39`. ISB-CGC data was created in December 2023.
- **Sample data:** Retrieved from `isb-cgc-bq.CPTAC_versioned.per_sample_file_metadata_hg38_gdc_r39`. ISB-CGC data was created in December 2023.

### Survival data

Survival fields are calculated from the clinical data and added as new columns in the clinical file.

- `OS_STATUS` is converted from `demo__vital_status`
- `OS_MONTHS` is converted from `demo__days_to_death`, falls back to `diag__days_to_last_follow_up`

- `DFS_STATUS` is converted from `diag_progression_or_recurrence` / `follow_progression_or_recurrence`
- `DFS_MONTHS` is converted from `diag__days_to_recurrence` / `follow__days_to_recurrence`, falls back to `OS_MONTHS`

### Timeline data

Timeline data is extracted from the clinical data and stored in a separate data file. After extraction, the corresponding BigQuery fields are removed from the clinical file. For example, a timeline status of `BIRTH` corresponds to the BigQuery field `demo__days_to_birth`.

The following status values are supported in `data_timeline_status.txt`:

- `Initial Diagnosis`
- `BIRTH`
- `DECEASED`
- `Last Follow Up`
- `Consented`
- `Lost to Follow Up`
- `Last Known Disease Status`
- `Recurrence`
### Other transformations

- `RACE` and `ETHNICITY` are capitalized.
- `AGE` is clipped from 18 to 89.
- `"not reported"` values are replaced with blanks.

## CNA data

- Retrieved from `isb-cgc-bq.CPTAC_versioned.copy_number_gene_level_hg38_gdc_r36`. ISB-CGC data was created in March 2023.
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

- Retrieved from `isb-cgc-bq.CPTAC_versioned.RNAseq_hg38_gdc_r35`. ISB-CGC data was created in December 2022.
- The `unstranded`, `tpm_unstranded`, and `fpkm_uq_unstranded` columns are pulled and each mapped to their own data file.
  - The regular FPKM values are excluded because [FPKM-UQ provides a more stable metric](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/#upper-quartile-fpkm).
- Transformations: see [Genomic data transformations](#genomic-data-transformations)



## Mutation data

- Retrieved from `isb-cgc-bq.CPTAC_versioned.masked_somatic_mutation_hg38_gdc_r37`. ISB-CGC data was created in October 2023.
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
| demo__gender | SEX |
| demo__race | RACE |
| demo__vital_status | VITAL_STATUS |
| demo__year_of_birth | BIRTH_YEAR |
| demo__year_of_death | YEAR_OF_DEATH |
| diag__age_at_diagnosis | AGE |
| diag__ajcc_clinical_m | CLIN_M_STAGE |
| diag__ajcc_pathologic_m | PATH_M_STAGE |
| diag__ajcc_pathologic_n | PATH_N_STAGE |
| diag__ajcc_pathologic_stage | PATH_STAGE |
| diag__ajcc_pathologic_t | PATH_T_STAGE |
| diag__ajcc_staging_system_edition | AJCC_STAGING_EDITION |
| diag__classification_of_tumor | TUMOR_CLASSIFICATION |
| diag__days_to_last_follow_up | DAYS_LAST_FOLLOWUP |
| diag__figo_stage | FIGO_GRADE |
| diag__last_known_disease_status | DISEASE_STATUS |
| diag__morphology | MORPHOLOGY |
| diag__primary_diagnosis | PRIMARY_DIAGNOSIS |
| diag__prior_malignancy | PRIOR_MALIGNANCY |
| diag__progression_or_recurrence | PROGRESSION_OR_RECURRENCE |
| diag__site_of_resection_or_biopsy | BIOPSY_SITE |
| diag__tumor_grade | TUMOR_GRADE |
| diag__year_of_diagnosis | YEAR_OF_DIAGNOSIS |
| disease_type | DISEASE_TYPE |
| exp__alcohol_history | ALCOHOL_HISTORY_DOCUMENTED |
| exp__pack_years_smoked | SMOKING_PACK_YEARS |
| exp__years_smoked | SMOKER_YEARS |
| primary_site | PRIMARY_SITE_PATIENT |
| proj__name | PROJECT_NAME |
| proj__project_id | PROJECT_ID |
| state | PROJECT_STATE |
| consent_type | CONSENT_TYPE |
| days_to_consent | DAYS_TO_CONSENT |
| days_to_lost_to_followup | DAYS_TO_LOST_FOLLOWUP |
| demo__cause_of_death | CAUSE_OF_DEATH |
| diag__days_to_last_known_disease_status | DAYS_TO_LAST_KNOWN_DISEASE_STATUS |
| diag__path__lymph_nodes_positive | LYMPH_NODES_POSITIVE |
| diag__path__tumor_largest_dimension_diameter | TUMOR_LARGEST_DIMENSION |
| diag__residual_disease | RESIDUAL_DISEASE |
| diag__tumor_focality | TUMOR_FOCALITY |
| exp__alcohol_intensity | ALCOHOL_INTENSITY |
| exp__secondhand_smoke_as_child | SECONDHAND_SMOKE_AS_CHILD |
| exp__tobacco_smoking_onset_year | SMOKING_ONSET_YEAR |
| exp__tobacco_smoking_quit_year | SMOKING_QUIT_YEAR |
| exp__tobacco_smoking_status | SMOKING_STATUS |
| exp__type_of_smoke_exposure | TYPE_SMOKING_EXPOSURE |
| exp__type_of_tobacco_used | TYPE_TOBACCO_EXPOSURE |
| follow__aids_risk_factors | AIDS_RISK_FACTORS |
| follow__bmi | BMI |
| follow__cdc_hiv_risk_factors | CDC_HIV_RISK_FACTORS |
| follow__comorbidity | COMORBIDITY |
| follow__days_to_recurrence | DAYS_TO_RECURRENCE |
| follow__diabetes_treatment_type | DIABETES_TX_TYPE |
| follow__disease_response | DISEASE_RESPONSE |
| follow__dlco_ref_predictive_percent | DLCO_REF_LUNG_VOL |
| follow__ecog_performance_status | ECOG_PERFORMANCE_STATUS |
| follow__fev1_fvc_post_bronch_percent | FEV1_FVC_POST_BRONCH_PERCENT |
| follow__fev1_fvc_pre_bronch_percent | FEV1_FVC_PRE_BRONCH_PERCENT |
| follow__fev1_ref_post_bronch_percent | FEV1_FVC_REF_POST_BRONCH_PERCENT |
| follow__fev1_ref_pre_bronch_percent | FEV1_FVC_REF_PRE_BRONCH_PERCENT |
| follow__height | HEIGHT |
| follow__hormonal_contraceptive_use | HORMONAL_CONTRACEPTIVE_USE |
| follow__hpv_positive_type | HPV_POSITIVE_TYPE |
| follow__karnofsky_performance_status | KPS |
| follow__pancreatitis_onset_year | PANCREATITIS_ONSET_YEAR |
| follow__weight | WEIGHT |
| index_date | INDEX_DATE |
| lost_to_followup | LOST_TO_FOLLOW_UP |


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