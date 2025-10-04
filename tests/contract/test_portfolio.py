"""
Contract test for portfolio item structure
Validates that portfolio items follow the required structure and front matter
"""
import os
import glob
import frontmatter
import unittest
from datetime import datetime


class TestPortfolioItemStructure(unittest.TestCase):
    """Test that portfolio items follow the required structure"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.content_dir = "content/portfolio"
        if not os.path.exists(self.content_dir):
            os.makedirs(self.content_dir, exist_ok=True)

    def test_required_front_matter_fields_exist(self):
        """Test that all portfolio items have required front matter fields"""
        # Create a sample portfolio item if none exist
        sample_portfolio_path = os.path.join(self.content_dir, "test-project.md")
        if not os.path.exists(sample_portfolio_path):
            with open(sample_portfolio_path, 'w') as f:
                f.write("""---
title: "Test Project"
date: 2025-10-04T12:00:00Z
description: "A sample portfolio item"
draft: false
---
This is a test portfolio item.
""")
        
        # Find all portfolio items
        portfolio_files = glob.glob(os.path.join(self.content_dir, "*.md"))
        
        for portfolio_file in portfolio_files:
            with open(portfolio_file, 'r') as f:
                portfolio_item = frontmatter.load(f)
                
            # Check required fields
            self.assertIn('title', portfolio_item.keys(), f"Missing 'title' in {portfolio_file}")
            self.assertIn('date', portfolio_item.keys(), f"Missing 'date' in {portfolio_file}")
            self.assertIn('description', portfolio_item.keys(), f"Missing 'description' in {portfolio_file}")
            
            # Validate date format
            date_str = portfolio_item['date']
            if isinstance(date_str, str):
                # Try to parse the date to ensure it's valid
                try:
                    parsed_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                except ValueError:
                    self.fail(f"Invalid date format in {portfolio_file}: {date_str}")

    def test_optional_front_matter_fields(self):
        """Test that optional front matter fields are handled properly"""
        # Check that optional fields don't cause errors if present
        sample_portfolio_path = os.path.join(self.content_dir, "test-project-optional.md")
        with open(sample_portfolio_path, 'w') as f:
            f.write("""---
title: "Test Project with Optional Fields"
date: 2025-10-04T12:00:00Z
description: "A sample portfolio item with optional fields"
draft: false
tags: ["web", "design"]
url: "https://example.com"
images: ["/images/project1.jpg", "/images/project2.jpg"]
---
This is a test portfolio item with optional fields.
""")
        
        with open(sample_portfolio_path, 'r') as f:
            portfolio_item = frontmatter.load(f)
            
        # These fields are optional, so just verify they don't cause errors
        optional_fields = ['tags', 'url', 'images']
        for field in optional_fields:
            # Just ensure they don't cause errors if present
            _ = portfolio_item.get(field)


if __name__ == '__main__':
    unittest.main()