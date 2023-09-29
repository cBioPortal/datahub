# **Information on the Curation of this Study**

## General
* Study: [https://www.science.org/doi/10.1126/science.aba7300](https://www.science.org/doi/10.1126/science.aba7300)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Clinicopathological information of 120 UCC patients."
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Patient ID		 |PATIENT_ID           |
  |Gender                |SEX                  |
  |Age                   |AGE                  |
  |Smoking		 |SMOKING	       |
  |Urothelium site	 |SAMPLE_SITE	       |
  |-			 |ADJ_UROTHELIUM_CANCER|
  |Grade		 |ADJ_TUMOR_GRADING    |
  |pT			 |PT_ADJ_TUMOR	       |
 
* Sample data was retrieved from Supplementary Table 4 - "Insertions and deletions (INDELs) detected in tumor and urothelium samples." and Supplementary Table 5 - "Single nucleotide variants (SNVs) detected in urothelium samples."
* Only samples of healthy urothelium were included
* Sample P7C underwent whole genome sequencing, all other samples underwent whole exome sequencing
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Sample                |SAMPLE_ID            |
  |-		         |PATIENT_ID           |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 4 - "Insertions and deletions (INDELs) detected in tumor and urothelium samples." and Supplementary Table 5 - "Single nucleotide variants (SNVs) detected in urothelium samples."
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all