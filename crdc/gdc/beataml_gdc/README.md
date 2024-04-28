# Comments & assumptions made during curation

## General

- Study is updated once every 3 months with latest data from [ISB-CGC BigQuery tables](https://isb-cgc.appspot.com/bq_meta_search/)
  - The ISB-CGC tables allow easy access to data collected from multiple NCI-CRDC repositories including the GDC, PDC, and others. The BEATAML data in this study comes from the GDC and is accessed through these tables.
- Reference genome used: hg38

- Only tumor sample data is included (no normal samples)

## Clinical data

- **Patient data:** Retrieved from `isb-cgc-bq.BEATAML1_0.clinical_gdc_current`
- **Sample data:** Retrieved from ``

### Survival data

- `OS_STATUS` is converted from `demo__vital_status` if present
- `OS_MONTHS` is converted from `demo__days_to_death` if present, falls back to `diag__days_to_last_follow_up`

- `DFS_STATUS` is converted from `diag_progression_or_recurrence` / `follow_progression_or_recurrence` if present
- `DFS_MONTHS` is converted from `diag__days_to_recurrence` / `follow__days_to_recurrence` if present, falls back to `OS_MONTHS`


### Other transformations

- `RACE` and `ETHNICITY` are capitalized.
- `AGE` is clipped from 18 to 89.




## mRNA Expression data

- Retrieved from `isb-cgc-bq.BEATAML1_0.RNAseq_hg38_gdc_current`
- The `unstranded` and `fpkm_uq_unstranded` columns are pulled and each mapped to their own data file.
  - The regular FPKM values are excluded because [FPKM-UQ provides a more stable metric](https://docs.gdc.cancer.gov/Data/Bioinformatics_Pipelines/Expression_mRNA_Pipeline/#upper-quartile-fpkm).
- Transformations: see [Genomic data transformations](#genomic-data-transformations)




## Mutation data

- Retrieved from `isb-cgc-bq.BEATAML1_0.masked_somatic_mutation_hg38_gdc_current`
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
| demo__age_at_index | AGE_AT_INDEX |
| demo__demographic_id | DEMOGRAPHIC_ID |
| demo__ethnicity | ETHNICITY |
| demo__gender | GENDER |
| demo__race | RACE |
| demo__vital_status | VITAL_STATUS |
| diag__age_at_diagnosis | AGE |
| diag__anno__annotation_id | ANNOTATION_ID |
| diag__anno__category | ANNOTATION_CATEGORY |
| diag__anno__classification | ANNOTATION_CLASSIFICATION |
| diag__anno__entity_id | ENTITY_ID |
| diag__anno__entity_type | ENTITY_TYPE |
| diag__anno__notes | ANNOTATION_NOTES |
| diag__diagnosis_id | DIAGNOSIS_ID |
| diag__eln_risk_classification | ELN_RISK_CLASSIFICATION |
| diag__morphology | MORPHOLOGY |
| diag__primary_diagnosis | PRIMARY_DIAGNOSIS |
| diag__progression_or_recurrence | PROGRESSION_OR_RECURRENCE |
| diag__tissue_or_organ_of_origin | SAMPLE_ORIGIN |
| disease_type | TUMOR_TYPE |
| index_date | INDEX_DATE |
| primary_site | PRIMARY_SITE_PATIENT |
| proj__name | PROJECT_NAME |
| proj__project_id | PROJECT_ID |
| submitter_id | PATIENT_ID |


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