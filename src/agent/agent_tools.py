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


# =====================================================================
# Tools que cruzan fraudlens_claims_ai con fraudlens_watchlist (DB2)
# =====================================================================

def check_watchlist(id_siniestro: str) -> str:
    """Devuelve si un siniestro cruza con alguna tabla de la watchlist."""
    from src.database import watchlist_repo

    df = load_scored_claims()
    if df.empty:
        return "No hay datos procesados para consultar la watchlist."
    match = df[df["id_siniestro"].str.upper() == id_siniestro.upper()]
    if match.empty:
        return f"No encuentro {id_siniestro} en la base operacional."
    claim = match.iloc[0]
    hits: list[str] = []

    provs = watchlist_repo.proveedores_observados()
    if not provs.empty and "id_proveedor" in df.columns and claim.get("id_proveedor") in set(provs["id_proveedor"]):
        prov_row = provs[provs["id_proveedor"] == claim["id_proveedor"]].iloc[0]
        hits.append(f"proveedor {claim['id_proveedor']} en watchlist ({prov_row['nivel_alerta']}: {prov_row['motivo']})")

    asegs = watchlist_repo.asegurados_antecedentes()
    if not asegs.empty and claim.get("id_asegurado") in set(asegs["id_asegurado"]):
        ase_row = asegs[asegs["id_asegurado"] == claim["id_asegurado"]].iloc[0]
        hits.append(f"asegurado {claim['id_asegurado']} con antecedente ({ase_row['motivo']})")

    vehs = watchlist_repo.vehiculos_marcados()
    if not vehs.empty and claim.get("id_vehiculo") in set(vehs["id_vehiculo"]):
        veh_row = vehs[vehs["id_vehiculo"] == claim["id_vehiculo"]].iloc[0]
        hits.append(f"vehiculo {claim['id_vehiculo']} marcado ({veh_row['motivo']})")

    if not hits:
        return f"{id_siniestro} no cruza con ninguna alerta de compliance."
    return f"{id_siniestro} cruza con compliance: " + "; ".join(hits) + "."


def cross_reference_claim(id_siniestro: str) -> dict:
    """Devuelve el expediente cruzado claim + watchlist para una respuesta rica."""
    from src.database import watchlist_repo

    df = load_scored_claims()
    if df.empty:
        return {"error": "sin_datos"}
    match = df[df["id_siniestro"].str.upper() == id_siniestro.upper()]
    if match.empty:
        return {"error": "siniestro_no_encontrado", "id_siniestro": id_siniestro}
    claim = match.iloc[0]
    result: dict = {
        "id_siniestro":   claim["id_siniestro"],
        "nivel_riesgo":   claim["nivel_riesgo"],
        "score_final":    float(claim["score_final"]),
        "ciudad":         claim.get("ciudad"),
        "ramo":           claim.get("ramo"),
        "proveedor":      claim.get("proveedor"),
        "asegurado":      claim.get("asegurado"),
        "monto":          float(claim.get("monto_reclamado", 0)),
        "watchlist_hits": [],
    }
    provs = watchlist_repo.proveedores_observados()
    if not provs.empty and claim.get("id_proveedor") in set(provs["id_proveedor"]):
        row = provs[provs["id_proveedor"] == claim["id_proveedor"]].iloc[0]
        result["watchlist_hits"].append({"tipo": "proveedor", **row.to_dict()})
    asegs = watchlist_repo.asegurados_antecedentes()
    if not asegs.empty and claim.get("id_asegurado") in set(asegs["id_asegurado"]):
        row = asegs[asegs["id_asegurado"] == claim["id_asegurado"]].iloc[0]
        result["watchlist_hits"].append({"tipo": "asegurado", **row.to_dict()})
    vehs = watchlist_repo.vehiculos_marcados()
    if not vehs.empty and claim.get("id_vehiculo") in set(vehs["id_vehiculo"]):
        row = vehs[vehs["id_vehiculo"] == claim["id_vehiculo"]].iloc[0]
        result["watchlist_hits"].append({"tipo": "vehiculo", **row.to_dict()})
    return result


def watchlist_summary() -> dict:
    """Resumen ejecutivo de cuanto cruzan ambas bases."""
    from src.database import watchlist_repo

    df = load_scored_claims()
    if df.empty:
        return {"error": "sin_datos"}
    provs = watchlist_repo.proveedores_observados()
    asegs = watchlist_repo.asegurados_antecedentes()
    vehs = watchlist_repo.vehiculos_marcados()
    prov_ids = set(provs["id_proveedor"]) if not provs.empty else set()
    aseg_ids = set(asegs["id_asegurado"]) if not asegs.empty else set()
    veh_ids = set(vehs["id_vehiculo"]) if not vehs.empty else set()

    claims_prov = df["id_proveedor"].isin(prov_ids) if "id_proveedor" in df.columns else pd.Series([False] * len(df))
    claims_aseg = df["id_asegurado"].isin(aseg_ids) if "id_asegurado" in df.columns else pd.Series([False] * len(df))
    claims_veh = df["id_vehiculo"].isin(veh_ids) if "id_vehiculo" in df.columns else pd.Series([False] * len(df))
    any_hit = claims_prov | claims_aseg | claims_veh

    rojos_cross = int((df.loc[any_hit, "nivel_riesgo"] == "Rojo").sum())
    return {
        "claims_total":              int(len(df)),
        "claims_con_alerta_compliance": int(any_hit.sum()),
        "claims_rojos_con_alerta":   rojos_cross,
        "watchlist_proveedores":     int(len(provs)),
        "watchlist_asegurados":      int(len(asegs)),
        "watchlist_vehiculos":       int(len(vehs)),
        "mensaje": (
            f"{int(any_hit.sum())} siniestros cruzan con la watchlist; "
            f"{rojos_cross} son rojos. Total operacional: {len(df)}."
        ),
    }


def pareto_red_providers(coverage: float = 0.8) -> dict:
    """Calcula el conjunto minimo de proveedores que concentra el N% de rojos.

    Implementa la pregunta de fuego del jurado: 'que proveedores concentran
    el 80% de las alertas rojas'.
    """
    df = load_scored_claims()
    if df.empty:
        return {"error": "sin_datos"}
    rojos = df[df["nivel_riesgo"] == "Rojo"]
    if rojos.empty:
        return {"error": "sin_rojos"}
    ranking = (
        rojos.groupby("proveedor").size().sort_values(ascending=False).rename("rojos").reset_index()
    )
    total = int(ranking["rojos"].sum())
    threshold = total * coverage
    accumulated = 0
    selected: list[dict] = []
    for _, row in ranking.iterrows():
        accumulated += int(row["rojos"])
        selected.append({"proveedor": row["proveedor"], "rojos": int(row["rojos"]), "acumulado": accumulated})
        if accumulated >= threshold:
            break
    return {
        "cobertura_objetivo": coverage,
        "rojos_totales":      total,
        "proveedores":        selected,
        "n_proveedores":      len(selected),
        "porcentaje_cubierto": round(accumulated / total, 4),
        "mensaje": (
            f"{len(selected)} proveedores concentran el "
            f"{accumulated / total:.0%} de las {total} alertas rojas."
        ),
    }


def simulate_claim_score(
    monto_reclamado: float,
    suma_asegurada: float,
    dias_desde_inicio_poliza: int,
    dias_entre_ocurrencia_reporte: int,
    documentos_completos: bool = True,
    ramo: str = "Vehiculos",
) -> dict:
    """Aplica reglas explicables a un siniestro nuevo (no persistido).

    Soporta la prueba de fuego 'cargue este siniestro ocurrido 24h despues
    de la poliza y explique el riesgo'.
    """
    reglas: list[dict] = []
    score = 0

    if dias_desde_inicio_poliza <= 7:
        score += 25
        reglas.append({"codigo": "R001", "puntos": 25, "regla": "Borde de vigencia: siniestro dentro de los primeros 7 dias."})
    if dias_entre_ocurrencia_reporte >= 10:
        score += 18
        reglas.append({"codigo": "R002", "puntos": 18, "regla": f"Reporte tardio: {dias_entre_ocurrencia_reporte} dias entre ocurrencia y reporte."})
    if suma_asegurada and monto_reclamado / suma_asegurada >= 0.7:
        score += 22
        reglas.append({"codigo": "R012", "puntos": 22, "regla": "Monto reclamado supera el 70% de la suma asegurada."})
    if not documentos_completos:
        score += 15
        reglas.append({"codigo": "R007", "puntos": 15, "regla": "Documentos incompletos al momento del reporte."})

    score = min(score, 100)
    if score >= 76:
        nivel = "Rojo"
        accion = "Revision urgente"
    elif score >= 41:
        nivel = "Amarillo"
        accion = "Revision priorizada"
    else:
        nivel = "Verde"
        accion = "Revision estandar"

    return {
        "score_final":     score,
        "nivel_riesgo":    nivel,
        "accion_sugerida": accion,
        "reglas_activadas": reglas,
        "input": {
            "monto_reclamado":             monto_reclamado,
            "suma_asegurada":              suma_asegurada,
            "dias_desde_inicio_poliza":    dias_desde_inicio_poliza,
            "dias_entre_ocurrencia_reporte": dias_entre_ocurrencia_reporte,
            "documentos_completos":        documentos_completos,
            "ramo":                        ramo,
        },
        "mensaje": (
            f"Nivel {nivel} con score {score}/100. "
            f"{len(reglas)} regla(s) activada(s). Decision automatica desactivada; "
            "se requiere revision humana."
        ),
    }
