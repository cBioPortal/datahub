#!/usr/bin/env bash
# This script runs validation on all public studies.

STUDIES_DIR="public/"

git remote add upstream git@github.com:cbioportal/datahub.git
git fetch upstream master

git lfs pull -I "public"

num_studies=${#list_of_study_dirs[@]}

test_reports_location="$HOME/test-reports"
validation_command="$HOME/cbioportal/core/src/main/scripts/importer/./validateStudies.py -d $HOME/repo/public/ -p $HOME/repo/.circleci/portalinfo -html $test_reports_location"
echo $'\nExecuting: '; echo $validation_command
if sh -c "$validation_command" ; then
    echo "Tests passed successfully"
    exit 0
else
    echo "Errors found"
    # move errors to ERRORS/ folder:
    erred_studies=`grep -rnlz $test_reports_location -e 'Validation status.*Failed' `
    mv $erred_studies $test_reports_location/ERRORS
    exit 1
fi
