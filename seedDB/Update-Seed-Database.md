# Update the seed database
To update the seed database to a recent version you should follow these steps:

1- Set up a new instance of the cBioPortal database, by using the most recent available seed database: [more information](https://github.com/cbioportal/datahub/blob/master/seedDB/README.md)

2- Run the migration script: [more information](https://github.com/cBioPortal/cbioportal/blob/master/docs/Updating-your-cBioPortal-installation.md#running-the-migration-script)

3- Move to the folder where you want to save the seed files and generate them. To do that, use the following commands (assuming that the database is running on port 8306):

```shell
mysqldump -u cbio -pP@ssword1 -P 8306 --host 127.0.0.1 --ignore-table cbioportal.pdb_uniprot_alignment --ignore-table cbioportal.pdb_uniprot_residue_mapping --ignore-table cbioportal.info --no-create-info --complete-insert cbioportal > seed-cbioportal_no-pdb_hg19.sql
mysqldump -u cbio -pP@ssword1 -P 8306 --host 127.0.0.1 --no-create-info cbioportal pdb_uniprot_alignment pdb_uniprot_residue_mapping --complete-insert > seed-cbioportal_only-pdb.sql
```

4- Zip the obtained files:
```shell
gzip seed-cbioportal_no-pdb_hg19.sql
gzip seed-cbioportal_only-pdb.sql
```

5- Now the files are ready to be updated! 
(::warning:: You will find the current schema in this link, where ```version``` is the current cBioPortal version preceded by a ```v```: ```https://raw.githubusercontent.com/cBioPortal/cbioportal/version/core/src/main/resources/db/cgds.sql```)
