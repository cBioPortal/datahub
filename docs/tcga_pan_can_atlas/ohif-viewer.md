# OHIF Viewer for TCGA CT Scans
OHIF URLs for CT Scans were obtained from the Imaging Data Commons and added as
resource data to all tcga_pan_can_2018 studies,

## Steps
### 1. Download Data from IDC

Go to IDC and select TCGA -> CT Scans. Download a manifest with all the links to ~/Downloads/idc_ohif.tsv.

### 2. Curate coadread_tcga semi-manually

Add all *resource* files for coad and read data and link patients to samples. This was done semi-manually.

### 3. Do the rest using a command one liner

Generate them for the rest:
```bash
for f in $(cut -f2 ~/Downloads/idc_ohif.tsv | gsort | uniq | grep tcga_ | grep -v Filters | grep -v coad | grep -v read); do (head -1 coadread_tcga_pan_can_atlas_2018/data_resource_patient.txt; cut -f1,2,4 ~/Downloads/idc_ohif.tsv | tail -n +9 | grep $f | cut -f1,3 | awk -vFS='\t' -vOFS='\t' '{$1=substr($1,0,12); $3="https://viewer.imaging.datacommons.cancer.gov/viewer/"$2; $2="IDC_OHIF_V2"; print $0}' | gsort -k1,1 | uniq | rev | uniq -f2 | rev; ) > ${f/tcga_/}_tcga_pan_can_atlas_2018/*data_resource*patient*; done
```

Note: there are a few patients that have multiple CT Scans. Not entirely sure what the difference is, the above command just selects the first one
