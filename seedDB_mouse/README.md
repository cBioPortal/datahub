# cBioPortal Seed Database for Mouse

These files are MySQL database dump files for seeding a new instance of the cBioPortal database for mouse. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, genes and uniprot-mappings.

The database schema and cBioPortal release follows different numbering cycles since cBioPortal 1.5.0 and database schema 2.1.0. This means that the version numbers won't be identical. 

## Latest mouse seed database
#### Seed database schema 2.4.0

This schema is required for cBioPortal release versions:
- **1.9.0**

When using a release version **> 1.9.0**, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.4.0**: [SQL file with create table statements](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.9.0/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database :** [seed-cbioportal_mm10_v2.4.0.sql.gz](https://github.com/cBioPortal/datahub/raw/master/seedDB/seed-cbioportal_mm10_v2.4.0.sql.gz)<br>
md5sum 1014ed1f9d72103f2b46e5615aacbc2f

## Previous mouse seed databases
#### Seed database schema 2.3.1

This schema is required for cBioPortal release versions: 
- **1.7.1**
- **1.7.2**
- **1.7.3**
- **1.8.0**

When using a release version **> 1.8.0**, a migration step to a new database schema might be required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

**Schema 2.3.1**: [SQL file with create table statements for portal release 1.7.3](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.7.3/db-scripts/src/main/resources/cgds.sql)<br>
**Seed database**: [cbioportal-seed SQL (.gz) file](seed-cbioportal_mm10_v2.3.1.sql.gz)

#### Seed database schema 2.1.0

This schema is required for **older** cBioPortal release versions:
- 1.5.0
- 1.5.1
- 1.5.2

When using this older seed database with a release version > 1.5.2, a migration step to a new database schema is required. The migration process is described [here](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script).

Schema 2.1.0: [SQL file with create table statements for portal release 1.5.0](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.5.1/db-scripts/src/main/resources/cgds.sql)<br>
Seed database: [cbioportal-seed SQL (.gz) file)](https://github.com/cBioPortal/datahub/raw/8031b659b99c833d7fbcd057834220cd6708a032/seedDB_mouse/seed-cbioportal_mm10_v2.1.0.sql.gz)

## For developers
Updating the seed database for Datahub is described [here](../seedDB/Update-Seed-Database.md).
