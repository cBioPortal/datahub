# **Information on the Curation of this Study**

## General
* Study: [http://www.nature.com/articles/s41586-018-0497-0](http://www.nature.com/articles/s41586-019-1672-7)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Patient information: Information on all the patients in this study, including their age, cohort, and cancer status."
* remapped clinical patient data:

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |patient_lable_in_figures|-                  |
  |patient_lable_in_files|PATIENT_ID           |
  |sex                   |SEX                  |
  |age                   |AGE                  |
  |cohort                |-                    |
  |bowel_cancer_diagnosis|ADJACENT_CANCER      |
 
* Sample data was retrieved from Supplementary Table 2 - "Signature contributions to each crypt: The contribution of each mutational signature to each crypt."
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |crypt                 |SAMPLE_ID            |
  |site                  |SAMPLE_LOCATION      |
  |patient               |PATIENT_ID           |
  |med_vafs              |MEDIAN_VAF           |
  |med_depths            |MEDIAN_SEQ_DEPTH     |
  |telomere              |TELOMERE_LENGTH      |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 3 - "Coding mutations: This table contains all coding mutations detected in our crypts."
  * Only coding variants were available for this study
  * Mutation data was edited into MAF format

## Case Lists
Case lists generated:
* Case list all
