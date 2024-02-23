# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-021-03822-7](https://www.nature.com/articles/s41586-021-03822-7)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Information about the individuals recruited for this study"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Donor-ID              |PATIENT_ID           |
  |Sex                   |SEX                  |
  |Age                   |AGE                  |
  |Vital status / Reason for Biopsy|SURVIVAL_STATUS|
  |Vital status / Reason for Biopsy|CAUSE_OF_DEATH|
  |Vital status / Reason for Biopsy|REASON_FOR_BIOPSY|
 
* Sample data was retrieved from Supplementary Table 4 - "Sample Information"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Sample                |SAMPLE_ID            |
  |DonorID               |PATIENT_ID           |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 5 - "Whole-genome SBS across all samples." and Supplementary Table 6 - "Whole-genome INDELs across all samples"
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all