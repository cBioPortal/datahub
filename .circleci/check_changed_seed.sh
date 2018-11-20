#!/usr/bin/env bash
# This script detects if seed database file is changed and triggers the validation accordingly

SEED_PREFIX="seedDB/seed-cbioportal_"

git remote add upstream git@github.com:cbioportal/datahub.git
git fetch upstream master
files_changing=`git diff --name-only --diff-filter=ACMRU upstream/master`

# Remove upstream remote here because python code will create it again.
git remote rm upstream

for file_changing in $files_changing
do
  echo "file > [$file_changing]"
  if [[ $file_changing == *$SEED_PREFIX* ]]; then
    docker network create cbio-net
    docker run -t -d --net=cbio-net --name python_circleci -v /var/run/docker.sock:/var/run/docker.sock -v /home/circleci/repo/:/home/circleci/repo/:rw -w /home/circleci/repo/.circleci circleci/python:3.6
    docker exec python_circleci bash install_dependencies.sh
    docker exec -t python_circleci sudo python validate_changed_seed.py
  fi
done
