# Data transformation of mappyacts_2022

## The data
Article: Berlanga et al, 2022, Cancer discovery

https://urldefense.com/v3/__https://aacrjournals.org/cancerdiscovery/article/12/5/1266/694532/The-European-MAPPYACTS-Trial-Precision-Medicine__;!!KVWo1iE!WPiCn5MflUhz2kGgXpiGcmMiJXcRxtGu4p-OyJtj97LZ3VOZivH-X3KfSclW0cEhhG5lSSe2pS4aEV83FGCkTCSW5UrzOg$ 

Somatic mutation data for 484 single nucleotide alterations reported as “potentially actionable”

## The data transformation

**Metadata**
- Clinical data are for the patient with somatic single nucleotide alterations reported as “potentially actionable”
- Data contained 1 sample per patient.
- Censoring data was not added.
- WXS samples has matched normals.

**Mutation data**
- Somatic mutation data for 484 single nucleotide alterations reported as “potentially actionable”
- The original coordinates (in `GRCh37` ) were transformed to `GRCh38` using
  [LiftOver](https://urldefense.com/v3/__https://genome.ucsc.edu/cgi-bin/hgLiftOver__;!!KVWo1iE!WPiCn5MflUhz2kGgXpiGcmMiJXcRxtGu4p-OyJtj97LZ3VOZivH-X3KfSclW0cEhhG5lSSe2pS4aEV83FGCkTCQV_Yy2Zw$ ). This affected the
  columns `NCBI_Build`, `Start_Position` and `End_Position`.
- 4 out of the 484 reported somatic single nucleotide alterations are not reported since they were not confirmed with a second caller and with a very low VAF (3 alterations) or had a too low coverage at this position (1 alteration).
- Two panel samples have been removed from the study due to lack of gene panels.

**CNA data**

- The data for Copy Number Variation was computed with [Sequenza R package](https://urldefense.com/v3/__https://sequenzatools.bitbucket.io/__;!!KVWo1iE!WPiCn5MflUhz2kGgXpiGcmMiJXcRxtGu4p-OyJtj97LZ3VOZivH-X3KfSclW0cEhhG5lSSe2pS4aEV83FGCkTCRt1eVGGA$ )
- The Entrez gene id was obtained from Hugo symbol using Biomart.

**Treatment data**

- Treatment data was not shared as it was censored.

**Note**
- Panel information was not shared by the authors.