# **Information on the Curation of this Study**

## General
* Study: [https://www.biorxiv.org/content/10.1101/2024.03.17.585238v1](https://www.biorxiv.org/content/10.1101/2024.03.17.585238v1)
* Reference genome used: GRCh38
* uploaded data was provided by the authors

## Clinical Data
* Patient data was provided by the authors
* only normal gastric tissue samples were included
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Donor		 |PATIENT_ID           |
  |Sex	                 |SEX                  |
  |Age			 |AGE                  |
  |H pylori status       |H.PYLORI.STATUS      |
  |Cohort		 |ADJ_NEOPLASM	       |

 
* Sample data was provided by the authors
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Sample                |SAMPLE_ID            |
  |Donor                 |PATIENT_ID           |
  |Site                  |SAMPLE_SITE          |
  |-			 |TISSUE_COLLECTION    |
  |-	                 |TISSUE_TYPE          |
  |-	                 |CLONALITY            |
  |-	                 |SEQ_TYPE             |

## Mutation Data
  * Mutation data was provided by the authors"
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* cases_all
* cases_sequenced