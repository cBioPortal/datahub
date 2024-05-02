Curation and transformation of dataset: 

General Information
Data source: Raw data files from author, supplementary files (for clinical data)
Reference publication: PubMed reference
Reference genome: GRCh38


Sample size selection
* The study cohort only displays ATC and co-occurring DTC cohort (190 samples). 

Sample breakdown:

--|--
| | ATC | co-occurring DTC |
| WES | 132| 19 |
| WGS | 9| 9 |
| Only CNA | 15 | 5 |
|+ 1 metastasis ATC sample|

Clinical Data
* Clinical data retrieved from author's files 
* Additional clinical attributes added from supplementary files 

Mutation Data
* Mutation data retrieved from author's files 
* The variants were annotated using Genome Nexus.

CNA Data
*CNA data retrieved from author's files 

Clinical Data remapping 
--|--
| Source | TISSUE_SOURCE | Sample |
| Type | TISSUE_TYPE | Sample |
| Patient Status | OS_STATUS | Patient |
| Survival Time | OS_MONTHS | Patient |
| Tumour Stage | TUMOR_STAGE | Sample |
| Age| AGE_CATEGORY | Patient |
| Nodal Metastases | NODAL_METASTASIS | Patient |
| Distant Metastasis | DISTANT_METASTASIS | Patient |
| Leukocytosis | LEUKOCYTOSIS | Patient |
| Surgery | SURGERY | Patient |
| Radiotherapy | RADIPOTHERAPY | Patient |
| Chemotherapy | CHEMOTHERAPY | Patient |
| Tumour Purity | TUMOR_PURITY | Sample |
|Cellularity| TUMOR_CELLULARITY | Sample |
| Average_Ploidy | TUMOR_PLOIDY | Sample |

*RNA-seq data pending from author.*
(Author's shared files are available in the cBioPortal Data Curation Drive -> Raw Data from authors (public studies) )