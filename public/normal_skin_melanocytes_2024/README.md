# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-020-2785-8]
[https://www.biorxiv.org/content/10.1101/2024.07.23.604673v2]
[https://www.biorxiv.org/content/10.1101/2024.06.04.597225v1]
* Reference genome used: GRCh37
* Normal Melanocytes (UCSF, Nature 2020)
* Uploaded data available from original publication and from authors
* Sequencing Platform - Whole exome sequencing
* The study has been divided by skin cell types from three articles (33029006,39091884,38895302)

## Clinical Data
* Patient data was retrieved from Supplementary Table S1 - "Summary of clinical and demographic information"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |sample number	     |PATIENT_ID           |
  |Gender                |SEX                  |
  |Age                   |AGE                  |
  |Skin Cancer History   |SKIN_CANCER_HISTORY  |
  |Fitzpatrick Score     |FITZPATRICK_SCORE    |
  |Smoking status        |SMOKING              |
  |Fitzpatrick score     |FITZPATRICK_SCORE    |
  |Working outside (UK)  |OUTSIDE_WORK_Y       |
  |Living abroad (subtropical/tropical regions|EXPOSED_LIVING       |
 
* Patient data was retrieved from Supplementary Table S1 - "Summary of clinical and demographic information"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |sample/follicle       |SAMPLE_ID            |
  |subject/Donor         |PATIENT_ID           |
  |-                     |TISSUE_TYPE	       |
  |Clonality             |CLONALITY            |
  |Tissue Type           |TISSUES_TYPE         |
  |Sample Site           |SAMPLE_SITE          |
  
## Mutation Data
  * Mutation data was retrieved from all the three articles.
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)
  
## Mutational Signatures Contribution SBS Data
  * Data was shared by the author.


## Case Lists
Case lists generated:
* cases_all
* cases_sequenced


## Missing Data:
* targeted sequencing (UCSF500) Data
* Copy Number Alterations Data
* Expression Data