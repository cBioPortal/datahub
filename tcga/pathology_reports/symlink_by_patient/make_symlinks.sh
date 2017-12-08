#!/bin/sh
# In order to have a simple URL for getting the pathology reports by patient
# id, we create these symlinks with PATIENT_ID.number
# there is only one case with 3 path reports so the cmd below works
rm TCGA*; for f in $(find .. -name '*.pdf'); do ln -s $f "$(basename $f | cut -d. -f1).0" || ln -s $f "$(basename $f | cut -d. -f1).1" || ln -s $f "$(basename $f | cut -d. -f1).2"; done
