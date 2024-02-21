# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-022-05072-7](https://www.nature.com/articles/s41586-022-05072-7)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 2 - "Metadata and number of genomes per cell subset for each individual."
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Donor		 |PATIENT_ID           |
  |Sex                   |SEX                  |
  |Age                   |AGE                  |
  |ClinicalHistory       |MEDICAL_HISTORY      |
 
* Sample data was retrieved from Supplementary Table 3 - "Per genome metadata and mutation burden, mutational signature, and telomere length results."
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |colony                |SAMPLE_ID            |
  |Donor                 |PATIENT_ID           |
  |Tissue                |SAMPLE_SITE          |
  |med_depths            |TISSUE_TYPE	       |
 
## Mutation Data
  * Mutation data was retrieved from the file "som2_indel_SNV_allDF_v2.txt.gz" from the [study's GitHub repository](https://github.com/machadoheather/lymphocyte_somatic_mutation/tree/main)
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all