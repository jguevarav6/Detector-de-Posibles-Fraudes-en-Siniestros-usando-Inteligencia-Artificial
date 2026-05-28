"""Consultas controladas para SQLite local."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


DATABASE_PATH = Path("data/processed/fraudlens_demo.sqlite")


def read_table(table_name: str, database_path: Path = DATABASE_PATH) -> pd.DataFrame:
    """Lee una tabla completa desde SQLite."""
    with sqlite3.connect(database_path) as connection:
        return pd.read_sql_query(f"SELECT * FROM {table_name}", connection)


def list_tables(database_path: Path = DATABASE_PATH) -> list[str]:
    """Lista tablas disponibles."""
    with sqlite3.connect(database_path) as connection:
        rows = connection.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()
    return [row[0] for row in rows]
