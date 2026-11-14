# Resource URL validation

The CircleCI changed-study and weekly all-study jobs check the `URL` column in
current `data_resource_*.txt` staging files after downloading the study's Git LFS
data. A URL succeeds only if its final GET response is HTTP 200. Definitions
without a `URL` column are skipped; the core validator still validates their
structure. Files under `archived_files` and other subdirectories are not checked.

The checker reports the filename, physical line number, and HTTP status or error
category. It returns exit code 1 on any failure, including missing URL headers,
malformed rows, unreadable files, and undownloaded Git LFS pointers. Blank and
placeholder URL values are invalid, consistent with the required URL field.
Repeated URLs are checked once per invocation; failures are reported for each
affected row.

To check a study from the repository root (this contacts its resource servers):

```sh
python .circleci/validate_resource_urls.py public/study_id
```

Multiple study directories can be supplied, including `crdc/gdc/study_id`.
Download their LFS data first using the instructions in the repository README.
No additional Python packages are required by this checker.

To run only the offline tests, with no study downloads or external HTTP requests:

```sh
python -m unittest discover -s tests -p 'test_resource_urls.py' -v
```

## Network behavior

- Uses GET for compatibility with servers that do not support HEAD, and closes
  the response after reading headers without downloading or decompressing its body.
- Uses a 10-second socket timeout and at most five redirects. DNS resolution uses
  the operating system resolver and is not covered by the socket timeout.
- Accepts HTTP/HTTPS on ports 80/443; rejects credentials, non-public IP addresses,
  mixed public/private DNS answers, and IPv6 transition addresses.
- Connects directly to a checked IP, preserving the hostname for Host and verified
  HTTPS certificates. It rechecks every redirect and refuses HTTPS-to-HTTP downgrades.
- Does not use environment proxies, local credential files, cookies, or authentication.
- Omits URLs and exception text from diagnostics to avoid exposing signed query strings.

HTTP 200 proves availability at check time, not that the returned content is the
intended resource. Temporary outages, rate limits, or authentication requirements
will fail validation. The network checks complement isolated CI runners and egress
controls; they do not replace them.
