# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-018-0811-x#MOESM14](https://www.nature.com/articles/s41586-018-0811-x#MOESM14)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Characteristics of subjects"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Cohort/Subject ID.    |PATIENT_ID           |
  |Sex                   |SEX                  |
  |Age (y)               |AGE                  |
  |Race                  |RACE                 |
  |Alcohol consumption   |ALCOHOL	       |
  |Smoking‡              |SMOKING	       |
  |ESCC−risk             |ESCC_RISK.           |
  |ESCC/HGD status       |ADJ_ESOPHAGEAL_DYSPLASIA_CANCER|
  |Tumor location♯       |TUMOR_LOCATION       |
  |Therapy¶              |THERAPY              |
  |TNM.                  |TNM     	       |
  |Stage §.              |STAGE 	       |
 
* Sample data was retrieved from Supplementary Table 2 - "Sample information"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Sample ID             |SAMPLE_ID            |
  |Case ID               |PATIENT_ID           |

* Only samples of normal esophageal epithelium were included in the upload

## Mutation Data
  * Mutation data was retrieved from Supplementary Table 8 - "Results of targeted capture sequencing"
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all