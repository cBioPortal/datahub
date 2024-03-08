# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-020-1961-1](https://www.nature.com/articles/s41586-020-1961-1)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Characteristics of subjects"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |ID			 |PATIENT_ID           |
  |Sex                   |SEX                  |
  |Age (year)            |AGE                  |
  |Smoking_status        |SMOKING	       |
  |Site of sampling	 |SAMPLE_SITE	       |
  |Pack-year	         |PACKYEARS	       |
  |Duration of smoking cessation (year)|SMOKING_CESSATION_YEARS|
  |Histology of biopsied area|SAMPLE_HISTOLOGY |
  |Medical history of lung disease (excluding malignancy)|LUNG_HISTORY|
  |Medical history of malignancy +/- systemic treatment|CANCER_HISTORY|
  |Medical history of malignancy +/- systemic treatment|CHEMOTHERAPY_HISTORY |
  |Indication of bronchoscopy|BIOPSY_INDICATION|
 
* Sample data was retrieved from Supplementary Table 2 - "Sequencing summary of bronchial epithelial cells"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Sample	         |SAMPLE_ID            |
  |Patient               |PATIENT_ID           |
  |Type	                 |Tissue_Type          |
 
## Mutation Data
* Mutation data was retrieved from the [study's Mendeley repository] (https://data.mendeley.com/datasets/b53h2kwpyy/2) files "Bronchial epithelium indels.xlsx" and "Bronchial epithelium subs.xlsx"
* Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all