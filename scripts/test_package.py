#!/usr/bin/env python3
import wmcoredb

def test_package():
    print("=== Testing wmcoredb Package ===")
    
    # Test version
    print(f"Version: {wmcoredb.__version__}")
    
    # Test backends
    backends = wmcoredb.list_backends()
    print(f"Backends: {backends}")
    assert "mariadb" in backends and "oracle" in backends
    
    # Test modules
    mariadb_modules = wmcoredb.list_modules("mariadb")
    oracle_modules = wmcoredb.list_modules("oracle")
    print(f"MariaDB modules: {mariadb_modules}")
    print(f"Oracle modules: {oracle_modules}")
    
    # Test SQL files
    mariadb_files = wmcoredb.list_sql_files("wmbs", "mariadb")
    oracle_files = wmcoredb.list_sql_files("wmbs", "oracle")
    print(f"MariaDB wmbs files: {mariadb_files}")
    print(f"Oracle wmbs files: {oracle_files}")
    
    # Test content
    mariadb_content = wmcoredb.get_sql_content("wmbs", "create_wmbs_tables.sql", "mariadb")
    oracle_content = wmcoredb.get_sql_content("wmbs", "create_wmbs_tables.sql", "oracle")
    print(f"MariaDB content starts with: {mariadb_content[:100]}")
    print(f"Oracle content starts with: {oracle_content[:100]}")
    
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_package()