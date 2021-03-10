# cBioPortal Seed Database

These files are MySQL database dump files for seeding a new instance of the cBioPortal database. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, genes, uniprot-mappings, drug and network data.

The database schema and cBioPortal release follows different numbering cycles since cBioPortal 1.5.0 and database schema 2.1.0. This means that the version numbers won't be identical. cBioPortal 1.9.0 with database schema 2.4.0 removed PDB annotations from the database.

## Release Notes
History and detailed notes for each release is described [HERE](Release-Notes.md).

## Our Release Process

#### Step 1 - Curation
- Generate an up-to-date `gene_info.txt`  
- Steps and scripts [HERE](https://github.com/cBioPortal/datahub-study-curation-tools/blob/master/gene-table-update/README.md)

#### Step 2 - Generate new seedDB mysqldump

#### Step 3 - Import miRNA gene set
- How to import [HERE](https://github.com/cBioPortal/cbioportal/blob/master/docs/Import-the-Seed-Database.md)
- Input mapping [HERE](https://github.com/cBioPortal/cbioportal/blob/master/core/src/main/resources/micrornas.tsv)

#### Step 4 - Import gene set
- Steps and scripts can be found [HERE](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/gene-table-update/gene-set)

#### Step 5 - Update Genome Nexus

#### Step 6 - Apply corresponding gene updates to all files
- Steps and scripts can be found [HERE](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/gene-table-update/data-file-migration)

## For Developers
- Updating the seed database for Datahub is described [HERE](Update-Seed-Database.md).
- Local data files needs to be updated as well, information can be found [HERE](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/gene-table-update/data-file-migration)
