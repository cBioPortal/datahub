#!/usr/bin/env bash
# This script runs validation on all public studies.

STUDIES_DIRS=("public" "crdc/gdc")
GIT_REMOTE_URL="git@github.com:cbioportal/datahub.git"
test_reports_location="$HOME/test-reports"

git remote get-url upstream || git remote add upstream "$GIT_REMOTE_URL"
git fetch upstream master

num_studies=${#list_of_study_dirs[@]}

for STUDIES_DIR in "${STUDIES_DIRS[@]}"; do
    for study in $HOME/repo/$STUDIES_DIR/*/; do
        git lfs pull -I "$study"
        validation_command="$HOME/cbioportal-core/scripts/importer/./validateData.py -s $study -p $HOME/repo/.circleci/portalinfo -html $test_reports_location"
        echo $'\nExecuting: '; echo $validation_command
        if sh -c "$validation_command" ; then
            echo "Tests passed successfully for $STUDIES_DIR"
            EXIT_STATUS=0
        else
            echo "Errors found"
            # move errors to ERRORS/ folder:
            erred_studies=$(grep -rnlz "$test_reports_location" -e 'Failed')
            if [ -n "$erred_studies" ]; then
                mv $erred_studies $test_reports_location/ERRORS
                EXIT_STATUS=1
            fi
        fi
    done
done

# Validate resource URLs
echo $'\n\nValidating resource URLs...'
python3 $HOME/repo/.circleci/validate_resource_urls.py
RESOURCE_VALIDATION_STATUS=$?

if [ $RESOURCE_VALIDATION_STATUS -ne 0 ]; then
    EXIT_STATUS=1
fi

exit "$EXIT_STATUS"
