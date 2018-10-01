# Update cBioPortal seed database files stored in datahub
This documentation file is addressed to developers. To update the seed database files to a recent version you should follow these steps:

1. Start a new instance of the cBioPortal database with the previous seed database ([more information](README.md)).

2. Run the migration script from a branch that includes the new database schema ([more information](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script)).

3. Update the gene and gene alias by following the instructions in https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-gene-and-gene_alias-tables.md

4. Update the cancer types by running `./update_cancer_types.py -p <local_dir>/portal.properties`

5. Move to the folder where you want to save the seed files. Use the following commands (assuming that the database is running on port 8306) to generate the new seed files. Please specify the species and the new schema version in the file name (e.g. for the human version of `v2.1.0`, the file name should be `seed-cbioportal_hg19_v2.1.0.sql`).

:warning: Do not confuse the schema version with the cBioPortal version.

Run `mysqldump` to generate the dump files. Make sure you use mysqldump version 5.7.
```shell
mysqldump -u cbio -pP@ssword1 -P 8306 --host 127.0.0.1 --ignore-table cbioportal.pdb_uniprot_alignment --ignore-table cbioportal.pdb_uniprot_residue_mapping --ignore-table cbioportal.info --no-create-info --complete-insert cbioportal > seed-cbioportal_hg19_v2.1.0.sql
```
:warning: The database schema is not included in these dump files.

6. In case gene sets are included in the seed, manually add a line at the end the sql file to update the gene set version.
```bash
-- Manually add gene set version
UPDATE info SET GENESET_VERSION="msigdb_6.1";
```

7. Zip the generated mysql dump files:
```shell
gzip seed-cbioportal_hg19_v2.1.0.sql
```

8. New files are ready to be uploaded to datahub.

:warning: The database schema itself is found at: `$PORTAL_HOME/db-scripts/src/main/resources/db/cgds.sql`
