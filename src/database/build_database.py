"""Construcción de SQLite local desde CSV sintéticos."""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


SYNTHETIC_DIR = Path("data/synthetic")
DATABASE_PATH = Path("data/processed/fraudlens_demo.sqlite")


TABLE_FILES = {
    "claims": "claims.csv",
    "policies": "policies.csv",
    "insured": "insured.csv",
    "vehicles": "vehicles.csv",
    "providers": "providers.csv",
    "documents": "documents.csv",
}


def build_database(input_dir: Path = SYNTHETIC_DIR, database_path: Path = DATABASE_PATH) -> Path:
    """Crea una base SQLite local con las tablas principales."""
    database_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(database_path) as connection:
        for table, filename in TABLE_FILES.items():
            path = input_dir / filename
            if not path.exists():
                raise FileNotFoundError(f"No existe CSV requerido: {path}")
            pd.read_csv(path).to_sql(table, connection, if_exists="replace", index=False)
        _create_empty_risk_scores(connection)
    return database_path


def _create_empty_risk_scores(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS risk_scores (
            id_siniestro TEXT PRIMARY KEY,
            score_reglas REAL,
            score_ml REAL,
            score_anomalia REAL,
            score_nlp REAL,
            score_final REAL,
            nivel_riesgo TEXT,
            reglas_activadas TEXT,
            explicacion TEXT,
            accion_sugerida TEXT
        )
        """
    )


if __name__ == "__main__":
    print(build_database())
