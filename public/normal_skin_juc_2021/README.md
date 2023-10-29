# **Information on the Curation of this Study**

## General
* Study: [https://www.sciencedirect.com/science/article/pii/S0923753420431990#appsec1](https://www.sciencedirect.com/science/article/pii/S0923753420431990#appsec1)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Dataset S2 - "Clinical and phenotypic data of donors"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |sampleID		 |PATIENT_ID           |
  |sex                   |SEX                  |
  |age                   |AGE                  |
  |UV_exposure_tissue    |UV_EXPOSURE_SAMPLE   |
  |sun_damage_tissue	 |SUN_DAMAGES_SAMPLE   |
  |sun_history		 |SUN_EXPOSURE     |
  |skin_phototype	 |FITZPATRICK_SCORE    |
 
* Sample data was retrieved from Supplementary Dataset S2 - "Clinical and phenotypic data of donors"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |sampleID              |SAMPLE_ID            |
  |sampleID              |PATIENT_ID           |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Dataset S1 - "List of all somatic mutations included in the final list" 
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all