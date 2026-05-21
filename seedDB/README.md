# cBioPortal Seed Database

These files are MySQL database dumps used to seed a new cBioPortal database instance. They include essential data for a fully operational cBioPortal website, such as cancer types, genes, uniprot-mappings, drug information, and network data.

The instructions for building and updating seedDBs can be found [here](#for-developers).

Gene and gene alias tables in seedDB are updated annually.

# Release Notes

## Latest seed database schema 2.14.5

This schema is required for cBioPortal release versions:
- 6.4.0 or higher

For release versions > 6.4.0, there might be a need to migrate to a new database schema. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.14.5**: [SQL file with create table statements](https://github.com/cBioPortal/cbioportal/blob/v6.4.0/src/main/resources/db-scripts/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_hg38_v2.14.5.sql.gz](https://github.com/cBioPortal/datahub/blob/master/seedDB/seed-cbioportal_hg19_hg38_v2.14.5.sql.gz)<br>

Updates to seed database:
- Entrez Gene IDs, gene symbols, and gene aliases have been updated based on the HGNC [Oct 7, 2025 release](https://storage.googleapis.com/public-download-files/hgnc/archive/archive/monthly/tsv/hgnc_complete_set_2025-10-07.txt). The detailed changes are listed [here](https://github.com/cBioPortal/datahub-study-curation-tools/blob/master/gene-table-update/build-input-for-importer/gene-table-release-archives/Gene_Table_v7_HGNC_Oct_07_2025/gene_updates.md).
- Gene Sets have been updated from MSigDB v2025.1.Hs.
- miRNA genes from HGNC is included.
- `cosmic_mutation` table is dropped from the seed.


## Previous seed databases

## Seed database schema 2.13.1 (October 2024 HGNC Version)

This schema is required for cBioPortal release versions:
- 5.3.14 or higher

For release versions > 5.3.14, there might be a need to migrate to a new database schema. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.13.1**: [SQL file with create table statements](https://github.com/cBioPortal/cbioportal/blob/v6.0.20/src/main/resources/db-scripts/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_hg38_v2.13.1.sql.gz](https://github.com/cBioPortal/datahub/blob/master/seedDB/seed-cbioportal_hg19_hg38_v2.13.1.sql.gz)<br>

Updates to seed database:
- Entrez Gene IDs, gene symbols, and gene aliases have been updated based on the HGNC [Oct 1, 2024 release](https://storage.googleapis.com/public-download-files/hgnc/archive/archive/monthly/tsv/hgnc_complete_set_2024-10-01.txt). The detailed changes are listed [here](https://github.com/cBioPortal/datahub-study-curation-tools/blob/master/gene-table-update/build-input-for-importer/gene-table-release-archives/Gene_Table_v6_HGNC_Oct_01_2024/gene-updates.md).
- Gene Sets have been updated from MSigDB v2024.1.Hs.

## Seed database schema 2.13.1 (October 2023 HGNC version)

This schema is required for cBioPortal release versions:
- 5.3.14 or higher

For release versions > 5.3.14, there might be a need to migrate to a new database schema. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.13.1**: [SQL file with create table statements](https://github.com/cBioPortal/cbioportal/blob/v5.3.14/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_hg38_v2.13.1.sql.gz](https://github.com/cBioPortal/datahub/blob/master/seedDB/seedDB_hg19_hg38_archive/seed-cbioportal_hg19_hg38_v2.13.1_Oct_2023.sql.gz)<br>
md5sum d8e328d43089c817dc26e144b2524e8a

Updates to seed database:
- Entrez Gene IDs, gene symbols, and gene aliases have been updated based on the HGNC [Oct 1, 2023 release](http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/archive/monthly/tsv/hgnc_complete_set_2023-10-01.txt). The detailed changes are listed [here](https://github.com/cBioPortal/datahub-study-curation-tools/blob/master/gene-table-update/build-input-for-importer/gene-table-release-archives/Gene_Table_v5_HGNC_Oct_01_2023/gene-updates.md).
- Gene Sets have been updated from MSigDB v2023.2.Hs.

### Seed database schema 2.13.0

From this release onwards, we offer a combined seed database for both hg19 and hg38. To access seed databases from previous versions, please refer to the respective archive folders.

This schema is required for cBioPortal release versions:
- 5.3.0 or higher

For release versions > 5.3.0, there might be a need to migrate to a new database schema. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.13.0**: [SQL file with create table statements](https://github.com/cBioPortal/cbioportal/blob/v5.3.0/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_hg38_v2.13.0.sql.gz](https://github.com/cBioPortal/datahub/blob/master/seedDB/seedDB_hg19_hg38_archive/seed-cbioportal_hg19_hg38_v2.13.0.sql.gz)<br>
md5sum b9e4035a9cc94dc01bbf6f5595842071

Updates to seed database:
- Entrez Gene IDs, gene symbols, and gene aliases have been updated based on the HGNC [April 1, 2023 release](http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/archive/monthly/tsv/hgnc_complete_set_2023-04-01.txt). You can find the detailed changes listed [here](https://github.com/cBioPortal/datahub-study-curation-tools/blob/master/gene-table-update/build-input-for-importer/gene-table-release-archives/Gene_Table_v4_HGNC_Apr_01_2023/gene-updates.md).
- Gene Sets have been updated from MSigDB v2023.1.Hs.


### Seed database schema 2.12.14

This schema is required for cBioPortal release versions:
- 5.0.0 or higher

For release versions > 5.0.0, there might be a need to migrate to a new database schema. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.12.14**: [SQL file with create table statements](https://github.com/cBioPortal/cbioportal/blob/v5.0.0/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_v2.12.14.sql.gz](https://github.com/cBioPortal/datahub/blob/master/seedDB/seedDB_hg19_archive/seed-cbioportal_hg19_v2.12.14.sql.gz)<br>
md5sum 05481d66334b65512aef0364ce282fe6

Updates to seed database:
- Entrez Gene IDs, gene symbols, and gene aliases have been updated based on the HGNC [Oct 1, 2022 release](http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/archive/monthly/tsv/hgnc_complete_set_2022-10-01.txt). The detailed changes are listed [here](https://github.com/cBioPortal/datahub-study-curation-tools/blob/master/gene-table-update/build-input-for-importer/gene-table-release-archives/Gene_Table_v3_HGNC_Oct_01_2022/gene-updates.md).
- Gene Sets have been updated from MSigDB 7.5.1.

### Seed database schema 2.12.12

This schema is required for cBioPortal release versions:
- 3.6.0 or higher

For release versions > 2.0.0, there might be a need to migrate to a new database schema. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.12.12**: [SQL file with create table statements](https://github.com/cBioPortal/cbioportal/blob/v4.0.0/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_v2.12.12.sql.gz](https://github.com/cBioPortal/datahub/blob/master/seedDB/seedDB_hg19_archive/seed-cbioportal_hg19_v2.12.12.sql.gz)<br>
md5sum 7d805d56aebcee85e2a8690e040310dd

Contents of seed database:
- Entrez Gene IDs, gene symbols, and gene aliases have been updated based on the HGNC [Jan 1, 2022 release](http://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/archive/monthly/tsv/hgnc_complete_set_2022-01-01.txt).
- Modifications (supplemental genes, miRNA, and phosphoprotein genes) are implemented using the [script](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/gene-table-update/build-input-for-importer).
- Gene Sets have been updated from [MSigDB 7.5.1](http://www.gsea-msigdb.org/gsea/msigdb/download_file.jsp?filePath=/msigdb/release/7.5.1/msigdb.v7.5.1.entrez.gmt).
- All data files in DATAHUB are updated to reflect the gene entry updates. The script/process is described [here](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/gene-table-update/data-file-migration).

### Seed database schema 2.12.8

This schema is required for cBioPortal release versions:
- 3.6.0 or higher

For release versions > 2.0.0, there might be a need to migrate to a new database schema. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.12.8**: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v3.6.10/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_v2.12.8.sql.gz](https://github.com/cBioPortal/datahub/blob/master/seedDB/seedDB_hg19_archive/seed-cbioportal_hg19_v2.12.8.sql.gz)<br>
md5sum f8d2c65f8d9db795da47ed5cf6f592a9

Contents of seed database:
- Entrez Gene IDs, gene symbols, and gene aliases have been updated based on the HGNC [Feb 20, 2021 release](https://www.genenames.org/download/statistics-and-files/) with small modifications listed below.  
  - To minimize data loss, we have preserved certain gene entries that are not available in the current HGNC in a supplemental file - Complete lists [here](https://github.com/cBioPortal/datahub/blob/gene_update_doc/seedDB/gene-update-list/gene-supp.md)
  - Updated outdated gene entries - Complete list [here](https://github.com/cBioPortal/datahub/blob/gene_update_doc/seedDB/gene-update-list/gene-update.md).
  - Removed duplicate `symbol <> entrez_ID` mapping - Complete list [here](https://github.com/cBioPortal/datahub/blob/gene_update_doc/seedDB/gene-update-list/gene-removed.md)
  - 7 genes dropped from gene panels - Complete list [here](https://github.com/cBioPortal/datahub/blob/gene_update_doc/seedDB/gene-update-list/panel-gene-removed.md) 
  - All data files in DATAHUB are updated to reflect the gene entry updates. The script/process is described [HERE](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/gene-table-update/data-file-migration).
- Gene Sets have been updated from MSigDB 6.1.

### Seed database schema 2.7.3

This schema is required for cBioPortal release versions:
- 2.0.0

For release versions > 2.0.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.7.3**: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v2.0.0/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_v2.7.3.sql.gz](https://github.com/cBioPortal/datahub/raw/master/seedDB/seedDB_hg19_archive/seed-cbioportal_hg19_v2.7.3.sql.gz)<br>
md5sum 85444ce645104dbc00610fc1f15e8c7a

Contents of seed database:
- Entrez Gene IDs, gene symbols, and gene aliases updated in December 2018 from [NCBI](ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz).
- Gene lengths retrieved from [Gencode Release 29 (mapped to GRCh37)](https://www.gencodegenes.org/releases/29lift37.html).
- Pfam graphics fetched in August 2017.
- Gene Sets from MSigDB 6.1.
- Cancer Types from OncoTree (fetched December 2018 from http://oncotree.mskcc.org).

### Seed database schema 2.7.2

This schema is required for cBioPortal release versions:
- 1.18.0

For release versions > 1.18.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.7.2: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.18.0/db-scripts/src/main/resources/cgds.sql)<br>
Seed database: [seed-cbioportal_hg19_v2.7.2.sql.gz](https://github.com/cBioPortal/datahub/raw/9d7b90c53c189b6d2c083d156cea2932cd318c0a/seedDB/seed-cbioportal_hg19_v2.7.2.sql.gz)<br>
md5sum b0a4e11b94d00a7291129c30ee4e0f70

Contents of seed database:
- Entrez Gene IDs, gene symbols, and gene aliases updated in April 2018 from [NCBI](ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz).
- Gene lengths retrieved from [Gencode Release 27 (mapped to GRCh37)](https://www.gencodegenes.org/releases/27lift37.html).
- Pfam graphics fetched in August 2017.
- Gene Sets from MSigDB 6.1.
- Cancer Types from OncoTree (fetched July 2018 from http://oncotree.mskcc.org).

### Seed database schema 2.6.0

This schema is required for cBioPortal release versions:
- 1.12.x
- 1.13.x
- 1.14.0

For release versions > 1.14.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.6.0: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.13.1/db-scripts/src/main/resources/cgds.sql)<br>
Seed database: [seed-cbioportal_hg19_v2.6.0.sql.gz](https://github.com/cBioPortal/datahub/raw/219cf5fc9a553dbc2bfa28a18283087def4a5cf4/seedDB/seed-cbioportal_hg19_v2.6.0.sql.gz)<br>
md5sum aafc9da7b72a29f3978ddca31004b8f5

Contents of seed database:
- Entrez Gene IDs, gene symbols, and gene aliases updated in April 2018 from [NCBI](ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz).
- Gene lengths retrieved from [Gencode Release 27 (mapped to GRCh37)](https://www.gencodegenes.org/releases/27lift37.html).
- Pfam graphics fetched in August 2017.
- Gene Sets from MSigDB 6.1.
- Cancer Types from OncoTree (fetched July 2018 from http://oncotree.mskcc.org)

### Seed database schema 2.4.0

This schema is required for cBioPortal release versions:
- 1.9.0

For release versions > 1.9.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.4.0: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.9.0/db-scripts/src/main/resources/cgds.sql)<br>
Seed database : [seed-cbioportal_hg19_v2.4.0.sql.gz](https://github.com/cBioPortal/datahub/raw/b9662010756188a18051c983b8c445dd033703a9/seedDB/seed-cbioportal_hg19_v2.4.0.sql.gz)<br>
md5sum 1014ed1f9d72103f2b46e5615aacbc2f

cBioPortal 1.9.0 with database schema 2.4.0 removed PDB annotations from the database.

Contents of seed database:
- Entrez Gene IDs, gene symbols, and aliases updated in August 2017 from NCBI.
- Gene lengths retrieved from Gencode Release 26 (mapped to GRCh37).
- Pfam graphics fetched in August 2017.

### Seed database schema 2.3.1

This schema is required for cBioPortal release versions:
- 1.7.1
- 1.7.2
- 1.7.3
- 1.8.0

For release versions > 1.8.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.3.1: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.7.3/db-scripts/src/main/resources/cgds.sql)<br>
Seed database part1 (no PDB tables): [seed-cbioportal_hg19_v2.3.1.sql.gz](https://github.com/cBioPortal/datahub/raw/285f60974a28940fe9a8f16d4e08d83a5ceb0085/seedDB/seed-cbioportal_hg19_v2.3.1.sql.gz)<br>
md5sum 324be3d975d22019ee0c82ce0542bcc3 <br>
Seed database part2 (optional, only PDB tables): [seed-cbioportal_hg19_v2.3.1_only-pdb.sql.gz](https://github.com/cBioPortal/datahub/raw/755548060edd3ce9d90f56369f5498d85ab3de1d/seedDB/seed-cbioportal_hg19_v2.3.1_only-pdb.sql.gz)<br>
md5sum 5774a7947cdf5ef78fd737f1bea688cc

Contents of seed database:
- Entrez Gene Ids, Hugo symbols and aliases updated in August 2017 from NCBI.
- Gene lengths retrieved from Gencode Release 26 (mapped to GRCh37).
- Pfam graphics fetched in August 2017.

### Seed database schema 2.1.0

This schema is required for **older** cBioPortal release versions:
- 1.5.0
- 1.5.1
- 1.5.2

When using this older seed database with a release version > 1.5.2, a migration step to a new database schema is required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.1.0: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.5.1/db-scripts/src/main/resources/cgds.sql)<br>
Seed database part1 (no PDB tables): [seed-cbioportal_hg19_v2.1.0.sql.gz](https://github.com/cBioPortal/datahub/raw/84fd66daf8325ad9721895d1cc503653686de15e/seedDB/seed-cbioportal_hg19_v2.1.0.sql.gz)<br>
md5sum fe4e8502034f72f182733a72b50dbbc8 <br>
Seed database part2 (optional, only PDB tables): [seed-cbioportal_hg19_v2.1.0_only-pdb.sql.gz](https://github.com/cBioPortal/datahub/raw/84fd66daf8325ad9721895d1cc503653686de15e/seedDB/seed-cbioportal_hg19_v2.1.0_only-pdb.sql.gz)<br>
md5sum 5774a7947cdf5ef78fd737f1bea688cc

Contents of seed database:
- Entrez Gene Ids, Hugo symbols and aliases updated in September 2016 from NCBI.
- Gene lengths retrieved from Gencode Release 25 (mapped to GRCh37).
- Pfam graphics fetched in September 2016.


## For Developers
- The process of updating the seed database for Datahub is described [here](Update-Seed-Database.md).
- The process of updating the gene tables in the seed database is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-gene-and-gene_alias-tables.md).
- Local data files needs to be updated as well, information can be found [here](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/gene-table-update/data-file-migration).
