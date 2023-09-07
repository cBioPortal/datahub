# **Information on the Curation of this Study**

## General
* Study: https://www.science.org/doi/10.1126/science.aba8347
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Table S1. Donor information"
* remapped clinical patient data:

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Donor ID              |PATIENT_ID           |
  |Gender                |SEX                  |
  |Age                   |AGE                  |
  |Tobakko intake        |SMOKING              |
  |Alcohol intake        |ALCOHOL              |
  |BMI (kg/m^2)          |BMI                  |
  |Libraries sequenced Exome|WXS_NORM_SAMPLES  |
  |Libraries sequenced WGS|WGS_NORM_SAMPLES    |
  |-                     |ADJ_UROTHELIUM_CANCER|
  |-                     |UTI_HISTORY          |
  |-                     |CHEMOTHERAPY_HISTORY |

 
* Sample data was retrieved from Supplementary Table 2 - "Table S2. Microbiopsy information"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |microbiopsy_id        |SAMPLE_ID            |
  |-                     |PATIENT_ID           |
  |histological_feature  |SAMPLE_TISSUE        |
  |patient               |PATIENT_ID           |
  |sent_for_exome_seq    |WXS                  |
  |exome_median_coverage |WXS_SEQ_DEPTH        |
  |sent_for_wgs          |WGS                  |
  |wgs_coverage          |WGS_SEQ_DEPTH        |
 
## Mutation Data
  * Mutation data was retrieved from Supplementary Table 4 - "Table S4. Substitution and indel calls from exome data" and Supplementary Table 5 - "Table S5. Substitution and indel calls from genome data"
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all
