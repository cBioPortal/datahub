These files are MySQL database dump for seeding a new instance of the cBioPortal DB for mouse. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, gene, uniprot-mappings, drug, pdb and network data. Data is compatible with:

- DB schema version **2.1.0**

Which is suitable for:

- release version **1.5.0** of cBioPortal.  
- release version **> 1.5.0** of cBioPortal (:warning: with possible migration script step). 

:information_source: the DB schema and the cBioPortal can follow different numbering cycles. This means that the version numbers won't be always identical. 

You can download the files by using the links below:

- **Schema 2.1.0**: [SQL file with create table statements for portal release 1.5.0](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.5.0/db-scripts/src/main/resources/cgds.sql) 
- **Seed data, part1**: [cbioportal-seed SQL (.igz) file - part1 (no pdb_ tables)](seed-cbioportal_mm10_v2.1.0.sql.gz)
- There is no part2 of mouse seed data (pdb tables are currently not used).

**For developers:** if you want to update the seed version, take a look at the [file from the human folder](../seedDB/Update-Seed-Database.md)
