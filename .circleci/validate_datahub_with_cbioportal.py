#!/usr/bin/env python3

# Copyright (c) 2018 The Hyve B.V.
# This code is licensed under the GNU Affero General Public License (AGPL),
# version 3, or (at your option) any later version.
#
# This file is part of cBioPortal.
#
# cBioPortal is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""Validate if cBioPortal Datahub and www.cbioportal.org contain the same studies

Used by CircleCI to test automatically.
"""

import requests
import sys
import os


def eprint(*args, **kwargs):
    """Function to print error messages"""
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)


def retrieve_study_ids_cbioportal():
    print('Retrieving study IDs from cBioPortal API')
    request_url = 'http://www.cbioportal.org/api/studies?projection=ID&pageSize=10000000&pageNumber=0&direction=ASC'
    request_headers = {'Accept': 'application/json'}
    request = requests.get(url=request_url, headers=request_headers)
    if request.ok:
        result_json = request.json()
        return result_json

    else:
        if request.status_code == 404:
            print('Error 404')
            sys.exit(1)
        else:
            request.raise_for_status()


def retrieve_study_ids_datahub():
    study_dir = os.path.join(os.path.dirname(os.getcwd()), 'public')
    study_ids_datahub = set((os.listdir(study_dir)))
    return study_ids_datahub


def compare_study_ids(study_ids_cbioportal, study_ids_datahub):
    if study_ids_cbioportal == study_ids_datahub:
        print('cBioPortal Datahub and cbioportal.org contain the same studies!')
    else:
        error_message = ''

        # Studies that are only on cbioportal.org
        only_cbioportal = study_ids_cbioportal.difference(study_ids_datahub)
        if len(only_cbioportal) > 0:
            error_message = error_message +\
                            ("\ncbioportal.org contains studies which are not on cBioPortal Datahub:\n%s\n" %
                             "\n".join(sorted(list(only_cbioportal))))

        # Studies that are only on Datahub
        only_datahub = study_ids_datahub.difference(study_ids_cbioportal)
        if len(only_datahub) > 0:
            error_message = error_message + \
                            ("\ncBioPortal Datahub contains studies which are not on cbioportal.org:\n%s\n" %
                             "\n".join(sorted(list(only_datahub))))
        eprint(error_message)


def main():
    # Retrieve study IDs from cbioportal.org
    study_ids_cbioportal_json = retrieve_study_ids_cbioportal()

    # Parse study IDs
    study_ids_cbioportal = []
    for study in study_ids_cbioportal_json:
        study_id = study['studyId']
        study_ids_cbioportal.append(study_id)
    study_ids_cbioportal = set(study_ids_cbioportal)

    # Retrieve study IDs from datahub
    study_ids_datahub = retrieve_study_ids_datahub()

    # Compare study IDs
    compare_study_ids(study_ids_cbioportal, study_ids_datahub)


if __name__ == '__main__':
    main()
