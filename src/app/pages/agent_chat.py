"""Pagina del agente consultivo local."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.agent.agent_router import answer_question
from src.app.components import ethics_notice, page_header


QUICK_QUESTIONS = [
    "Top 10 siniestros de mayor riesgo",
    "Proveedores con mas alertas",
    "Documentos faltantes en casos criticos",
    "Ciudades con mayor concentracion",
    "Generar resumen ejecutivo",
]


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Agente consultivo",
        "Consulta patrones operativos mediante respuestas controladas sobre datos procesados.",
    )
    ethics_notice()

    cols = st.columns(len(QUICK_QUESTIONS))
    for col, question in zip(cols, QUICK_QUESTIONS):
        if col.button(question, use_container_width=True):
            st.session_state["agent_prompt"] = question

    prompt = st.chat_input("Preguntale al agente antifraude...")
    if prompt:
        st.session_state["agent_prompt"] = prompt

    active_prompt = st.session_state.get("agent_prompt", QUICK_QUESTIONS[0])
    with st.chat_message("user"):
        st.write(active_prompt)
    with st.chat_message("assistant"):
        st.write(answer_question(active_prompt, claims))
