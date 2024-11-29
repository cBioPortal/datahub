# NCI-CRDC Datahub

The [Cancer Research Data Commons (CRDC)](https://datacommons.cancer.gov/) is an initiative by the National Cancer Institute (NCI) that provides access to multiple cancer data sources from the federal government. Data sources include:

- [Genomic Data Commons (GDC)](https://gdc.cancer.gov/)

This directory contains NCI-CRDC studies generated using the [ISB-CGC portal](https://bq-search.isb-cgc.org/search?status=current). Data is pulled from the ISB-CGC BigQuery tables once every 3 months and reflects the latest data available for each study. More details about methods and data transformations can be found in the README files for each individual study.

## GDC Program Overview

Supported programs:

- [TCGA](https://www.cancer.gov/ccg/research/genome-sequencing/tcga)
- [CPTAC](https://gdc.cancer.gov/about-gdc/contributed-genomic-data-cancer-research/clinical-proteomic-tumor-analysis-consortium-cptac)
- [TARGET](https://www.cancer.gov/ccg/research/genome-sequencing/target)

### TCGA

- **Cancer type mapping:** Each study corresponds to one TCGA project. The suffix of the TCGA project is taken and converted to an OncoTree code, which is used for the name of the study.
    - **Example:** For the TCGA project `TCGA-LAML`, the `LAML` suffix is taken and converted to the Oncotree code `AML`. The resulting cBioPortal study is `aml_tcga_gdc`.
    - [Mapping file](https://github.com/cBioPortal/nci-crdc-pipeline/blob/main/resources/oncotree_mappings/tcga.txt)

#### List of TCGA cBioPortal Studies

- [`acc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=acc_tcga_gdc): TCGA-ACC, [Adenocortical Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-ACC)
- [`aml_tcga_gdc`](https://www.cbioportal.org/study/summary?id=aml_tcga_gdc): TCGA-LAML, [Acute Myeloid Leukemia](https://portal.gdc.cancer.gov/projects/TCGA-LAML)
- [`blca_tcga_gdc`](https://www.cbioportal.org/study/summary?id=blca_tcga_gdc): TCGA-BLCA, [Bladder Urothelial Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-BLCA)
- [`brca_tcga_gdc`](https://www.cbioportal.org/study/summary?id=brca_tcga_gdc): TCGA-BRCA, [Breast Invasive Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-BRCA)
- [`ccrcc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=ccrcc_tcga_gdc): TCGA-KIRC, [Kidney Renal Clear Cell Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-KIRC)
- [`cesc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=cesc_tcga_gdc): TCGA-CESC, [Cervical Squamous Cell Carcinoma and Endocervical Adenocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-CESC)
- [`chol_tcga_gdc`](https://www.cbioportal.org/study/summary?id=chol_tcga_gdc): TCGA-CHOL, [Cholangiocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-CHOL)
- [`chrcc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=chrcc_tcga_gdc): TCGA-KICH, [Kidney Chromophobe](https://portal.gdc.cancer.gov/projects/TCGA-KICH)
- [`coad_tcga_gdc`](https://www.cbioportal.org/study/summary?id=coad_tcga_gdc): TCGA-COAD, [Colon Adenocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-COAD)
- [`difg_tcga_gdc`](https://www.cbioportal.org/study/summary?id=difg_tcga_gdc): TCGA-LGG, [Brain Lower Grade Glioma](https://portal.gdc.cancer.gov/projects/TCGA-LGG)
- [`dlbclnos_tcga_gdc`](https://www.cbioportal.org/study/summary?id=dlbclnos_tcga_gdc): TCGA-DLBC, [Lymphoid Neoplasm Diffuse Large B-cell Lymphoma](https://portal.gdc.cancer.gov/projects/TCGA-DLBC)
- [`esca_tcga_gdc`](https://www.cbioportal.org/study/summary?id=esca_tcga_gdc): TCGA-ESCA, [Esophageal Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-ESCA)
- [`gbm_tcga_gdc`](https://www.cbioportal.org/study/summary?id=gbm_tcga_gdc): TCGA-GBM, [Glioblastoma Multiforme](https://portal.gdc.cancer.gov/projects/TCGA-GBM)
- [`hcc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=hcc_tcga_gdc): TCGA-LIHC, [Liver Hepatocellular Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-LIHC)
- [`hgsoc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=hgsoc_tcga_gdc): TCGA-OV, [Ovarian Serous Cystadenocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-OV)
- [`hnsc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=hnsc_tcga_gdc): TCGA-HNSC, [Head and Neck Squamous Cell Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-HNSC)
- [`luad_tcga_gdc`](https://www.cbioportal.org/study/summary?id=luad_tcga_gdc): TCGA-LUAD, [Lung Adenocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-LUAD)
- [`lusc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=lusc_tcga_gdc): TCGA-LUSC, [Lung Squamous Cell Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-LUSC)
- [`mnet_tcga_gdc`](https://www.cbioportal.org/study/summary?id=mnet_tcga_gdc): TCGA-PCPG, [Pheochromocytoma and Paraganglioma](https://portal.gdc.cancer.gov/projects/TCGA-PCPG)
- [`nsgct_tcga_gdc`](https://www.cbioportal.org/study/summary?id=nsgct_tcga_gdc): TCGA-TGCT, [Testicular Germ Cell Tumors](https://portal.gdc.cancer.gov/projects/TCGA-TGCT)
- [`paad_tcga_gdc`](https://www.cbioportal.org/study/summary?id=paad_tcga_gdc): TCGA-PAAD, [Pancreatic Adenocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-PAAD)
- [`plmeso_tcga_gdc`](https://www.cbioportal.org/study/summary?id=plmeso_tcga_gdc): TCGA-MESO, [Mesothelioma](https://portal.gdc.cancer.gov/projects/TCGA-MESO)
- [`prad_tcga_gdc`](https://www.cbioportal.org/study/summary?id=prad_tcga_gdc): TCGA-PRAD, [Prostate Adenocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-PRAD)
- [`prcc_tcga_gdc`](https://www.cbioportal.org/study/summary?id=prcc_tcga_gdc): TCGA-KIRP, [Kidney Renal Papillary Cell Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-KIRP)
- [`read_tcga_gdc`](https://www.cbioportal.org/study/summary?id=read_tcga_gdc): TCGA-READ, [Rectum Adenocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-READ)
- [`skcm_tcga_gdc`](https://www.cbioportal.org/study/summary?id=skcm_tcga_gdc): TCGA-SKCM, [Skin Cutaneous Melanoma](https://portal.gdc.cancer.gov/projects/TCGA-SKCM)
- [`soft_tissue_tcga_gdc`](https://www.cbioportal.org/study/summary?id=soft_tissue_tcga_gdc): TCGA-SARC, [Sarcoma](https://portal.gdc.cancer.gov/projects/TCGA-SARC)
- [`stad_tcga_gdc`](https://www.cbioportal.org/study/summary?id=stad_tcga_gdc): TCGA-STAD, [Stomach Adenocarcinoma](https://portal.gdc.cancer.gov/projects/TCGA-STAD)
- [`thpa_tcga_gdc`](https://www.cbioportal.org/study/summary?id=thpa_tcga_gdc): TCGA-THCA, [Thyroid Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-THCA)
- [`thym_tcga_gdc`](https://www.cbioportal.org/study/summary?id=thym_tcga_gdc): TCGA-THYM, [Thymoma](https://portal.gdc.cancer.gov/projects/TCGA-THYM)
- [`ucec_tcga_gdc`](https://www.cbioportal.org/study/summary?id=ucec_tcga_gdc): TCGA-UCEC, [Uterine Corpus Endometrial Carcinoma](https://portal.gdc.cancer.gov/projects/TCGA-UCEC)
- [`ucs_tcga_gdc`](https://www.cbioportal.org/study/summary?id=ucs_tcga_gdc): TCGA-UCS, [Uterine Carcinosarcoma](https://portal.gdc.cancer.gov/projects/TCGA-UCS)
- [`um_tcga_gdc`](https://www.cbioportal.org/study/summary?id=um_tcga_gdc): TCGA-UVM, [Uveal Melanoma](https://portal.gdc.cancer.gov/projects/TCGA-UVM)

### CPTAC

- **Cancer type mapping:** CPTAC is comprised of the CPTAC-2 and CPTAC-3 projects, both of which encompass multiple cancer types. Each study corresponds to a subset of these projects with a particular OncoTree code. The code is determined by looking at `disease_type` and `primary_site` in the BigQuery tables.
    - **Example:** The `luad_cptac` study is generated from all samples with primary site `Bronchus and lung` and disease type `Adenomas and Adenocarcinomas`.
    - [Mapping file](https://github.com/cBioPortal/nci-crdc-pipeline/blob/main/resources/oncotree_mappings/cptac.txt)

#### List of CPTAC cBioPortal Studies

- [`brain_cptac_gdc`](https://www.cbioportal.org/study/summary?id=brain_cptac_gdc): [CNS/Brain Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22brain%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`breast_cptac_gdc`](https://www.cbioportal.org/study/summary?id=breast_cptac_gdc): [Breast Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22breast%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`coad_cptac_gdc`](https://www.cbioportal.org/study/summary?id=coad_cptac_gdc): [Colon Adenocarcinoma](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22colon%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`luad_cptac_gdc`](https://www.cbioportal.org/study/summary?id=luad_cptac_gdc): [Lung Adenocarcinoma](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A%5B%22adenomas%20and%20adenocarcinomas%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22bronchus%20and%20lung%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`lusc_cptac_gdc`](https://www.cbioportal.org/study/summary?id=lusc_cptac_gdc): [Lung Squamous Cell Carcinoma](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A%5B%22squamous%20cell%20neoplasms%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22bronchus%20and%20lung%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`ohnca_cptac_gdc`](https://www.cbioportal.org/study/summary?id=ohnca_cptac_gdc): [Head and Neck Carcinoma, Other](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22other%20and%20ill-defined%20sites%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`ovary_cptac_gdc`](https://www.cbioportal.org/study/summary?id=ovary_cptac_gdc): [Ovarian Cancer](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22other%20and%20unspecified%20female%20genital%20organs%22%2C%22ovary%22%2C%22rectum%22%2C%22retroperitoneum%20and%20peritoneum%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`pancreas_cptac_gdc`](https://www.cbioportal.org/study/summary?id=pancreas_cptac_gdc): [Pancreatic Cancer](https://portal.gdc.cancer.gov/repository?facetTab=files&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22pancreas%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`rcc_cptac_gdc`](https://www.cbioportal.org/study/summary?id=rcc_cptac_gdc): [Renal Cell Carcinoma](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A%5B%22Adenomas%20and%20Adenocarcinomas%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22Kidney%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)
- [`uec_cptac_gdc`](https://www.cbioportal.org/study/summary?id=uec_cptac_gdc): [Uterine Endometrioid Carcinoma](https://portal.gdc.cancer.gov/repository?facetTab=cases&filters=%7B%22op%22%3A%22and%22%2C%22content%22%3A%5B%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.disease_type%22%2C%22value%22%3A%5B%22Adenomas%20and%20Adenocarcinomas%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22Uterus%2C%20NOS%22%5D%7D%7D%2C%7B%22op%22%3A%22in%22%2C%22content%22%3A%7B%22field%22%3A%22cases.project.program.name%22%2C%22value%22%3A%5B%22CPTAC%22%5D%7D%7D%5D%7D)

### TARGET

- **Cancer type mapping:** Each study corresponds to one or more TARGET projects. The TARGET project suffix is converted to an OncoTree code, which is used for the name of the study.
    - **Example:** For the TARGET project `TARGET-ALL-P2`, the `ALL-P2` suffix is taken and converted to the Oncotree code `BLL`. The resulting cBioPortal study is `bll_target_gdc`.
    - [Mapping file](https://github.com/cBioPortal/nci-crdc-pipeline/blob/main/resources/oncotree_mappings/target.txt)

#### List of TARGET cBioPortal Studies

- [`bll_target_gdc`](https://www.cbioportal.org/study/summary?id=bll_target_gdc): TARGET-ALL-P2, [Acute Lymphoblastic Leukemia - Phase II](https://portal.gdc.cancer.gov/projects/TARGET-ALL-P2)
- [`alal_target_gdc`](https://www.cbioportal.org/study/summary?id=alal_target_gdc): TARGET-ALL-P3, [Acute Lymphoblastic Leukemia - Phase III](https://portal.gdc.cancer.gov/projects/TARGET-ALL-P3)
- [`aml_target_gdc`](https://www.cbioportal.org/study/summary?id=aml_target_gdc): TARGET-AML, [Acute Myeloid Leukemia](https://portal.gdc.cancer.gov/projects/TARGET-AML)
- [`nbl_target_gdc`](https://www.cbioportal.org/study/summary?id=nbl_target_gdc): TARGET-NBL, [Neuroblastoma](https://portal.gdc.cancer.gov/projects/TARGET-NBL)
- [`os_target_gdc`](https://www.cbioportal.org/study/summary?id=os_target_gdc): TARGET-OS, [Osteosarcoma](https://portal.gdc.cancer.gov/projects/TARGET-OS)
- [`wt_target_gdc`](https://www.cbioportal.org/study/summary?id=wt_target_gdc): TARGET-WT, [Wilms' Tumor](https://portal.gdc.cancer.gov/projects/TARGET-WT)
