"""Pruebas de generación de datos sintéticos."""

from pathlib import Path

import pandas as pd

from src.data_generation.generate_synthetic_data import generate_all


def test_generate_all_creates_expected_csv_files(tmp_path: Path) -> None:
    outputs = generate_all(output_dir=tmp_path, seed=123)

    assert set(outputs) == {"insured", "policies", "vehicles", "providers", "claims", "documents", "watchlist"}
    for path in outputs.values():
        assert path.exists()


def test_claims_are_synthetic_and_include_risk_patterns(tmp_path: Path) -> None:
    outputs = generate_all(output_dir=tmp_path, seed=123)
    claims = pd.read_csv(outputs["claims"])

    assert len(claims) == 1000
    assert claims["id_siniestro"].str.startswith("SIN-").all()
    assert claims["id_asegurado"].str.startswith("ASE-").all()
    assert claims["etiqueta_fraude_simulada"].isin([0, 1]).all()
    assert claims["etiqueta_fraude_simulada"].sum() > 0
    assert (claims["dias_entre_ocurrencia_reporte"] >= 0).all()
