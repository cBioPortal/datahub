# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41588-023-01468-x](https://www.nature.com/articles/s41588-023-01468-x)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Donor demographics"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |donor		 |PATIENT_ID           |
  |Sex                   |SEX                  |
  |Age                   |AGE                  |
  |Site                  |SAMPLE_SITE          |
  |Occupation		 |OCCUPATION_AREA      |
  |Fitzpatrick score	 |FITZPATRICK_SCORE    |
  |Smoker		 |SMOKING	       |
 
* Sample data was retrieved from Supplementary Table 1 - "List of all independent mutations after merging those which span multiple samples"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |samples               |SAMPLE_ID            |
  |donor                 |PATIENT_ID           |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 1 - "List of all independent mutations after merging those which span multiple samples"
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all