# HTAN MSK Colorectal Cancer Cohort:

## Data collection:
- Data Source: 
	- [Data on HTAN Portal](https://humantumoratlas.org/publications/hta8_2024_nature_a-r-moorman?tab=overview)
	- Reference publication: [PubMed Reference](https://pubmed.ncbi.nlm.nih.gov/39478232/)
	- Reference genome used: GRCh37 (MSK-IMPACT for genomic sequencing)

## Sample size details
- Paper mentions 31 patients were sequenced. The [Supp Table 1b](https://www.nature.com/articles/s41586-024-08150-0#Sec54) shows 29 patients/83 samples used in the Manuscript. These were used for cBioPortal.
- 28 samples from 26 patients went through MSK-IMPACT sequencing.
- All 83 samples went through scRNA-seq
- 58 samples from 28 patients has MxIF imaging data from minerva.

## Clinical data
- Patient-Level Data: `Supp Table 1a`, `Participants` tab in HTAN Portal
- Sample-Level Data: `Biospecimens` tab in HTAN Portal

## Mutation data
- Data obtained from MSK-IMPACT 

## scRNA-seq data
- scRNA data is obtained from https://github.com/dpeerlab/progressive-plasticity-crc-metastasis#data-access
- File used: [All.h5ad: Master table with combined Immune, Epithelial and Stromal Cells](https://dp-lab-data-public.s3.us-east-1.amazonaws.com/progressive-plasticity-crc-metastasis/h5ads/All.h5ad)
- Total Cell count: 164,304 from 83 samples (Immune: 111609, Epithelial: 47437, Stromal: 5258)
- The raw scRNA counts were averaged across cells within each sample (pseudo-bulk), then converted to CPM and log-transformed. 
- See https://gist.github.com/rmadupuri/9d70fa6d9f51f135d6896f23d6c1d803 for the exploration of anndata object and transformation to pseudo-bulk.  

## Imaging data
- MxIF images were available for 58 samples from 28 patients: `MxIF` tab. 
- Multiple aliquots per sample were available, with one designated for scRNA profiling and others for imaging. Although these aliquots have different HTAN sample IDs, the MxIF images from additional aliquots were labeled with the scRNA aliquot ID in cBioPortal.
- For patient HTA8_6001, the sample identifiers are as follows: 
	HTA8_6001_001101 corresponds to single-cell RNA-seq, 
	HTA8_6001_001102 and HTA8_6001_001103 are both MxIF
	The MxIF images from aliquots 1102 and 1103 were linked to ID 1101 in cBio.