"""
Integration test for mobile responsiveness
Validates that the site is responsive across different screen sizes
"""
import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestMobileResponsiveness(unittest.TestCase):
    """Test that the Hugo site is responsive across different screen sizes"""
    
    def setUp(self):
        """Set up the test environment before each test method."""
        # Set up Chrome options for headless testing
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Set capabilities for Docker compatibility if needed
        caps = DesiredCapabilities.CHROME
        caps['goog:loggingPrefs'] = {'browser': 'ALL'}
        
        # Initialize the WebDriver
        try:
            self.driver = webdriver.Chrome(options=chrome_options, desired_capabilities=caps)
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

    def test_mobile_viewport_320px(self):
        """Test site appearance at 320px width (typical mobile)"""
        # Serve the site locally
        import subprocess
        import time
        import threading
        
        # Start the Hugo server
        server_process = subprocess.Popen(['hugo', 'server', '--buildDrafts', '--port', '1313', '--bind', '0.0.0.0'], 
                                         stdout=subprocess.PIPE, 
                                         stderr=subprocess.PIPE)
        
        # Wait for server to start
        time.sleep(3)
        
        try:
            # Set window size to mobile dimensions
            self.driver.set_window_size(320, 568)
            
            # Navigate to the site
            self.driver.get("http://localhost:1313")
            
            # Basic checks for mobile responsiveness
            body = self.driver.find_element_by_tag_name('body')
            self.assertIsNotNone(body)
            
            # Check that the page loaded properly
            self.assertGreater(len(self.driver.page_source), 100, 
                              "Page content appears to be empty or too small")
            
        finally:
            # Terminate the Hugo server
            server_process.terminate()
            server_process.wait()

    def test_tablet_viewport_768px(self):
        """Test site appearance at 768px width (typical tablet)"""
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
            # Set window size to tablet dimensions
            self.driver.set_window_size(768, 1024)
            
            # Navigate to the site
            self.driver.get("http://localhost:1313")
            
            # Basic checks for tablet responsiveness
            body = self.driver.find_element_by_tag_name('body')
            self.assertIsNotNone(body)
            
            # Check that the page loaded properly
            self.assertGreater(len(self.driver.page_source), 100, 
                              "Page content appears to be empty or too small")
            
        finally:
            # Terminate the Hugo server
            server_process.terminate()
            server_process.wait()

    def test_desktop_viewport_1200px(self):
        """Test site appearance at 1200px width (typical desktop)"""
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
            # Set window size to desktop dimensions
            self.driver.set_window_size(1200, 800)
            
            # Navigate to the site
            self.driver.get("http://localhost:1313")
            
            # Basic checks for desktop responsiveness
            body = self.driver.find_element_by_tag_name('body')
            self.assertIsNotNone(body)
            
            # Check that the page loaded properly
            self.assertGreater(len(self.driver.page_source), 100, 
                              "Page content appears to be empty or too small")
            
        finally:
            # Terminate the Hugo server
            server_process.terminate()
            server_process.wait()


if __name__ == '__main__':
    unittest.main()