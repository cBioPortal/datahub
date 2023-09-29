# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s43587-022-00261-5](https://www.nature.com/articles/s43587-022-00261-5)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Case information analyzed in this study for ploidy analysis."
* only patients labeled as "Unaffected Control" were included in the data upload

* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Case ID		 |PATIENT_ID           |
  |Age (yr)              |AGE                  |
  |Sex                   |SEX                  |
  |Cause of Death/Clinical History|CAUSE_OF_DEATH|
 
* Sample data was retrieved from rom Supplementary Table 3 - "List of sSNV candidates." and Supplementary Table 4 - "Exonic sSNVs in cardiomyocytes."

 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 3 - "List of sSNV candidates." and Supplementary Table 4 - "Exonic sSNVs in cardiomyocytes."
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all