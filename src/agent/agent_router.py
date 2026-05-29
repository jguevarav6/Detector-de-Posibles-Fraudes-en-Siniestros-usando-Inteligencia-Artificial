"""Router local de intenciones para el agente consultivo."""

from __future__ import annotations

import re

import pandas as pd

from src.agent import agent_tools as tools


def answer_question(question: str, claims: pd.DataFrame | None = None) -> str:
    """Responde preguntas operativas con tools controladas."""
    df = claims if claims is not None else tools.load_scored_claims()
    if df.empty:
        return "No hay datos procesados. Ejecuta primero python setup_demo.py."

    normalized = question.lower()
    claim_id = _extract_claim_id(question)
    if "por que" in normalized or "por qué" in normalized or claim_id:
        return tools.explain_claim(df, claim_id)
    if "proveedor" in normalized:
        return tools.provider_alert_summary(df)
    if "ciudad" in normalized:
        return tools.city_risk_summary(df)
    if "ramo" in normalized:
        return tools.branch_risk_summary(df)
    if "document" in normalized:
        return tools.missing_documents_summary(df)
    if "monto" in normalized:
        return tools.atypical_amounts(df)
    if "inicio" in normalized or "poliza" in normalized or "póliza" in normalized:
        return tools.near_policy_start(df)
    if "narrativa" in normalized or "similar" in normalized or "patron" in normalized or "patrón" in normalized:
        return tools.similar_narratives(df)
    if "resumen" in normalized or "ejecutivo" in normalized:
        return tools.executive_summary(df)
    if "recomienda" in normalized or "revisar primero" in normalized:
        return tools.top_risk_claims(df, limit=5)
    return tools.top_risk_claims(df)


def _extract_claim_id(text: str) -> str | None:
    match = re.search(r"SIN-\d{5}", text.upper())
    return match.group(0) if match else None
