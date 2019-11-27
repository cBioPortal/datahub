# cBioPortal Seed Database for hg38

This directory contains the seed database files for human genome build 38 (hg38/GRCh38).
This seed database was created by loading gene annotations from from [NCBI Gencode](https://www.gencodegenes.org/human/) and gene info from [NCBI FTP](http://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz) using the Java class [ImportGeneData.java](https://github.com/cBioPortal/cbioportal/blob/master/core/src/main/java/org/mskcc/cbio/portal/scripts/ImportGeneData.java). See [docs](https://docs.cbioportal.org/3.-cbioportal-maintenance/updating-gene-and-gene_alias-tables) for more documentation.
A database dump was created following [these docs](https://github.com/cBioPortal/datahub/blob/master/seedDB/Update-Seed-Database.md).

The seed database can be loaded as usual.
