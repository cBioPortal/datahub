These files are MySQL database dump for seeding a new instance of the cBioPortal DB for mouse. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, gene, uniprot-mappings, drug, pdb and network data. Data is compatible with:

- DB schema version **1.4.0**

Which is suitable for:

- release version **1.4.1** of cBioPortal.  
- release version **> 1.4.1** of cBioPortal (:warning: with possible migration script step). 

:information_source: the DB schema and the cBioPortal can follow different numbering cycles. This means that the version numbers won't be always identical. 

You can download the files by using the links below:

- **Schema 1.4.0**: [SQL file with create table statements for portal release 1.4.1](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.4.1/core/src/main/resources/db/cgds.sql) 
- **Seed data, part1**: [cbioportal-seed SQL (.igz) file - part1 (no pdb_ tables)](https://github.com/thehyve/datahub/raw/mouse/seedDB_mouse/seed-cbioportal_no-pdb_mm10.sql.gz)
- There is no part2 of mouse seed data (pdb tables are currently not used).

**For developers:** if you want to update the seed version, take a look at the [file from the human folder](https://github.com/cbioportal/datahub/blob/master/seedDB/Update-Seed-Database.md)
