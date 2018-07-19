Validation status of latest studies added to this repo: [![CircleCI](https://circleci.com/gh/cBioPortal/datahub.svg?style=svg)](https://circleci.com/gh/cBioPortal/datahub)

# cBioPortal Public Datahub
The datahub is a repository for store data only. It contains staging files which are pre-validated and can be loaded directly into the cBioPortal.

Behind the scenes git-lfs is used to manage the large files. https://github.com/github/git-lfs

## How to Download Data
### Downloading zip files individual studies
At [cbioportal.org](http://www.cbioportal.org/data_sets.jsp) a zipped folder with staging files from each study can be downloaded. These zip files are compressed versions of the study folders in the master branch of this repository.

### Example downloading individual study with git-lfs
It is also possible to download uncompressed staging files from this repository with git-lfs.

After you have installed git-lfs, configure it not to download all data files right away:
```
git lfs install --skip-repo --skip-smudge
```

Clone the git repository and install lfs hooks into it:
```
git clone https://github.com/cBioPortal/datahub.git
cd datahub
git lfs install --local --skip-smudge
```

Download the data files for a study folder, for example brca_tcga:
```
git lfs pull -I public/brca_tcga
```

## Download a complete MySQL export of the database
http://download.cbioportal.org/mysql-snapshots/mysql-dump-toc.html

## License
The data are available under [the ODC Open Database License (ODbL)](http://opendatacommons.org/licenses/odbl/1.0/) (summary available [here](http://www.opendatacommons.org/licenses/odbl/1-0/summary/)): you are free to share and modify the data so long as you attribute any public use of the database, or works produced from the database; keep the resulting data-sets open; and offer your shared or adapted version of the data-set under the same ODbL license.

TCGA data are availabe under Broad Institute GDAC TCGA Analysis Pipeline License. The Cancer Genome Atlas Consortium is pleased to provide the researchcommunity with preliminary data prior to publication.  Users are requested to carefully consider that these data are preliminary and have yet to be validated. Researchers are warned that the preliminary data have a significant uncertainty, are likely to change, and should be used with caution.

## Disclaimer
We are in the process of updating data. Some studies may result in 'fail' from validation.
