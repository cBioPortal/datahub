# cBioPortal Seed Database

These files are MySQL database dump files for seeding a new instance of the cBioPortal DB. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, gene, uniprot-mappings, drug, pdb and network data. Data is compatible with:

- DB schema version **2.1.0**

Which is suitable for:

- release version **1.5.1** of cBioPortal.  
- release version **> 1.5.1** of cBioPortal (:warning: with possible migration script step). 

:information_source: the DB schema and the cBioPortal can follow different numbering cycles. This means that the version numbers won't be always identical. 

You can download the files by using the links below:

- **Schema 2.1.0**: [SQL file with create table statements for portal release 1.5.1](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.5.1/db-scripts/src/main/resources/cgds.sql) 
- **Seed data, part1**: [cbioportal-seed SQL (.gz) file - part1 (no pdb_ tables)](seed-cbioportal_hg19_v2.1.0.sql.gz)
- **Seed data, part2 (optional)** [cbioportal-seed SQL (.gz) file - part2 (only pdb_ tables)](seed-cbioportal_hg19_v2.1.0_only-pdb.sql.gz)

**For developers:** [How to update the seed version stored in datahub](Update-Seed-Database.md)
