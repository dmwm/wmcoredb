#!/usr/bin/env python3
"""
Example usage of the wmcoredb package.

This script demonstrates how to use the wmcoredb package to access
database schema files for WMCore components.
"""

import wmcoredb
import pathlib


def main():
    """Demonstrate package usage."""
    print("=== WMCore Database Schema Package Example ===\n")
    
    # Display package information
    print(f"Package version: {wmcoredb.__version__}")
    print(f"Package author: {wmcoredb.__author__}")
    print()
    
    # List available backends
    backends = wmcoredb.list_backends()
    print(f"Available database backends: {backends}")
    print()
    
    # List available schemas
    schemas = wmcoredb.list_schemas()
    print(f"Available schemas: {schemas}")
    print()
    
    # Display comprehensive schema information
    print("=== Schema Information ===")
    schema_info = wmcoredb.get_schema_info()
    
    for backend in backends:
        print(f"\n{backend.upper()} Backend:")
        if backend in schema_info:
            for schema, files in schema_info[backend].items():
                print(f"  {schema}:")
                for filename in files:
                    print(f"    - {filename}")
        else:
            print("  No schemas available")
    
    print("\n=== Example: Accessing WMBS Schema ===")
    
    # Example: Get SQL files for WMBS schema in Oracle
    wmbs_files = wmcoredb.get_sql_files('wmbs', 'oracle')
    print(f"WMBS Oracle SQL files ({len(wmbs_files)} files):")
    for file_path in wmbs_files:
        print(f"  - {file_path.name}")
    
    # Example: Get SQL files for WMBS schema in MariaDB
    wmbs_mariadb_files = wmcoredb.get_sql_files('wmbs', 'mariadb')
    print(f"\nWMBS MariaDB SQL files ({len(wmbs_mariadb_files)} files):")
    for file_path in wmbs_mariadb_files:
        print(f"  - {file_path.name}")
    
    print("\n=== Example: Reading SQL Content ===")
    
    # Example: Read content of a specific SQL file
    from wmcoredb.schema import get_sql_content
    
    # Get content of WMBS tables file for Oracle
    content = get_sql_content('wmbs', 'oracle', 'create_wmbs_tables.sql')
    if 'create_wmbs_tables.sql' in content:
        sql_content = content['create_wmbs_tables.sql']
        print(f"WMBS Oracle tables file (first 200 chars):")
        print(f"  {sql_content[:200]}...")
    else:
        print("WMBS Oracle tables file not found")
    
    print("\n=== Example: Schema Path Access ===")
    
    # Example: Get schema directory path
    schema_path = wmcoredb.get_schema_path('agent', 'oracle')
    if schema_path:
        print(f"Agent Oracle schema path: {schema_path}")
        print(f"Path exists: {schema_path.exists()}")
    else:
        print("Agent Oracle schema path not found")


if __name__ == "__main__":
    main() 