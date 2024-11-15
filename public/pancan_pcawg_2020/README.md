# Mutational Signatures inclusion
The original publication contains [mutational signature activity scores](https://www.synapse.org/#!Synapse:syn11804065) 
extracted by SigProfiler. 

## Input files
- [single-base substitution signature activity](https://www.synapse.org/#!Synapse:syn11738669) - PCAWG_sigProfiler_SBS_signatures_in_samples.csv
- [double-base substitution signature activity](https://www.synapse.org/#!Synapse:syn11738667) -  PCAWG_sigProfiler_DBS_signatures_in_samples.csv
- [insertion-deletion signature activity](https://www.synapse.org/#!Synapse:syn11738668) -  PCAWG_SigProfiler_ID_signatures_in_samples.csv
- [mutations](data_mutations.txt) - data_mutations.txt

## Contribution files
The original files contain activity scores. Activity and contribution scores can be calculated from each other.
For each signature type (SBS/DBS/INDEL) the contribution scores were calculated per sample as follows:
```
contribution (signature x) = activity (signature x) / total activity of all signatures in sample
```
Only samples present in the cBioPortal study were included.

## Mutational matrix
The mutational matrix was extracted from the `data_mutations.txt` file using SigProfilerMatrixGenerator python package
(v1.2.15) and the included reference genome GRCh37 (`SigProfilerMatrixGenerator.install.install('GRCh37')`).
Only samples with contribution scores were included.

### Tumor Break Load (TBL):

**Data Source**
 - TBL scores based on Lakbir et al., 2024 (Manuscript in progress)
 - Overview of TBL calculation, from [Lakbir et al., Eur J Cancer 2024](https://pubmed.ncbi.nlm.nih.gov/36334560/)
 - Data is provided as a sample-level clinical attribute labeled `Tumor Break Load`
