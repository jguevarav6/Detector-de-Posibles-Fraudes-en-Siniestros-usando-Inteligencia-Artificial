"""Pruebas de construcción de SQLite local."""

from pathlib import Path

from src.data_generation.generate_synthetic_data import generate_all
from src.database.build_database import build_database
from src.database.queries import list_tables


def test_build_database_creates_expected_tables(tmp_path: Path) -> None:
    synthetic_dir = tmp_path / "synthetic"
    database_path = tmp_path / "processed" / "fraudlens_demo.sqlite"

    generate_all(output_dir=synthetic_dir, seed=321)
    build_database(input_dir=synthetic_dir, database_path=database_path)

    assert database_path.exists()
    assert set(list_tables(database_path)) >= {
        "claims",
        "policies",
        "insured",
        "vehicles",
        "providers",
        "documents",
        "risk_scores",
    }
