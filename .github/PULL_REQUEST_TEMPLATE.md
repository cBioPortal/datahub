# What?
Fix # (see https://help.github.com/en/articles/closing-issues-using-keywords)

Describe changes proposed in this pull request:
- a
- b

# checks
For all pull requests:
- [ ] Passes validation

For a new study (in addition to above):
- [ ] Does study name and study ID follow our convention? e.g. Tumor_Type (Institue, Journal Year); brca_mskcc_2015
- [ ] Is the study meta data complete? e.g. pmid, citation
- [ ] Were all samples profiled with WES/WGS? If not, is gene panel file curated?
- [ ] Are oncotree codes of all samples curated; Cancer Type and Cancer Type Detailed needs to be added in addition to Oncotree Code
- [ ] Clinical sample and patient data with meta files.
- [ ] Mutations data with meta file.
- [ ] Is the study based on hg38? If so, is the reference_genome: hg38 option included in meta study.
- [ ] CNA data with meta files
- [ ] CNA segment data with meta files
- [ ] Expression data including z-scores with meta files
- [ ] Other genomic profiles with meta files
- [ ] Case-lists for all profiles.
- [ ] Manual checking (Niki or JJ): Triage or private Portal link here

