# Curation and transformation of Pre-cancer HTAN CRC Vanderbilt Dataset:

## Data collection:
- Data Source: [Data on HTAN Portal](https://data.humantumoratlas.org/publications/vanderbilt_crc_chen_2021?tab=abstract)
- Reference publication: [PubMed Reference](https://pubmed.ncbi.nlm.nih.gov/34910928/)
- Reference genome used: GRCh37 for WXS and GRCh38 for scRNA-seq

## Sample size selection
- Discovery & Validation set samples were used to generate the study (61 polyps). 30 samples were whole exome sequenced. 55 samples went though scRNA-seq exp analysis.
- Two patients (`HTA11_3918 and HTA11_4781`) were not listed in the supplementary clinical tables but were included in the Oncoplot analysis (Figure 1). They have been added to the cohort to match the oncoplot.

## Clinical data
- Patient-Level Data: `Table S1`, `Participants` tab in HTAN Portal
- Sample-Level Data:`Table S1`, `Biospecimens` tab in HTAN Portal

## Mutation data
- The Level 3 Bulk DNA filtered data files were obtained from the Vanderbilt team.
- Variants were annotated using Genome Nexus.

## scRNA-seq data
- The Discovery, Validation set h5ad files for both epithelial and non-epithelial cells were used from [cellxgene](https://cellxgene.cziscience.com/collections/a48f5033-3438-4550-8574-cdff3263fdfd)
	- Files used: `Discovery (DIS) set of human colorectal tumor: Epithelial` && `Validation (Val) set of human colorectal tumor: Epithelial` && `VAL and DIS datasets: Non-Epithelial`
- The absolute and relative cell frequencies in Generic Assay format were calculated
- The pseudo bulk RNA expression counts per sample was calculated from scRNA-seq by averaging the values across the cells. 
- The script to generate the absolute, relative cell freq and pseudo bulk RNA-seq data from h5ad files : https://gist.github.com/rmadupuri/447b5689b256ccc4880aa26fb91b72ff
- The pseudo bulk RNA expression data was log transformed and zscores were calculated.

## Imaging data
- H&E data was available for 26 samples: `H&E` tab
- MxIF images were available for 25 samples: `MxIF` tab. Multiple images were available per sample and as we do not support this, the images were split to multiple tabs for now as MxIF Image 1, 2, 3..