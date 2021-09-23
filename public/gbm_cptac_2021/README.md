# Data transformation of gbm_cptac_2021

## The data
Article: Liang-Bo Wang  et al. 2021 Cell. 

https://www.cell.com/cancer-cell/fulltext/S1535-6108(21)00050-7

Data was downloaded from the supplementary files:
- Table S1 (`mmc2.xlsx`): clinical data
- Table S2 (`mmc3.xlsx`): somatic mutation data, CNA gistic, expression mRNA, cRNA, miRNA, protein data, phosphoproteome,
acetylome, lipidome, metabolome.

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
  [Lift Genome](https://genome.ucsc.edu/cgi-bin/hgLiftOver). This affected the
  columns `NCBI_Build`, `Start_Position` and `End_Position`. The rows for which there
  was no match for hg19 coordinates were removed (78 out of 6757 rows).
- Some mutations have multiple amino acid correspondences (e.g. `p.xxx; p.yyy`).
  We moved each one to a different row.
- The original sample names (column `Tumor_Sample_Barcode`)
  did not match exactly the clinical samples. We simply removed the
  suffix `*_T`.

**CNA data**

- The data for Discrete Copy Number Variation was directly read from
the supplementary table S2, sheet `somatic_cnv_gene_gistic`.
- The Entrez gene id was obtained from Hugo symbol using Biomart.
- We found no information that would allow us to infer the continuous copy number variation data.

**Expression data**

_mRNA_

- The FPKM-UQ values of mRNA expression.
  were directly inferred from the table S2, sheet `gene_expression_fpkm_uq`.
- Gene symbols were inferred from Ensembl Biomart using the Ensembl codes.
- The z-scores were calculated from all tumor samples in the study.


_cRNA_

- Circular RNA expression in FPKM-UQ was directly inferred from the table S2, sheet `circular_rna_fpkm_uq`.
- Transformed as generic assay.
- ENTITY_STABLE_ID was simply the Hugo symbol.
- Other added column was the cRNA_ID.

_miRNA_

- miRNA expression in TPM was read from the table S2, sheet `mirna_mature_tpm`.
- As for mutation data, the coordinates were transformed from hg38 to hg19.
- Transformed as generic assay.
- ENTITY_STABLE_ID was simply the unique id.
- Other added columns were START_POSITION and END_POSITION of the mutation sites.

**Protein data**

- The log2 normalized values were directly inferred from the table S2,
  sheet `proteome_normalized`.
- The z-scores were calculated from all tumor samples in the study.

**Other assays**

_Phosphoprotein_

- Phosphoprotein log2 peptide level quantification read from the sheet
  `phosphoproteome_normalized`.
- Transformed as generic assay.
- ENTITY_STABLE_ID was simply the Hugo symbol.
- Other added columns were PHOSPHOSITES and PEPTIDE: 
  detailed modification sites information.

_Acetylome_

- Acetylprotein log2 peptide level quantification read from the sheet `acetylome_normalized`
- Transformed as generic assay.
- ENTITY_STABLE_ID was simply the Hugo symbol.
- Other added columns were ACETYLSITES and PEPTIDE:
  detailed modification sites information.

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