# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41588-022-01296-5#Sec12](https://www.nature.com/articles/s41588-022-01296-5#Sec12)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 6 - "Sample information, including gender, age, cohort, biopsy region, and coeliac condition of the donors."
* Patients and consequently mutation data from two previous studies (Lee-Six and Moore) as well as six patients with coeliac disease and one patient with Lynch Syndrome were excluded.
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |patient		 |PATIENT_ID           |
  |sex                   |SEX                  |
  |age                   |AGE                  |
  |biopsy_region         |SAMPLE_SITE          |
  |chemo_history_before_surgery|CHEMOTHERAPY_HISTORY |
 
* Sample IDs from the provided sample data file did not match the sample IDs from the mutational data files - thus, sample IDs from the mutational data files were used in the sample data file
* Sample data was retrieved from [study's GitHub repository](https://github.com/YichenWang1/small_bowel) following the path data/somatic_mutations/indel and data/somatic_mutations/snp
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |microbiopsy_id        |SAMPLE_ID            |
  |Patient               |PATIENT_ID           |

 
## Mutation Data
  * Mutation data was retrieved from the [study's GitHub repository](https://github.com/YichenWang1/small_bowel) following the path data/somatic_mutations/indel and data/somatic_mutations/snp
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all