"""Configuracion de MySQL sin depender de credenciales versionadas."""

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


def mysql_settings() -> MySQLSettings:
    """Devuelve configuracion MySQL para demo local.

    Las variables de entorno tienen prioridad. Los defaults son para entorno local de hackathon.
    """
    return MySQLSettings(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        database=os.getenv("MYSQL_DATABASE", "fraudlens_claims_ai"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "root"),
    )
