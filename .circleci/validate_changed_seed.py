#!/usr/bin/python3

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

"""Validate changed seed - Validate if the new seed database does not contain any of the checked errors.
"""

import MySQLdb
import sys
import os
import git
import docker
import urllib.request
import time
import _mysql_exceptions
from time import gmtime, strftime


def eprint(*args, **kwargs):
    """Print error message and exit"""
    print(*args, file=sys.stderr, **kwargs)
    sys.exit(1)


def check_changed_seed():
    """Check whether the seed database files are changed"""

    # Check whether the seed has changed
    repo = git.Repo(os.path.dirname(os.getcwd()))
    remote = repo.create_remote('upstream', url='https://github.com/cBioPortal/datahub/')
    remote.fetch()
    changed_files = repo.git.diff('upstream/master', name_only=True, diff_filter='ACMRU').split('\n')

    seed_files = set()
    for changed_file in changed_files:
        if 'seedDB/seed-cbioportal_' in changed_file:
            seed_files.add(changed_file)

    if len(seed_files) == 0:
        print('Seed database files are not changed. It is not necessary to the the seed database.')
        sys.exit(0)
    elif len(seed_files) > 1:
        eprint('Found multiple seed databases. Unable to test whether seed is updated correctly.')

    seed_file = list(seed_files)[0]
    return seed_file


def start_mysql_database(seed_location):
    """Start a mysql database with the seed files"""

    # Prepare to start a mysql database with cbioportal seed
    client = docker.from_env()
    database_location = os.path.join(os.getcwd(), 'db_files')
    schema_url = 'https://raw.githubusercontent.com/cBioPortal/cbioportal/master/db-scripts/src/main/resources/cgds.sql'
    schema_location = os.path.join(os.getcwd(), 'cgds.sql')
    urllib.request.urlretrieve(schema_url, schema_location)
    docker_sock_location = '/var/run/docker.sock'

    # Start database
    client.containers.run("mysql:5.7",
                          name='cbioDB',
                          network='cbio-net',
                          detach=True,
                          environment={'MYSQL_ROOT_PASSWORD': 'P@ssword1',
                                       'MYSQL_USER': 'cbio',
                                       'MYSQL_PASSWORD': 'P@ssword1',
                                       'MYSQL_DATABASE': 'cbioportal',
                                       },
                          ports={'3306/tcp': 3306},
                          volumes={database_location: {'bind': '/var/lib/mysql/', 'mode': 'rw'},
                                   schema_location: {'bind': '/docker-entrypoint-initdb.d/cgds.sql', 'mode': 'ro'},
                                   seed_location: {'bind': '/docker-entrypoint-initdb.d/seed_part1.sql.gz',
                                                   'mode': 'ro'},
                                   docker_sock_location: {'bind': docker_sock_location, 'mode': 'rw'}
                                   },
                          )

    # Check then the docker container is up
    connected = False
    database = ''
    tries = 0
    max_tries = 10
    while not connected:
        try:
            tries += 1
            database = MySQLdb.connect(host='cbioDB', port=3306, user='cbio', passwd='P@ssword1', db='cbioportal',
                                       connect_timeout=500)
            connected = True
        except _mysql_exceptions.OperationalError:
            print(strftime("%H:%M:%S", gmtime()) + ' Database container is not ready (%s/%s)' % (tries, max_tries))
            if tries == max_tries:
                eprint('Cannot connect to MySQL database container')
            time.sleep(60)
            pass

    print(strftime("%H:%M:%S", gmtime()) + ' Database container is ready!\n')
    return database


def check_gene_table(cursor):
    """Check whether the seed database contains values."""

    cursor.execute('SELECT count(*) FROM cbioportal.gene')
    number_genes = cursor.fetchone()[0]
    if number_genes == 0:
        eprint('No genes in seed database')
    elif number_genes < 55000:
        # The seed in September 2018 contains 60070 genes.
        eprint('Unexpected low number of genes in seed database: %s' % number_genes)
    else:
        print('Genes in seed database: %s' % number_genes)


def check_gene_alias_table(cursor):
    """Check whether the gene alias table contains values."""

    cursor.execute('SELECT count(*) FROM cbioportal.gene_alias')
    number_aliases = cursor.fetchone()[0]
    if number_aliases == 0:
        eprint('No genes in seed database')
    elif number_aliases < 65000:
        # The seed in September 2018 contains 66840 gene aliases.
        eprint('Unexpected low number of gene aliases in seed database: %s' % number_aliases)
    else:
        print('Gene aliases in seed database: %s' % number_aliases)


def check_cancer_type_table(cursor):
    """ Check whether the cancer types table contains values."""

    cursor.execute('SELECT count(*) FROM cbioportal.type_of_cancer')
    number_cancer_types = cursor.fetchone()[0]
    if number_cancer_types == 0:
        eprint('No cancer types in seed database')
    elif number_cancer_types < 800:
        # The seed in September 2018 contains 839 cancer types.
        eprint('Unexpected low number of cancer types in seed database: %s' % number_cancer_types)
    else:
        print('Cancer types in seed database: %s' % number_cancer_types)


def check_gene_symbols_unique(cursor):
    """ Check whether the gene symbols are unique."""

    cursor.execute('SELECT HUGO_GENE_SYMBOL FROM cbioportal.gene')
    gene_symbols = [x[0] for x in cursor.fetchall()]
    if len(gene_symbols) != len(list(set(gene_symbols))):
        # Find the duplicate symbols
        seen = {}
        duplicates = []
        for symbol in gene_symbols:
            if symbol not in seen:
                seen[symbol] = 1
            else:
                if seen[symbol] == 1:
                    duplicates.append(symbol)
                seen[symbol] += 1
        eprint('Gene symbols in HUGO_GENE_SYMBOL column in gene table are not unique:\n%s' % ", ".join(duplicates))
    else:
        print('Gene symbols in HUGO_GENE_SYMBOL column in gene table are unique')


def check_number_of_studies(cursor):
    """ Check whether the number of studies is equal to zero."""

    cursor.execute('SELECT count(*) FROM cbioportal.cancer_study')
    number_studies = cursor.fetchone()[0]
    if number_studies != 0:
        eprint('This seed database contains %s studies' % number_studies)
    else:
        print('0 studies found in seed database')


def check_info_table(cursor):
    """ Check whether the info table contains 2 values"""

    cursor.execute('SELECT * FROM cbioportal.info')
    info_values = cursor.fetchall()[0]
    if not (len(info_values)) == 2:
        eprint('The "info" table contains other than 2 values: %s' % info_values)
    elif info_values[1] is None or info_values[1] == '':
        eprint('Missing gene set version in seed database. This is a manual addition to the automated database dump.\n'
               'See step 6 at https://github.com/cBioPortal/datahub/blob/master/seedDB/Update-Seed-Database.md')
    else:
        print('The "info" table is correctly filled.\n'
              'GENESET_VERSION in info table: %s\n'
              'These tests ran with cgds.sql from cBioPortal master branch, schema: %s' % (info_values[1], info_values[0]))


def main():
    # Retrieve the location of the seed
    seed_location = os.path.join(os.path.dirname(os.getcwd()), check_changed_seed())

    # Start the cbioportal mysql database in a Docker container
    database = start_mysql_database(seed_location)
    cursor = database.cursor()

    # Check if gene table not empty
    check_gene_table(cursor)

    # Check if gene alias table not empty
    check_gene_alias_table(cursor)

    # Check if cancer type table not empty
    check_cancer_type_table(cursor)

    # Check whether the hugo gene symbols in the gene table are unique
    check_gene_symbols_unique(cursor)

    # Check the number of studies, which should be 0
    check_number_of_studies(cursor)

    # Check the info table for empty values
    check_info_table(cursor)

    print('\n')
    print('Tests completed. The updated seed database seems valid.')


if __name__ == '__main__':
    main()
