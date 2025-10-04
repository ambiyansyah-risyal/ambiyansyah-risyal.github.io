"""
Integration test for site build process
Validates that the Hugo site can be built successfully
"""
import os
import subprocess
import unittest


class TestSiteBuild(unittest.TestCase):
    """Test that the Hugo site can be built successfully"""
    
    def test_hugo_build_command(self):
        """Test that the 'hugo' build command executes successfully"""
        # Run the hugo build command
        result = subprocess.run(['hugo'], 
                                capture_output=True, 
                                text=True, 
                                cwd=os.getcwd())
        
        # The command should exit with code 0 (success)
        self.assertEqual(result.returncode, 0, 
                         f"Hugo build failed with error: {result.stderr}")
        
        # Check that public directory was created
        self.assertTrue(os.path.exists('public'), 
                        "Public directory was not created after build")
        
        # Check that index.html exists in public directory
        self.assertTrue(os.path.exists('public/index.html'), 
                        "Public/index.html was not created after build")
        
    def test_hugo_build_with_minification(self):
        """Test that the 'hugo --minify' build command executes successfully"""
        # Run the hugo build command with minification
        result = subprocess.run(['hugo', '--minify'], 
                                capture_output=True, 
                                text=True, 
                                cwd=os.getcwd())
        
        # The command should exit with code 0 (success)
        self.assertEqual(result.returncode, 0, 
                         f"Hugo build with minification failed with error: {result.stderr}")
        
        # Check that public directory was created
        self.assertTrue(os.path.exists('public'), 
                        "Public directory was not created after minified build")


if __name__ == '__main__':
    unittest.main()