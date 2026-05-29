"""Construccion reproducible de las dos bases MySQL desde CSV sinteticos.

- `fraudlens_claims_ai`: operacional (claims, policies, insured, vehicles,
  providers, documents, risk_scores).
- `fraudlens_watchlist`: compliance (proveedores_observados,
  asegurados_antecedentes, vehiculos_marcados, narrativas_recurrentes).
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import mysql.connector
import pandas as pd
from mysql.connector import MySQLConnection

from src.database.settings import MySQLSettings, mysql_settings, watchlist_settings


SYNTHETIC_DIR = Path("data/synthetic")
WATCHLIST_DIR = Path("data/watchlist")

CLAIMS_TABLES = {
    "insured":   "insured.csv",
    "policies":  "policies.csv",
    "vehicles":  "vehicles.csv",
    "providers": "providers.csv",
    "claims":    "claims.csv",
    "documents": "documents.csv",
    "watchlist": "watchlist.csv",
}

WATCHLIST_TABLES = {
    "proveedores_observados":  "proveedores_observados.csv",
    "asegurados_antecedentes": "asegurados_antecedentes.csv",
    "vehiculos_marcados":      "vehiculos_marcados.csv",
    "narrativas_recurrentes":  "narrativas_recurrentes.csv",
}


def build_database(input_dir: Path = SYNTHETIC_DIR, settings: MySQLSettings | None = None) -> str:
    """Crea la base operacional y carga las tablas sinteticas."""
    config = settings or mysql_settings()
    _create_database(config)
    with _connect(config, database=config.database) as connection:
        cursor = connection.cursor()
        for table, file_name in CLAIMS_TABLES.items():
            csv_path = input_dir / file_name
            if csv_path.exists():
                _replace_table(connection, cursor, table, pd.read_csv(csv_path))
        _ensure_risk_scores(cursor)
        connection.commit()
    return f"mysql://{config.user}@{config.host}:{config.port}/{config.database}"


def build_watchlist_database(
    input_dir: Path = WATCHLIST_DIR,
    settings: MySQLSettings | None = None,
) -> str:
    """Crea la base de compliance y carga las cuatro tablas de watchlist."""
    config = settings or watchlist_settings()
    _create_database(config)
    with _connect(config, database=config.database) as connection:
        cursor = connection.cursor()
        for table, file_name in WATCHLIST_TABLES.items():
            csv_path = input_dir / file_name
            if csv_path.exists():
                _replace_table(connection, cursor, table, pd.read_csv(csv_path))
        connection.commit()
    return f"mysql://{config.user}@{config.host}:{config.port}/{config.database}"


def write_risk_scores(scores: pd.DataFrame, settings: MySQLSettings | None = None) -> None:
    config = settings or mysql_settings()
    _create_database(config)
    with _connect(config, database=config.database) as connection:
        cursor = connection.cursor()
        _replace_table(connection, cursor, "risk_scores", scores)
        connection.commit()


def _create_database(config: MySQLSettings) -> None:
    with _connect(config, database=None) as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{config.database}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        connection.commit()


def _connect(config: MySQLSettings, database: str | None) -> MySQLConnection:
    kwargs: dict[str, Any] = {
        "host": config.host,
        "port": config.port,
        "user": config.user,
        "password": config.password,
        "connection_timeout": 5,
    }
    if database:
        kwargs["database"] = database
    return mysql.connector.connect(**kwargs)


def _replace_table(connection: MySQLConnection, cursor: Any, table: str, df: pd.DataFrame) -> None:
    tmp = f"{table}__new"
    cursor.execute(f"DROP TABLE IF EXISTS `{tmp}`")
    cursor.execute(_create_table_sql(tmp, df))
    if not df.empty:
        columns = list(df.columns)
        placeholders = ", ".join(["%s"] * len(columns))
        column_sql = ", ".join(f"`{column}`" for column in columns)
        values = [_clean_row(row) for row in df[columns].itertuples(index=False, name=None)]
        cursor.executemany(f"INSERT INTO `{tmp}` ({column_sql}) VALUES ({placeholders})", values)
    cursor.execute(f"DROP TABLE IF EXISTS `{table}`")
    cursor.execute(f"RENAME TABLE `{tmp}` TO `{table}`")
    connection.commit()


def _create_table_sql(table: str, df: pd.DataFrame) -> str:
    columns = []
    for column in df.columns:
        columns.append(f"`{column}` {_mysql_type(df[column])}")
    base = table[:-5] if table.endswith("__new") else table
    if base == "risk_scores" and "id_siniestro" in df.columns:
        columns.append("PRIMARY KEY (`id_siniestro`)")
    return f"CREATE TABLE `{table}` ({', '.join(columns)}) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"


def _mysql_type(series: pd.Series) -> str:
    if pd.api.types.is_bool_dtype(series):
        return "BOOLEAN"
    if pd.api.types.is_integer_dtype(series):
        return "BIGINT"
    if pd.api.types.is_float_dtype(series):
        return "DOUBLE"
    max_len = int(series.dropna().astype(str).str.len().max() or 0)
    return "TEXT" if max_len > 240 else f"VARCHAR({max(max_len, 32)})"


def _clean_row(row: tuple[Any, ...]) -> tuple[Any, ...]:
    clean = []
    for value in row:
        if pd.isna(value):
            clean.append(None)
        elif isinstance(value, pd.Timestamp):
            clean.append(value.to_pydatetime())
        else:
            clean.append(value)
    return tuple(clean)


def _ensure_risk_scores(cursor: Any) -> None:
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS `risk_scores` (
            `id_siniestro` VARCHAR(32) PRIMARY KEY,
            `score_reglas` DOUBLE,
            `score_ml` DOUBLE,
            `score_anomalia` DOUBLE,
            `score_nlp` DOUBLE,
            `score_final` DOUBLE,
            `nivel_riesgo` VARCHAR(32),
            `reglas_activadas` TEXT,
            `explicacion` TEXT,
            `accion_sugerida` TEXT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
        """
    )
