# cBioPortal Seed Database

These files are MySQL database dump files for seeding a new instance of the cBioPortal database. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, genes, uniprot-mappings, drug and network data.

The database schema and cBioPortal release follows different numbering cycles since cBioPortal 1.5.0 and database schema 2.1.0. This means that the version numbers won't be identical. cBioPortal 1.9.0 with database schema 2.4.0 removed PDB annotations from the database.

## Latest seed database
#### Seed database schema 2.7.3

This schema is required for cBioPortal release versions:
- **2.0.0**

When using a release version **> 2.0.0**, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.7.3**: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v2.0.0/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database**: [seed-cbioportal_hg19_v2.7.3.sql.gz](https://github.com/cBioPortal/datahub/raw/master/seedDB/seed-cbioportal_hg19_v2.7.3.sql.gz)<br>
md5sum 85444ce645104dbc00610fc1f15e8c7a

Contents of seed database:
- Entrez Gene IDs, HGNC symbols and gene aliases updated in December 2018 from [NCBI](ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz)
- Gene lengths retrieved from [Gencode Release 29 (mapped to GRCh37)](https://www.gencodegenes.org/releases/29lift37.html)
- Pfam graphics fetched in August 2017
- Gene Sets from MSigDB 6.1
- Cancer Types from OncoTree (fetched December 2018 from http://oncotree.mskcc.org)

## Previous seed databases
#### Seed database schema 2.7.2

This schema is required for cBioPortal release versions:
- 1.18.0

When using a release version > 1.18.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.7.2: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.18.0/db-scripts/src/main/resources/cgds.sql)<br>
Seed database: [seed-cbioportal_hg19_v2.7.2.sql.gz](https://github.com/cBioPortal/datahub/raw/9d7b90c53c189b6d2c083d156cea2932cd318c0a/seedDB/seed-cbioportal_hg19_v2.7.2.sql.gz)<br>
md5sum b0a4e11b94d00a7291129c30ee4e0f70

Contents of seed database:
- Entrez Gene IDs, HGNC symbols and gene aliases updated in April 2018 from [NCBI](ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz)
- Gene lengths retrieved from [Gencode Release 27 (mapped to GRCh37)](https://www.gencodegenes.org/releases/27lift37.html)
- Pfam graphics fetched in August 2017
- Gene Sets from MSigDB 6.1
- Cancer Types from OncoTree (fetched July 2018 from http://oncotree.mskcc.org)

#### Seed database schema 2.6.0

This schema is required for cBioPortal release versions:
- 1.12.x
- 1.13.x
- 1.14.0

When using a release version > 1.14.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.6.0: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.13.1/db-scripts/src/main/resources/cgds.sql)<br>
Seed database: [seed-cbioportal_hg19_v2.6.0.sql.gz](https://github.com/cBioPortal/datahub/raw/219cf5fc9a553dbc2bfa28a18283087def4a5cf4/seedDB/seed-cbioportal_hg19_v2.6.0.sql.gz)<br>
md5sum aafc9da7b72a29f3978ddca31004b8f5

Contents of seed database:
- Entrez Gene IDs, HGNC symbols and gene aliases updated in April 2018 from [NCBI](ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/Homo_sapiens.gene_info.gz)
- Gene lengths retrieved from [Gencode Release 27 (mapped to GRCh37)](https://www.gencodegenes.org/releases/27lift37.html)
- Pfam graphics fetched in August 2017
- Gene Sets from MSigDB 6.1
- Cancer Types from OncoTree (fetched July 2018 from http://oncotree.mskcc.org)

#### Seed database schema 2.4.0

This schema is required for cBioPortal release versions:
- 1.9.0

When using a release version > 1.9.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.4.0: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.9.0/db-scripts/src/main/resources/cgds.sql)<br>
Seed database : [seed-cbioportal_hg19_v2.4.0.sql.gz](https://github.com/cBioPortal/datahub/raw/b9662010756188a18051c983b8c445dd033703a9/seedDB/seed-cbioportal_hg19_v2.4.0.sql.gz)<br>
md5sum 1014ed1f9d72103f2b46e5615aacbc2f

Contents of seed database:
- Entrez Gene IDs, HGNC symbols and aliases updated in August 2017 from NCBI
- Gene lengths retrieved from Gencode Release 26 (mapped to GRCh37)
- Pfam graphics fetched in August 2017

#### Seed database schema 2.3.1

This schema is required for cBioPortal release versions:
- 1.7.1
- 1.7.2
- 1.7.3
- 1.8.0

When using a release version > 1.8.0, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.3.1: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.7.3/db-scripts/src/main/resources/cgds.sql)<br>
Seed database part1 (no PDB tables): [seed-cbioportal_hg19_v2.3.1.sql.gz](https://github.com/cBioPortal/datahub/raw/285f60974a28940fe9a8f16d4e08d83a5ceb0085/seedDB/seed-cbioportal_hg19_v2.3.1.sql.gz)<br>
md5sum 324be3d975d22019ee0c82ce0542bcc3 <br>
Seed database part2 (optional, only PDB tables): [seed-cbioportal_hg19_v2.3.1_only-pdb.sql.gz](https://github.com/cBioPortal/datahub/raw/755548060edd3ce9d90f56369f5498d85ab3de1d/seedDB/seed-cbioportal_hg19_v2.3.1_only-pdb.sql.gz)<br>
md5sum 5774a7947cdf5ef78fd737f1bea688cc

Contents of seed database:
- Entrez Gene Ids, Hugo symbols and aliases updated in August 2017 from NCBI
- Gene lengths retrieved from Gencode Release 26 (mapped to GRCh37)
- Pfam graphics fetched in August 2017

#### Seed database schema 2.1.0

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
- Entrez Gene Ids, Hugo symbols and aliases updated in September 2016 from NCBI
- Gene lengths retrieved from Gencode Release 25 (mapped to GRCh37)
- Pfam graphics fetched in September 2016

## For developers
Updating the seed database for Datahub is described [here](Update-Seed-Database.md).
