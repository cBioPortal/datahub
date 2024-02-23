# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-020-2785-8#Sec31](https://www.nature.com/articles/s41586-020-2785-8#Sec31)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "A summary of all clones included in this study, including anatomic origins, cell count and identity, and targeted-, exome-, and RNA-sequencing data metrics."
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Donor		 |PATIENT_ID           |
  |Donor                 |SEX                  |
  |Donor                 |AGE                  |
  |Anatomic Site	 |MELANOMA_IS          |
  |Anatomic Site	 |BCC_IS	       |
 
* Sample data was retrieved from Supplementary Table 1 - "A summary of all clones included in this study, including anatomic origins, cell count and identity, and targeted-, exome-, and RNA-sequencing data metrics."
* For samples that underwent targeted and whole exome sequencing, only exome sequencing data was included
* Further, engineered samples, bulk samples and samples that only underwent RNA-sequencing were excluded
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |ID                    |SAMPLE_ID            |
  |Donor                 |PATIENT_ID           |
  |Cell Identity         |TISSUE_TYPE          |
  |Anatomic Site         |SAMPLE_SITE	       |
  |Anatomic Site         |ADJ_BCC	       |
  |Anatomic Site         |ADJ_MIS	       |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 3 - "All validated and inferred somatic mutations identified in normal melanocytes; includes Oncotator annotations and validation inferences based upon haplotyping and expression data."
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all