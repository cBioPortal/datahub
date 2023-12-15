# **Information on the Curation of this Study**

## General
* Study: [https://aacrjournals.org/cancerdiscovery/article/11/2/340/3261/Selection-of-Oncogenic-Mutant-Clones-in-Normal](https://aacrjournals.org/cancerdiscovery/article/11/2/340/3261/Selection-of-Oncogenic-Mutant-Clones-in-Normal)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Patient demographics"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |sample number	 |PATIENT_ID           |
  |Gender                |SEX                  |
  |Age                   |AGE                  |
  |Location              |SAMPLE_SITE          |
  |Initial diagnosis     |SKINCANCER_HISTORY   |
  |Smoking status        |SMOKING              |
  |Fitzpatrick score     |FITZPATRICK_SCORE    |
  |Working outside (UK)  |OUTSIDE_WORK_Y       |
  |Living abroad (subtropical/tropical regions|EXPOSED_LIVING       |
 
* Sample data was retrieved from Supplementary Table 4 - "List of all mutations detected in all 2mm2 gridded samples" and Supplementary Table 4 - "List of all mutations detected in hair follicle samples"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |sample/follicle       |SAMPLE_ID            |
  |subject/Donor         |PATIENT_ID           |
  |-                     |TISSUE_TYPE	       |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 4 - "List of all mutations detected in all 2mm2 gridded samples" and Supplementary Table 4 - "List of all mutations detected in hair follicle samples"
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all