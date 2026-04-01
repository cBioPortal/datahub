#!/usr/bin/env python3
"""
Validate resource URLs in changed data_resource_*.txt files.
Only checks files that were modified in the current branch.
"""
import os
import sys
import subprocess
import requests
import csv
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TIMEOUT = 10

def check_url(url, timeout=TIMEOUT):
    """Check if a URL returns a 200 status code."""
    if not url or url.strip().lower() in ['[not applicable]', '[not available]', '[pending]', '[discrepancy]', '[completed]', '[null]', '', 'na']:
        return True  # Skip empty/null values
    
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True, stream=True)
        response.close()
        return response.status_code == 200
    except requests.RequestException:
        return False

def validate_resource_file(filepath):
    """Validate all URLs in a resource file."""
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, delimiter='\t')
            
            if not reader.fieldnames or 'URL' not in reader.fieldnames:
                return errors
            
            for row_num, row in enumerate(reader, start=2):  # start at 2 because row 1 is header
                url = row.get('URL', '').strip()
                
                if not url or url.lower() in ['[not applicable]', '[not available]', '[pending]', '[discrepancy]', '[completed]', '[null]', '', 'na']:
                    continue
                
                if not check_url(url):
                    errors.append({
                        'file': filepath,
                        'line': row_num,
                        'url': url,
                        'status': f'URL returned non-200 status code or is unreachable'
                    })
    except Exception as e:
        errors.append({
            'file': filepath,
            'error': f'Error reading file: {str(e)}'
        })
    
    return errors

def get_changed_files():
    """Get list of changed resource files from git."""
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', '--diff-filter=ACMRU', 'upstream/master'],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True
        )
        files = result.stdout.strip().split('\n')
        return [f for f in files if 'data_resource_' in f and f.endswith('.txt')]
    except Exception:
        return []

def main():
    """Find and validate changed resource files."""
    changed_files = get_changed_files()
    
    if not changed_files:
        print("No resource files changed")
        return 0
    
    all_errors = []
    
    for filename in changed_files:
        filepath = REPO_ROOT / filename
        if filepath.is_file():
            errors = validate_resource_file(str(filepath))
            all_errors.extend(errors)
    
    # Report errors
    if all_errors:
        print("Resource URL validation errors found:")
        for error in all_errors:
            if 'error' in error:
                print(f"  {error['file']}: {error['error']}")
            else:
                print(f"  {error['file']}:{error['line']}: {error['status']}")
                print(f"    URL: {error['url']}")
        return 1
    else:
        if changed_files:
            print(f"Validated {len(changed_files)} changed resource file(s) - all URLs returned 200 status code")
        return 0

if __name__ == '__main__':
    sys.exit(main())
