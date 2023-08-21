# Run cBioPortal using Docker Compose
Download necessary files (seed data, example config and example study from
datahub):
```
./init.sh
```

Start docker containers. This can take a few minutes the first time because the
database needs to import some data.
```
docker compose up
```
If you are developing and want to expose the database for inspection through a program like Sequel Pro, run:
```
docker compose -f docker-compose.yml -f open-db-ports.yml up
```
In a different terminal import a study
```
docker compose exec cbioportal metaImport.py -u http://cbioportal:8080 -s study/lgg_ucsf_2014/ -o
```

Restart the cbioportal container after importing:
```
docker compose restart cbioportal
```

The compose file uses docker volumes which persist data between reboots. To completely remove all data run:

```
docker compose down -v
```

If you were able to successfully set up a local installation of cBioPortal, please add it here: https://www.cbioportal.org/installations. Thank you!

## Known issues

## Loading other seed databases
### hg38 support
To enable hg38 support. First delete any existing databases and containers:
```
docker compose down -v
```
Then run
```
init_hg38.sh
```
Followed by:
```
docker compose up
```
When loading hg38 data make sure to set `reference_genome: hg38` in [meta_study.txt](https://docs.cbioportal.org/5.1-data-loading/data-loading/file-formats#meta-file-4). The example study in `study/` is `hg19` based. 

## Example Commands
### Connect to the database
```
docker compose exec cbioportal-database \
    sh -c 'mysql -hcbioportal-database -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE"'
```

## Advanced topics
### Run different cBioPortal version

A different version of cBioPortal can be run using docker compose by declaring the `DOCKER_IMAGE_CBIOPORTAL`
environmental variable. This variable can point a DockerHub image like so:

```
export DOCKER_IMAGE_CBIOPORTAL=cbioportal/cbioportal:3.1.0
docker compose up
```

which will start the v3.1.0 portal version rather than the newer default version.

### Change the heap size
#### Web app
You can change the heap size in the command section of the cbioportal container

#### Importer
For the importer you can't directly edit the java command used to import a study. Instead add `JAVA_TOOL_OPTIONS` as an environment variable to the cbioportal container and set the desired JVM parameters there (e.g. `JAVA_TOOL_OPTIONS: "-Xms4g -Xmx8g"`).
