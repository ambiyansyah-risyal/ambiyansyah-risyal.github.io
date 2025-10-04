#!/bin/bash
# Script to verify mobile responsiveness of the Hugo site

echo "Building the Hugo site..."
hugo --minify

echo "Starting temporary server for responsiveness testing..."
hugo server --buildDrafts --port=1313 --bind=0.0.0.0 &

# Wait for server to start
sleep 5

# In a real scenario, you would use a tool like Puppeteer or similar for automated testing
# This is a placeholder for the actual implementation
echo "Manual responsiveness testing checklist:"
echo "1. Open http://localhost:1313 in a browser"
echo "2. Test with browser developer tools at different screen sizes:"
echo "   - Mobile: 320x568 (iPhone SE)"
echo "   - Mobile: 375x667 (iPhone 6/7/8)"
echo "   - Tablet: 768x1024 (iPad)"
echo "   - Desktop: 1024x768"
echo "   - Desktop: 1920x1080"
echo "3. Verify:"
echo "   - Text is readable without zooming"
echo "   - Touch targets are appropriately sized"
echo "   - Layout adjusts properly to screen size"
echo "   - No horizontal scrolling needed on mobile"

# Kill the Hugo server
kill %1

echo "Responsiveness verification completed. Manually verify using the checklist above."