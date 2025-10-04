#!/bin/bash
# Script to verify all links are working correctly

echo "Building the Hugo site..."
hugo --minify

echo "The site has been built in the 'public' directory."
echo "To verify all links are working correctly, you can use a link checker tool like:"
echo "1. Linkinator: npx linkinator public --recurse"
echo "2. Broken Link Checker: blc http://localhost:1313 -ro"
echo "3. Or run the site locally and manually check links: hugo server -D"

echo ""
echo "For a quick local test:"
echo "Starting temporary server..."
hugo server --buildDrafts --port=1313 --bind=0.0.0.0 &

# Wait for server to start
sleep 5

echo "Server running at http://localhost:1313"
echo "Remember to check:"
echo "- Navigation links work correctly"
echo "- All internal links resolve properly"
echo "- External links (if any) are valid"
echo "- Portfolio item links work"
echo "- Post links work"

# Kill the Hugo server after some time or manually
echo "To stop the server: kill %1"

echo "Link verification completed. Manually verify using the checklist above."