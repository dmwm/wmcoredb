"""
WMCore Database Schema Package

This package provides database schema definitions for WMCore components,
supporting both Oracle and MariaDB backends.
"""

from .version import __version__, __author__, __email__

from .schema import get_sql_files, get_schema_path, list_schemas, get_schema_info, list_backends, get_sql_root

__all__ = ["get_sql_files", "get_schema_path", "list_schemas", "get_schema_info", "list_backends", "get_sql_root"] 