# **Information on the Curation of this Study**

## General
* Study: [https://www.nature.com/articles/s41586-023-06333-9](https://www.nature.com/articles/s41586-023-06333-9)
* Reference genome used: GRCh37
* uploaded data available from original publication

## Clinical Data
* Patient data was retrieved from Supplementary Table 1 - "Characteristics of participants"
* Only patients without a relevant germline mutation were included
* remapped clinical patient data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Participant ID	 |PATIENT_ID           |
  |-                     |SEX                  |
  |Age (y)               |AGE                  |
  |Body mass index       |BMI		       |
  |-			 |SMOKING	       |
  |Smoking (pack-years)  |PACKYEARS            |
  |-	                 |ALCOHOL              |
  |Age at first childbirth (y)|ALCOHOL_G_DAY        |
  |Age at menarche (y)   |MENARCHE_AGE         |
  |Menopausal status *   |MENOPAUSE_STATUS     |
  |Age at menopause (y)  |MEOPAUSE_AGE         |
  |Parity		 |PARITY               |
  |Age at first childbirth (y)|FIRST_BIRTH_AGE      |
  |Menopausal status *   |ADJ_BREAST_CANCER    |
  |pStage ¶              |STAGE   	       |
  |pT ¶		         |TUMOR_PT             |
  |pN ¶		         |TUMOR_PN             |
  |Histology §           |HISTOLOGY            |
  |Histological classifiction ‡‡|HISTOLOGY_CLASS      |
  |ER (%)                |TUMOR_ER             |
  |PR (%)                |TUMOR_PR             |
  |Ki-67 labelling index (%)|TUMOR_KI67           |
  |HER2 (IHC score)      |TUMOR_HER2_IHC       |
  |Surgery	         |CANCER_SURGERY       |
  |Preoperative drug therapy|NEOADJUVANT_CHEMO    |
 
* Sample data was retrieved from Supplementary Table 2 - " Sample information"
* remapped clinical sample data (non-listed original columns were dropped):

  | Original Column Name | Remapped Column Name|
  |----------------------|---------------------|
  |Sample ID	         |SAMPLE_ID            |
  |Participant ID        |PATIENT_ID           |
  |Histology †	         |TISSUE_TYPE	       |
 
## Mutation Data
 * Mutation data was retrieved from the file "Nishimuraorganoid_WGS_mutation_list.txt" of the [study's Zenodo repository] (https://zenodo.org/record/8015913)
 * Only whole genome sequencing data from single-cell derived colonies were included. Other samples lacked required information
 * Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
* Case list all