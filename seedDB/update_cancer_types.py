#!/usr/bin/env python3.6

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

"""Update cancer types script - updates cancer types from OncoTree API to an empty cBioPortal database

http://oncotree.mskcc.org/#/home?tab=api

Run with the command line option --help for usage information.
"""

from __future__ import print_function
import requests
import MySQLdb
import sys
import argparse


def eprint(*args, **kwargs):
    """Print error message and exit"""
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)


def retrieve_oncotree_cancer_types():
    """Retrieve cancer types from OncoTree API"""

    print('Retrieving cancer types from OncoTree API')
    request_url = 'http://oncotree.mskcc.org/api/tumorTypes/tree?version=oncotree_latest_stable'
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
    return


def parse_cancer_types_json(cancer_types_json):
    """Parse JSON formatted cancer types received from OncoTree API"""

    print('Parsing JSON formatted cancer types received from OncoTree API')

    def flatten_oncotree(node, node_name):
        """Recursive function to flatten the JSON formatted cancer types"""

        type_of_cancer_id = node_name.lower()
        name = node['name']
        clinical_trial_keywords = node['name'].lower()
        dedicated_color = node['color']
        short_name = node_name
        parent = node['parent'].lower()

        cancer_type = [type_of_cancer_id, name, clinical_trial_keywords, dedicated_color, short_name, parent]
        cancer_types.append(cancer_type)

        if len(node['children'].values()) > 0:
            for child_node in node['children'].keys():
                flatten_oncotree(node['children'][child_node], child_node)

    # Save cancer types as tuples in a list
    cancer_types = list()

    # The root node, 'TISSUE' can be skipped
    for child in cancer_types_json['TISSUE']['children'].keys():
        #     print child
        flatten_oncotree(cancer_types_json['TISSUE']['children'][child], child)

    return cancer_types


def get_portal_properties(portal_properties_filename):
    """Retrieve database settings from portal.properties"""

    print('Retrieving database settings from portal.properties')

    portal_properties = {}
    with open(portal_properties_filename, 'r') as portal_properties_file:
        for line in portal_properties_file:

            # Skip line if its blank or a comment
            line = line.strip()
            if len(line) == 0 or line.startswith('#'):
                continue

            # Check whether the line contains a single property
            if len(line.split('=')) > 2:
                continue

            # Read relevant portal properties
            property_key, property_value = line.split('=')
            if property_key == 'db.host':
                # Check if host and port can be read.
                if len(property_value.split(':')) != 2:
                    eprint('Unable to read host from db.host in portal.properties.\n'
                           'Expected format: host:port\n'
                           'Found: %s' % property_value)
                host, port = property_value.split(':')

                # localhost has to be converted to 127.0.0.1
                if host == 'localhost':
                    host = '127.0.0.1'
                portal_properties['host'] = host
                portal_properties['port'] = int(port)

            elif property_key == 'db.portal_db_name':
                portal_properties['database'] = property_value

            elif property_key == 'db.user':
                portal_properties['user'] = property_value

            elif property_key == 'db.password':
                portal_properties['passwd'] = property_value

    required_properties = ['host', 'user', 'passwd', 'database', 'port']
    for required_property in required_properties:
        if required_property not in portal_properties:
            eprint('Unable to extract %s from portal.properties')
    return portal_properties


def insert_cancer_types(cancer_types, portal_properties):
    """Insert cancer types in cBioPortal database"""

    print('Inserting cancer types in cBioPortal database')
    db = MySQLdb.connect(host=portal_properties['host'],
                         user=portal_properties['user'],
                         passwd=portal_properties['passwd'],
                         db=portal_properties['database'],
                         port=portal_properties['port'])
    cursor = db.cursor()

    # Check whether the database is empty
    cursor.execute('SELECT * FROM cbioportal.cancer_study')
    cancer_studies = cursor.fetchall()
    if len(cancer_studies) > 0:
        eprint('cancer_study table is not empty. Please use an empty cBioPortal database when updating cancer '
               'types. Afterwards this empty database can be exported to create a new seed database.\n'
               'https://github.com/cBioPortal/datahub/tree/master/seedDB')

    # Remove foreign key restrictions
    cursor.execute('ALTER TABLE cancer_study DROP FOREIGN KEY cancer_study_ibfk_1')
    cursor.execute('ALTER TABLE sample DROP FOREIGN KEY sample_ibfk_2')

    # Remove previous cancer types
    cursor.execute('TRUNCATE type_of_cancer')

    # Insert new cancer types
    sql = 'INSERT INTO type_of_cancer ' \
          '(TYPE_OF_CANCER_ID, NAME, CLINICAL_TRIAL_KEYWORDS, DEDICATED_COLOR, SHORT_NAME, PARENT) ' \
          'VALUES (%s, %s, %s, %s, %s, %s)'
    cursor.executemany(sql, cancer_types)

    # Restore foreign key restrictions
    cursor.execute('ALTER TABLE cancer_study ADD CONSTRAINT cancer_study_ibfk_1 FOREIGN KEY (TYPE_OF_CANCER_ID) '
                   'REFERENCES type_of_cancer (TYPE_OF_CANCER_ID)')
    cursor.execute('ALTER TABLE sample ADD CONSTRAINT sample_ibfk_2 FOREIGN KEY (TYPE_OF_CANCER_ID) REFERENCES '
                   'type_of_cancer (TYPE_OF_CANCER_ID)')
    db.commit()


def main(portal_properties_filename):
    # First retrieve data base settings from portal properties file
    cancer_types_json = retrieve_oncotree_cancer_types()
    cancer_types = parse_cancer_types_json(cancer_types_json)
    portal_properties = get_portal_properties(portal_properties_filename)
    insert_cancer_types(cancer_types, portal_properties)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='-p <portal_properties_file>',
                                     description='This code updates the cancer types in an empty cBioPortal database. '
                                                 'Afterwards this database can be exported to create a new seed '
                                                 'database.')

    arguments = parser.add_argument_group('Named arguments')
    arguments.add_argument('-p', '--portal_properties_file',
                           required=True,
                           help='Path to portal.properties file')

    args = parser.parse_args()
    main(args.portal_properties_file)
