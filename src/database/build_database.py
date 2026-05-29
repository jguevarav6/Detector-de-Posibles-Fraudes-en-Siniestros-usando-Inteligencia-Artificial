"""Construccion reproducible de MySQL desde CSV sinteticos."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import mysql.connector
import pandas as pd
from mysql.connector import MySQLConnection

from src.database.settings import MySQLSettings, mysql_settings


SYNTHETIC_DIR = Path("data/synthetic")
TABLE_FILES = {
    "insured": "insured.csv",
    "policies": "policies.csv",
    "vehicles": "vehicles.csv",
    "providers": "providers.csv",
    "claims": "claims.csv",
    "documents": "documents.csv",
    "watchlist": "watchlist.csv",
}


def build_database(input_dir: Path = SYNTHETIC_DIR, settings: MySQLSettings | None = None) -> str:
    """Crea base MySQL y carga tablas sinteticas."""
    config = settings or mysql_settings()
    _create_database(config)
    with _connect(config, database=config.database) as connection:
        cursor = connection.cursor()
        for table, file_name in TABLE_FILES.items():
            csv_path = input_dir / file_name
            if csv_path.exists():
                _replace_table(connection, cursor, table, pd.read_csv(csv_path))
        _ensure_risk_scores(cursor)
        connection.commit()
    return f"mysql://{config.user}@{config.host}:{config.port}/{config.database}"


def write_risk_scores(scores: pd.DataFrame, settings: MySQLSettings | None = None) -> None:
    """Persiste scores procesados en MySQL."""
    config = settings or mysql_settings()
    _create_database(config)
    with _connect(config, database=config.database) as connection:
        cursor = connection.cursor()
        _replace_table(connection, cursor, "risk_scores", scores)
        connection.commit()


def _create_database(config: MySQLSettings) -> None:
    with _connect(config, database=None) as connection:
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{config.database}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
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
    cursor.execute(f"DROP TABLE IF EXISTS `{table}`")
    cursor.execute(_create_table_sql(table, df))
    if df.empty:
        return
    columns = list(df.columns)
    placeholders = ", ".join(["%s"] * len(columns))
    column_sql = ", ".join(f"`{column}`" for column in columns)
    values = [_clean_row(row) for row in df[columns].itertuples(index=False, name=None)]
    cursor.executemany(f"INSERT INTO `{table}` ({column_sql}) VALUES ({placeholders})", values)
    connection.commit()


def _create_table_sql(table: str, df: pd.DataFrame) -> str:
    columns = []
    for column in df.columns:
        columns.append(f"`{column}` {_mysql_type(df[column])}")
    if table == "risk_scores" and "id_siniestro" in df.columns:
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
