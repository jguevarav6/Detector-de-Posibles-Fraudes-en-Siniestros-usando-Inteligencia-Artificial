"""Configuracion de MySQL para las dos bases de datos del sistema.

FraudLens usa una arquitectura de dos bases separadas:

- `fraudlens_claims_ai` (operacional): siniestros, polizas, asegurados,
  vehiculos, proveedores, documentos y risk_scores.
- `fraudlens_watchlist` (compliance): proveedores observados, asegurados con
  antecedentes, vehiculos marcados y narrativas recurrentes. Es la base que
  un equipo de cumplimiento mantiene de forma independiente al operativo.

El agente y el MCP consultan ambas para responder preguntas que requieran
cruzar datos transaccionales con la lista restrictiva.
"""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class MySQLSettings:
    host: str
    port: int
    database: str
    user: str
    password: str


def database_backend() -> str:
    return os.getenv("DB_BACKEND", "mysql").strip().lower()


def _settings(database_env: str, default_db: str) -> MySQLSettings:
    return MySQLSettings(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        database=os.getenv(database_env, default_db),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "root"),
    )


def mysql_settings() -> MySQLSettings:
    """Base operacional principal (siniestros, polizas, scoring)."""
    return _settings("MYSQL_DATABASE", "fraudlens_claims_ai")


def watchlist_settings() -> MySQLSettings:
    """Base de compliance con la watchlist de proveedores y asegurados."""
    return _settings("MYSQL_WATCHLIST_DATABASE", "fraudlens_watchlist")
