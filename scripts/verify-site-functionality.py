#!/usr/bin/env python3
"""
Site Functionality Verification Script

This script verifies that the Hugo site is functioning properly after 
implementing privacy-safe measures.
"""

import os
import sys
import subprocess
from pathlib import Path


def test_hugo_build():
    """Test that the Hugo site builds without errors"""
    print("Testing Hugo site build...")
    result = subprocess.run(['hugo'], capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"ERROR: Hugo build failed with return code {result.returncode}")
        print(f"Error output: {result.stderr}")
        return False
    
    print("✓ Hugo site builds successfully")
    return True


def test_public_directory_exists():
    """Test that the public directory exists after build"""
    print("Testing public directory exists...")
    public_dir = Path('public')
    
    if not public_dir.exists():
        print("ERROR: Public directory does not exist after build")
        return False
    
    print("✓ Public directory exists after build")
    return True


def test_html_files_generated():
    """Test that HTML files were generated"""
    print("Testing HTML files were generated...")
    public_dir = Path('public')
    
    html_files = list(public_dir.rglob('*.html'))
    
    if not html_files:
        print("ERROR: No HTML files were generated")
        return False
    
    print(f"✓ Found {len(html_files)} HTML files generated")
    return True


def test_index_file_exists():
    """Test that the index.html file exists"""
    print("Testing index.html file exists...")
    index_file = Path('public/index.html')
    
    if not index_file.exists():
        print("ERROR: index.html file does not exist")
        return False
    
    print("✓ index.html file exists")
    return True


def test_css_and_js_files_exist():
    """Test that CSS and JS files exist to ensure site styling still works"""
    print("Testing CSS and JS files exist...")
    public_dir = Path('public')
    
    css_files = list(public_dir.rglob('*.css'))
    js_files = list(public_dir.rglob('*.js'))
    
    if not css_files and not js_files:
        print("WARNING: No CSS or JS files found, site may not be styled properly")
        return True  # Not a failure, just a warning
    
    print(f"✓ Found {len(css_files)} CSS files and {len(js_files)} JS files")
    return True


def test_no_tracking_in_html():
    """Additional check: ensure no tracking scripts are in the HTML"""
    print("Testing that no tracking scripts are in HTML files...")
    public_dir = Path('public')
    
    tracking_indicators = [
        'google-analytics',
        'google.com/analytics',
        'facebook.com/tr',
        'gtm.js',
        'gtag',
        'hotjar',
        'matomo',
        'piwik',
        'hubspot',
    ]
    
    problematic_files = []
    
    for html_file in public_dir.rglob('*.html'):
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read().lower()
            for indicator in tracking_indicators:
                if indicator in content:
                    problematic_files.append({
                        'file': str(html_file),
                        'indicator': indicator
                    })
    
    if problematic_files:
        print(f"ERROR: Found tracking indicators in {len(problematic_files)} files:")
        for item in problematic_files:
            print(f"  - {item['file']}: {item['indicator']}")
        return False
    
    print("✓ No tracking scripts found in HTML files")
    return True


def run_functionality_verification():
    """Run all functionality verification tests"""
    print("Starting site functionality verification...")
    print()
    
    tests = [
        test_hugo_build,
        test_public_directory_exists,
        test_html_files_generated,
        test_index_file_exists,
        test_css_and_js_files_exist,
        test_no_tracking_in_html
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
            print()  # Add spacing between tests
        except Exception as e:
            print(f"ERROR: Test {test.__name__} failed with exception: {e}")
            failed += 1
            print()
    
    print(f"Tests completed: {passed} passed, {failed} failed")
    
    return failed == 0


def main():
    """Main execution function"""
    success = run_functionality_verification()
    
    if success:
        print("\\n✓ All functionality tests passed! Site is working properly after privacy-safe implementation.")
        sys.exit(0)
    else:
        print("\\n✗ Some functionality tests failed. Site may have issues after privacy-safe implementation.")
        sys.exit(1)


if __name__ == '__main__':
    main()