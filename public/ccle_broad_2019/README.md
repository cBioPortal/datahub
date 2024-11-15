# Notes for proteomics data from Nusinow et al. 2020

Proteomics data was generated for various cell lines, in an extensive study (see https://gygi.hms.harvard.edu/publications/ccle.html for a summary).

Data was retrieved from here:
Sample Information: https://gygi.hms.harvard.edu/data/ccle/Table_S1_Sample_Information.xlsx
Proteomics data: https://gygi.hms.harvard.edu/data/ccle/protein_quant_current_normalized.csv.gz

- The values in the data represent protein abundance ratios relative to the abundance of reference proteins in "bridge samples". Bridge samples are not loaded.
- Three samples were removed from the matrix (CAL120_BREAST_TenPx02, SW948_LARGE_INTESTINE_TenPx11 HCT15_LARGE_INTESTINE_TenPx30), because the cell lines involved multiple samples. These three cell lines were explicitly mentioned in the accompanied manuscript about the data, and the authors proposed to remove these if needed (see https://www.biorxiv.org/content/10.1101/2020.02.03.932384v1.full).
- The data was collapsed to per-gene values, the original data was per-protein. The Uniprot column was used with the Uniprot API to map protein IDs to NCBI Entrez IDs.
  - 2055 (16%) of the proteins could not mapped to NCBI entrez IDs, in which case I filled the blanks using the gene symbol which was already present in the original data.
  - 2130 (17%) of the proteins returned non-unique gene IDs, indicating that some proteins originated from the same gene. The duplicates were collapsed to per per-gene values by taking the average.
- A matrix was generated containing Z-scores derived from the log2-ratios per-gene. This enables the user to select protein abundance values as a separate profile from the query-by-gene interface in cBioPortal.
- Sample annotations were added to the clinical sample data indicating the 10-Plex ID and the TMT label.

### Tumor Break Load (TBL):

**Data Source**
 - TBL scores based on Lakbir et al., 2024 (Manuscript in progress)
 - Overview of TBL calculation, from [Lakbir et al., Eur J Cancer 2024](https://pubmed.ncbi.nlm.nih.gov/36334560/)
 - Data is provided as a sample-level clinical attribute labeled `Tumor Break Load`
