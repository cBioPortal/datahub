# cBioPortal Seed Database

These files are MySQL database dump files for seeding a new instance of the cBioPortal database. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, genes, uniprot-mappings, drug, Protein Data Bank (PDB) and network data. 

The database schema and cBioPortal release follows different numbering cycles since cBioPortal 1.5.0 and database schema 2.1.0. This means that the version numbers won't be identical. 

## Latest seed database
#### Seed database schema 2.3.1

This schema is required for cBioPortal release versions: 
- **1.7.1**
- **1.7.2**
- **1.7.3**
- **1.8.0**

When using a release version **> 1.8.0**, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.3.1**: [SQL file with create table statements for portal release 1.7.3](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.7.3/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database part1**: [cbioportal-seed SQL (.gz) file - part1 (no PDB  tables)](seed-cbioportal_hg19_v2.3.1.sql.gz)<br>
**Seed database part2 (optional):** [cbioportal-seed SQL (.gz) file - part2 (only PDB tables)](seed-cbioportal_hg19_v2.3.1_only-pdb.sql.gz)

## Previous seed databases
#### Seed database schema 2.1.0

This schema is required for **older** cBioPortal release versions:
- 1.5.0
- 1.5.1
- 1.5.2

When using this older seed database with a release version > 1.5.2, a migration step to a new database schema is required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.1.0: [SQL file with create table statements for portal release 1.5.0](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.5.1/db-scripts/src/main/resources/cgds.sql)<br>
Seed database part1: [cbioportal-seed SQL (.gz) file - part1 (no PDB tables)](https://github.com/cBioPortal/datahub/raw/84fd66daf8325ad9721895d1cc503653686de15e/seedDB/seed-cbioportal_hg19_v2.1.0.sql.gz)<br>
Seed database part2 (optional): [cbioportal-seed SQL (.gz) file - part2 (only PDB tables)](https://github.com/cBioPortal/datahub/raw/84fd66daf8325ad9721895d1cc503653686de15e/seedDB/seed-cbioportal_hg19_v2.1.0_only-pdb.sql.gz)

## For developers
Updating the seed database for Datahub is described [here](Update-Seed-Database.md).
