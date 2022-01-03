# Data transformation of lusc_cptac_2021

## The data
Article:
Shankha Satpathy et al. 2021 Cell.

https://www.cell.com/cell/fulltext/S0092-8674(21)00857-6

Data were retrieved from Supplementary Tables S1, S2 and S3, and [LinkedOmics](http://www.linkedomics.org/data_download/CPTAC-LSCC/).

### Metadata

- Clinical data was inferred from the supplementary table S1, sheet `Table S1B`.
  Manual distinction was made on patient and sample attributes.
- Data contained 1 tumor sample per patient.

### Mutation data

- Data from supplementary table S2, sheet `Table S2I`: Somatic mutation in MAF format, in HG38.
- The original data contains chromosome values of 0 and float numbers. Those rows did not follow the table format and were removed (24 out of 35529).
- We ran maf2maf (64 rows lost).
- The original coordinates (in GRCh38) were transformed to GRCh37 (hg19)
  using [Lift Genome](https://genome.ucsc.edu/cgi-bin/hgLiftOver).
This affected the columns NCBI_Build, Start_Position and End_Position. 
The rows for which there was no match for hg19 coordinates were removed (23 out of 35465).
- The name of the samples was edited to match with the metadata: 
removed `CPTAC3-LSCC` prefix and `-T` suffix.

[comment]: <> (### CNA data)

[comment]: <> (- Data from table S2, sheet `Table S2B`: Gene level copy number data, log-ratio.)

[comment]: <> (- The values for continuous CNA data were directly read from the file.)

[comment]: <> (- One row with an empty Hugo Symbol was removed.)

[comment]: <> (- The Entrez Gene ID was obtained from the respective Hugo symbols using Biomart.)

[comment]: <> (- The discrete CNA data were derived from the continuous files, with thresholds as follows: &#40;-inf, -1&#41;: -2, \[-1, -0.1&#41;: -1, \[-0.1, 0.1\]: 0, &#40;0.1, 1\]: 1, &#40;1, inf&#41;: 2.)

### Expression data
_mRNA_

- Data from table S2, sheet `Table S2E`: RNA-seq Log2-transformed upper-quartile (UQ)-normalized FPKM values, median-centered by gene.
- The expression values were directly read from this data.
- The Entrez Gene IDs were derived from the Hugo symbols using Biomart.
- The columns that corresponded normal samples were removed (94)
- The z-scores were calculated using all samples as the reference population. 
For the computation, the zeroes were excluded and the values were log-transformed.

_miRNA_

- Data from table S2, sheet `Table S2G`: miRNA data TPM values, median-centered by gene.
- The columns that corresponded normal samples were removed (94)
- The z-scores were calculated using all diploid samples as the reference population. For the computation, the zeroes were excluded and the values were log-transformed.

_cRNA_

- Data from LinkedOmics, table containing tumor samples: Circular RNA expression RSEM, upper quantile normalized and log2 transformed
- Transformed as generic assay. Other added columns were derived from the "id" column: ENTITY_STABLE_ID (chr_start_end_HugoSymbol),
    NAME (chr_start_end) and GENE_SYMBOL (Hugo symbol).

### Methylation data

- Data from table S2, sheet `Table S2H`: Gene level methylation beta values.
- The Entrez Gene IDs were derived from the Hugo symbols using Biomart.
- The columns that corresponded normal samples were removed (91)

### Protein data

- Data from table S3, sheet `Table S3C`: Global proteome, aggregated to gene-level and log-transformed.
- The columns that corresponded normal samples were removed (99)
- The z-scores were calculated using all diploid samples as the reference population.

### Phosphoproteomics data

- Data from table S3, sheet `Table S3F`: Phosphoproteome, aggregated to gene-level and log-transformed.

- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID (derived from Hugo symbol)
  NAME (phosphorylation sites) and GENE_SYMBOL (Hugo symbol).

### Acetylproteomics data

- Data from table S2, sheet `Table S3I`: Acetylproteome, aggregated to gene-level and log-transformed.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID (derived from Hugo symbol)
  NAME (acetylation sites) and GENE_SYMBOL (Hugo symbol).

### Ubiquitylproteomics data

- Data from table S3, sheet `Table S3M`: Ubiquitylome, aggregated to gene-level.
- Transformed as generic assay. Other added columns were ENTITY_STABLE_ID (derived from Hugo symbol)
  NAME (ubiquitylation sites) and GENE_SYMBOL (Hugo symbol).







