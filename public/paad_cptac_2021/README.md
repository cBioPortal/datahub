# Data transformation of paad_cptac_2021

## The data
Article: Liwei Cao  et al. 2021 Cell.

https://www.cell.com/cell/fulltext/S0092-8674(21)00997-1

Clinical data were retrieved from Supplementary Table 1. 
Other data 
(somatic mutation data, segment data, CNA gistic, expression, proteomics,
miRNA, circRNA, phosphoproteomics, N-glycoproteomics and gene methylation)
were downloaded from the linked data in 
http://www.linkedomics.org/data_download/CPTAC-PDAC/
for the data sets related to tumor.


# Metadata

- Clinical data was inferred from the supplementary table S1.
  Manual distinction was made on patient and sample attributes.
- Data contained 1 sample per patient

# Mutation data

- From file `Mutation_results.maf.txt`: somatic mutation (maf). 
- We only included the columns that form part of the extended MAF format.
-The original coordinates (in `GRCh38`) were transformed to `GRCh37` (hg19) using
  [Lift Genome](https://genome.ucsc.edu/cgi-bin/hgLiftOver). This affected the
  columns `NCBI_Build`, `Start_Position` and `End_Position`. The rows for which there
  was no match for hg19 coordinates were removed (57 out of 6382).
- Some mutations have multiple amino acid correspondences (e.g. `p.xxx; p.yyy`).
  We moved each one to a different row.
  
# CNA data

- From file `SCNA_log2_gene_level.cct.txt`: Gene level copy number data, ratio (gistic2 log2ratio).
- The values for continuous CNA data were directly read from the file.
- The Entrez Gene ID was obtained from the respective Hugo symbols using Biomart.
- The discrete CNA data were derived from the continuous files, 
  with thresholds as follows: 
  (-inf, -1): -2, \[-1, -0.1): -1, \[-0.1, 0.1\]: 0, (0.1, 1\]: 1, (1, inf): 2.

# Expression data

- From file `mRNA_RSEM_UQ_log2_Tumor.cct.txt`: RNAseq data RSEM upper-quartile normalized (Illumina HiSeq platform, Gene-level).
- The expression values were directly read from this data.
- The Entrez Gene IDs were derived from the Hugo symbols using Biomart.
- The coordinates were transformed from hg38 to hg19, the 
  same way as for the mutation data.
- The z-scores were calculated using all diploid samples as the reference population. For the computation, the zeroes were excluded and the values were log-transformed.

# Protein data

- From file `proteomics_gene_level_MD_abundance_tumor.cct.txt`: Proteomics data, median-normalized intensity.
- The protein values were obtained directly from the file.
- The z-scores were calculated using all samples as the reference population.

# miRNA expression

- From file `microRNA_TPM_log2_Tumor.cct.txt`: miRNA expression TPM, log2(+1) transformed.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID, NAME and GENE_SYMBOL (unnamed).

# circRNA expression

- From file `circRNA_RSEM_UQ_log2_Tumor.cct.txt`: circRNA expression RSEM, log2(+1) transformed.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID, NAME and GENE_SYMBOL (unnamed).

# Phosphoproteomics data

- From file `phosphoproteomics_site_level_MD_abundance_tumor.cct.txt`: Phosphoproteomics site level data, median-normalized intensity (site level).
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID (Index), NAME (Index), DESCRIPTION (Peptide) and GENE_SYMBOL (Gene).

# N-glycoproteomics data

- From file `glycoproteomics_Site_level_ratio_tumor.cct.txt`: N-glycoproteomics peptide level data.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID (Modifications), NAME (Modifications) and GENE_SYMBOL (Gene).


# Methylation data

- From file `methylation_betaValue_Tumor.cct.txt`: Gene level methylation data.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID, NAME and GENE_SYMBOL (unnamed).



