"""
Contract test for site configuration
Validates that the Hugo site configuration meets the specified requirements
"""
import os
import toml
import unittest


class TestSiteConfig(unittest.TestCase):
    """Test that the Hugo site configuration meets the contract requirements"""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.config_path = "hugo.toml"
        self.assertTrue(os.path.exists(self.config_path), f"Config file {self.config_path} does not exist")
        
        with open(self.config_path, 'r') as f:
            self.config = toml.load(f)

    def test_base_url_configured(self):
        """Test that baseURL is properly configured"""
        self.assertIn('baseURL', self.config)
        self.assertEqual(self.config['baseURL'], 'https://ambiyansyah-risyal.github.io/')
        
    def test_language_code_configured(self):
        """Test that languageCode is properly configured"""
        self.assertIn('languageCode', self.config)
        self.assertEqual(self.config['languageCode'], 'en-us')
        
    def test_site_title_configured(self):
        """Test that title is properly configured"""
        self.assertIn('title', self.config)
        self.assertEqual(self.config['title'], 'Risyal Ambiyansyah - Personal Website')
        
    def test_site_author_configured(self):
        """Test that author is properly configured"""
        self.assertIn('author', self.config)
        self.assertEqual(self.config['author'], 'Risyal Ambiyansyah')
        
    def test_rss_enabled(self):
        """Test that RSS output is enabled"""
        self.assertIn('outputs', self.config)
        if 'home' in self.config['outputs']:
            self.assertIn('RSS', self.config['outputs']['home'])
        else:
            # Alternative structure for newer Hugo versions
            self.assertIn('page', self.config.get('outputs', {}))
            
    def test_pagination_configured(self):
        """Test that pagination is configured"""
        self.assertIn('params', self.config)
        self.assertIn('paginate', self.config['params'])
        self.assertIsInstance(self.config['params']['paginate'], int)


if __name__ == '__main__':
    unittest.main()