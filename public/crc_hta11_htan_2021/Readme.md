# Curation and transformation of Pre-cancer HTAN CRC Vanderbilt Dataset:

## General Information
- Data Source: [Data on HTAN Portal](https://data.humantumoratlas.org/publications/vanderbilt_crc_chen_2021?tab=abstract)
- Reference publication: [PubMed Reference](https://pubmed.ncbi.nlm.nih.gov/34910928/)
- Reference genome used: GRCh37 for WXS and GRCh38 for scRNA-seq

## Sample size selection
- Discovery set samples were used to generate the study (27 polyps)
- We can extend the cohort with Validation set samples in future.

## Clinical data
- Patient-Level Data: `Table S1`, `Participants` tab in HTAN Portal
- Sample-Level Data:`Table S1`, `Biospecimens` tab in HTAN Portal

## Timeline Data
- Sample Collection and Processing days from enrollment date is added to timeline from `Biospecimens` tab.

## Mutation Data
- The Level 3 Bulk DNA files were downloaded from HTAN Portal for each sample.
- The VCF's were converted to MAF format and the variants with the FILTER variable marked as PASS were picked. 
- Variants were annotated using Genome Nexus

## scRNA-seq Data
- The Discovery set h5ad files for both epithelial and non-epithelial cells were used from [cellxgene](https://cellxgene.cziscience.com/collections/a48f5033-3438-4550-8574-cdff3263fdfd)
	- Discovery (DIS) set of human colorectal tumor: Epithelial
	- VAL and DIS datasets: Non-Epithelial
	- The single cell raw count data were normalized by median library size, log-like transformed with Arcsinh, and Z-score standardized per gene
- The absolute and relative cell frequencies in Generic Assay format were calculated
- The pseudo bulk RNA expression counts per sample was calculated from scRNA-seq by averaging the values across the cells. 
- The script to generate the files : https://gist.github.com/rmadupuri/ffcdd2c753e28fd057a9c4bebf0fd9ca
- Zscores were not calculated as the available data was already log-transformed & zscore normalized and the data follows normal distribution.

## Imaging data
- H&E data was available for 25 samples: `H&E` tab
- MxIF images were available for 23 samples: `MxIF` tab