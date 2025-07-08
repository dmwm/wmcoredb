#!/usr/bin/env python3
"""
Comprehensive test script for the wmcoredb package.

This script tests the package build, installation, and functionality
without publishing to PyPI.
"""

import subprocess
import sys
import pathlib
import tempfile
import shutil
from pathlib import Path


def run_command(cmd, description, check=True):
    """Run a command and handle errors."""
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=check, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed")
        print(f"Error: {e.stderr}")
        return False


def test_package_build():
    """Test building the package."""
    print("=== Testing Package Build ===\n")
    
    # Clean previous builds
    if Path("dist").exists():
        shutil.rmtree("dist")
    if Path("build").exists():
        shutil.rmtree("build")
    if Path("*.egg-info").exists():
        for egg in Path(".").glob("*.egg-info"):
            shutil.rmtree(egg)
    
    # Build the package
    if not run_command("python -m build", "Building package"):
        return False
    
    # Check that build artifacts exist
    dist_files = list(Path("dist").glob("*"))
    if not dist_files:
        print("✗ No build artifacts found in dist/")
        return False
    
    print(f"✓ Build artifacts created: {[f.name for f in dist_files]}")
    return True


def test_package_installation():
    """Test installing the package."""
    print("\n=== Testing Package Installation ===\n")
    
    # Install the package
    if not run_command("pip install dist/*.whl", "Installing package"):
        return False
    
    # Test basic import
    test_script = """
import wmcoredb
print(f"✓ Package imported successfully")
print(f"Version: {wmcoredb.__version__}")
print(f"Author: {wmcoredb.__author__}")
"""
    
    if not run_command(f"python -c '{test_script}'", "Testing basic import"):
        return False
    
    return True


def test_package_functionality():
    """Test the package functionality."""
    print("\n=== Testing Package Functionality ===\n")
    
    test_script = """
import wmcoredb
import pathlib

# Test basic functions
print("Testing basic functions...")
schemas = wmcoredb.list_schemas()
print(f"Available schemas: {schemas}")

backends = wmcoredb.list_backends()
print(f"Available backends: {backends}")

# Test getting SQL files
print("\\nTesting SQL file access...")
sql_files = wmcoredb.get_sql_files('wmbs', 'oracle')
print(f"WMBS Oracle files: {[f.name for f in sql_files]}")

# Test getting schema info
print("\\nTesting schema info...")
info = wmcoredb.get_schema_info()
print(f"Schema info keys: {list(info.keys())}")

# Test reading SQL content
print("\\nTesting SQL content reading...")
from wmcoredb.schema import get_sql_content
content = get_sql_content('wmbs', 'oracle', 'create_wmbs_tables.sql')
if 'create_wmbs_tables.sql' in content:
    sql_content = content['create_wmbs_tables.sql']
    print(f"SQL content length: {len(sql_content)} characters")
    print(f"First 100 chars: {sql_content[:100]}...")
else:
    print("Could not read SQL content")

print("\\n✓ All functionality tests passed!")
"""
    
    if not run_command(f"python -c '{test_script}'", "Testing package functionality"):
        return False
    
    return True


def test_sql_files_included():
    """Test that SQL files are included in the package."""
    print("\n=== Testing SQL Files Inclusion ===\n")
    
    # Check wheel contents
    wheel_files = subprocess.run(
        "unzip -l dist/*.whl | grep -E '\\.sql$'",
        shell=True, capture_output=True, text=True
    )
    
    if wheel_files.returncode == 0:
        print("✓ SQL files found in wheel:")
        print(wheel_files.stdout)
    else:
        print("✗ No SQL files found in wheel")
        return False
    
    # Check tar.gz contents
    tar_files = subprocess.run(
        "tar -tzf dist/*.tar.gz | grep -E '\\.sql$'",
        shell=True, capture_output=True, text=True
    )
    
    if tar_files.returncode == 0:
        print("✓ SQL files found in tar.gz:")
        print(tar_files.stdout)
    else:
        print("✗ No SQL files found in tar.gz")
        return False
    
    return True


def test_example_script():
    """Test running the example script."""
    print("\n=== Testing Example Script ===\n")
    
    if not run_command("python examples/usage_example.py", "Running example script"):
        return False
    
    return True


def test_package_uninstall():
    """Test uninstalling the package."""
    print("\n=== Testing Package Uninstall ===\n")
    
    if not run_command("pip uninstall wmcoredb -y", "Uninstalling package"):
        return False
    
    return True


def main():
    """Main test function."""
    print("=== WMCore Database Schema Package Test Suite ===\n")
    
    success = True
    
    # Test 1: Build package
    if not test_package_build():
        success = False
    
    # Test 2: Install package
    if not test_package_installation():
        success = False
    
    # Test 3: Test functionality
    if not test_package_functionality():
        success = False
    
    # Test 4: Check SQL files inclusion
    if not test_sql_files_included():
        success = False
    
    # Test 5: Run example script
    if not test_example_script():
        success = False
    
    # Test 6: Uninstall package
    if not test_package_uninstall():
        success = False
    
    # Summary
    print("\n=== Test Summary ===")
    if success:
        print("🎉 All tests passed! The package is ready for publishing.")
        print("\nNext steps:")
        print("1. Create a git tag: git tag 1.0.0")
        print("2. Push the tag: git push origin 1.0.0")
        print("3. Monitor the GitHub Actions workflow")
        sys.exit(0)
    else:
        print("❌ Some tests failed. Please fix the issues before publishing.")
        sys.exit(1)


if __name__ == "__main__":
    main() 