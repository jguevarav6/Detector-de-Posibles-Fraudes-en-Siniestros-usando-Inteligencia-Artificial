"""Pruebas mínimas del frontend demo."""

from src.app.demo_data import load_claims


def test_load_claims_returns_demo_dataframe() -> None:
    claims = load_claims()

    assert not claims.empty
    assert {"id_siniestro", "score_final", "nivel_riesgo"}.issubset(claims.columns)


def test_demo_claims_have_expected_risk_levels() -> None:
    claims = load_claims()

    assert {"Verde", "Amarillo", "Rojo"}.issubset(set(claims["nivel_riesgo"]))
