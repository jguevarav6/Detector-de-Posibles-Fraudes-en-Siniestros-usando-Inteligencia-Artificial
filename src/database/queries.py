"""Consultas controladas para MySQL."""

from __future__ import annotations

import pandas as pd

from src.database.build_database import _connect
from src.database.settings import MySQLSettings, mysql_settings


ALLOWED_TABLES = {
    "claims",
    "policies",
    "insured",
    "vehicles",
    "providers",
    "documents",
    "watchlist",
    "risk_scores",
}


def read_table(table_name: str, settings: MySQLSettings | None = None) -> pd.DataFrame:
    """Lee una tabla permitida desde MySQL."""
    if table_name not in ALLOWED_TABLES:
        raise ValueError(f"Tabla no permitida: {table_name}")
    config = settings or mysql_settings()
    with _connect(config, database=config.database) as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM `{table_name}`")
        rows = cursor.fetchall()
        columns = [item[0] for item in cursor.description]
        return pd.DataFrame(rows, columns=columns)


def list_tables(settings: MySQLSettings | None = None) -> list[str]:
    """Lista tablas disponibles en la base MySQL de la demo."""
    config = settings or mysql_settings()
    with _connect(config, database=config.database) as connection:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        return [row[0] for row in cursor.fetchall()]
