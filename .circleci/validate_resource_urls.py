#!/usr/bin/env python3
"""Check resource URLs in study directories without downloading their bodies."""

import argparse
import csv
import http.client
import ipaddress
from pathlib import Path
import socket
import ssl
import sys
from urllib.parse import quote, urljoin, urlsplit


TIMEOUT = 10
MAX_REDIRECTS = 5
REDIRECT_STATUSES = {301, 302, 303, 307, 308}
LFS_HEADER = 'version https://git-lfs.github.com/spec/v1'


class UnsafeURL(ValueError):
    """A fixed diagnostic that contains no input URL or credentials."""


class PublicConnection(http.client.HTTPConnection):
    """Connect to the checked IP while retaining the hostname for Host and TLS."""

    def __init__(self, hostname, port, address, tls, timeout):
        super().__init__(hostname, port, timeout=timeout)
        self.address = address
        self.tls = tls

    def connect(self):
        sock = socket.create_connection((self.address, self.port), self.timeout)
        if self.tls:
            try:
                sock = ssl.create_default_context().wrap_socket(
                    sock, server_hostname=self.host)
            except BaseException:
                sock.close()
                raise
        self.sock = sock


def public_endpoint(url):
    """Reject credentials and non-public destinations before opening a socket."""
    if any(ord(character) < 32 or ord(character) == 127 for character in url):
        raise UnsafeURL('URL contains control characters')
    parsed = urlsplit(url)
    if parsed.scheme not in ('http', 'https') or not parsed.hostname:
        raise UnsafeURL('URL must start with http:// or https://')
    if parsed.username is not None or parsed.password is not None:
        raise UnsafeURL('URLs with credentials are not allowed')
    hostname = parsed.hostname.encode('idna').decode('ascii')
    normalized_hostname = hostname.rstrip('.').lower()
    if ('%' in hostname or normalized_hostname.endswith('.localhost') or
            normalized_hostname == 'localhost'):
        raise UnsafeURL('Local or scoped hostnames are not allowed')
    port = parsed.port
    if port is None:
        port = 443 if parsed.scheme == 'https' else 80
    if port not in (80, 443):
        raise UnsafeURL('Only public web ports 80 and 443 are allowed')

    try:
        addresses = [ipaddress.ip_address(hostname)]
    except ValueError:
        addresses = [ipaddress.ip_address(result[4][0]) for result in
                     socket.getaddrinfo(hostname, port, type=socket.SOCK_STREAM)]
    if not addresses:
        raise UnsafeURL('Hostname has no addresses')
    for address in addresses:
        mapped = getattr(address, 'ipv4_mapped', None)
        if (not address.is_global or address.is_multicast or
                (mapped is not None and not mapped.is_global)):
            raise UnsafeURL('URL resolves to a non-public address')
        # Translation/transition addresses can hide an IPv4 destination.
        if isinstance(address, ipaddress.IPv6Address) and (
                address.sixtofour is not None or address.teredo is not None or
                address in ipaddress.ip_network('64:ff9b::/96') or
                address in ipaddress.ip_network('64:ff9b:1::/48')):
            raise UnsafeURL('IPv6 transition addresses are not allowed')
    return parsed, hostname, port, str(addresses[0])


def check_url(url, timeout=TIMEOUT):
    """Return None for HTTP 200, or a diagnostic that never exposes the URL."""
    current_url = url
    try:
        for redirect_count in range(MAX_REDIRECTS + 1):
            parsed, hostname, port, address = public_endpoint(current_url)
            connection = PublicConnection(
                hostname, port, address, parsed.scheme == 'https', timeout)
            response = None
            try:
                target = quote(parsed.path or '/', safe="/%:@!$&'()*+,;=-._~")
                if parsed.query:
                    target += '?' + quote(parsed.query, safe="/?%:@!$&'()*+,;=-._~")
                connection.request('GET', target, headers={
                    'User-Agent': 'cBioPortal-datahub-resource-validator',
                    'Accept-Encoding': 'identity',
                })
                response = connection.getresponse()
                status = response.status
                location = response.getheader('Location')
            finally:
                if response is not None:
                    response.close()
                connection.close()

            if status == 200:
                return None
            if status not in REDIRECT_STATUSES:
                return 'HTTP {} (expected 200)'.format(status)
            if not location:
                return 'HTTP {} redirect has no Location header'.format(status)
            if redirect_count == MAX_REDIRECTS:
                return 'Too many redirects'
            next_url = urljoin(current_url, location)
            if parsed.scheme == 'https' and urlsplit(next_url).scheme == 'http':
                return 'HTTPS redirect downgrades to HTTP'
            current_url = next_url
    except UnsafeURL as error:
        return str(error)
    except ValueError as error:
        # Parser exceptions may contain a URL or credential; use a fixed message.
        return 'Invalid or unsafe URL ({})'.format(type(error).__name__)
    except (OSError, http.client.HTTPException, UnicodeError) as error:
        return 'Request failed ({})'.format(type(error).__name__)


def validate_resource_file(path, cache):
    """Read a raw TSV file, preserving physical line numbers in diagnostics."""
    errors = []
    try:
        with path.open(encoding='utf-8-sig', newline='') as source:
            reader = csv.reader(source, delimiter='\t', quoting=csv.QUOTE_NONE)
            header = None
            for row in reader:
                if not row or not any(cell.strip() for cell in row) or row[0].startswith('#'):
                    continue
                if header is None:
                    if row[0] == LFS_HEADER:
                        return ['{}: Git LFS pointer; download the study data first'.format(path)]
                    header = [cell.strip() for cell in row]
                    if len(header) != len(set(header)):
                        return ['{}:{}: Duplicate column headers'.format(path, reader.line_num)]
                    if 'URL' not in header:
                        if path.name == 'data_resource_definition.txt':
                            return []  # Definitions describe resources; they have no URLs.
                        return ['{}:{}: Missing URL column'.format(path, reader.line_num)]
                    url_index = header.index('URL')
                    continue
                if len(row) != len(header):
                    errors.append('{}:{}: Row does not match the header'.format(path, reader.line_num))
                    continue
                url = row[url_index].strip()
                if url not in cache:
                    cache[url] = check_url(url)
                if cache[url] is not None:
                    errors.append('{}:{}: {}'.format(path, reader.line_num, cache[url]))
            if header is None:
                errors.append('{}: Empty resource file'.format(path))
    except (OSError, UnicodeError, csv.Error) as error:
        errors.append('{}: Cannot read resource file ({})'.format(path, type(error).__name__))
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root-directory', type=Path,
                        default=Path(__file__).resolve().parents[1])
    parser.add_argument('studies', nargs='+', type=Path,
                        help='Study directories, absolute or relative to the repository')
    args = parser.parse_args(argv)
    root = args.root_directory.resolve()
    errors = []
    cache = {}
    files_checked = 0
    for study in dict.fromkeys(args.studies):
        directory = root / study
        if not directory.resolve().is_relative_to(root) or not directory.is_dir():
            errors.append('{}: Study must be a directory inside the repository'.format(study))
            continue
        # Only current staging files; archived files and reports are not inputs.
        for path in sorted(directory.glob('data_resource_*.txt')):
            if path.is_symlink() or not path.resolve().is_relative_to(root):
                errors.append('{}: Resource file must stay inside the repository'.format(path))
                continue
            files_checked += 1
            errors.extend(validate_resource_file(path, cache))
    for error in errors:
        print(error, file=sys.stderr)
    print('Checked {} resource file(s), {} unique URL(s), {} error(s)'.format(
        files_checked, len(cache), len(errors)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
