# Data transformation of gbm_cptac_2021

## The data
Article: Liang-Bo Wang  et al. 2021 Cell. 

https://www.cell.com/cancer-cell/fulltext/S1535-6108(21)00050-7

Data was downloaded from the supplementary files:
- Table S1 (`mmc2.xlsx`): clinical data
- Table S2 (`mmc3.xlsx`): somatic mutation data, CNA gistic, expression mRNA, cRNA, miRNA, protein data, phosphoproteome,
acetylome, lipidome, metabolome and DNA methylation.

## The data transformation

**Metadata**
- Clinical data was inferred from the supplementary table S1. 
  Manual distinction was made on patient and sample attributes.
- Data contained 1 sample per patient.
- Censoring data was not added.

**Mutation data**
- The data was taken from the supplementary table S2, sheet `somatic_mutation`.
- We only included the columns that form part of the extended MAF format.
- The original coordinates (in `GRCh38`) were transformed to `GRCh37` (hg19) using 
  [LiftOver](https://genome.ucsc.edu/cgi-bin/hgLiftOver). This affected the
  columns `NCBI_Build`, `Start_Position` and `End_Position`. The rows for which there
  was no match for hg19 coordinates were removed (78 out of 6757 rows).
- Some mutations have multiple amino acid correspondences (e.g. `p.xxx; p.yyy`).
  We moved each one to a different row.
- The original sample names (column `Tumor_Sample_Barcode`)
  did not match exactly the clinical samples. We simply removed the
  suffix `*_T`.

**CNA data**

__continuous__

- The data for Continuous Copy Number Variation was read from the file `HS_CPTAC_GBM_wgs_somatic_cnv_per_gene` in LinkedOmics
(http://linkedomics.org/data_download/CPTAC-GBM/).
- The Entrez gene id was obtained from Hugo symbol using Biomart.


__discrete__

- The data for Discrete Copy Number Variation was directly read from
the supplementary table S2, sheet `somatic_cnv_gene_gistic`.
- The Entrez gene id was obtained from Hugo symbol using Biomart.
- We found no information that would allow us to infer the continuous copy number variation data.

**Expression data**

_mRNA_

- The FPKM-UQ values of mRNA expression.
  were directly inferred from the table S2, sheet `gene_expression_fpkm_uq`.
- Gene symbols were inferred from Ensembl Biomart using the Ensembl codes.
- The z-scores were calculated using both diploid and all samples as the reference population.
For the computation, the zeroes were excluded and the values were log-transformed.


_cRNA_

- Circular RNA expression in FPKM-UQ was directly inferred from the table S2, sheet `circular_rna_fpkm_uq`.
- Transformed as generic assay.
- ENTITY_STABLE_ID was the cRNA_ID, which includes the Hugo symbol.
- Other added columns were the NAME (cRNA_ID), DESCRIPTION (gene type) and GENE_SYMBOL (Hugo symbol).

_miRNA_

- miRNA expression in TPM was read from the table S2, sheet `mirna_mature_tpm`.
- Transformed as expression data.
- The z-scores were calculated using all diploid samples as the reference population.
  For the computation, the zeroes were excluded, and the values were log-transformed.


**Protein data**

- The log2 normalized values were directly inferred from the table S2,
  sheet `proteome_normalized`.
  The z-scores were calculated using all diploid samples as the reference population.

**Somatic CNV segment data**

- The log2 normalized values were directly inferred from the table S2,
  sheet `somatic_cnv_segment`.
- The original coordinates (in `GRCh38`) were transformed to `GRCh37` 
  (hg19) using the same method as for mutation data.

**Other assays**

_Phosphoprotein_

- Phosphoprotein log2 peptide level quantification read from the sheet
  `phosphoproteome_normalized`.
- Transformed as generic assay.
- ENTITY_STABLE_ID was the site_id (includes protein NCBI id).
- Other added columns were NAME (site_id), DESCRIPTION (phosphosites + peptide) and GENE_SYMBOL (Hugo symbol) of the modified sites.


_Acetylome_

- Acetylprotein log2 peptide level quantification read from the sheet `acetylome_normalized`
- Transformed as generic assay.
- ENTITY_STABLE_ID was the site_id (includes protein NCBI id).
- Other added columns were NAME (site_id), DESCRIPTION (acetylsite + peptide) and GENE_SYMBOL (Hugo symbol) of the modified sites.

_Lipidome_

- Lipidome quantification (log2) read from the sheets
  `lipidome_positive_normalized` and `lipidome_negative_normalized`,
  and saved into two respective data files.
- Transformed as generic assay.
- ENTITY_STABLE_ID was simply the Lipid identifier.

_Metabolome_

- Metabolome quantification (log2) read from the sheet `metabolome_normalized`.
- Transformed as generic assay.
- ENTITY_STABLE_ID was simply the Metabolite identifier.

_DNA Methylation_

- Genome-wide DNA methylation profiling (beta values) from the [CPTAC data portal](https://cptac-data-portal.georgetown.edu/study-summary/S057).
- Transformed as generic assay