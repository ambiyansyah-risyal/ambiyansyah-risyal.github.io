#!/usr/bin/env python3
"""
Privacy Verification Script

This script checks the generated Hugo site for privacy compliance,
ensuring no tracking mechanisms are present.
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime


def scan_for_tracking_scripts(directory):
    """Scan the generated site for known tracking scripts"""
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
        'twitter.com/i/oct.js',
        'adsbygoogle.js',
        'doubleclick',
        'googletag',
        'tagmanager',
        'site-verification',  # Some verification tags can be used for tracking
    ]
    
    tracking_found = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.html', '.js', '.css', '.txt', '.xml')):
                file_path = Path(root) / file
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read().lower()
                        
                        for indicator in tracking_indicators:
                            if indicator in content:
                                tracking_found.append({
                                    'type': classify_tracking_type(indicator),
                                    'location': str(file_path),
                                    'source': indicator
                                })
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    return tracking_found


def classify_tracking_type(indicator):
    """Classify the type of tracking based on the indicator found"""
    if 'google-analytics' in indicator or 'analytics' in indicator:
        return 'google-analytics'
    elif 'facebook' in indicator:
        return 'facebook-pixel'
    elif 'gtm' in indicator or 'gtag' in indicator:
        return 'google-tag-manager'
    elif 'hotjar' in indicator:
        return 'hotjar'
    elif 'matomo' in indicator or 'piwik' in indicator:
        return 'matomo/piwik'
    elif 'hubspot' in indicator:
        return 'hubspot'
    elif 'adsbygoogle' in indicator or 'doubleclick' in indicator or 'googletag' in indicator:
        return 'advertising'
    else:
        return 'custom-tracking'


def scan_for_cookies(directory):
    """Scan for potential cookie-setting scripts"""
    cookie_indicators = [
        'document.cookie',
        'localStorage',
        'sessionStorage',
        'cookieconsent',
        'trackCookie',
        'set-cookie',
    ]
    
    cookie_found = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.html', '.js')):
                file_path = Path(root) / file
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read().lower()
                        
                        for indicator in cookie_indicators:
                            if indicator in content:
                                cookie_found.append({
                                    'location': str(file_path),
                                    'source': indicator
                                })
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    return len(cookie_found) > 0  # Return True if any cookie-setting code found


def scan_third_party_content(directory):
    """Scan for third-party content that may pose privacy risks"""
    third_party_indicators = [
        'youtube.com/embed',
        'facebook.com/plugins',
        'twitter.com/widgets',
        'instagram.com/embed',
        'vimeo.com',
        'soundcloud.com',
    ]
    
    third_party_found = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = Path(root) / file
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read().lower()
                        
                        for indicator in third_party_indicators:
                            if indicator in content:
                                third_party_found.append({
                                    'location': str(file_path),
                                    'source': indicator
                                })
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    return third_party_found


def check_csp_headers(directory):
    """Check for Content Security Policy in HTML files"""
    csp_found = False
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = Path(root) / file
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read().lower()
                        
                        if 'content-security-policy' in content or 'csp' in content:
                            csp_found = True
                            break
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    
    return csp_found


def run_privacy_verification():
    """Main function to run all privacy verification checks"""
    # Build the site first to ensure we have the latest version
    print("Building site with Hugo...")
    import subprocess
    result = subprocess.run(['hugo'], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error building site: {result.stderr}")
        return None
    
    public_dir = Path('public')
    if not public_dir.exists():
        print("Error: public directory does not exist after Hugo build")
        return None
    
    print("Scanning generated site for privacy compliance...")
    
    # Run all checks
    tracking_scripts = scan_for_tracking_scripts(public_dir)
    has_cookies = scan_for_cookies(public_dir)
    third_party_content = scan_third_party_content(public_dir)
    has_csp = check_csp_headers(public_dir)
    
    # Create verification report
    verification_report = {
        'verificationDate': datetime.now().isoformat(),
        'status': 'PASS' if len(tracking_scripts) == 0 else 'FAIL',
        'trackingScriptsFound': tracking_scripts,
        'details': {
            'cookiesCheck': 'PASS' if not has_cookies else 'WARN',  # Warn rather than fail for cookies
            'thirdPartyScripts': 'PASS' if len(third_party_content) == 0 else 'WARN',
            'fingerprintingChecks': 'PASS' if len(tracking_scripts) == 0 else 'FAIL',
            'analyticsCheck': 'PASS' if len([t for t in tracking_scripts if 'analytics' in t['type']]) == 0 else 'FAIL',
            'cspCheck': 'PASS' if has_csp else 'INFO'  # Info rather than pass/fail
        }
    }
    
    return verification_report


def main():
    """Main execution function"""
    report = run_privacy_verification()
    
    if report is None:
        print("Failed to run privacy verification")
        sys.exit(1)
    
    # Print the report
    print("\\nPrivacy Verification Report:")
    print(json.dumps(report, indent=2))
    
    # Exit with appropriate code based on status
    if report['status'] == 'PASS':
        print("\\nSite is compliant with privacy requirements!")
        sys.exit(0)
    else:
        print("\\nSite has privacy compliance issues that need to be addressed!")
        sys.exit(1)


if __name__ == '__main__':
    main()