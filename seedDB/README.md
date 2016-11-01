These files are MySQL database dump for seeding a new instance of the cBioPortal DB. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, gene, uniprot-mappings, drug, pdb and network data. Data is compatible with:
- DB schema version **1.3.1**
Which is suitable for
- release version **1.3.1** of cBioPortal.  
- release version **> 1.3.1** of cBioPortal (:warning: with possible migration script step). 

You can download the files by using the links below:

- **Schema**: [SQL file with create table statements for release 1.3.1](https://raw.githubusercontent.com/cBioPortal/cbioportal/v1.3.1/core/src/main/resources/db/cgds.sql) 
- **Seed data, part1**: [cbioportal-seed SQL (.gz) file - part1 (no pdb_ tables)](https://github.com/cbioportal/datahub/raw/88020174c83290fa545bff3925109f63959461fd/seedDB/seed-cbioportal_no-pdb_hg19.sql.gz)
- **Seed data, part2 (optional)** [cbioportal-seed SQL (.gz) file - part2 (only pdb_ tables)](https://github.com/cbioportal/datahub/raw/88020174c83290fa545bff3925109f63959461fd/seedDB/seed-cbioportal_only-pdb.sql.gz)

