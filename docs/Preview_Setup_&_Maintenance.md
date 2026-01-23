# Okteto Developer Setup for cBioPortal Maintainers

This documentation serves as an outline for the exact work performed to setup the Okteto preview pipeline. If this were ever to be set up again from scratch, following these steps should replicate the existing infrastructure. For more insight as to why things were developed in this manner, refer to [Preview Overview](Preview_Overview.md).

## One time Setup (If re-building from scratch):

1. Okteto Account Creation - Visit [Here](https://www.okteto.com/try-free/) and link a GitHub account. Note that the account must be linked to a business email (i.e. non-gmail account).
2. Install the Okteto CLI and initialize the context as per instructions [here](https://www.okteto.com/docs/getting-started/#installing-okteto-cli).
3. Generate Okteto Personal Access Token (PAT) as per instructions [here](https://www.okteto.com/docs/cloud/personal-access-tokens/)
4. Clone the `cbioportal-docker-compose` repository and run the initialization script, `./init.sh` in the root directory.
5. Remove all instances of the `:ro` text within the `docker-compose.yml` file, as this is not supported by Okteto.
6. Run `okteto context use https://cloud.okteto.com`, to initialize the namespace Okteto will use.
7. Run `okteto build` to build and push an initial *cbioportal* and *cbioportal-database* image to the Okteto Registry with the initialized configuration present.

Within the Datahub repo:

8. Add new secret variable OKTETO_TOKEN using the PAT.
9. Add new secret variable OKTETO_URL (https://cloud.okteto.com).
10. In the repo settings > Code and automation > Actions > General > Workflow Permissions, enable workflow read-write permissions to allow Okteto to post messages in a PR.
11. Add new workflow file (`preview.yml`) from PR to .github folder of datahub repository.
12. Add the following files to setup infrastructure for re-building image in PR. Specifically:

    a. Run `mkdir -p preview/cbioportal-docker-compose/study` to create the necessary directories

    b. Add a `.gitkeep` file within the `study` directory to ensure git keeps track of an empty repository

    c. Within the `preview/cbioportal-docker-compose` directory, add a modified `docker-compose.yml`, from the file in Step 5 (the file must have all instances of the string `:ro`, removed as Okteto does not support this syntax).

    d. Within the `preview/cbioportal-docker-compose` directory, add a `.env` file containing the images to be built, with the link pointing to the Okteto registry:
        
        DOCKER_IMAGE_CBIOPORTAL=registry.cloud.okteto.net/<namespace>/cbioportal-docker-compose-cbioportal:okteto-with-volume-mounts

        DOCKER_IMAGE_MYSQL=registry.cloud.okteto.net/<namespace>/cbioportal-docker-compose-cbioportal-database:okteto-with-volume-mounts

Following this setup, subsequent PRs should correctly trigger a staging environment with the new studies imported.

## Maintenance of Current Setup

### Rebuilding the Image to Update cBioPortal Version
Once the workflow has been setup, the private registry has already been initialized. The .env file specifies the private registry, and as such, the deploy preview environment pulls from the previously built images. One thing to note however is that currently, the build version of cbioportal is locked to whatever the most up to date version is during the initial setup where the image was built and pushed from `cbioportal-docker-compose`. Therefore, there may come a point when the version of cBioPortal is too out of date and must be updated.

Essentially, steps 4-7 must be rerun to update the build image. 

To simplify this process, a `preview_init.sh` script has been created to replicate this process, and should be executable provided Okteto and git has been correctly set up on the running machine.


### Changing of Namespace
If the Okteto account were ever to be migrated to a different namespace, it should be sufficient to simply re-run steps 4-7, and rename all instances of the namespace to the current desired user (e.g. justinjao) in the `preview.yml`, `preview_closed.yml`, and `.env` files.

### Note About Directory Structure
The namespace of the directory is important, as this is how the `okteto build` command determines what namespace to push the service to (i.e. if the directory is called `cbioportal-docker-compose`, it would push to `okteto.dev/cbioportal-docker-compose-cbioportal:okteto-with-volume-mounts`). This is why within Datahub, while it may not make much sense to have a directory named `cbioportal-docker-compose`, there exists such a specific directory nested under `preview`. The directory could have been changed, which would result in the build image tag name differing. However, the thinking here was that maintaining this namespeace would be easiest for maintenance, as this allows steps 4-7 to easily be automated into the `preview_init.sh` script to rebuild the image via a clean clone of the `cbioportal-docker-compose` repo, without any other change.