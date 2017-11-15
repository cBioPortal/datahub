# cBioPortal Seed Database

These files are MySQL database dump files for seeding a new instance of the cBioPortal database. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, genes, uniprot-mappings, drug and network data.

The database schema and cBioPortal release follows different numbering cycles since cBioPortal 1.5.0 and database schema 2.1.0. This means that the version numbers won't be identical. cBioPortal 1.9.0 with database schema 2.4.0 removed PDB annotations from the database.

## Latest seed database
#### Seed database schema 2.4.0

This schema is required for cBioPortal release versions:
- **1.9.0**

When using a release version **> 1.9.0**, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.4.0**: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.9.0/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database :** [seed-cbioportal_hg19_v2.4.0.sql.gz](https://github.com/cBioPortal/datahub/raw/master/seedDB/seed-cbioportal_hg19_v2.4.0.sql.gz)<br>
md5sum 1014ed1f9d72103f2b46e5615aacbc2f

Contents of seed database:
- Entrez Gene IDs, HGNC symbols and aliases updated in August 2017 from NCBI
- Gene lengths retrieved from Gencode Release 26 (mapped to GRCh37)
- Pfam graphics fetched in August 2017

## Previous seed databases
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
