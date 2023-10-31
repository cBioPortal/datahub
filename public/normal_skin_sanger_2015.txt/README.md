# **Information on the Curation of this Study**

## General
* Study: [https://www.science.org/doi/10.1126/science.aaa6806](https://www.science.org/doi/10.1126/science.aaa6806)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 "Patient Characteristics."
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Patient ID            |PATIENT_ID           |
  |Age (years)           |AGE                  |
  |Gender                |SEX                  |
  |Sun exposure          |SUN_EXPOSURE         |
  |Smoker                |ADJACENT_CANCER      |
 
* Sample data was retrieved from Supplementary Data 1
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Data 1
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all