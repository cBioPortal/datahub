# Curation and transformation of CLCA Dataset:

## General Information
- Data Source: [CLCA data](http://lifeome.net:8080/clca/#/)
- Reference publication: [PubMed Reference](https://pubmed.ncbi.nlm.nih.gov/38355797/)
- Whole Genome Sequencing of 494 Hepatocelluar Carcinoma Cases.
- Reference genome used: GRCh37

## Clinical Data
- Data Source: (http://lifeome.net:8080/clca/#/cases/)
- Patient data and sample data was retrieved from Supplementary Table 1 - (41586_2024_7054_MOESM3_ESM.xlsx).

## Mutational Data
- Mutation data was retrieved from (http://lifeome.net:8080/clca/#/mutations)
- Mutation data was edited into MAF format and annotated using the [Genome Nexus Annotation Pipeline](https://github.com/genome-nexus/genome-nexus-annotation-pipeline)

## Case Lists
Case lists generated:
- cases_all
- cases_sequenced

## RNA Seq TPM Data
- RNA Sequencing TPM data was retrieved from Supplementary Table 2 (41586_2024_7054_MOESM4_ESM.xlsx)
- Z-Scores has been calculated.

# Meta Study
- Whole genome sequencing of 494 chinese Hepatocellular carcinomas and their matched normals. 
- cancer_study_identifier: hcc_clca_2024
- name: Hepatocellular Carcinoma (CLCA, Nature 2024)

To do:

- Waiting for SV data and CNA data as they are not in cbioportal format.
