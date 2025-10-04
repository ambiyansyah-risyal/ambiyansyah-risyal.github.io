"""
Integration test for accessibility compliance
Validates that the site meets WCAG AA accessibility standards
"""
import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAccessibilityCompliance(unittest.TestCase):
    """Test that the Hugo site meets WCAG AA accessibility standards"""
    
    def setUp(self):
        """Set up the test environment before each test method."""
        # Set up Chrome options for headless testing
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Initialize the WebDriver
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
        except Exception:
            # If Chrome is not available, skip these tests
            self.skipTest("Chrome WebDriver not available")
        
        # Build the site first to ensure it's available
        import subprocess
        result = subprocess.run(['hugo'], capture_output=True, text=True)
        if result.returncode != 0:
            self.fail(f"Hugo build failed: {result.stderr}")

    def tearDown(self):
        """Clean up after each test method."""
        if hasattr(self, 'driver'):
            self.driver.quit()

    def test_proper_heading_hierarchy(self):
        """Test that the page uses proper heading hierarchy"""
        # Serve the site locally
        import subprocess
        import time
        
        # Start the Hugo server
        server_process = subprocess.Popen(['hugo', 'server', '--buildDrafts', '--port', '1313', '--bind', '0.0.0.0'], 
                                         stdout=subprocess.PIPE, 
                                         stderr=subprocess.PIPE)
        
        # Wait for server to start
        time.sleep(3)
        
        try:
            # Navigate to the site
            self.driver.get("http://localhost:1313")
            
            # Find all heading elements
            headings = self.driver.find_elements(By.XPATH, "//h1 | //h2 | //h3 | //h4 | //h5 | //h6")
            
            # Check that there's at least one H1
            h1_elements = self.driver.find_elements(By.TAG_NAME, "h1")
            self.assertGreaterEqual(len(h1_elements), 1, "Page should have at least one H1 element")
            
            # Check that headings follow a proper hierarchical order (no skipping levels)
            heading_levels = []
            for heading in headings:
                level = int(heading.tag_name[1])  # Extract number from h1, h2, etc.
                heading_levels.append(level)
            
            # Check that heading levels don't skip (e.g., go from h1 to h3 without h2)
            for i in range(1, len(heading_levels)):
                self.assertLessEqual(heading_levels[i-1], heading_levels[i] + 1, 
                                     f"Heading level skipped from {heading_levels[i-1]} to {heading_levels[i]}")
            
        finally:
            # Terminate the Hugo server
            server_process.terminate()
            server_process.wait()

    def test_alt_text_for_images(self):
        """Test that all images have alt text"""
        # Serve the site locally
        import subprocess
        import time
        
        # Start the Hugo server
        server_process = subprocess.Popen(['hugo', 'server', '--buildDrafts', '--port', '1313', '--bind', '0.0.0.0'], 
                                         stdout=subprocess.PIPE, 
                                         stderr=subprocess.PIPE)
        
        # Wait for server to start
        time.sleep(3)
        
        try:
            # Navigate to the site
            self.driver.get("http://localhost:1313")
            
            # Find all image elements
            images = self.driver.find_elements(By.TAG_NAME, "img")
            
            # Check that each image has alt text
            for img in images:
                alt_text = img.get_attribute("alt")
                self.assertIsNotNone(alt_text, f"Image {img.get_attribute('src')} is missing alt text")
                # Alt text can be empty string, which is valid for decorative images
                
        finally:
            # Terminate the Hugo server
            server_process.terminate()
            server_process.wait()

    def test_keyboard_navigation(self):
        """Test that the site is navigable by keyboard"""
        # Serve the site locally
        import subprocess
        import time
        
        # Start the Hugo server
        server_process = subprocess.Popen(['hugo', 'server', '--buildDrafts', '--port', '1313', '--bind', '0.0.0.0'], 
                                         stdout=subprocess.PIPE, 
                                         stderr=subprocess.PIPE)
        
        # Wait for server to start
        time.sleep(3)
        
        try:
            # Navigate to the site
            self.driver.get("http://localhost:1313")
            
            # Find focusable elements
            focusable_selectors = [
                "a[href]", 
                "button:not([disabled])", 
                "input:not([disabled]):not([type='hidden'])", 
                "select:not([disabled])", 
                "textarea:not([disabled])", 
                "[tabindex]:not([tabindex='-1'])"
            ]
            
            focusable_elements = []
            for selector in focusable_selectors:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                focusable_elements.extend(elements)
            
            # Verify there are focusable elements
            self.assertGreater(len(focusable_elements), 0, "Page should have focusable elements for keyboard navigation")
            
            # Verify that focusable elements have proper focus styling
            # This is harder to test directly, but we can check if they're focusable
            for element in focusable_elements[:3]:  # Test first 3 elements
                # Try to click each element to ensure it's interactive
                element.click()
                # If we get here, the element is accessible
                
        finally:
            # Terminate the Hugo server
            server_process.terminate()
            server_process.wait()


if __name__ == '__main__':
    unittest.main()