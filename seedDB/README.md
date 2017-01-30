These files are MySQL database dump for seeding a new instance of the cBioPortal DB. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, gene, uniprot-mappings, drug, pdb and network data. Data is compatible with:

- DB schema version **1.4.0**

Which is suitable for:

- release version **1.4.1** of cBioPortal.  
- release version **> 1.4.1** of cBioPortal (:warning: with possible migration script step). 

:information_source: the DB schema and the cBioPortal can follow different numbering cycles. This means that the version numbers won't be always identical. 

You can download the files by using the links below:

- **Schema 1.4.0**: [SQL file with create table statements for portal release 1.4.1](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.4.1/core/src/main/resources/db/cgds.sql) 
- **Seed data, part1**: [cbioportal-seed SQL (.gz) file - part1 (no pdb_ tables)](https://github.com/cbioportal/datahub/raw/master/seedDB/seed-cbioportal_no-pdb_hg19.sql.gz)
- **Seed data, part2 (optional)** [cbioportal-seed SQL (.gz) file - part2 (only pdb_ tables)](https://github.com/cbioportal/datahub/raw/master/seedDB/seed-cbioportal_only-pdb.sql.gz)

**For developers:** [How to update the seed version](https://github.com/cbioportal/datahub/blob/master/seedDB/Update-Seed-Database.md)
