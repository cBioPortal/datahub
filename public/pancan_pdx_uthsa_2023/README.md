# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41467-023-43373-1]
* Reference genome used: GRCh38
* The pediatric solid tumor PDX cohort comprised both Patient Tumor (PT) and PDX tumor from 14 Wilms tumors, 13 hepatoblastomas, 12 osteosarcomas, 10 germ cell tumors, and 19 others solid tumors.
* Uploaded data available from original publication and from authors
* Sequencing Platform - Whole Genome and Whole Exome sequencing 


## Clinical Data
* Patient data was retrieved from Supplementary Table S1 - "Summary of clinical and demographic information"
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |PatientID	         |PATIENT_ID           |
  |Gender                |SEX                  |
  |Age                   |AGE                  |
  |Race		             |RACE
  |Ethnicity             |ETHNICITY    |
 
* Patient data was retrieved from Supplementary Table S1 - "Summary of clinical and demographic information"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name           | Remapped Column Name          |
  |------------------------------- |-------------------------------|
  |PatientID                       |SAMPLE_ID                      |
  |Cancer Type                     |CANCER_TYPE                    |
  |Primary/Relapse Sample          |PRIMARY_RELAPSE                |
  |Therapy prior to PDX collection |THERAPY_PRIOR_TO_PDX_COLLECTION|
  |Type of Germline                |TYPE_OF_GERMLINE               |
  |Primary Tumor Site              |PRIMARY_TUMOR_SITE             |
  |Primary Tumor Laterality        |PRIMARY_TUMOR_LATERALITY       |
  |Site of Tumor Collection        |SITE_OF_TUMOR_COLLECTION       |
  |Tumor Collection Laterality     |TUMOR_COLLECTION_LATERALITY    |
  |Procedure Type                  |PROCEDURE_TYPE                 |
  
## Mutation Data
  * Mutation data was retrieved from Data S2 - "Deep sequencing result of 585_PT and 585_PDX".
  * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)
  
## Structural Variants Data
  * Mutation data was retrieved from Supplementary Table S10.
  
## Segment File Data
  * Segment file from [Synapse](https://www.synapse.org/Synapse:syn35811916/files/)

## CNA Data
  * CNA gistic data from [Synapse](https://www.synapse.org/Synapse:syn35811916/files/)  


## Case Lists
Case lists generated:
* cases_all
* cases_sequenced
* cases_sv

## Missing Data:
* Expression Data