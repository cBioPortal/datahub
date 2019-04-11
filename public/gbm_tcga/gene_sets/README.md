This study contains GSVA scoring data calculated with gene set analysis described on the [cbioportal-gsva-analysis GitHub page](https://github.com/thehyve/cbioportal-gsva-analysis).

Gene set scores are calculated for the 4 GBM gene sets from Verhaak et al. (Cancer Cell 2010, PubMed ID: 20129251), Hallmark and Oncogenic gene sets (C6) collections from [MSigDB](http://software.broadinstitute.org/gsea/msigdb) (version 6.1). GSVA scores were calculated from the RSEM normalized RNA-Seq expression data.

To load this study, gene sets should be imported into your cBioPortal instance:
- If your cBioPortal instance started from a [seed database](https://github.com/cBioPortal/datahub/tree/master/seedDB) of version 2.6.0 or higher the gene sets are present.
- Otherwise gene sets can be loaded by using the provided GMT and YAML file in this folder, see documentation about loading in the [cBioPortal docs](https://github.com/cBioPortal/cbioportal/blob/master/docs/Import-Gene-Sets.md)

More info on using this data can be found on a blogspot from The Hyve: http://blog.thehyve.nl/blog/gene-set-visualization-in-the-new-cbioportal-oncoprint
