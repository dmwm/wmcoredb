#!/usr/bin/env python3
"""
Example usage of the wmcoredb package.
"""

import wmcoredb


def main():
    print("=== WMCore Database Schema Package Example ===\n")
    
    # List available backends
    print("Available backends:")
    backends = wmcoredb.list_backends()
    for backend in backends:
        print(f"  - {backend}")
    print()
    
    # List available modules for MariaDB
    print("Available modules (MariaDB):")
    modules = wmcoredb.list_modules("mariadb")
    for module in modules:
        print(f"  - {module}")
    print()
    
    # List SQL files in WMBS module
    print("SQL files in WMBS module (MariaDB):")
    sql_files = wmcoredb.list_sql_files("wmbs", "mariadb")
    for sql_file in sql_files:
        print(f"  - {sql_file}")
    print()
    
    # Get a specific SQL file path
    print("Getting WMBS tables SQL file path:")
    try:
        file_path = wmcoredb.get_sql_file("wmbs", "create_wmbs_tables.sql", "mariadb")
        print(f"  Path: {file_path}")
    except FileNotFoundError as e:
        print(f"  Error: {e}")
    print()
    
    # Get SQL file content
    print("Getting WMBS tables SQL content (first 200 chars):")
    try:
        content = wmcoredb.get_sql_content("wmbs", "create_wmbs_tables.sql", "mariadb")
        print(f"  Content preview: {content[:200]}...")
    except FileNotFoundError as e:
        print(f"  Error: {e}")
    print()
    
    # Example for Oracle backend
    print("Available modules (Oracle):")
    oracle_modules = wmcoredb.list_modules("oracle")
    for module in oracle_modules:
        print(f"  - {module}")
    print()
    
    # Get Oracle SQL file
    print("Getting Oracle WMBS tables SQL file:")
    try:
        oracle_file = wmcoredb.get_sql_file("wmbs", "create_wmbs_tables.sql", "oracle")
        print(f"  Path: {oracle_file}")
    except FileNotFoundError as e:
        print(f"  Error: {e}")


if __name__ == "__main__":
    main() 