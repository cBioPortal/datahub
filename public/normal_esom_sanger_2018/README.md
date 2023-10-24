# **Information on the Curation of this Study**

## General
* Study: [https://www.science.org/doi/10.1126/science.aau3879](https://www.science.org/doi/10.1126/science.aau3879)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "List of donors and metadata"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |PD			 |PATIENT_ID           |
  |M/F                   |SEX                  |
  |Age                   |AGE                  |
  |Ethnicity             |ETHNICITY            |
  |cohort                |SMOKING_PACKYEARS    |
  |Diabetes		 |DIABETES_FH          |
  |Cancer history	 |CANCER_HISTORY       |
 
* Sample data was retrieved from Supplementary Table 2 - "Table of coding mutations found in the 844 samples"
 
## Mutation Data
* Mutation data was retrieved from Supplementary Table 2 - "Table of coding mutations found in the 844 samples"
* Mutations with mut == "INS" were excluded because the mutant nucleotides are not provided
* Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all