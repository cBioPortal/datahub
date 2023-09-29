# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-022-04640-1#Sec31](https://www.nature.com/articles/s41586-022-04640-1#Sec31)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Sample information."
* only patients with Diagnosis = "Normal" were selected.
* Patients/samples included in previous studies were excluded.
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Case ID               |PATIENT_ID           |
  |Sex                   |SEX                  |
  |Age (yrs)             |AGE                  |
  |Cause of Death        |CAUSE_OF_DEATH       |
 
* Sample data was retrieved from Supplementary Table 1 - "Sample information."
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Neuron ID             |SAMPLE_ID            |
  |Case ID               |PATIENT_ID           |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 3 - "sSNV candidates identified in each neuron." 
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all