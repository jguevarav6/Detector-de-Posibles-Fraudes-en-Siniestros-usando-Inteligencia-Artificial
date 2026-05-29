"""Pagina del agente consultivo local."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.agent.agent_router import answer_question
from src.app.components import ethics_notice, page_header, section_title


QUICK_QUESTIONS = [
    ("Pareto: 80% de alertas rojas",        "Que proveedores concentran el 80% de las alertas rojas"),
    ("Cruce con watchlist (DB1 + DB2)",     "Cuantos siniestros cruzan con la watchlist de compliance"),
    ("Top siniestros de mayor riesgo",      "Top 10 siniestros de mayor riesgo"),
    ("Proveedores con mas alertas",         "Proveedores con mas alertas"),
    ("Documentos faltantes criticos",       "Documentos faltantes en casos criticos"),
    ("Ciudades con mayor concentracion",    "Ciudades con mayor concentracion"),
    ("Patrones narrativos repetidos",       "Patrones narrativos repetidos"),
    ("Resumen ejecutivo",                   "Generar resumen ejecutivo"),
]


# Tabla simple: por keyword detectado -> tool MCP que se dispara.
# Permite mostrar trazabilidad visible debajo de cada respuesta del agente.
_TRACE_MAP = [
    (("pareto", "80", "ochenta", "concentran"),       ("pareto_red_providers",     "claims_ai")),
    (("watchlist", "compliance", "cruz", "antecedente"), ("get_watchlist_summary", "claims_ai+watchlist")),
    (("proveedor", "taller", "clinica", "perito"),    ("get_provider_alert_summary","claims_ai")),
    (("ciudad", "sucursal"),                          ("get_city_risk_summary",    "claims_ai")),
    (("ramo", "cobertura"),                           ("get_branch_risk_summary",  "claims_ai")),
    (("document",),                                   ("get_missing_documents_critical","claims_ai")),
    (("narrativa", "similar", "patron"),              ("get_similar_narratives",   "claims_ai")),
    (("resumen", "ejecutivo"),                        ("generate_executive_summary","claims_ai")),
    (("por que", "explica", "razon", "motivo"),       ("explain_claim_risk",       "claims_ai")),
    (("top", "mayor riesgo", "criticos", "rojos"),    ("get_top_risk_claims",      "claims_ai")),
]


def _trace_for(question: str) -> tuple[str, str]:
    """Devuelve (tool_name, db_source) para mostrar como trazabilidad MCP."""
    import re

    q = question.lower()
    if re.search(r"SIN-\d+", question.upper()):
        if any(k in q for k in ("watchlist", "compliance", "cruz", "antecedente")):
            return ("cross_reference_claim", "claims_ai+watchlist")
        return ("explain_claim_risk", "claims_ai")
    for keywords, trace in _TRACE_MAP:
        if any(k in q for k in keywords):
            return trace
    return ("get_top_risk_claims", "claims_ai")


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Asistente FraudLens",
        "Pregunta en lenguaje natural o usa los accesos rapidos. Responde con datos del dataset procesado, sin recalcular scores.",
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
    tool, source = _trace_for(question)
    trace = f"\n\n<small style='color:#5b6677;'>MCP tool: <code>{tool}</code> &middot; fuente: <code>{source}</code></small>"
    history.append({"role": "assistant", "content": response + trace})
