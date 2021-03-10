# cBioPortal Seed Database

These files are MySQL database dump files for seeding a new instance of the cBioPortal database. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, genes, uniprot-mappings, drug and network data.

The database schema and cBioPortal release follows different numbering cycles since cBioPortal 1.5.0 and database schema 2.1.0. This means that the version numbers won't be identical. cBioPortal 1.9.0 with database schema 2.4.0 removed PDB annotations from the database.

## Release Notes
History and detailed notes for each release is described [HERE](Release-Notes.md).

## Release Process
- Step 1 - Curation Generate Input [HERE](https://github.com/cBioPortal/datahub-study-curation-tools/blob/master/gene-table-update/README.md)
- Step 2 - Generate new seedDB mysqldump
- Step 3 - Import miRNA gene set
- Step 4 - Import gene set
- Step 5 - Update genome nexus
- Step 6 - Apply corresponding gene updates to all files:

## For Developers
Updating the seed database for Datahub is described [HERE](Update-Seed-Database.md).
* Local data files needs to be updated as well 
