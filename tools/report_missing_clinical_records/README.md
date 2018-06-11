### Usage
Collect and add missing samples to `data_clinical_sample.txt` from genomic profiles.

### Command Line
```
  -h, --help            show this help message and exit
  -d STUDYDIR, --study-directory=STUDYDIR
                        path to study directory
  -a, --add-missing-records
                        flag for adding missing records to clinical files
  -r, --remove-normal-records
                        flag for removing normal records from data files
  -o OUTPUTDIR, --output-data-directory=OUTPUTDIR
                        output directory used after removing normal records
                        from data
```

### Example
```
mkdir path/to/output_folder
cd path/to/study
python report-missing-clinical-records.py -d . -ar -o path/to/output_folder
```

### Notes
After the running script, the basic clinical info for the added sample should still be filled in, such as `ONCOTREE_CODE`

