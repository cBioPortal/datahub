#!/usr/bin/env python3
"""
Validate that all resource URLs in data_resource_*.txt files return HTTP 200 status code.
"""
import os
import sys
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

def main():
    """Find and validate all resource files."""
    study_dirs = [REPO_ROOT / 'public', REPO_ROOT / 'crdc' / 'gdc']
    all_errors = []
    
    for study_dir in study_dirs:
        if not study_dir.exists() or not study_dir.is_dir():
            continue
        
        # Find all data_resource_*.txt files
        for root, dirs, files in os.walk(str(study_dir)):
            for file in files:
                if file.startswith('data_resource_') and file.endswith('.txt'):
                    filepath = os.path.join(root, file)
                    errors = validate_resource_file(filepath)
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
        print("All resource URLs validated successfully (returned 200 status code)")
        return 0

if __name__ == '__main__':
    sys.exit(main())
