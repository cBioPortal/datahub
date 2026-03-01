# TCGA Imaging Data Integration with cBioPortal

This document describes the process of acquiring TCGA imaging studies from the NCI Imaging Data Commons (IDC) and integrating them as patient resources in cBioPortal's TCGA Pan Cancer Atlas 2018 studies. The images can be viewed using OHIF (radiology) and SLIM (pathology) viewers within the portal.

## Data Structure in IDC

IDC organizes imaging data hierarchically:

```
Collections → Patients → Studies → Series → Instances
```

- **Study**: One complete imaging exam for a patient, regardless of modality (e.g., "CT Chest with Contrast", "MRI Brain"). One patient could have undergone multiple imaging studies over time.
- **Series**: Individual image batches within a study (e.g., different CT scan sections or sequences)

**Note**: While a single study may contain multiple imaging modalities, data was extracted at the study level and then split by modality for cBioPortal integration. This modality-level organization allows users to selectively access specific imaging types (e.g., CT scans vs. H&E slides) for each patient.

## Available Imaging Modalities

| Code | Modality | Viewer | Resource ID | Resource Tab Name |
|------|----------|--------|-------------|-------------------|
| CR | Computed Radiography | OHIF | IDC_OHIF_CR | Computed Radiography |
| CT | Computed Tomography | OHIF | IDC_OHIF_CT | CT Scan |
| DX | Digital Radiography | OHIF | IDC_OHIF_DX | Digital Radiography |
| MG | Mammography | OHIF | IDC_OHIF_MG | Mammography |
| MR | Magnetic Resonance | OHIF | IDC_OHIF_MR | Magnetic Resonance |
| NM | Nuclear Medicine | OHIF | IDC_OHIF_NM | Nuclear Medicine |
| PT | Positron Emission Tomography | OHIF | IDC_OHIF_PT | PET Scan |
| SM | Slide Microscopy (H&E) | SLIM | IDC_SLIM | H&E Slide |

**Note**: Annotation (ANN), Segmentation (SEG) and Structured Report (SR) are excluded as standalone resources since they are automatically loaded with their parent imaging studies in OHIF. Other (OT) modality is also excluded.

## Implementation Steps

### Generate Resource Files

Patient-level resource files are generated for each TCGA Pan Cancer study by:
1. Downloading TCGA imaging metadata from IDC using the idc-index package
2. Linking patients to their imaging studies via OHIF and SLIM viewer URLs

**Script**: [generate_imaging_resources.py](https://github.com/cBioPortal/datahub-study-curation-tools/tree/master/generate_imaging_resources)

## Output Files

For each TCGA Pan-Cancer Atlas 2018 study, two files are generated:

1. **`data_resource_patient.txt`**: Links patients to their imaging studies
   - Columns: `PATIENT_ID`, `RESOURCE_ID`, `URL`
   
2. **`data_resource_definition.txt`**: Defines the resource types available in the study
   - Columns: `RESOURCE_ID`, `DISPLAY_NAME`, `RESOURCE_TYPE`, `DESCRIPTION`, `OPEN_BY_DEFAULT`, `PRIORITY`

## Viewer URLs

- **OHIF Viewer** (for radiology imaging): `https://viewer.imaging.datacommons.cancer.gov/viewer/{StudyInstanceUID}`
- **SLIM Viewer** (for slide microscopy): `https://viewer.imaging.datacommons.cancer.gov/slim/studies/{StudyInstanceUID}`
