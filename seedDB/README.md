These files are MySQL database dump for seeding a new instance of the cBioPortal DB. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, gene, uniprot-mappings, drug, pdb and network data. Data is compatible with:

- DB schema version **2.1.0**

Which is suitable for:

- release version ~~**1.3.1**~~ of cBioPortal.  
- release version ~~**> 1.3.1**~~ of cBioPortal (:warning: with possible migration script step). 
- [cBioPortal test-version with gene set functionality](https://github.com/cBioPortal/cbioportal/tree/geneset_frontend)

:information_source: the DB schema and the cBioPortal can follow different numbering cycles. This means that the version numbers won't be always identical. 

You can download the schema by using the link below:

- **Schema 2.1.0**: [SQL file with create table statements for portal release 2.1.0](https://github.com/cBioPortal/cbioportal/blob/geneset_frontend/db-scripts/src/main/resources/cgds.sql) 
- **Seed data, part1**: [cbioportal-seed SQL (.gz) file - part1 (no PDB tables)](seed-cbioportal_no-pdb_hg19.sql.gz)
- **Seed data, part2 (optional)** [cbioportal-seed SQL (.gz) file - part2 (only PDB tables)](seed-cbioportal_only-pdb.sql.gz)
