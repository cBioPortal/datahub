# Data transformation of brca_broad_2020

Article: Krug et al. 2020 Cell. https://www.cell.com/cell/fulltext/S0092-8674(20)31400-8

Data was downloaded from the supplementary files:
- Table S1: Metadata and mutation data
- Table S2: Proteome data, phosphoproteome data, acetylproteome data, mRNA expression data, CNA data


## Notes on data transformation

Metadata
- Clinical data was directly inferred from the Excel sheet. Manual distinction as made on patient/sample attributes.
- Data contained 1 sample per patient

Mutation data

- The MAF was filtered according to the following algorithm (based on https://doi.org/10.1016/j.ccell.2020.10.015): 
remove mutation if VAF (t_alt_count / (t_ref_count + t_alt_count)) <= 0.65 and AF in any population annotation (1000 genomes, etc.) > .001
In addition, it was checked against germline calls, removing one additional call that was likely missed because the hg19 annotation data source used is somewhat out of date. In total 655 mutations out of 29,673 were filtered out that way.

Protein data
- Gene symbols were inferred from Ensembl Biomart from the Refseq Protein IDs
- For duplicate genes, rows were collapsed and the average values were used
- Z-scores were calculated from all tumor samples in the study

Phosphoproteome and acetylproteome data
- Transformed to GENERIC_ASSAY since only a single protein quantification profile is allowed
- gene symbols were inferred from Ensembl Biomart from the Refseq Protein IDs
- ENTITY_STABLE_ID constructed in the form <gene_symbol>_<mod_sites>
  - in case of duplicate entries, a suffix of "__n_" was added to the ID.
- Column is added (PHOSPHOSITES/ACETYLSITES) to indicate detailed modification sites information
  - From the documention in supplementary table S2:
  >Unique identifier for each phosphosite (VM, variable modification) with RefseqProteinID_sites_#sitesPresent_#sitesLocalized_firstSite_lastSite. The numbers in sites, firstSite, lastSite indicate the amino acid position in the protein sequence of accession_number. The N-terminal amino acid of the protein is position 1. The purpose of firstSite and lastSite is to provide a range of possibilities when unlocalized sites are present (#sitesLocalized < #sitesPresent).

Expression data
- FPKM values directly inferred from the table
- Z-scores calculated from all tumor samples

CNA data
- Continuous data was inferred from the table
- Discrete CNA calls were delivered by the authors upon request