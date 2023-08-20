# cBioPortal Public Datahub   
The datahub is a repository for data storage only. It contains staging files which are validated and can be loaded directly into the  cBioPortal.

Behind the scenes git-lfs is used to manage the large files. https://github.com/github/git-lfs

## Test Status   
Validation status of all studies on Datahub master branch. This runs weekly using the validation code from the cBioPortal master branch. It also validates if the studies on cbioportal.org and on Datahub are in sync.

[![CircleCI](https://circleci.com/gh/cBioPortal/datahub/tree/master.svg?style=svg)](https://circleci.com/gh/cBioPortal/datahub/tree/master)

## How to Download Data
### Downloading zip files individual studies
At [cbioportal.org datasets page](https://www.cbioportal.org/datasets) a zipped file with staging files from each study can be downloaded. These zip files are compressed versions of the study folders in the master branch of this repository.

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

## How to Upload Data
#### Create a new branch from the 'master' branch.
```
git checkout master
git pull origin master
git checkout -b [name_of_your_new_branch]
```
For general background on creating and managing branches within GitHub, see:  [Git Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging).

#### Commit changes, and push the branch back to GitHub.
```
[back to the root directory]
git add .
git commit -m '[notes_for_your_change]'
git push origin [name_of_your_new_branch]
```

#### Open a Pull Request on GitHub to the 'master' branch.
For instructions on submitting a pull-request, please see:  [Using Pull Requests ](https://help.github.com/articles/using-pull-requests/) and [Sending Pull Requests](http://help.github.com/send-pull-requests/).

## Download a complete MySQL export of the latest database
http://download.cbioportal.org/mysql-snapshots/mysql-snapshots-toc.html


## License
The data are available under [the ODC Open Database License (ODbL)](http://opendatacommons.org/licenses/odbl/1.0/).You are free to share and modify the data as long as you attribute any public use of the database, or works produced from the database; keep the resulting data-sets open; and offer your shared or adapted version of the data-set under the same ODbL license.

TCGA data are availabe under Broad Institute GDAC TCGA Analysis Pipeline License. The Cancer Genome Atlas Consortium is pleased to provide the research community with preliminary data prior to publication.  Users are requested to carefully consider that these data are preliminary and have yet to be validated. Researchers are warned that the preliminary data have a significant uncertainty, are likely to change, and should be used with caution.

## User Assistance
For questions, please post on our user discussion group at: https://groups.google.com/g/cbioportal
