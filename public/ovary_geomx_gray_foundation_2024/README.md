# Data transformation of ovary_geomx_gray_foundation_2024

Article: Kader et al. Cancer Discov 2024. https://aacrjournals.org/cancerdiscovery/article/doi/10.1158/2159-8290.CD-24-1366/750608/Multimodal-Spatial-Profiling-Reveals-Immune

Data was downloaded from the supplementary files:
- Table S1 and Table S2: Patient and Sample clinical data.


## Notes on data transformation

**Metadata**
- Clinical data was inferred from the supplementary table S1 and S2. 
- Manual distinction was made on patient and sample attributes.

**Expression data**

_mRNA_

- RNA seq expression levels obtained from GeOmx were inferred from the table S8, sheet.
- Gene expression data for spatially resolved regions (tumor, immune, stromal compartments).

**Cell_type_fractions**

- Counts of immune and stromal cells were normalized per ROI area (e.g., cells/mm²).
- Data was shared by the author.
- Transformed as generic assay

**Cell_intensity**

- Intensity of P53 was measured in Relative Fluorescence Units (RFU), a standardized method for quantifying fluorescence-based protein expression levels.
- Data was shared by the author.
- Transformed as generic assay