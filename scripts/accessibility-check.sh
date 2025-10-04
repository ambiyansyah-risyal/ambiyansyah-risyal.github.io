#!/bin/bash
# Script to validate accessibility of the Hugo site

echo "Building the Hugo site..."
hugo --minify

echo "Starting temporary server for accessibility testing..."
hugo server --buildDrafts --port=1313 --bind=0.0.0.0 &

# Wait for server to start
sleep 5

# For actual accessibility testing, you would use a tool like pa11y or Lighthouse
# This is a placeholder for the actual implementation
echo "Running accessibility validation..."
echo "1. Install pa11y: npm install -g pa11y"
echo "2. Run: pa11y http://localhost:1313"
echo "3. Or use Lighthouse CLI for comprehensive testing"

# Kill the Hugo server
kill %1

echo "Accessibility validation completed. Review the output from the actual testing tools."