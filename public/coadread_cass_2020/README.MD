General Information

Data Source: Paper's supplementary files
Publication PubMed ID: 32888432  
Reference genome used: GRCh37

Clinical Data
* Data displays 146 tumor samples from Chinese colorectal cancer patients 
* Data retrieved from Table S1, Clinicopathoglogic features
* Follow-up time is mentioned to be in days, therefore progression and overall survival time is assumed to be days
* Overall survival in days was converted to months to match cBioPortal file formats.

Clinical Data Remapping 

Original clinical data columns were remapped to new column names for patients and samples, as listed in the table below.

|Original column |Renamed column |Patient/Sample|
-- | -- | --
Atomic site | Tumor Site | Patient |
Atomic site detail | Tumor Site Detailed | Patient |
Stage | Tumor Stage | Patient |
TNM | TNM Stage | Patient |
Met or not Met | Metastatic Status | Sample |
Primary Necorsis | Primary Tumor Necrosis (%) | Sample |
Primary Purity | Primary Tumor Purity (%) | Sample |
Mets Necrosis | Metastatic Tumor Necrosis (%) | Sample |
Mets Purity | Metastatic Tumor Purity (%) | Sample |
Metastatic sites beforein operation | Metastatic Site | Patient |
PreTherapy | Pre-Therapy | Patient |
PreTherapy with targeted agents | Pre-Therapy With Targeted Agents | Patient |
Postoperative therapy with targeted agents | Post-Operative Therapy With Targeted Agents | Patient |
Progression | Split into Tumor Progression & Progression Site columns | Patient |
SurvivalTime | Overall Survival (Months) | Patient |
Survival | Overall Survival Status | Patient |
comment_Paired | Primary Tumor Paired Status | Sample |
LM_43 | Distant Liver Metastatic Tissues | Patient |

Mutation Data 
* Data retrieved from Table S1 3.Somatic mutations, showing somatic single-nucleotide variants (SNVs) and small insertions-deletions (INDELs) identified by WES in the 146 CCRC cohort.
* Variants were annotated using Genome Nexus.


