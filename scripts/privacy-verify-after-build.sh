#!/bin/bash

# Hook script to run privacy verification after Hugo builds the site
# This script is intended to be run as part of the Hugo build process

set -e  # Exit on any error

echo "Running privacy verification after Hugo build..."

# Path to the privacy scan script
PRIVACY_SCAN_SCRIPT="./scripts/privacy-scan.sh"

# Check if the public directory exists (where Hugo builds the site)
if [ ! -d "public" ]; then
    echo "Error: public directory does not exist. Has Hugo built the site?"
    exit 1
fi

# Run the privacy scan on the generated site
if [ -f "$PRIVACY_SCAN_SCRIPT" ]; then
    echo "Running privacy scan on generated site..."
    "$PRIVACY_SCAN_SCRIPT" "./public"
    
    # Capture the exit code
    SCAN_EXIT_CODE=$?
    
    if [ $SCAN_EXIT_CODE -eq 0 ]; then
        echo "✅ Privacy scan passed! Site is compliant."
    else
        echo "❌ Privacy scan failed! Issues detected in the generated site."
        echo "Check privacy-scan-report.txt for details."
        exit 1  # Fail the build if privacy scan fails
    fi
else
    echo "Warning: Privacy scan script not found at $PRIVACY_SCAN_SCRIPT"
    echo "Skipping privacy verification."
fi

echo "Privacy verification completed."