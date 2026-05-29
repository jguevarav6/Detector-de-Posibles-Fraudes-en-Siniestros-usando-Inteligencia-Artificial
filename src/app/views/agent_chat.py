"""Pagina del agente consultivo local."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.agent.agent_router import answer_question
from src.app.components import ethics_notice, page_header, section_title


QUICK_QUESTIONS = [
    ("Top siniestros de mayor riesgo", "Top 10 siniestros de mayor riesgo"),
    ("Proveedores con mas alertas", "Proveedores con mas alertas"),
    ("Documentos faltantes criticos", "Documentos faltantes en casos criticos"),
    ("Ciudades con mayor concentracion", "Ciudades con mayor concentracion"),
    ("Ramos con mayor riesgo", "Ramos con mayor riesgo"),
    ("Asegurados frecuentes", "Asegurados frecuentes"),
    ("Montos atipicos", "Montos atipicos"),
    ("Patrones narrativos repetidos", "Patrones narrativos repetidos"),
    ("Resumen ejecutivo", "Generar resumen ejecutivo"),
]


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Agente consultivo",
        "Consulta patrones operativos del dataset procesado. El agente usa tools locales controladas y no toma decisiones de pago.",
    )
    ethics_notice()

    if "agent_history" not in st.session_state:
        st.session_state["agent_history"] = [
            {
                "role": "assistant",
                "content": (
                    "Hola. Soy el agente consultivo de FraudLens. "
                    "Puedo responder con datos procesados sobre prioridades de revision, "
                    "patrones de proveedores, ciudades, montos atipicos y narrativas similares. "
                    "Selecciona una pregunta rapida o escribe la tuya."
                ),
            }
        ]

    left, right = st.columns([2.3, 1])

    with left:
        section_title("Conversacion", "Historial persistente durante la sesion.")
        chat_container = st.container(height=460, border=True)
        with chat_container:
            for msg in st.session_state["agent_history"]:
                avatar = "🤖" if msg["role"] == "assistant" else "👤"
                with st.chat_message(msg["role"], avatar=avatar):
                    st.markdown(msg["content"])

        prompt = st.chat_input("Preguntale al agente antifraude...")
        if prompt:
            _append_and_answer(prompt, claims)
            st.rerun()

    with right:
        section_title("Preguntas rapidas")
        for label, question in QUICK_QUESTIONS:
            if st.button(label, width="stretch", key=f"qq_{label}"):
                _append_and_answer(question, claims)
                st.rerun()
        st.html(
            """
            <div style="margin-top:12px; background:#e8f0fe; border:1px solid #c7d8f9;
                        border-left:4px solid #1e5bd6; border-radius:10px; padding:12px 14px;
                        color:#1a3a7d; font-size:.82rem; line-height:1.5;">
              <strong>Como funciona</strong><br>
              El router clasifica la pregunta y llama una tool local sobre
              <code>scored_claims.csv</code>. No genera lenguaje acusatorio
              ni recalcula scores.
            </div>
            """
        )
        if st.button("Limpiar conversacion", width="stretch"):
            st.session_state["agent_history"] = []
            st.rerun()


def _append_and_answer(question: str, claims: pd.DataFrame) -> None:
    history = st.session_state.setdefault("agent_history", [])
    history.append({"role": "user", "content": question})
    response = answer_question(question, claims)
    history.append({"role": "assistant", "content": response})
