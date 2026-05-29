"""Exportaciones y resumenes operativos de FraudLens."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


REPORTS_DIR = Path("data/processed/reports")


def critical_cases(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve casos rojos ordenados por score."""
    return df[df["nivel_riesgo"] == "Rojo"].sort_values("score_final", ascending=False)


def review_queue(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve casos rojos y amarillos para revision priorizada."""
    return df[df["nivel_riesgo"].isin(["Rojo", "Amarillo"])].sort_values("score_final", ascending=False)


def executive_summary(df: pd.DataFrame) -> dict:
    """Resumen serializable para reportes o pitch."""
    critical = critical_cases(df)
    queue = review_queue(df)
    return {
        "total_siniestros": int(len(df)),
        "casos_rojos": int(len(critical)),
        "casos_amarillos": int((df["nivel_riesgo"] == "Amarillo").sum()),
        "casos_verdes": int((df["nivel_riesgo"] == "Verde").sum()),
        "casos_revisables": int(len(queue)),
        "monto_rojo": float(critical["monto_reclamado"].sum()),
        "monto_revisable": float(queue["monto_reclamado"].sum()),
    }


def export_demo_reports(df: pd.DataFrame, output_dir: Path = REPORTS_DIR) -> dict[str, Path]:
    """Exporta CSV de casos rojos, cola revisable y resumen ejecutivo."""
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "casos_rojos": output_dir / "fraudlens_casos_rojos.csv",
        "bandeja_revisable": output_dir / "fraudlens_bandeja_revisable.csv",
        "resumen_ejecutivo": output_dir / "fraudlens_resumen_ejecutivo.csv",
    }
    critical_cases(df).to_csv(outputs["casos_rojos"], index=False)
    review_queue(df).to_csv(outputs["bandeja_revisable"], index=False)
    pd.DataFrame([executive_summary(df)]).to_csv(outputs["resumen_ejecutivo"], index=False)
    return outputs
