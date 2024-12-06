# NCI-CRDC Datahub

The [Cancer Research Data Commons (CRDC)](https://datacommons.cancer.gov/) is an initiative by the National Cancer Institute (NCI) that provides access to multiple cancer data sources from the federal government. Data sources include:

- [Genomic Data Commons (GDC)](https://gdc.cancer.gov/)

This directory contains NCI-CRDC studies generated using the [ISB-CGC portal](https://bq-search.isb-cgc.org/search?status=current). Data is pulled from the ISB-CGC BigQuery tables once every 3 months and reflects the latest data available for each study. More details about methods and data transformations can be found in the README files for each individual study.

## GDC Program Overview

Supported programs:

- [TCGA](https://www.cancer.gov/ccg/research/genome-sequencing/tcga)
- [CPTAC](https://gdc.cancer.gov/about-gdc/contributed-genomic-data-cancer-research/clinical-proteomic-tumor-analysis-consortium-cptac)

### TCGA

- **Cancer type mapping:** Each study corresponds to one TCGA project. The suffix of the TCGA project is taken and converted to an OncoTree code, which is used for the name of the study.
    - **Example:** For the TCGA project `TCGA-LAML`, the `LAML` suffix is taken and converted to the OncoTree code `AML`. The resulting cBioPortal study is `aml_tcga_gdc`.
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
    - **Example:** The `luad_cptac3_gdc` study is a subset of CPTAC-3 generated from all samples with primary site `Bronchus and lung` and disease type `Adenomas and Adenocarcinomas`.
    - [Mapping file](https://github.com/cBioPortal/nci-crdc-pipeline/blob/main/resources/oncotree_mappings/cptac.txt)

#### List of CPTAC cBioPortal Studies

- [`brain_cptac3_gdc`](https://www.cbioportal.org/study/summary?id=brain_cptac3_gdc): CNS/Brain Cancer, [CPTAC-3](https://portal.gdc.cancer.gov/projects/CPTAC-3)
- [`breast_cptac2_gdc`](https://www.cbioportal.org/study/summary?id=breast_cptac2_gdc): Breast Cancer, [CPTAC-2](https://portal.gdc.cancer.gov/projects/CPTAC-2)
- [`coad_cptac2_gdc`](https://www.cbioportal.org/study/summary?id=coad_cptac2_gdc): Colon Adenocarcinoma, [CPTAC-2](https://portal.gdc.cancer.gov/projects/CPTAC-2)
- [`luad_cptac3_gdc`](https://www.cbioportal.org/study/summary?id=luad_cptac3_gdc): Lung Adenocarcinoma, [CPTAC-3](https://portal.gdc.cancer.gov/projects/CPTAC-3)
- [`lusc_cptac3_gdc`](https://www.cbioportal.org/study/summary?id=lusc_cptac3_gdc): Lung Squamous Cell Carcinoma, [CPTAC-3](https://portal.gdc.cancer.gov/projects/CPTAC-3)
- [`ohnca_cptac3_gdc`](https://www.cbioportal.org/study/summary?id=ohnca_cptac3_gdc): Head and Neck Carcinoma, Other, [CPTAC-3](https://portal.gdc.cancer.gov/projects/CPTAC-3)
- [`ovary_cptac2_gdc`](https://www.cbioportal.org/study/summary?id=ovary_cptac2_gdc): Ovarian Cancer, [CPTAC-2](https://portal.gdc.cancer.gov/projects/CPTAC-2)
- [`pancreas_cptac3_gdc`](https://www.cbioportal.org/study/summary?id=pancreas_cptac3_gdc): Pancreatic Cancer, [CPTAC-3](https://portal.gdc.cancer.gov/projects/CPTAC-3)
- [`rcc_cptac3_gdc`](https://www.cbioportal.org/study/summary?id=rcc_cptac3_gdc): Renal Cell Carcinoma, [CPTAC-3](https://portal.gdc.cancer.gov/projects/CPTAC-3)
- [`uec_cptac3_gdc`](https://www.cbioportal.org/study/summary?id=uec_cptac3_gdc): Uterine Endometrioid Carcinoma, [CPTAC-3](https://portal.gdc.cancer.gov/projects/CPTAC-3)
