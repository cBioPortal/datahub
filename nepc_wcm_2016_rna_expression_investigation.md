# NEPC WCM 2016: RNA-Expression Investigation

## Objective
Investigate negative RNA-expression values in the cBioPortal `nepc_wcm_2016` study.

## Findings
- The original Datahub entry was added in commit `32de2648833997c5725c4f7c4dd5ef2ea48666be` on August 16, 2018.
- The original file was named `data_expression_median.txt`.
- Its metadata describes continuous mRNA expression but does not document the normalization method, transformation, or units.
- A later historical file, `data_RNA_Seq_expression_median.txt`, contained negative values. This does not establish that the original file contained identical values or explain their cause.
- Datahub issue #1586 also raised questions about negative values in this study. The issue's closure does not independently confirm the processing method.

## Conclusion
The exact processing responsible for the negative values remains unconfirmed. Negative values can arise from transformations or standardization, but the available evidence does not establish which method was used here.

## Questions for the cBioPortal curation team
1. What normalization and transformation were applied to the original expression file?
2. Are negative values expected in this profile?
3. Is there documentation confirming the expression scale and units?

## References
- Study files: https://github.com/cBioPortal/datahub/tree/master/public/nepc_wcm_2016
- Original commit: https://github.com/cBioPortal/datahub/commit/32de2648833997c5725c4f7c4dd5ef2ea48666be
- Related issue #1586: https://github.com/cBioPortal/datahub/issues/1586
- Study paper: https://pmc.ncbi.nlm.nih.gov/articles/PMC4777652/
