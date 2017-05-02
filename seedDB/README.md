# cBioPortal Seed Database

These files are MySQL database dump files for seeding a new instance of the cBioPortal DB. They contain all the necessary background data for a properly functioning cBioPortal website, including cancer types, gene, uniprot-mappings, drug, pdb and network data. This seed data is compatible with:

- cBioPortal DB schema version **2.3.0**

Which is suitable for:

- cBioPortal version **1.6.0**
- cBioPortal version **> 1.6.0** (:warning: with possible migration script step)

:information_source: the DB schema and the cBioPortal can follow different numbering cycles. This means that the version numbers won't be always identical.

You can download the files by using the links below:

- **Schema 2.3.0**: [SQL file with create table statements for portal release 1.5.1](https://raw.githubusercontent.com/cBioPortal/cbioportal/geneset/db-scripts/src/main/resources/cgds.sql) :warning: when 1.6.0 is merged to master, this should direct to 1.6.0 tag
- **Seed data, part1**: [cbioportal-seed SQL (.gz) file - part1 (no pdb_ tables)](seed-cbioportal_hg19_v2.3.0.sql.gz)
- **Seed data, part2 (optional)** [cbioportal-seed SQL (.gz) file - part2 (only pdb_ tables)](seed-cbioportal_hg19_v2.3.0_only-pdb.sql.gz)

**For developers:** [How to update the seed version stored in datahub](Update-Seed-Database.md)
