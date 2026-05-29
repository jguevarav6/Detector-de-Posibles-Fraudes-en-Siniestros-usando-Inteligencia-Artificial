"""Servicio de scoring hibrido para FraudLens Claims AI."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from src.database.build_database import write_risk_scores
from src.database.settings import MySQLSettings
from src.explainability.explain_score import explain_claim, suggested_action
from src.features.build_features import build_claim_features
from src.models.train_model import add_ml_scores
from src.nlp.narrative_similarity import add_nlp_scores
from src.rules.fraud_rules import add_rule_scores


PROCESSED_DIR = Path("data/processed")
SCORED_CLAIMS_PATH = PROCESSED_DIR / "scored_claims.csv"
RISK_SCORES_PATH = PROCESSED_DIR / "risk_scores.csv"

UI_COLUMNS = [
    "id_siniestro",
    "fecha_ocurrencia",
    "fecha_reporte",
    "ciudad",
    "ramo",
    "cobertura",
    "proveedor",
    "monto_reclamado",
    "score_reglas",
    "score_ml",
    "score_anomalia",
    "score_nlp",
    "score_final",
    "nivel_riesgo",
    "accion_sugerida",
    "reglas_activadas",
    "explicacion",
    "documentos",
    "asegurado",
    "vehiculo",
    "dias_desde_inicio_poliza",
    "dias_desde_fin_poliza",
    "dias_entre_ocurrencia_reporte",
    "historial_siniestros_asegurado",
    "similar_claim_id",
    "max_similarity",
    "descripcion",
    "id_proveedor",
    "id_asegurado",
    "proveedor_porcentaje_casos_observados",
    "proveedor_lista_restrictiva",
    "poliza_suma_asegurada",
    "monto_vs_suma_asegurada",
    "etiqueta_fraude_simulada",
]


def run_scoring_pipeline(
    input_dir: Path = Path("data/synthetic"),
    output_dir: Path = PROCESSED_DIR,
    db_settings: MySQLSettings | None = None,
) -> pd.DataFrame:
    """Ejecuta features, NLP, ML, reglas, score final y persistencia."""
    output_dir.mkdir(parents=True, exist_ok=True)
    scored = build_claim_features(input_dir)
    scored = add_nlp_scores(scored)
    scored = add_ml_scores(scored, output_dir=output_dir)
    scored = add_rule_scores(scored)
    scored = _finalize_scores(scored)

    ui_df = _to_ui_contract(scored)
    ui_df.to_csv(output_dir / SCORED_CLAIMS_PATH.name, index=False)

    risk_scores = ui_df[
        [
            "id_siniestro",
            "score_reglas",
            "score_ml",
            "score_anomalia",
            "score_nlp",
            "score_final",
            "nivel_riesgo",
            "reglas_activadas",
            "explicacion",
            "accion_sugerida",
        ]
    ]
    risk_scores.to_csv(output_dir / RISK_SCORES_PATH.name, index=False)
    write_risk_scores(risk_scores, settings=db_settings)
    return ui_df


def classify_risk(score: float) -> str:
    if score >= 76:
        return "Rojo"
    if score >= 41:
        return "Amarillo"
    return "Verde"


def _finalize_scores(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["score_final"] = (
        0.55 * result["score_reglas"]
        + 0.25 * result["score_ml"]
        + 0.10 * result["score_anomalia"]
        + 0.10 * result["score_nlp"]
    ).clip(0, 100).round(2)
    result["nivel_riesgo"] = result["score_final"].apply(classify_risk)
    result["accion_sugerida"] = result["nivel_riesgo"].apply(suggested_action)
    result["explicacion"] = result.apply(explain_claim, axis=1)
    return result


def _to_ui_contract(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["documentos"] = result.apply(_document_summary, axis=1)
    result["similar_claim_id"] = result["similar_claim_id"].fillna("")
    result["max_similarity"] = result["max_similarity"].fillna(0).astype(float)
    for column in UI_COLUMNS:
        if column not in result:
            result[column] = ""
    return result[UI_COLUMNS].sort_values("score_final", ascending=False).reset_index(drop=True)


def _document_summary(row: pd.Series) -> str:
    issues = []
    if int(row.get("documentos_faltantes", 0)) > 0:
        issues.append(f"{int(row['documentos_faltantes'])} faltantes")
    if int(row.get("documentos_ilegibles", 0)) > 0:
        issues.append(f"{int(row['documentos_ilegibles'])} ilegibles")
    if int(row.get("documentos_inconsistentes", 0)) > 0:
        issues.append(f"{int(row['documentos_inconsistentes'])} inconsistentes")
    return ", ".join(issues) if issues else "Documentos completos"
