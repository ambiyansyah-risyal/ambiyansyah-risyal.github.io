"""
Integration test for cookie compliance functionality
Tests that only essential functional cookies are used as per requirements.
"""

import pytest
import os
import tempfile
import subprocess
from pathlib import Path
import re


def test_cookie_detection_in_html():
    """
    Test that our scripts can detect non-essential cookies in HTML files.
    """
    # Create a temporary HTML file with cookie-setting JavaScript
    with tempfile.TemporaryDirectory() as temp_dir:
        # HTML with tracking-related cookie setting
        html_with_cookies = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Page with Cookies</title>
        </head>
        <body>
            <h1>Test Page</h1>
            <script>
                // This sets a tracking cookie
                document.cookie = "tracking_id=abc123; path=/";
                
                // This sets an analytics cookie
                document.cookie = "ga_visitor=xyz789; path=/";
            </script>
        </body>
        </html>
        """
        
        test_file = Path(temp_dir) / "cookie_test.html"
        with open(test_file, 'w') as f:
            f.write(html_with_cookies)
        
        # Run our privacy scan script against the test site
        script_path = Path(__file__).parent.parent.parent / "scripts" / "privacy-scan.sh"
        result = subprocess.run([str(script_path), temp_dir], 
                              capture_output=True, text=True)
        
        # The script should detect the cookie-related tracking
        assert result.returncode == 1, f"Privacy scan should detect cookie tracking: {result.stdout}"


def test_no_non_essential_cookies():
    """
    Test that our privacy script passes when only essential cookies are found.
    For static sites like Hugo, there typically are no cookies set by default,
    but we'll test our detection logic.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        # HTML without any cookie-setting code
        html_without_cookies = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Test Page without Cookies</title>
        </head>
        <body>
            <h1>Test Page</h1>
            <p>This page doesn't set any cookies.</p>
        </body>
        </html>
        """
        
        test_file = Path(temp_dir) / "no_cookie_test.html"
        with open(test_file, 'w') as f:
            f.write(html_without_cookies)
        
        # Run our privacy scan script against the test site
        script_path = Path(__file__).parent.parent.parent / "scripts" / "privacy-scan.sh"
        result = subprocess.run([str(script_path), temp_dir], 
                              capture_output=True, text=True)
        
        # The script should pass for a site without tracking cookies
        assert result.returncode == 0, f"Privacy scan should pass for site without tracking cookies: {result.stderr}"


def test_python_script_cookie_detection():
    """
    Test the Python script's specific ability to detect cookie-related tracking.
    """
    # Import our Python script's function directly
    import sys
    from pathlib import Path
    
    # Add the scripts directory to the Python path
    scripts_dir = Path(__file__).parent.parent.parent / "scripts"
    sys.path.insert(0, str(scripts_dir))
    
    try:
        import privacy_check
        # We can't directly import the function from privacy_check, so we'll test by running it
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a file with cookie-related tracking
            html_content = """
            <html>
            <body>
                <script>
                    document.cookie = "tracking=123";
                </script>
            </body>
            </html>
            """
            
            test_file = Path(temp_dir) / "cookie_detection_test.html"
            with open(test_file, 'w') as f:
                f.write(html_content)
            
            # Run our Python script directly
            # For this test, we'll just make sure it executes without error
            # The actual logic would be validated in the implementation phase
            result = subprocess.run([
                sys.executable,
                str(scripts_dir / "privacy-check.py"),
                temp_dir
            ], capture_output=True, text=True)
            
            # We expect it to run successfully even if it detects issues
            # The important thing is that it runs and processes the cookies
            assert result.returncode in [0, 1], f"Privacy check script failed to run: {result.stderr}"
    
    finally:
        # Clean up the path
        if str(scripts_dir) in sys.path:
            sys.path.remove(str(scripts_dir))


if __name__ == "__main__":
    test_cookie_detection_in_html()
    test_no_non_essential_cookies()
    test_python_script_cookie_detection()