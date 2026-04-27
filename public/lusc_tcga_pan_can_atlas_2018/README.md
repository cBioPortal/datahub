## Improving PanCancer Atlas Data: (transformation steps for the new data types being added)

### The Timeline/Treatment data:

**Data Source**
- GDAC Firehose: https://gdac.broadinstitute.org/
- File Used: `Merge_Clinical.Level_1.20160128` (clin.merged.txt) for each cancer type.

**Data Transformation** 
- The detailed transformation steps are listed in the Pull Request [here](https://github.com/cBioPortal/datahub/pull/1597)

### The Genetic Ancestry data:


**Data Source**
- GDAC Firehose: https://gdc.cancer.gov/about-data/publications/CCG-AIM-2020
- File Used: `Admixture_by_sample.txt` (Admix percent by sample) for each cancer type.


### The Methylation data:

**Data Source**
- GDAC Firehose: https://gdc.cancer.gov/node/977
- File Used: `jhu-usc.edu_PANCAN_HumanMethylation450.betaValue_whitelisted.tsv` (DNA methylation 450K only beta value data matrix) for each cancer type.

**Data Transformation** 
 - The detailed transformation steps are listed in the Pull Request [here](https://github.com/cBioPortal/datahub/pull/1597)
 - The meta info for the Infinium Illumina 450k probes used for this profile is under the folder "probe_meta" "probe_450k_mapinfo_PQ.txt" is the original download from Illumina.