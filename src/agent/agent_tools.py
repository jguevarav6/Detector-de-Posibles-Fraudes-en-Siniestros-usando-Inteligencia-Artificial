"""Tools controladas para el agente local de FraudLens."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


SCORED_CLAIMS_PATH = Path("data/processed/scored_claims.csv")


def load_scored_claims(path: Path = SCORED_CLAIMS_PATH) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def top_risk_claims(df: pd.DataFrame, limit: int = 10) -> str:
    top = df.sort_values("score_final", ascending=False).head(limit)
    items = [f"{row.id_siniestro} ({row.nivel_riesgo}, score {row.score_final:.0f})" for row in top.itertuples()]
    return "Casos de mayor prioridad de revision: " + ", ".join(items)


def explain_claim(df: pd.DataFrame, id_siniestro: str | None = None) -> str:
    row = _claim_row(df, id_siniestro)
    if row is None:
        return "No encontre ese siniestro en los datos procesados."
    return f"{row.id_siniestro}: {row.explicacion} Reglas: {row.reglas_activadas}."


def provider_alert_summary(df: pd.DataFrame, limit: int = 5) -> str:
    summary = (
        df.groupby("proveedor")
        .agg(casos=("id_siniestro", "count"), rojos=("nivel_riesgo", lambda s: int((s == "Rojo").sum())), score=("score_final", "mean"))
        .sort_values(["rojos", "score"], ascending=False)
        .head(limit)
    )
    return "Proveedores con mas alertas: " + "; ".join(
        f"{idx}: {row.rojos} rojos, {row.casos} casos, score promedio {row.score:.0f}" for idx, row in summary.iterrows()
    )


def city_risk_summary(df: pd.DataFrame, limit: int = 5) -> str:
    summary = df.groupby("ciudad")["score_final"].mean().sort_values(ascending=False).head(limit)
    return "Ciudades con mayor concentracion: " + ", ".join(f"{city} ({score:.0f})" for city, score in summary.items())


def branch_risk_summary(df: pd.DataFrame, limit: int = 5) -> str:
    summary = df.groupby("ramo")["score_final"].mean().sort_values(ascending=False).head(limit)
    return "Ramos con mayor prioridad promedio: " + ", ".join(f"{branch} ({score:.0f})" for branch, score in summary.items())


def missing_documents_summary(df: pd.DataFrame, limit: int = 8) -> str:
    critical = df[(df["nivel_riesgo"] == "Rojo") & (df["documentos"] != "Documentos completos")].head(limit)
    if critical.empty:
        return "No hay casos rojos con documentos faltantes en el archivo procesado."
    return "Documentos a revisar en casos criticos: " + "; ".join(f"{row.id_siniestro}: {row.documentos}" for row in critical.itertuples())


def atypical_amounts(df: pd.DataFrame, limit: int = 8) -> str:
    top = df.sort_values("monto_reclamado", ascending=False).head(limit)
    return "Montos mas altos para validar: " + "; ".join(f"{row.id_siniestro}: ${row.monto_reclamado:,.0f}" for row in top.itertuples())


def near_policy_start(df: pd.DataFrame, limit: int = 8) -> str:
    top = df[df["dias_desde_inicio_poliza"] <= 7].sort_values("score_final", ascending=False).head(limit)
    return "Siniestros cerca del inicio de poliza: " + ", ".join(f"{row.id_siniestro} ({row.dias_desde_inicio_poliza} dias)" for row in top.itertuples())


def similar_narratives(df: pd.DataFrame, limit: int = 8) -> str:
    top = df[df["similar_claim_id"].fillna("") != ""].sort_values("max_similarity", ascending=False).head(limit)
    if top.empty:
        return "No se detectaron narrativas similares sobre el umbral definido."
    return "Narrativas similares detectadas: " + "; ".join(
        f"{row.id_siniestro} similar a {row.similar_claim_id} ({row.max_similarity:.0%})" for row in top.itertuples()
    )


def executive_summary(df: pd.DataFrame) -> str:
    red = int((df["nivel_riesgo"] == "Rojo").sum())
    yellow = int((df["nivel_riesgo"] == "Amarillo").sum())
    amount_red = float(df.loc[df["nivel_riesgo"] == "Rojo", "monto_reclamado"].sum())
    return (
        f"Resumen ejecutivo: {len(df)} siniestros procesados, {red} rojos y {yellow} amarillos. "
        f"El monto reclamado en prioridad roja suma ${amount_red:,.0f}. "
        "La salida prioriza revision humana y no confirma fraude."
    )


def _claim_row(df: pd.DataFrame, id_siniestro: str | None):
    if df.empty:
        return None
    if id_siniestro:
        match = df[df["id_siniestro"].str.upper() == id_siniestro.upper()]
        if not match.empty:
            return match.iloc[0]
    return df.sort_values("score_final", ascending=False).iloc[0]
