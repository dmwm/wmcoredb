#!/usr/bin/env python3
"""
Development setup script for wmcoredb package.

This script helps with local development and testing of the wmcoredb package.
"""

import subprocess
import sys
import pathlib
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed")
        print(f"Error: {e.stderr}")
        return False


def main():
    """Main setup function."""
    print("=== WMCore Database Schema Development Setup ===\n")
    
    # Check if we're in the right directory
    if not Path("pyproject.toml").exists():
        print("Error: pyproject.toml not found. Please run this script from the project root.")
        sys.exit(1)
    
    # Install development dependencies
    print("Installing development dependencies...")
    if not run_command("pip install build pytest", "Installing build tools"):
        sys.exit(1)
    
    # Build the package
    print("\nBuilding package...")
    if not run_command("python -m build", "Building package"):
        sys.exit(1)
    
    # Install the package in development mode
    print("\nInstalling package in development mode...")
    if not run_command("pip install -e .", "Installing package in development mode"):
        sys.exit(1)
    
    # Run tests
    print("\nRunning tests...")
    if not run_command("python test_package.py", "Running comprehensive tests"):
        print("Warning: Tests failed, but continuing...")
    
    # Test package functionality
    print("\nTesting package functionality...")
    test_script = """
import wmcoredb
import sys

try:
    print(f"Package version: {wmcoredb.__version__}")
    print(f"Available schemas: {wmcoredb.list_schemas()}")
    print(f"Available backends: {wmcoredb.list_backends()}")
    
    # Test getting SQL files
    sql_files = wmcoredb.get_sql_files('wmbs', 'oracle')
    print(f"WMBS Oracle files: {[f.name for f in sql_files]}")
    
    print("✓ Package functionality test passed")
    sys.exit(0)
except Exception as e:
    print(f"✗ Package functionality test failed: {e}")
    sys.exit(1)
"""
    
    if not run_command(f"python -c '{test_script}'", "Testing package functionality"):
        sys.exit(1)
    
    print("\n=== Setup Complete ===")
    print("The wmcoredb package is now ready for development.")
    print("\nNext steps:")
    print("1. Run the example: python examples/usage_example.py")
    print("2. Make changes to the code")
    print("3. Test changes: python test_package.py")
    print("4. Build package: python -m build")
    print("5. To publish: git tag 1.0.0 && git push --tags")


if __name__ == "__main__":
    main() 