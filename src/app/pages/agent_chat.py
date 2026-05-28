"""Página del agente consultivo local."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.components import ethics_notice, page_header


QUICK_QUESTIONS = [
    "Top 10 siniestros de mayor riesgo",
    "Proveedores con más alertas",
    "Documentos faltantes en casos críticos",
    "Ciudades con mayor concentración",
    "Generar resumen ejecutivo",
]


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Agente consultivo",
        "Consulta patrones operativos mediante respuestas controladas sobre datos procesados.",
    )
    ethics_notice()

    st.caption("Versión frontend: respuestas demo hasta conectar `src/agent/agent_router.py`.")
    cols = st.columns(len(QUICK_QUESTIONS))
    for col, question in zip(cols, QUICK_QUESTIONS):
        if col.button(question, use_container_width=True):
            st.session_state["agent_prompt"] = question

    prompt = st.chat_input("Pregúntale al agente antifraude...")
    if prompt:
        st.session_state["agent_prompt"] = prompt

    active_prompt = st.session_state.get("agent_prompt", QUICK_QUESTIONS[0])
    with st.chat_message("user"):
        st.write(active_prompt)
    with st.chat_message("assistant"):
        st.write(_demo_response(active_prompt, claims))


def _demo_response(prompt: str, claims: pd.DataFrame) -> str:
    normalized = prompt.lower()
    if "proveedor" in normalized:
        top = claims.groupby("proveedor")["score_final"].mean().sort_values(ascending=False).head(3)
        return "Proveedores con mayor score promedio: " + ", ".join(f"{idx} ({val:.0f})" for idx, val in top.items())
    if "document" in normalized:
        critical = claims[claims["nivel_riesgo"] == "Rojo"]["documentos"].tolist()
        return "Documentos a revisar en casos críticos: " + "; ".join(critical)
    if "ciudad" in normalized:
        top = claims.groupby("ciudad")["score_final"].mean().sort_values(ascending=False).head(3)
        return "Ciudades con mayor score promedio: " + ", ".join(f"{idx} ({val:.0f})" for idx, val in top.items())
    if "resumen" in normalized:
        red = int((claims["nivel_riesgo"] == "Rojo").sum())
        yellow = int((claims["nivel_riesgo"] == "Amarillo").sum())
        return f"Resumen ejecutivo: {red} casos rojos y {yellow} amarillos requieren revisión priorizada. No es una acusación de fraude."
    top = claims.sort_values("score_final", ascending=False).head(10)["id_siniestro"].tolist()
    return "Casos de mayor prioridad de revisión: " + ", ".join(top)
