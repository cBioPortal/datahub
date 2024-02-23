# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41588-022-01035-w](https://www.nature.com/articles/s41588-022-01035-w)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Characteristics of subjects"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Subject ID 		 |PATIENT_ID           |
  |Gender                |SEX                  |
  |Age                   |AGE                  |
  |Smoking_status        |SMOKING              |
  |Smoking_pack_year	 |PACKYEARS	       |
  |Quit                  |SMOKING_CESSATION_YEARS|
  |COPD                  |COPD                 |
  |Cancer type           |CANCER_HISTORY       |
  |Cancer stage          |Lung Cancer Stage    |
 
* Sample data was retrieved from Supplementary Table 2 - "Sequencing summary of human proximal bronchial basal cells"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Cell ID               |SAMPLE_ID            |
  |Subject ID            |PATIENT_ID           |
 
## Mutation Data
* Mutation data was retrieved from 
* VCFs file were transferred into minimaf format using the [R Package 'vcfR'](https://cran.r-project.org/web/packages/vcfR/vignettes/intro_to_vcfR.html)
* The Tumor_Sample_Barcode column was added following the file names
* Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all