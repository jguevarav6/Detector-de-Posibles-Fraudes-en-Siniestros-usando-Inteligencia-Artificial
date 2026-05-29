"""Pruebas de scoring explicable."""

from pathlib import Path

from src.data_generation.generate_synthetic_data import generate_all
from src.database.build_database import build_database
from src.database.settings import mysql_settings
from src.scoring.scoring_service import UI_COLUMNS, run_scoring_pipeline


def test_scoring_pipeline_creates_ui_contract(tmp_path: Path) -> None:
    synthetic_dir = tmp_path / "synthetic"
    processed_dir = tmp_path / "processed"
    settings = mysql_settings()
    test_settings = type(settings)(
        host=settings.host,
        port=settings.port,
        database="fraudlens_claims_ai_test_scoring",
        user=settings.user,
        password=settings.password,
    )

    generate_all(output_dir=synthetic_dir, seed=456)
    build_database(input_dir=synthetic_dir, settings=test_settings)
    scored = run_scoring_pipeline(input_dir=synthetic_dir, output_dir=processed_dir, db_settings=test_settings)

    assert len(scored) == 1000
    assert set(UI_COLUMNS).issubset(scored.columns)
    assert scored["score_final"].between(0, 100).all()
    assert scored["nivel_riesgo"].isin(["Verde", "Amarillo", "Rojo"]).all()
    assert {"proveedor_porcentaje_casos_observados", "proveedor_lista_restrictiva", "monto_vs_suma_asegurada"}.issubset(scored.columns)
    assert (processed_dir / "scored_claims.csv").exists()
    assert (processed_dir / "model_metrics.json").exists()
