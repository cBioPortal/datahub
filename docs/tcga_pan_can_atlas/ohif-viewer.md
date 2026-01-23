# TCGA Imaging Data Integration with cBioPortal

This document describes the process of acquiring TCGA imaging studies from the NCI Imaging Data Commons (IDC) and integrating them as patient resources in cBioPortal's TCGA Pan Cancer Atlas 2018 studies. The images can be viewed using OHIF (radiology) and SLIM (pathology) viewers within the portal.

## Data Structure in IDC

IDC organizes imaging data hierarchically:

```
Collections → Patients → Studies → Series → Instances
```

- **Study**: One complete imaging exam for a patient, regardless of modality (e.g., "CT Chest with Contrast", "MRI Brain"). One patient could have undergone multiple imaging studies over time.
- **Series**: Individual image batches within a study (e.g., different CT scan sections or sequences)

**Note**: While a single study may contain multiple imaging modalities, data was extracted at the study level and then split by modality for cBioPortal integration. This modality-level organization enables allows users to selectively access specific imaging types (e.g., CT scans vs. H&E slides) for each patient.

## Available Imaging Modalities

| Code | Modality | Viewer | Resource ID |
|------|----------|--------|-------------|
| CR | Computed Radiography | OHIF | IDC_OHIF_CR |
| CT | Computed Tomography | OHIF | IDC_OHIF_CT |
| DX | Digital Radiography | OHIF | IDC_OHIF_DX |
| MG | Mammography | OHIF | IDC_OHIF_MG |
| MR | Magnetic Resonance | OHIF | IDC_OHIF_MR |
| NM | Nuclear Medicine | OHIF | IDC_OHIF_NM |
| PT | Positron Emission Tomography | OHIF | IDC_OHIF_PT |
| SM | Slide Microscopy (H&E) | SLIM | IDC_SLIM |

**Note**: Annotation (ANN), Segmentation (SEG) and Structured Report (SR) are excluded as standalone resources since they are automatically loaded with their parent imaging studies in OHIF. Other (OT) modality is also excluded.

## Implementation Steps

### 1. Download Data from IDC

[idc-index](https://github.com/ImagingDataCommons/IDC-Tutorials/blob/master/notebooks/getting_started/part2_searching_basics.ipynb) package was used to programmatically download UID's for all tcga from IDC.
```python
from idc_index import IDCClient

client = IDCClient()

client.sql_query("SELECT * FROM index WHERE collection_id LIKE '%tcga%'").to_csv("idc_tcga.txt", sep='\t', index=None)
```

### 2. Generate data 

Generate patient-level resource files for each TCGA Pan Cancer study by linking patients to their imaging studies via OHIF and SLIM viewer URLs.

```python
import pandas as pd
import numpy as np
import os

df_tcga = pd.read_csv("idc_tcga.txt", sep='\t', dtype=str)

# Remove modalities that cannot directly be viewed along with Other type
df_tcga = df_tcga[~df_tcga['Modality'].isin(['ANN', 'SEG', 'SR', 'OT'])]

# Group the patients by collection_id, PatientID, StudyInstanceUID, Modality
cols = ['PatientID', 'StudyInstanceUID', 'Modality']
resource_df = df_tcga[cols].drop_duplicates().reset_index(drop=True)

# Map modalities
modality_map = {
    'CR': 'IDC_OHIF_CR',
    'CT': 'IDC_OHIF_CT',
    'DX': 'IDC_OHIF_DX',
    'MG': 'IDC_OHIF_MG',
    'MR': 'IDC_OHIF_MR',
    'NM': 'IDC_OHIF_NM',
    'PT': 'IDC_OHIF_PT',
    'SM': 'IDC_SLIM'
}
resource_df['Modality'] = resource_df['Modality'].replace(modality_map)

# Add StudyInstanceUID URL
resource_df['StudyInstanceUID'] = np.where(
    resource_df['Modality'] == 'IDC_SLIM',
    'https://viewer.imaging.datacommons.cancer.gov/slim/studies/' + resource_df['StudyInstanceUID'],
    'https://viewer.imaging.datacommons.cancer.gov/viewer/' + resource_df['StudyInstanceUID']
)

# Rename columns
resource_df = resource_df[['PatientID', 'Modality', 'StudyInstanceUID']]
resource_df.columns = ['PATIENT_ID', 'RESOURCE_ID', 'URL']

# Write filtered resource files per study
dh_files_path = "/Users/madupurr/Github/datahub/public"

# resource defenition file map
definition_map = {
    'IDC_OHIF_CR': 'Computed Radiography',
    'IDC_OHIF_CT': 'CT Scan',
    'IDC_OHIF_DX': 'Digital Radiography',
    'IDC_OHIF_MG': 'Mammography',
    'IDC_OHIF_MR': 'Magnetic Resonance',
    'IDC_OHIF_NM': 'Nuclear Medicine',
    'IDC_OHIF_PT': 'PET Scan',
    'IDC_SLIM': 'H&E Slide'
}

for st in os.listdir(dh_files_path):
    if 'tcga_pan_can_atlas_2018' in st:
        patient_file = os.path.join(dh_files_path, st, 'data_clinical_patient.txt')
        resource_file = os.path.join(dh_files_path, st, 'data_resource_patient.txt')
        resource_def_file = os.path.join(dh_files_path, st, 'data_resource_definition.txt')
        
        clinical_df = pd.read_csv(patient_file, sep='\t', skiprows=4, dtype=str)
        patient_ids = clinical_df['PATIENT_ID'].unique()    
        
        # Filter resource_df for only matching patients
        filtered_resource_df = resource_df[resource_df['PATIENT_ID'].isin(patient_ids)]
        
        # Write to tab-separated file
        filtered_resource_df = filtered_resource_df.sort_values(by='PATIENT_ID').reset_index(drop=True)
        filtered_resource_df.to_csv(resource_file, sep='\t', index=False)
        print(f"Written {len(filtered_resource_df)} resources to {resource_file}")
        
        # Get unique RESOURCE_IDs for this study that are in definition_map
        resource_ids_in_study = filtered_resource_df['RESOURCE_ID'].unique()
        
        # Build resource definition DataFrame only if there are RESOURCE_IDs
        if len(resource_ids_in_study) > 0:
            resource_def_df = pd.DataFrame({
            'RESOURCE_ID': resource_ids_in_study,
            'DISPLAY_NAME': [definition_map[rid] for rid in resource_ids_in_study],
            'RESOURCE_TYPE': 'PATIENT',
            'DESCRIPTION': [definition_map[rid] for rid in resource_ids_in_study],
            'OPEN_BY_DEFAULT': 'TRUE',
            'PRIORITY': 1
            })
            
            # Write to data_resource_definition.txt file
            resource_def_df.to_csv(resource_def_file, sep='\t', index=False)
            print(f"Written definitions to {resource_def_file}")
        

```

#### Output Files

For each TCGA Pan-Cancer Atlas 2018 study, the script generates two files:

1. **`data_resource_patient.txt`**: Links patients to their imaging studies
   - Columns: `PATIENT_ID`, `RESOURCE_ID`, `URL`
   
2. **`data_resource_definition.txt`**: Defines the resource types available in the study
   - Columns: `RESOURCE_ID`, `DISPLAY_NAME`, `RESOURCE_TYPE`, `DESCRIPTION`, `OPEN_BY_DEFAULT`, `PRIORITY`

#### Viewer URLs

- **OHIF Viewer** (for radiology imaging): `https://viewer.imaging.datacommons.cancer.gov/viewer/{StudyInstanceUID}`
- **SLIM Viewer** (for slide microscopy): `https://viewer.imaging.datacommons.cancer.gov/slim/studies/{StudyInstanceUID}`

#### Notes

- Only patients already present in the clinical data files are included in the resource files
- All resource files are sorted by `PATIENT_ID` for consistency
