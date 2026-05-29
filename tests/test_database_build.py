"""Pruebas de construccion de MySQL local."""

from pathlib import Path

from src.data_generation.generate_synthetic_data import generate_all
from src.database.build_database import build_database
from src.database.queries import list_tables
from src.database.settings import mysql_settings


def test_build_database_creates_expected_mysql_tables(tmp_path: Path) -> None:
    synthetic_dir = tmp_path / "synthetic"
    settings = mysql_settings()
    test_settings = type(settings)(
        host=settings.host,
        port=settings.port,
        database="fraudlens_claims_ai_test_db",
        user=settings.user,
        password=settings.password,
    )

    generate_all(output_dir=synthetic_dir, seed=321)
    target = build_database(input_dir=synthetic_dir, settings=test_settings)

    assert target.startswith("mysql://")
    assert set(list_tables(test_settings)) >= {
        "claims",
        "policies",
        "insured",
        "vehicles",
        "providers",
        "documents",
        "risk_scores",
    }
