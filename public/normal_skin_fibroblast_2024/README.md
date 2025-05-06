# **Information on the Curation of this Study**

## General
* Study: [https://pmc.ncbi.nlm.nih.gov/articles/PMC11291049/]
* Reference genome used: GRCh37
* Normal Keratinocytes (UCSF, BioRxiv 2024)
* Uploaded data available from original publication and from authors
* Sequencing Platform - Whole exome sequencing 
* The study has been divided by skin cell types from one article: 39091884

## Clinical Data
* Patient data was retrieved from Supplementary Table S1 - "Summary of clinical and demographic information"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |sample number	     |PATIENT_ID           |
  |Gender                |SEX                  |
  |Age                   |AGE                  |
  |Ethnicity	         |ETHNICITY            |
  |Tanning Bed Usage     |TANNING_BED_USAGE    |

 
* Patient data was retrieved from Supplementary Table S1 - "Summary of clinical and demographic information"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name   | Remapped Column Name|
  |------------------------|---------------------|
  |sample/follicle         |SAMPLE_ID            |
  |subject/Donor           |PATIENT_ID           |
  |Number of cells in Clone|N_CELLS	             |
  |Adjacent to Cancer      |ADJACENT_TO_CANCER   |
  |Probe Type              |PROBE_TYPE           |
  |Cell Type               |CELL_TYPE            |
  
## Mutation Data
  * Mutation data was retrieved from all the three articles.
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)
  
## Mutational Signatures Contribution SBS Data
  * Data was shared by the author.