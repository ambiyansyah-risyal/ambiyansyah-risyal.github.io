#!/bin/bash

# Script to scan the generated site for tracking mechanisms
# Usage: ./privacy-scan.sh [path_to_generated_site]

SITE_PATH="${1:-public}"
REPORT_FILE="privacy-scan-report.txt"

echo "Starting privacy scan of site at: $SITE_PATH"
echo "Scan started at: $(date)" > "$REPORT_FILE"

# Define tracking patterns to search for
TRACKING_PATTERNS=(
    "google-analytics"
    "google.com/analytics"
    "facebook.com/tr"
    "gtm.js"
    "gtag"
    "facebook-pixel"
    "hotjar"
    "plausible"
    "matomo"
    "mixpanel"
    "segment"
    "ga.js"
    "urchin"
    "tagmanager"
    "adsbygoogle"
    "doubleclick"
    "googletag"
)

# Find and search all HTML files
HTML_FILES=$(find "$SITE_PATH" -name "*.html" -type f)

FOUND_TRACKING=0
for pattern in "${TRACKING_PATTERNS[@]}"; do
    echo "Searching for pattern: $pattern"
    for file in $HTML_FILES; do
        if grep -l -i "$pattern" "$file" > /dev/null 2>&1; then
            echo "ALERT: Found potential tracking pattern '$pattern' in $file" | tee -a "$REPORT_FILE"
            FOUND_TRACKING=1
        fi
    done
done

# Check for tracking-related cookies
echo "Checking for tracking-related cookies in headers..."
for file in $HTML_FILES; do
    if grep -i "document.cookie" "$file" | grep -i -E "(track|analytic|ad|pixel|stat)" > /dev/null 2>&1; then
        echo "ALERT: Found potential tracking cookie usage in $file" | tee -a "$REPORT_FILE"
        FOUND_TRACKING=1
    fi
done

# Check for tracking-related external resources
echo "Checking for external tracking resources..."
for file in $HTML_FILES; do
    if grep -i -E "(src|href|link)" "$file" | grep -i -E "(google|facebook|analytics|tracking|pixel|hotjar|plausible|matomo|mixpanel|segment)" | grep -E "\.(js|css|png|jpg|gif)" > /dev/null 2>&1; then
        grep -i -E "(src|href|link)" "$file" | grep -i -E "(google|facebook|analytics|tracking|pixel|hotjar|plausible|matomo|mixpanel|segment)" | grep -E "\.(js|css|png|jpg|gif)" >> "$REPORT_FILE"
        FOUND_TRACKING=1
    fi
done

echo "Scan completed at: $(date)" >> "$REPORT_FILE"

if [ $FOUND_TRACKING -eq 0 ]; then
    echo "✅ No tracking mechanisms detected!"
    echo "Status: PASS" >> "$REPORT_FILE"
    exit 0
else
    echo "❌ Tracking mechanisms detected! Check $REPORT_FILE for details."
    echo "Status: FAIL" >> "$REPORT_FILE"
    exit 1
fi