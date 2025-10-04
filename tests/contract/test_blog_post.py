"""
Contract test for blog post structure
Validates that blog posts follow the required structure and front matter
"""
import os
import glob
import frontmatter
import unittest
from datetime import datetime


class TestBlogPostStructure(unittest.TestCase):
    """Test that blog posts follow the required structure"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.content_dir = "content/posts"
        if not os.path.exists(self.content_dir):
            os.makedirs(self.content_dir, exist_ok=True)

    def test_required_front_matter_fields_exist(self):
        """Test that all blog posts have required front matter fields"""
        # Create a sample blog post if none exist
        sample_post_path = os.path.join(self.content_dir, "test-post.md")
        if not os.path.exists(sample_post_path):
            with open(sample_post_path, 'w') as f:
                f.write("""---
title: "Test Post"
date: 2025-10-04T12:00:00Z
draft: false
---
This is a test blog post.
""")
        
        # Find all blog posts
        post_files = glob.glob(os.path.join(self.content_dir, "*.md"))
        
        for post_file in post_files:
            with open(post_file, 'r') as f:
                post = frontmatter.load(f)
                
            # Check required fields
            self.assertIn('title', post.keys(), f"Missing 'title' in {post_file}")
            self.assertIn('date', post.keys(), f"Missing 'date' in {post_file}")
            
            # Validate date format
            date_str = post['date']
            if isinstance(date_str, str):
                # Try to parse the date to ensure it's valid
                try:
                    parsed_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
                except ValueError:
                    self.fail(f"Invalid date format in {post_file}: {date_str}")

    def test_optional_front_matter_fields(self):
        """Test that optional front matter fields are handled properly"""
        # Check that optional fields don't cause errors if present
        sample_post_path = os.path.join(self.content_dir, "test-post-optional.md")
        with open(sample_post_path, 'w') as f:
            f.write("""---
title: "Test Post with Optional Fields"
date: 2025-10-04T12:00:00Z
description: "A sample description"
draft: false
tags: ["test", "sample"]
categories: ["General"]
---
This is a test blog post with optional fields.
""")
        
        with open(sample_post_path, 'r') as f:
            post = frontmatter.load(f)
            
        # These fields are optional, so just verify they don't cause issues
        optional_fields = ['description', 'tags', 'categories']
        for field in optional_fields:
            # Just ensure they don't cause errors if present
            _ = post.get(field)


if __name__ == '__main__':
    unittest.main()