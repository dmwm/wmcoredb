# Development Scripts

This directory contains development and testing scripts for the wmcoredb package.

## Scripts

### `setup_dev.py`
Development setup script that:
- Installs build dependencies (build, pytest)
- Builds the package
- Installs the package in development mode
- Runs comprehensive tests
- Tests package functionality

**Usage:**
```bash
python scripts/setup_dev.py
```

### `test_package.py`
Comprehensive test script that:
- Builds the package
- Installs the package
- Tests all functionality
- Verifies SQL files are included
- Runs the example script
- Uninstalls the package

**Usage:**
```bash
python scripts/test_package.py
```

## Quick Development Workflow

1. **Initial setup:**
   ```bash
   python scripts/setup_dev.py
   ```

2. **Make changes to the code**

3. **Test changes:**
   ```bash
   python scripts/test_package.py
   ```

4. **Run example:**
   ```bash
   python examples/usage_example.py
   ```

5. **Build for distribution:**
   ```bash
   python -m build
   ```

## Notes

- These scripts are for development and testing only
- They are not included in the PyPI package
- Use them to validate changes before committing 