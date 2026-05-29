"""Explicaciones humanas para scores de revision."""

from __future__ import annotations

import pandas as pd


ETHICS_SUFFIX = "No es una acusacion de fraude; es una alerta para revision humana especializada."


def explain_claim(row: pd.Series) -> str:
    """Construye una explicacion trazable y no acusatoria."""
    parts = [
        f"El caso queda en nivel {row['nivel_riesgo']} con score {row['score_final']:.0f}.",
        str(row.get("explicacion_reglas", "")),
    ]
    if float(row.get("score_ml", 0)) >= 60:
        parts.append("El modelo supervisado tambien asigna una probabilidad sintetica elevada de prioridad.")
    if float(row.get("score_anomalia", 0)) >= 70:
        parts.append("El detector de anomalias lo ubica fuera del patron habitual del dataset.")
    if float(row.get("score_nlp", 0)) >= 60:
        parts.append(str(row.get("nlp_explanation", "")))
    parts.append(ETHICS_SUFFIX)
    return " ".join(part for part in parts if part)


def suggested_action(level: str) -> str:
    """Accion operacional sugerida por prioridad."""
    if level == "Rojo":
        return "Priorizar revision documental y analisis antifraude humano"
    if level == "Amarillo":
        return "Revisar senales y validar respaldos antes de cierre"
    return "Revision estandar con controles habituales"
