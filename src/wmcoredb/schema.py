"""
Schema utilities for WMCore Database Schema.

This module provides functions to access and work with SQL schema files
for both Oracle and MariaDB backends.
"""

import os
import pathlib
from typing import Dict, List, Optional, Tuple


def get_package_root() -> pathlib.Path:
    """Get the root directory of the wmcoredb package."""
    return pathlib.Path(__file__).parent


def get_sql_root() -> pathlib.Path:
    """Get the SQL files directory."""
    return get_package_root() / "sql"


def list_schemas() -> List[str]:
    """
    List all available schema components.
    
    Returns:
        List of schema component names (e.g., ['wmbs', 'agent', 'bossair', ...])
    """
    sql_root = get_sql_root()
    if not sql_root.exists():
        return []
    
    schemas = []
    for backend_dir in ['oracle', 'mariadb']:
        backend_path = sql_root / backend_dir
        if backend_path.exists():
            for item in backend_path.iterdir():
                if item.is_dir() and item.name not in schemas:
                    schemas.append(item.name)
    return sorted(schemas)


def get_schema_path(schema: str, backend: str = "oracle") -> Optional[pathlib.Path]:
    """
    Get the path to a specific schema directory.
    
    Args:
        schema: Schema name (e.g., 'wmbs', 'agent', 'bossair')
        backend: Database backend ('oracle' or 'mariadb')
        
    Returns:
        Path to the schema directory, or None if not found
    """
    if backend not in ['oracle', 'mariadb']:
        raise ValueError("backend must be 'oracle' or 'mariadb'")
    
    schema_path = get_sql_root() / backend / schema
    return schema_path if schema_path.exists() else None


def get_sql_files(schema: str, backend: str = "oracle") -> List[pathlib.Path]:
    """
    Get all SQL files for a specific schema and backend.
    
    Args:
        schema: Schema name (e.g., 'wmbs', 'agent', 'bossair')
        backend: Database backend ('oracle' or 'mariadb')
        
    Returns:
        List of SQL file paths, sorted by filename
    """
    schema_path = get_schema_path(schema, backend)
    if not schema_path:
        return []
    
    sql_files = []
    for file_path in schema_path.iterdir():
        if file_path.is_file() and file_path.suffix == '.sql':
            sql_files.append(file_path)
    
    return sorted(sql_files)


def get_sql_content(schema: str, backend: str = "oracle", filename: Optional[str] = None) -> Dict[str, str]:
    """
    Get the content of SQL files for a specific schema and backend.
    
    Args:
        schema: Schema name (e.g., 'wmbs', 'agent', 'bossair')
        backend: Database backend ('oracle' or 'mariadb')
        filename: Optional specific filename to read
        
    Returns:
        Dictionary mapping filename to SQL content
    """
    sql_files = get_sql_files(schema, backend)
    content = {}
    
    for file_path in sql_files:
        if filename is None or file_path.name == filename:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content[file_path.name] = f.read()
            except (IOError, OSError) as e:
                # Skip files that can't be read
                continue
    
    return content


def list_backends() -> List[str]:
    """
    List available database backends.
    
    Returns:
        List of available backends (e.g., ['oracle', 'mariadb'])
    """
    sql_root = get_sql_root()
    if not sql_root.exists():
        return []
    
    backends = []
    for backend_dir in ['oracle', 'mariadb']:
        backend_path = sql_root / backend_dir
        if backend_path.exists():
            backends.append(backend_dir)
    
    return sorted(backends)


def get_schema_info() -> Dict[str, Dict[str, List[str]]]:
    """
    Get comprehensive information about all available schemas and backends.
    
    Returns:
        Dictionary with structure: {backend: {schema: [files]}}
    """
    info = {}
    
    for backend in list_backends():
        info[backend] = {}
        for schema in list_schemas():
            schema_path = get_schema_path(schema, backend)
            if schema_path:
                files = [f.name for f in get_sql_files(schema, backend)]
                if files:
                    info[backend][schema] = files
    
    return info 