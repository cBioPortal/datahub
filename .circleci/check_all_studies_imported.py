"""
Check if studies on datahub are imported in live public portal

Currently comparing study folder name on datahub vs live public portal studies
endpoint. Should prolly look at actual `cancer_study_identifier: study_name` in
meta_study.txt file, but this seems to work.

Also tracks added/removed studies in the public portal.
"""

import requests
import sys
import os

FAIL = '\033[91m'
END = '\033[0m'

public_study_folders = requests.get("https://api.github.com/repos/cBioPortal/datahub/contents/public")
gdc_study_folders = requests.get("https://api.github.com/repos/cBioPortal/datahub/contents/crdc/gdc")
datahub_study_names = set(map(lambda x: x["name"], public_study_folders.json()))
datahub_study_names |= set(map(lambda x: x["name"], gdc_study_folders.json()))

live_studies = requests.get("https://www.cbioportal.org/api/studies")
live_study_names = set(map(lambda x: x["studyId"], live_studies.json()))

# Define the values for both study counts
live_count = len(live_study_names)
datahub_count = len(datahub_study_names)

print("Number of live studies:", live_count)
print("Number of studies on datahub:", datahub_count)

errors = 0
if len(datahub_study_names - live_study_names) > 0:
    errors += 1
    print(FAIL, "Not all studies on datahub are imported: {}".format(datahub_study_names - live_study_names), END, sep='')

if len(live_study_names - datahub_study_names) > 0:
    errors += 1
    print(FAIL, "Not all studies on www.cbioportal.org are in datahub: {}".format(live_study_names - datahub_study_names), END, sep='')

# Save the previous study list next to this script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LAST_IDS_FILE = os.path.join(SCRIPT_DIR, "last_live_study_ids.txt")

# Track changes to the number of studies in the portal
if os.path.exists(LAST_IDS_FILE):
    with open(LAST_IDS_FILE, "r") as f:
        raw = f.read().strip()
        last_ids = set(raw.split("\n")) if raw else set()
else:
    last_ids = None

if last_ids is None:
    print("No previous study list found (first run).")
else:
    last_live_count = len(last_ids)
    diff = live_count - last_live_count

    if diff > 0:
        print(f"Live studies increased by {diff}.")
    elif diff < 0:
        print(f"Live studies decreased by {abs(diff)}.")
    else:
        print("No change in number of live studies.")

    added = live_study_names - last_ids
    removed = last_ids - live_study_names

    if added:
        print("\nAdded studies since last run:")
        for s in sorted(added):
            print("  +", s)

    if removed:
        print("\nRemoved studies since last run:")
        for s in sorted(removed):
            print("  -", s)

    if not added and not removed:
        print("No changes in study list.")

# Save current live study list for next run
try:
    with open(LAST_IDS_FILE, "w") as f:
        f.write("\n".join(sorted(live_study_names)))
    print("Saved current study list to:", LAST_IDS_FILE)
except Exception as e:
    print("ERROR saving study list:", e)
