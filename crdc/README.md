# NCI-CRDC Datahub

The [Cancer Research Data Commons (CRDC)](https://datacommons.cancer.gov/) is an initiative by the National Cancer Institute (NCI) that provides access to multiple cancer data sources from the federal government. Data sources include:

- [Genomic Data Commons (GDC)](https://gdc.cancer.gov/)

This directory contains NCI-CRDC studies generated using the [ISB-CGC portal](https://isb-cgc.appspot.com/). Data is pulled from the ISB-CGC BigQuery tables once every 3 months and reflects the latest data available for each study. More details about methods and data transformations can be found in the README files for each individual study.

## GDC Program Overview

- [TCGA](#tcga)
- [CPTAC](#cptac)
- [TARGET](#target)

### TCGA

- **Cancer type mapping:** Each study corresponds to one TCGA project. The suffix of the TCGA project is taken and converted to an OncoTree code, which is used for the name of the study.
    - **Example:** For the TCGA project `TCGA-LAML`, the `LAML` suffix is taken and converted to the Oncotree code `AML`. The resulting cBioPortal study is `aml_tcga_gdc`.
    - [Mapping file](https://github.com/cBioPortal/nci-crdc-pipeline/blob/main/resources/oncotree_mappings/tcga.txt)

#### List of TCGA cBioPortal Studies

- `acc_tcga_gdc`: [TCGA-ACC](https://portal.gdc.cancer.gov/projects/TCGA-ACC), Adenocortical Carcinoma
- `aml_tcga_gdc`: [TCGA-LAML](https://portal.gdc.cancer.gov/projects/TCGA-LAML), Acute Myeloid Leukemia
- `blca_tcga_gdc`: [TCGA-BLCA](https://portal.gdc.cancer.gov/projects/TCGA-BLCA), Bladder Urothelial Carcinoma
- `brca_tcga_gdc`: [TCGA-BRCA](https://portal.gdc.cancer.gov/projects/TCGA-BRCA), Breast Invasive Carcinoma
- `ccrcc_tcga_gdc`: [TCGA-KIRC](https://portal.gdc.cancer.gov/projects/TCGA-KIRC), Kidney Renal Clear Cell Carcinoma
- `cesc_tcga_gdc`: [TCGA-CESC](https://portal.gdc.cancer.gov/projects/TCGA-CESC), Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma
- `chol_tcga_gdc`: [TCGA-CHOL](https://portal.gdc.cancer.gov/projects/TCGA-CHOL), Cholangiocarcinoma
- `chrcc_tcga_gdc`: [TCGA-KICH](https://portal.gdc.cancer.gov/projects/TCGA-KICH), Kidney Chromophobe
- `coad_tcga_gdc`: [TCGA-COAD](https://portal.gdc.cancer.gov/projects/TCGA-COAD), Colon Adenocarcinoma
- `difg_tcga_gdc`: [TCGA-LGG](https://portal.gdc.cancer.gov/projects/TCGA-LGG), Brain Lower Grade Glioma
- `dlbclnos_tcga_gdc`: [TCGA-DLBC](https://portal.gdc.cancer.gov/projects/TCGA-DLBC), Lymphoid Neoplasm Diffuse Large B-cell Lymphoma
- `esca_tcga_gdc`: [TCGA-ESCA](https://portal.gdc.cancer.gov/projects/TCGA-ESCA), Esophageal Carcinoma
- `gbm_tcga_gdc`: [TCGA-GBM](https://portal.gdc.cancer.gov/projects/TCGA-GBM), Glioblastoma Multiforme
- `hcc_tcga_gdc`: [TCGA-LIHC](https://portal.gdc.cancer.gov/projects/TCGA-LIHC), Liver Hepatocellular Carcinoma
- `hgsoc_tcga_gdc`: [TCGA-OV](https://portal.gdc.cancer.gov/projects/TCGA-OV), Ovarian Serous Cystadenocarcinoma
- `hnsc_tcga_gdc`: [TCGA-HNSC](https://portal.gdc.cancer.gov/projects/TCGA-HNSC), Head and Neck Squamous Cell Carcinoma
- `luad_tcga_gdc`: [TCGA-LUAD](https://portal.gdc.cancer.gov/projects/TCGA-LUAD), Lung Adenocarcinoma
- `lusc_tcga_gdc`: [TCGA-LUSC](https://portal.gdc.cancer.gov/projects/TCGA-LUSC), Lung Squamous Cell Carcinoma
- `mnet_tcga_gdc`: [TCGA-PCPG](https://portal.gdc.cancer.gov/projects/TCGA-PCPG), Pheochromocytoma and Paraganglioma
- `nsgct_tcga_gdc`: [TCGA-TGCT](https://portal.gdc.cancer.gov/projects/TCGA-TGCT), Testicular Germ Cell Tumors
- `paad_tcga_gdc`: [TCGA-PAAD](https://portal.gdc.cancer.gov/projects/TCGA-PAAD), Pancreatic Adenocarcinoma
- `plmeso_tcga_gdc`: [TCGA-MESO](https://portal.gdc.cancer.gov/projects/TCGA-MESO),	Mesothelioma
- `prad_tcga_gdc`: [TCGA-PRAD](https://portal.gdc.cancer.gov/projects/TCGA-PRAD), Prostate Adenocarcinoma
- `prcc_tcga_gdc`: [TCGA-KIRP](https://portal.gdc.cancer.gov/projects/TCGA-KIRP), Kidney Renal Papillary Cell Carcinoma
- `read_tcga_gdc`: [TCGA-READ](https://portal.gdc.cancer.gov/projects/TCGA-READ), Rectum Adenocarcinoma
- `skcm_tcga_gdc`: [TCGA-SKCM](https://portal.gdc.cancer.gov/projects/TCGA-SKCM), Skin Cutaneous Melanoma
- `soft_tissue_tcga_gdc`: [TCGA-SARC](https://portal.gdc.cancer.gov/projects/TCGA-SARC), Sarcoma
- `stad_tcga_gdc`: [TCGA-STAD](https://portal.gdc.cancer.gov/projects/TCGA-STAD), Stomach Adenocarcinoma
- `thpa_tcga_gdc`: [TCGA-THCA](https://portal.gdc.cancer.gov/projects/TCGA-THCA), Thyroid Carcinoma
- `thym_tcga_gdc`: [TCGA-THYM](https://portal.gdc.cancer.gov/projects/TCGA-THYM), Thymoma
- `ucec_tcga_gdc`: [TCGA-UCEC](https://portal.gdc.cancer.gov/projects/TCGA-UCEC), Uterine Corpus Endometrial Carcinoma
- `ucs_tcga_gdc`: [TCGA-UCS](https://portal.gdc.cancer.gov/projects/TCGA-UCS), Uterine Carcinosarcoma
- `um_tcga_gdc`: [TCGA-UVM](https://portal.gdc.cancer.gov/projects/TCGA-UVM), Uveal Melanoma

### CPTAC

- **Cancer type mapping:** CPTAC is comprised of the CPTAC-2 and CPTAC-3 projects, both of which encompass multiple cancer types. Each study corresponds to a subset of these projects with a particular OncoTree code. The code is determined by looking at `disease_type` and `primary_site` in the BigQuery tables.
    - **Example:** The `luad_cptac` study is generated from all samples with primary site `Bronchus and lung` and disease type `Adenomas and Adenocarcinomas`.
    - [Mapping file](https://github.com/cBioPortal/nci-crdc-pipeline/blob/main/resources/oncotree_mappings/cptac.txt))

#### List of CPTAC cBioPortal Studies

- `brain_cptac_gdc`: [Brain Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22brain%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `breast_cptac_gdc`: [Breast Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22breast%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `coad_cptac_gdc`: [Colon Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22colon%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `luad_cptac_gdc`: [Lung Adenocarcinoma](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A%5B%22adenomas%20and%20adenocarcinomas%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22bronchus%20and%20lung%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `lusc_cptac_gdc`: [Lung Squamous Cell Carcinoma](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A%5B%22squamous%20cell%20neoplasms%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22bronchus%20and%20lung%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `ohnca_cptac_gdc`: [Head and Neck Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22other%20and%20ill-defined%20sites%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `ovary_cptac_gdc`: [Ovarian Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22other%20and%20unspecified%20female%20genital%20organs%22%2C%22ovary%22%2C%22rectum%22%2C%22retroperitoneum%20and%20peritoneum%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `pancreas_cptac_gdc`: [Pancreatic Cancer](https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22pancreas%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `rcc_cptac_gdc`: [Renal Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A%5B%22Adenomas%20and%20Adenocarcinomas%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22Kidney%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- `uec_cptac_gdc`: [Endometrial Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A%5B%22Adenomas%20and%20Adenocarcinomas%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22Uterus%2C%20NOS%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)

### TARGET

- **Cancer type mapping:** Each study corresponds to one or more TARGET projects. The name of the project is derived from the OncoTree code defined in the mapping file.
    - **Example:** The `bll_target_gdc` study has OncoTree code `BLL` and is sourced from the GDC projects `TARGET-ALL-P1` and `TARGET-ALL-P2`.
    - [Mapping file](https://github.com/cBioPortal/nci-crdc-pipeline/blob/main/resources/oncotree_mappings/target.txt)

#### List of TARGET cBioPortal Studies

- `alal_target_gdc`: [TARGET-ALL-P3](https://portal.gdc.cancer.gov/projects/TARGET-ALL-P3), Acute Lymphoblastic Leukemia - Phase III
- `aml_target_gdc`: [TARGET-AML](https://portal.gdc.cancer.gov/projects/TARGET-AML), Acute Myeloid Leukemia
- `bll_target_gdc`: [TARGET-ALL-P1](https://portal.gdc.cancer.gov/projects/TARGET-ALL-P1) and [TARGET-ALL-P2](https://portal.gdc.cancer.gov/projects/TARGET-ALL-P2), Acute Lymphoblastic Leukemia - Phases I and II
- `ccsk_target_gdc`: [TARGET-CCSK](https://portal.gdc.cancer.gov/projects/TARGET-CCSK), Clear Cell Sarcoma of the Kidney
- `mrt_target_gdc`: [TARGET-RT](https://portal.gdc.cancer.gov/projects/TARGET-RT), Rhabdoid Tumor
- `nbl_target_gdc`: [TARGET-NBL](https://portal.gdc.cancer.gov/projects/TARGET-NBL), Neuroblastoma
- `os_target_gdc`: [TARGET-OS](https://portal.gdc.cancer.gov/projects/TARGET-OS), Osteosarcoma
- `wt_target_gdc`: [TARGET-WT](https://portal.gdc.cancer.gov/projects/TARGET-WT), High-Risk Wilms Tumor
