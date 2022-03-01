# Data transformation of luad_cptac_2020

## The data
Article:
Michael A. Gillette et al. 2020 Cell.

https://www.cell.com/cell/fulltext/S0092-8674(20)30744-3


Clinical data were retrieved from Supplementary Tables S1, S2 and S3. 


# Metadata

- Clinical data was inferred from the supplementary table S1, sheet `Annotions_S1A`. Manual distinction was made on patient and sample attributes.
- Data contained 1 tumor sample per patient.

# Mutation data

- Data from table S2, sheet `Table S2B` in MAF format.
- The original coordinates (in GRCh38) were transformed to GRCh37 (hg19)
  using [Lift Genome](https://genome.ucsc.edu/cgi-bin/hgLiftOver). This affected the columns NCBI_Build, Start_Position and End_Position. The rows for which there was no match for 
  hg19 coordinates were removed (382 out of 32250).
- The name of the samples was edited to match with metadata: removed `*_T`, replaced `-` with `.`, and added `X` when necessary.
- Some mutations have multiple amino acid correspondences (e.g. p.xxx; p.yyy). We moved each one to a different row.

# CNA data

- Data from table S2, sheet `Table S2A`: adjusted, log2-transformed gene-level copy number coverage ratios obtained from CNVEX. 
- The values for continuous CNA data were directly read from the file.
- The Entrez Gene ID was obtained from the respective Hugo symbols using Biomart.
- The discrete CNA data were derived from the continuous files, with thresholds as follows: (-inf, -1): -2, \[-1, -0.1): -1, \[-0.1, 0.1\]: 0, (0.1, 1\]: 1, (1, inf): 2.

# Expression data
_mRNA_

- Data from table S2, sheet `Table S2D`: gene-level, upper-quartile normalized counts converted to log2-transformed RPKM values.
- The expression values were directly read from this data.
- The Entrez Gene IDs were derived from the Hugo symbols using Biomart.
- The z-scores were calculated using all samples as the reference population. For the computation, the zeroes were excluded and the values were log-transformed.

_miRNA_

- Data from table S2, sheet `Table S2F`: log2-transformed TPM counts for mature microRNA transcripts.
- The z-scores were calculated using all samples as the reference population. For the computation, the zeroes were excluded and the values were log-transformed.


# Methylation data

- Data from table S2, sheet `Table S2C`: gene-level methylation beta values obtained by averaging beta levels for CpG islands in the promoter and 5' UTR of each gene.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID, NAME and GENE_SYMBOL (all derived from the Hugo Symbol).

# Protein data

- Data from table S3, sheet `Table S3A`: two-component normalized Log2 transformed protein expression.
- The z-scores were calculated using all samples as the reference population.

# Phosphosites data

- Data from table S3, sheet `Table S3B`: two-component normalized Log2 transformed phosphosite.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID (id),
  NAME (accession number), DESCRIPTION (gene description) and GENE_SYMBOL (gene symbol).

# Acetylsites data

- Data from table S3, sheet `Table S3C`: two-component normalized Log2 transformed acetylsite.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID (id),
  NAME (accession number), DESCRIPTION (gene description) and GENE_SYMBOL (gene symbol).









