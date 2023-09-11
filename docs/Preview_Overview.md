# Preview Environment Project Documentation

To streamline the quality control process of reviewing external data sources, cBioPortal seeks to automate the deployment of a live staging instance with the new studies already imported. The Preview Environment workflow utilizes a combination of infrastructure-as-code tooling (`docker-compose`, `GitHub Actions`), and a fully-managed developer environment provisioned by Okteto (which runs via a `GitHub Action`).

The specification for building the containerized web applications is primarily accomplished through the configuration provided by the [`cbioportal-docker-compose`](https://github.com/cBioPortal/cbioportal-docker-compose) repository.

Okteto can appropriately parse the `docker-compose.yml` file, but to use these with Okteto to deploy a working staging instance of cBioPortal requires a few additional things to be set up in the infrastructure:

* configuration files for the cbioportal instance
* initial files and SQL commands to seed the initial SQL database
* have these files already present in an accessible image (for reasons outlined below).

These requirements are thus achieved through an initial setup procedure, followed by 2 workflow files, `preview.yml`, which deploys the staging environment with the study imported, and `preview_closed.yml`, which tears down the deployed instance.

The following document outlines each of the steps of the workflow, and provides insight where necessary as to why they were designed in such a manner.

### Initial Setup

![image](./Intial_Setup.svg)

The [`cbioportal-docker-compose`](https://github.com/cBioPortal/cbioportal-docker-compose) repository contains the files necessary to build a fully running instance of `cbioportal`. However, to get this to run, and to allow Okteto to access this in their `Deploy Preview` action, certain configuration files (such as the `portal.properties` document), and data to seed the SQL database, must be present.

The `cbioportal-docker-compose` repository contains a script, `init.sh`, that initializes these files. After checking out the repository, this script can be executed, and an `okteto build` command can be run to push the image.

This step is thus performed for 2 reasons: to initialize the namespace in the private Okteto registry, as well as to push an image with the configuration files and seeded DB files already in the image.

For a more detailed breakdown of the steps necessary here, as well as other prerequisites to getting this setup, see [Preview Setup](Preview_Setup.md).

(AVERY: should I reference the setup doc? Or is it certain that will be internal facing, and this might be public facing?)

### Workflow Overview

In brief, the proposed workflow works by pulling the previously described pre-built images of cBioPortal (with the configuration files added) and the cBioPortal SQL database (with the database files for seeding already added as well). These images are used to launch a container with the new studies imported as well, and this container is re-built to the same namespace registry. The `Deploy Preview` action by Okteto then pulls this image and uses it to deploy the preview environment. Upon which, a `metaImport.py` script can be run to import the study into the running application instance.

![Preview](./Preview2.svg)

### Identify and Get New Files (2)
The datahub repo is very large, and most files are stored using [Git LFS](https://git-lfs.com/), which by default doesn't store the actual file content in the repository (rather, they are references to the data, which is stored elsewhere). However, when importing an actual study, we need the actual file data. As a result, it is not possible to check out the entire repository's files during a GitHub Action workflow (the runner runs out of space). We therefore need to know which exact studies are the newly added ones that we want to preview, and checkout only these specific files from the repository. This also has the added benefit of making the review process for previewing the studies easier, as only new studies are imported into the staging instance.

The workflow uses a combination of various actions to determine the new directories added, and some text processing to convert them to strings in the proper format for input to the `checkout` action step. It is then checked out using Git's [sparse checkout](https://git-scm.com/docs/git-sparse-checkout) feature.

### Rebuilding cbioportal Image and Pulling Images (3)
Within the `datahub` repo, there is a `cbioportal-docker-compose` directory (nested under `preview`) containing the infrastructure needed to deploy to Okteto. Specifically, there is:
* a `docker-compose.yml` file, nearly identical to the one within the `cbioportal-docker-compose` repo, apart from a minor syntax change
* a .env file specifying the locations to pull the images from during the deploy process
* an empty `study` directory where new studies will be copied to

Once the new studies have been determined, they are transferred to this `study` directory. The `cbioportal` image is then re-built and pushed to the Okteto registry using an `okteto build` command (pushing to the exact registry defined in the .env file for `cbioportal`). As part of this process, all the files within the `study` directory are mounted into the re-built cbioportal container, which is how the studies are made available to the Okteto instance.


### Deploy Containers to Preview Environment (4)
Okteto's `Deploy Preview` action checks out the datahub repository and builds the PR environment from a clean clone. This is the primary reason why the previous image build steps were necessary (to both determine which study to be imported, as well as prevent cloning every other study). 

The built images (the pre-built `cbioportal-database` one from the setup, and the newly built `cbioportal`), which are specified in the `.env` file, are then pulled from the Okteto registry and used in the subsequent `Deploy Preview` action by Okteto. The `docker.compose.yml` is read by the `Deploy Preview` action, and the deploy process is started.

> :bulb: The GitHub Action for the deploy process actually finishes prematurely -- even after the service deploys on Okteto, it takes a while for the database to finish initializing. In between this time when the deploy action finishes, and the database is initializing, the public URL returns a 502 error. Therefore, an additional action step, **Wait For Response** is added to ping the URL until the service is fully functional, before proceeding.

One the deploy has fully finished, a message is posted on the PR with the public URL available to visit. At this step, a live staging instance is now deployed, and the studies are present in a `study` directory within the `cbioportal` container. However, the new studies have yet to be imported.

### Import Study (5)

The `kubectl` command is used to run a `metaImport.py` script (which is also located within the `cbioportal` container). This imports the data the database, at which point the data will then be visible on the staging instance. This is setup to be able to import multiple studies. 

Note that currently, the setup initialization seeds the database with certain gene panel IDs. However, if a new study is imported containing IDs not already existing within the database, the `metaImport.py` script will fail. 
![error](./gene_panel_error.png)

As such, this step is setup to always pass within the workflow for now, until this issue can be addressed in a future update to the workflow.

> :bulb: To prevent users from missing the error, an additional action step, **Add PR Comment If Import Fails** is added, to notify users if this step fails.


### Teardown of Preview Environment (6 & 7)

Finally, when a PR is either closed or merged, a `preview_closed.yml` workflow is run, which automatically tears down the deployed environment. This is currently necessary due to cost saving measures, as well as the fact that on the free tier, we are limited to roughly 2-3 open Preview Environments at any point in time.
