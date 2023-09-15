# Steps taken for curation and transformation of GLASS Dataset:

## General Information
- Data Source: [GLASS data on Synapse](https://www.synapse.org/#!Synapse:syn17038081/wiki/585622)
- Reference publication: [PubMed Reference](https://pubmed.ncbi.nlm.nih.gov/35649412/)
- The data here represents the GLASS `2022-05-31` release version. 
- Reference genome used: GRCh37

## Sample size selection
- Silver set samples were used for the study.
- Files used: analysis_silver_set & analysis_rna_silver_set (If a sample had multiple aliquots, the silver set represented a single aliquot per sample)
	- `analysis_silver_set`: Contains DNA pairs that pass fingerprinting and coverage QC, representing a single aliquot per patient (maximal timepoint for patients with multiple recurrences).
	- `rna_silver_set`: Lists RNA pairs passing fingerprinting and clinical QC, with the maximal timepoint taken for patients with multiple recurrences.
- Overall Cohort Size: 598 samples (299 DNA pairs and 139 RNA pairs) from 299 patients.

## Clinical data
- Patient-Level Data: `clinical_cases`
- Sample-Level Data: `clinical_surgeries`, `biospecimen_sample_types`, `biospecimen_samples`, `biospecimen_aliquots`, `analysis_estimate_purity`
- Patient and sample files were subset to silver set samples.
	 
## Timeline Data
- Cumulative time elapsed in months between surgeries is provided. For the initial surgery, t0 is consistently set to 0, and subsequent relative events are added into the timeline.
- File used: `clinical_surgeries`
- Surgery and Treatment (Chemo, Radiation and Targeted therapy) events relative to first surgery are added to timeline.

## Mutation Data
- Files used:  `variants_passgeno_20220531.csv.gz` and `variants_anno_20220531.csv.gz`
- Mutation data was processed, filtered for variants that passed filters in single-sample Mutect2 mode.
	- Each row in variants_passgeno table represents a single variant detected using multi-sample Mutect2 and is reported for a given sample. Thus, for each patient the variant information is listed for all samples (including normal blood). Single-sample mutation calls were overlaid on the multi-sample calls to infer whether variants were called in individual samples. 
	- The ssm2_pass_call column is a flag indicating whether the variant was called and passed filters in single-sample Mutect2 mode. Selected only the variants that passed filters and called in single-sample Mutect2 mode.
	- The file is processed as : https://gist.github.com/rmadupuri/5e78309792181dbb1cdec88475f5afb5
	- Each row in the variants_anno file indicates further annotations for the variants in the passgeno file. 
	- The anno file is merged to passgeno file as: https://gist.github.com/rmadupuri/757197f0d0cef4871254e5b2ffd51d4c
- IDH1, IDH2, and TERTp variants were force-filtered based on clinical tests and alt_counts.
	- All the IDH1, IDH2 variants with the sample IDH_status = 'IDHmut' and the variants alt_count > 0, all TERT variants with alt_count > 0 are picked.
	- https://gist.github.com/rmadupuri/92bbb19859b74d057088dbb4943e7a67
- Check for duplicate variants and remove : https://gist.github.com/rmadupuri/570782777e3e4e44ac31aae3f94cdf4a
- The variants were annotated using Genome Nexus.

## RNA-seq Expression
- File used: `gene_tpm_matrix_all_samples.tsv`
- Samples were filtered based on the rna_silver_set
- Expression data was log transformed and z-scores were calculated using https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/zscores/zscores_relative_allsamples (with -l, -e tags).

## Methylation Data
- Files used: `betas.450.tsv`, `betas.epic.tsv`, `betas.merged.tsv` (methylation beta-values per CpG probe ID (row) by aliquot (column) is given)
- Added methylation profiles for the Illumina 450K array, EPIC array, and merged 450K and EPIC arrays.

## H&E Images
- H&E slides were accessible for five patients and obtained from the [Digital Slide Archive](https://styx.neurology.emory.edu/girder/#collection/625dda70622f966e826a0446/folder/625dda90622f966e826a0448)

## Clinical data remapping
- Original clinical data columns were remapped to new column names for patients and samples, as listed in the table below.

Original column | Renamed column | Patient/sample
-- | -- | --
case_barcode | PATIENT_ID | Patient
case_project | CASE_PROJECT | Patient
Case_source | TISSUE_SOURCE | Patient
case_sex | SEX | Patient
case_age_diagnosis_years | AGE | Patient
case_vital_status | OS_STATUS | Patient
case_overall_survival_mo | OS_MONTHS | Patient
case_barcode | PATIENT_ID | Sample
sample_barcode | SAMPLE_ID | Sample
grade | TUMOR_GRADE | Sample
who_classification | TUMOR_CLASSIFICATION | Sample
histology | HISTOLOGY | Sample
idh_status | IDH_STATUS | Sample
codel_status | CODEL_STATUS | Sample
surgery_type | SURGERY_TYPE | Sample
surgery_indication | SURGERY_INDICATION | Sample
surgery_extent_of_resection | SURGERY_EXTENT_OF_RESECTION | Sample
surgery_laterality | SURGERY_LATERALITY | Sample
surgery_location | SURGERY_LOCATION | Sample
treatment_tmz | TREATMENT_TMZ | Sample
treatment_tmz_cycles | TREATMENT_TMZ_CYCLES | Sample
treatment_tmz_cycles_6 | TREATMENT_TMZ_CYCLES_6 | Sample
treatment_concurrent_tmz | TREATMENT_CONCURRENT_TMZ | Sample
treatment_radiotherapy | TREATMENT_RADIOTHERAPY | Sample
treatment_radiation_dose_gy | TREATMENT_RADIATION_DOSE_GY | Sample
idh_codel_subtype | IDH_CODEL_STATUS | Sample
treatment_alkylating_agent | TREATMENT_ALKYLATING_AGENT | Sample
mgmt_methylation_method | MGMT_METHYLATION_METHOD | Sample
aliquot_barcode | ALIQUOT_BARCODE | Sample
aliquot_analysis_type | ALIQUOT_ANALYSIS_TYPE | Sample
aliquot_portion | ALIQUOT_PORTION_ID | Sample
aliquot_batch | ALIQUOT_BATCH | Sample
sample_type_description | SAMPLE_TYPE | Sample


