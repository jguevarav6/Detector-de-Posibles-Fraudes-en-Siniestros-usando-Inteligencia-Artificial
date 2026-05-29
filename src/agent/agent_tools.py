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


def frequent_insured_summary(df: pd.DataFrame, limit: int = 8) -> str:
    summary = (
        df.groupby("id_asegurado")
        .agg(casos=("id_siniestro", "count"), score=("score_final", "mean"), rojos=("nivel_riesgo", lambda s: int((s == "Rojo").sum())))
        .sort_values(["casos", "rojos", "score"], ascending=False)
        .head(limit)
    )
    return "Asegurados sinteticos con mayor frecuencia: " + "; ".join(
        f"{idx}: {row.casos} casos, {row.rojos} rojos, score promedio {row.score:.0f}" for idx, row in summary.iterrows()
    )


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


def top_risk_claims_json(limit: int = 10) -> list[dict]:
    df = load_scored_claims()
    if df.empty:
        return []
    cols = ["id_siniestro", "nivel_riesgo", "score_final", "ciudad", "ramo", "proveedor", "monto_reclamado"]
    return df.sort_values("score_final", ascending=False).head(limit)[cols].to_dict("records")


def explain_claim_json(id_siniestro: str) -> dict:
    df = load_scored_claims()
    if df.empty:
        return {"error": "siniestro_no_encontrado", "id_siniestro": id_siniestro}
    match = df[df["id_siniestro"].str.upper() == id_siniestro.upper()]
    if match.empty:
        return {"error": "siniestro_no_encontrado", "id_siniestro": id_siniestro}
    row = match.iloc[0]
    return {
        "id_siniestro": row.id_siniestro,
        "nivel_riesgo": row.nivel_riesgo,
        "score_final": float(row.score_final),
        "reglas_activadas": row.reglas_activadas,
        "explicacion": row.explicacion,
        "accion_sugerida": row.accion_sugerida,
    }


def provider_alert_summary_json(limit: int = 10) -> list[dict]:
    df = load_scored_claims()
    if df.empty:
        return []
    summary = (
        df.groupby("proveedor")
        .agg(casos=("id_siniestro", "count"), rojos=("nivel_riesgo", lambda s: int((s == "Rojo").sum())), score_promedio=("score_final", "mean"))
        .sort_values(["rojos", "score_promedio"], ascending=False)
        .head(limit)
        .reset_index()
    )
    return summary.to_dict("records")


def city_risk_summary_json(limit: int = 10) -> list[dict]:
    df = load_scored_claims()
    if df.empty:
        return []
    summary = (
        df.groupby("ciudad")
        .agg(casos=("id_siniestro", "count"), score_promedio=("score_final", "mean"), rojos=("nivel_riesgo", lambda s: int((s == "Rojo").sum())))
        .sort_values(["score_promedio", "rojos"], ascending=False)
        .head(limit)
        .reset_index()
    )
    return summary.to_dict("records")


def missing_documents_critical_json(limit: int = 10) -> list[dict]:
    df = load_scored_claims()
    if df.empty:
        return []
    critical = df[(df["nivel_riesgo"] == "Rojo") & (df["documentos"] != "Documentos completos")]
    return critical.sort_values("score_final", ascending=False).head(limit)[["id_siniestro", "score_final", "documentos"]].to_dict("records")


def similar_narratives_json(id_siniestro: str | None = None, limit: int = 10) -> list[dict]:
    df = load_scored_claims()
    if df.empty:
        return []
    similar = df[df["similar_claim_id"].fillna("") != ""]
    if id_siniestro:
        similar = similar[similar["id_siniestro"].str.upper() == id_siniestro.upper()]
    return similar.sort_values("max_similarity", ascending=False).head(limit)[["id_siniestro", "similar_claim_id", "max_similarity"]].to_dict("records")


def executive_summary_json() -> dict:
    df = load_scored_claims()
    if df.empty:
        return {"casos": 0, "mensaje": "No hay datos procesados."}
    return {
        "casos": int(len(df)),
        "rojos": int((df["nivel_riesgo"] == "Rojo").sum()),
        "amarillos": int((df["nivel_riesgo"] == "Amarillo").sum()),
        "verdes": int((df["nivel_riesgo"] == "Verde").sum()),
        "monto_rojo": float(df.loc[df["nivel_riesgo"] == "Rojo", "monto_reclamado"].sum()),
        "mensaje": executive_summary(df),
    }


def _claim_row(df: pd.DataFrame, id_siniestro: str | None):
    if df.empty:
        return None
    if id_siniestro:
        match = df[df["id_siniestro"].str.upper() == id_siniestro.upper()]
        if not match.empty:
            return match.iloc[0]
    return df.sort_values("score_final", ascending=False).iloc[0]
