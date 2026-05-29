"""Acceso a la base de compliance fraudlens_watchlist con fallback a CSV.

Estrategia: si hay MySQL disponible, se leen las 4 tablas con SQL real;
si no (ejemplo, deploy en Streamlit Community Cloud), se cae automaticamente
a los CSV versionados en `data/watchlist/`. La interfaz publica es la misma:
funciones que devuelven `pd.DataFrame`.
"""

from __future__ import annotations

import logging
from functools import lru_cache
from pathlib import Path

import pandas as pd

from src.database.settings import MySQLSettings, watchlist_settings


logger = logging.getLogger("fraudlens.watchlist")

WATCHLIST_CSV_DIR = Path("data/watchlist")

TABLE_TO_CSV = {
    "proveedores_observados":  "proveedores_observados.csv",
    "asegurados_antecedentes": "asegurados_antecedentes.csv",
    "vehiculos_marcados":      "vehiculos_marcados.csv",
    "narrativas_recurrentes":  "narrativas_recurrentes.csv",
}


def read_watchlist_table(table: str, settings: MySQLSettings | None = None) -> pd.DataFrame:
    """Lee una tabla de la base de compliance.

    Intenta MySQL primero; si falla por cualquier motivo (sin servicio,
    sin credenciales, deploy remoto), usa el CSV equivalente.
    """
    if table not in TABLE_TO_CSV:
        raise ValueError(f"Tabla no permitida en watchlist: {table}")
    config = settings or watchlist_settings()
    df = _read_from_mysql(table, config)
    if df is not None:
        return df
    return _read_from_csv(table)


def proveedores_observados(settings: MySQLSettings | None = None) -> pd.DataFrame:
    return read_watchlist_table("proveedores_observados", settings)


def asegurados_antecedentes(settings: MySQLSettings | None = None) -> pd.DataFrame:
    return read_watchlist_table("asegurados_antecedentes", settings)


def vehiculos_marcados(settings: MySQLSettings | None = None) -> pd.DataFrame:
    return read_watchlist_table("vehiculos_marcados", settings)


def narrativas_recurrentes(settings: MySQLSettings | None = None) -> pd.DataFrame:
    return read_watchlist_table("narrativas_recurrentes", settings)


def watchlist_status(settings: MySQLSettings | None = None) -> dict[str, str | int]:
    """Devuelve estado de la conexion para mostrar en el dashboard."""
    config = settings or watchlist_settings()
    counts: dict[str, str | int] = {}
    source = "MySQL"
    for table in TABLE_TO_CSV:
        df = _read_from_mysql(table, config)
        if df is None:
            source = "CSV (fallback)"
            df = _read_from_csv(table)
        counts[table] = len(df)
    counts["source"] = source
    counts["database"] = config.database
    return counts


def _read_from_mysql(table: str, config: MySQLSettings) -> pd.DataFrame | None:
    try:
        import mysql.connector  # noqa: F401
        from src.database.build_database import _connect
    except Exception as exc:
        logger.warning("MySQL no disponible para %s, usando CSV: %s", table, exc)
        return None
    try:
        with _connect(config, database=config.database) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM `{table}`")
            rows = cursor.fetchall()
            columns = [item[0] for item in cursor.description]
            return pd.DataFrame(rows, columns=columns)
    except Exception as exc:
        logger.warning("Lectura MySQL fallida para %s, usando CSV: %s", table, exc)
        return None


@lru_cache(maxsize=8)
def _read_from_csv(table: str) -> pd.DataFrame:
    path = WATCHLIST_CSV_DIR / TABLE_TO_CSV[table]
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)
