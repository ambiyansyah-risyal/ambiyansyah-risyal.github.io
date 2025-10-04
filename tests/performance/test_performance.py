import time
import subprocess
import os
from pathlib import Path


def test_build_performance():
    """Test that the Hugo build process performance is acceptable"""
    start_time = time.time()
    
    # Run the Hugo build command
    result = subprocess.run(['hugo'], capture_output=True, text=True)
    
    end_time = time.time()
    build_duration = end_time - start_time
    
    # Check that the build was successful
    assert result.returncode == 0, f"Hugo build failed: {result.stderr}"
    
    # Check that build time is within acceptable limits (e.g., under 30 seconds)
    # This limit can be adjusted based on the actual site size and complexity
    assert build_duration < 30, f"Build took too long: {build_duration:.2f} seconds"
    
    print(f"Build completed in {build_duration:.2f} seconds")


def test_site_size():
    """Test that the generated site size is reasonable and hasn't grown unexpectedly"""
    # Get the size of the public directory
    def get_directory_size(path):
        """Calculate the total size of a directory in bytes"""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.exists(filepath):
                    total_size += os.path.getsize(filepath)
        return total_size

    public_dir = Path('public')
    if public_dir.exists():
        size_bytes = get_directory_size(public_dir)
        size_mb = size_bytes / (1024 * 1024)
        
        # Set a reasonable limit - adjust based on actual site requirements
        # For a simple privacy-safe site, 10MB should be more than enough
        assert size_mb < 10, f"Site size is too large: {size_mb:.2f} MB"
        
        print(f"Site size: {size_mb:.2f} MB")
    else:
        # If public directory doesn't exist, build the site first
        subprocess.run(['hugo'], check=True)
        size_bytes = get_directory_size(public_dir)
        size_mb = size_bytes / (1024 * 1024)
        assert size_mb < 10, f"Site size is too large: {size_mb:.2f} MB"
        
        print(f"Site size: {size_mb:.2f} MB")


def test_generated_files_count():
    """Test that the number of generated files is reasonable"""
    def count_files(directory):
        """Count the number of files in a directory recursively"""
        count = 0
        for root, dirs, files in os.walk(directory):
            count += len(files)
        return count

    # Build the site first to ensure we have generated files
    subprocess.run(['hugo'], check=True)
    
    public_dir = Path('public')
    if public_dir.exists():
        file_count = count_files(public_dir)
        
        # Set a reasonable limit for the number of files
        # Adjust based on the actual site complexity
        assert file_count < 1000, f"Too many generated files: {file_count}"
        
        print(f"Number of generated files: {file_count}")
    else:
        assert False, "Public directory does not exist after Hugo build"


if __name__ == '__main__':
    # Ensure we're in the correct directory where hugo.toml exists
    # Run the tests
    test_build_performance()
    test_site_size()
    test_generated_files_count()
    print("All performance tests passed!")