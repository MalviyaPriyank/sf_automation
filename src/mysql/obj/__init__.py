"""
SQL Builder Package
A Python library for building and executing MySQL SQL statements.
"""

from .base import SQLBuilder
from .database import CreateDatabase, AlterDatabase, DropDatabase
from .table import (
    CreateTable,
    AlterTable,
    DropTable,
    RenameTable,
    TruncateTable,
    ColumnDefinition
)
from .view import CreateView, AlterView, DropView
from .executor import DatabaseExecutor, DatabaseConnection, PermissionError

__version__ = "1.0.0"
__all__ = [
    "SQLBuilder",
    # Database operations
    "CreateDatabase",
    "AlterDatabase",
    "DropDatabase",
    # Table operations
    "CreateTable",
    "AlterTable",
    "DropTable",
    "RenameTable",
    "TruncateTable",
    "ColumnDefinition",
    # View operations
    "CreateView",
    "AlterView",
    "DropView",
    # Executor
    "DatabaseExecutor",
    "DatabaseConnection",
    "PermissionError",
]