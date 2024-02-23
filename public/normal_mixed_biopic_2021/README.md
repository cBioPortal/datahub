# **Information on the Curation of this Study**

## General
* Study: https://www.nature.com/articles/s41586-021-03836-1
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Clinical information for the five donors in the current study."
* remapped clinical patient data:

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Sample ID             |PATIENT_ID           |
  |patient_lable_in_files|PATIENT_ID           |
  |Gender                |SEX                  |
  |Age                   |AGE                  |
  |Cause of death        |CAUSE_OF_DEATH       |
  |Smoking               |SMOKING              |
  |Drinking              |ALCOHOL              |
  |Medical history       |MEDICAL_HISTORY      |
  |-                     |INFERRED_RACE        |

* Mutation data was retrieved from multiple sheets of Supplementary Table 2 "Whole-exome sequencing information."

 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 2 "Whole-exome sequencing information."
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all