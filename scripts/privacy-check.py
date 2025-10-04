#!/usr/bin/env python3
"""
Privacy Compliance Verification Script
This script checks for privacy compliance by scanning the generated site for tracking mechanisms.
"""

import os
import sys
import re
import json
from datetime import datetime
from pathlib import Path


def scan_for_tracking_mechanisms(site_path):
    """Scan the generated site for tracking mechanisms."""
    tracking_patterns = [
        r'google-analytics',
        r'google\.com/analytics',
        r'facebook\.com/tr',
        r'gtm\.js',
        r'gtag',
        r'facebook-pixel',
        r'hotjar',
        r'plausible',
        r'matomo',
        r'mixpanel',
        r'segment',
        r'ga\.js',
        r'urchin',
        r'tagmanager',
        r'adsbygoogle',
        r'doubleclick',
        r'googletag',
    ]

    tracking_found = []
    html_files = list(Path(site_path).rglob("*.html"))

    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read().lower()

            for pattern in tracking_patterns:
                if re.search(pattern, content):
                    tracking_found.append({
                        "type": pattern,
                        "location": str(html_file),
                        "source": pattern
                    })
        except Exception as e:
            print(f"Error reading file {html_file}: {str(e)}")

    return tracking_found


def check_cookies(content):
    """Check for tracking-related cookies in content."""
    cookie_tracking_patterns = [
        r'document\.cookie',
        r'localStorage',
        r'sessionStorage',
    ]

    found_cookies = []
    for pattern in cookie_tracking_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            found_cookies.append({
                "type": "cookie-tracking",
                "pattern": pattern,
                "source": content[:200]  # First 200 chars of the content containing the pattern
            })

    return found_cookies


def check_external_resources(content):
    """Check for tracking-related external resources."""
    external_tracking_patterns = [
        r'(src|href|link).*?(google|facebook|analytics|tracking|pixel|hotjar|plausible|matomo|mixpanel|segment).*?\.(js|css|png|jpg|gif)',
    ]

    found_resources = []
    for pattern in external_tracking_patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            found_resources.append({
                "type": "external-resource",
                "pattern": pattern,
                "matches": matches
            })

    return found_resources


def generate_verification_report(tracking_found, cookies_found, resources_found):
    """Generate the verification report."""
    report = {
        "verificationDate": datetime.now().isoformat(),
        "status": "PASS" if not (tracking_found or cookies_found or resources_found) else "FAIL",
        "trackingScriptsFound": tracking_found,
        "details": {
            "cookiesCheck": "PASS" if not cookies_found else "FAIL",
            "thirdPartyScripts": "PASS" if not resources_found else "FAIL",
            "fingerprintingChecks": "PENDING",  # This would require more complex analysis
            "analyticsCheck": "PASS" if not tracking_found else "FAIL"
        },
        "summary": {
            "trackingScripts": len(tracking_found),
            "cookieIssues": len(cookies_found),
            "externalResources": len(resources_found)
        }
    }
    return report


def main(site_path):
    """Main function to run the privacy verification."""
    if not os.path.exists(site_path):
        print(f"Error: Path {site_path} does not exist")
        return 1

    print(f"Starting privacy compliance verification for site: {site_path}")

    # Scan for tracking mechanisms
    tracking_found = scan_for_tracking_mechanisms(site_path)

    # Additional checks
    cookies_found = []
    resources_found = []
    html_files = list(Path(site_path).rglob("*.html"))

    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                cookies_found.extend(check_cookies(content))
                resources_found.extend(check_external_resources(content))
        except Exception as e:
            print(f"Error reading file {html_file}: {str(e)}")

    # Generate report
    report = generate_verification_report(tracking_found, cookies_found, resources_found)

    # Print results
    print(json.dumps(report, indent=2))

    # Write report to file
    with open("privacy-verification-report.json", "w") as f:
        json.dump(report, f, indent=2)

    print(f"Verification completed. Report saved to privacy-verification-report.json")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 privacy-check.py <path_to_generated_site>")
        sys.exit(1)

    site_path = sys.argv[1]
    sys.exit(main(site_path))