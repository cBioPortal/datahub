# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-021-03345-1#Sec30](https://www.nature.com/articles/s41586-021-03345-1#Sec30)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Summary overview of placental samples collected and their mutation profile."
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Case_ID		 |PATIENT_ID           |
  |Sex                   |FETAL_SEX            |
  |age                   |UMBILICAL_CORD_ID    |
  |cohort                |MATERNAL_BLOOD_ID    |
  |Clinical_additional   |BIRTH_WEIGHT	       |
  |Clinical_additional   |PLACENTA_WEIGHT      |
  |Clinical_additional   |PREECLAMPSIA         |
  |Clinical_additional   |PAPP_A	       |
  |Clinical_additional   |PI_UMBILICAL_ARTERY  |
  |Clinical_additional   |PI_UTERINE_ARTERY    |
  |Clinical_additional   |SFLT_PIGF_RATIO      |
  |Clinical_additional    |ACGV		       |
 
* Sample data was retrieved from Supplementary Table 1 - "Summary overview of placental samples collected and their mutation profile."
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Sample                |SAMPLE_ID            |
  |Case_ID               |PATIENT_ID           |
  |Experimental_arm      |CLONALITY            |
  |Histo_description     |TISSUE_TYPE	       |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 4 - "List of all substitutions and indels called across the cohort."
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all