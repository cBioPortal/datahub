"""
Check if studies on datahub are imported in live public portal

Currently comparing study folder name on datahub vs live public portal studies
endpoint. Should prolly look at actual `cancer_study_identifier: study_name` in
meta_study.txt file, but this seems to work.
"""
import requests
import sys

FAIL = '\033[91m'
END = '\033[0m'

public_study_folders = requests.get("https://api.github.com/repos/cBioPortal/datahub/contents/public")
datahub_study_names = set(map(lambda x: x["name"], public_study_folders.json()))

live_studies = requests.get("https://www.cbioportal.org/api/studies")
live_study_names = set(map(lambda x: x["studyId"], live_studies.json()))

print("Number of live studies: {}".format(len(live_study_names)))
print("Number of studies on datahub: {}".format(len(datahub_study_names)))

errors = 0
if len(datahub_study_names - live_study_names) > 0:
    errors += 1
    print(FAIL, "Not all studies on datahub are imported: {}".format(datahub_study_names - live_study_names), END, sep='')

if len(live_study_names - datahub_study_names) > 0:
    errors += 1
    print(FAIL, "Not all studies on www.cbioportal.org are in datahub: {}".format(live_study_names - datahub_study_names), END, sep='')

if errors > 0:
    sys.exit(1)
else:
    sys.exit(0)
