# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-019-1670-9](https://www.nature.com/articles/s41586-019-1670-9)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Clinical data on subjects included in the study."
* only patients with Aetiology = "NORMAL" and Cancer = "Colorectal Ca" were included
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |PD ID		 |PATIENT_ID           |
  |Gender                |SEX                  |
  |Age at resection (yrs)|AGE                  |
  |Smoking status        |SMOKING              |
  |bowel_cancer_diagnosis|ADJACENT_CANCER      |
  |Steatosis (0-3)       |STEATOSIS_SCORE      |
  |Lobular inflammation (0-2)|LOBULAR_INFLAMMATION_SCORE|
  |Hepatocellular ballooning (0-2)|HEPATOCELLULAR_BALLOONING_SCORE|
  |NAS score	         |NAS_SCORE            |
  |Creat (µM)	         |PREOP_CREATININE     |
  |Bili (µM)		 |PREOP_ BILIRUBIN     |
  |Sodium (µM)	         |PREOP_SODIUM         |
  |PT (secs)	         |PREOP_PT             |
 
* Sample data was retrieved from the [study's Mendeley website](https://data.mendeley.com/datasets/ktx7jp8sch/1) - "all_mutations_normal_cancer_snv_indels.csv"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |sample                |SAMPLE_ID            |
  |donor                 |PATIENT_ID           |
 
## Mutation Data
  * Mutation data was retrieved from the [study's Mendeley website](https://data.mendeley.com/datasets/ktx7jp8sch/1) - "all_mutations_normal_cancer_snv_indels.csv"
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all