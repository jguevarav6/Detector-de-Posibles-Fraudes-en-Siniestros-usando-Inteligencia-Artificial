"""Pagina de reportes y descargas."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.agent.agent_router import answer_question
from src.app.components import ethics_notice, format_currency, page_header, section_title


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Exportar y resumen",
        "Descarga CSV de casos criticos y revisables; revisa el resumen ejecutivo y el checklist de demo.",
    )
    ethics_notice()

    critical = claims[claims["nivel_riesgo"] == "Rojo"].sort_values("score_final", ascending=False)
    review = claims[claims["nivel_riesgo"].isin(["Rojo", "Amarillo"])].sort_values("score_final", ascending=False)

    c1, c2, c3 = st.columns(3)
    c1.metric("Casos rojos", len(critical))
    c2.metric("Casos a revisar", len(review))
    c3.metric("Monto rojo", format_currency(float(critical["monto_reclamado"].sum())))

    section_title("Descargas")
    a, b, c = st.columns(3)
    a.download_button(
        "Descargar casos rojos",
        critical.to_csv(index=False).encode("utf-8"),
        file_name="fraudlens_casos_rojos.csv",
        mime="text/csv",
        use_container_width=True,
    )
    b.download_button(
        "Descargar bandeja revisable",
        review.to_csv(index=False).encode("utf-8"),
        file_name="fraudlens_bandeja_revisable.csv",
        mime="text/csv",
        use_container_width=True,
    )
    c.download_button(
        "Descargar todos los scores",
        claims.to_csv(index=False).encode("utf-8"),
        file_name="fraudlens_scores.csv",
        mime="text/csv",
        use_container_width=True,
    )

    section_title("Resumen ejecutivo")
    st.info(answer_question("Generar resumen ejecutivo", claims))
    st.warning(
        "Las metricas del modelo se calculan sobre datos sinteticos. Sirven para demostrar el metodo, no para prometer desempeno productivo."
    )

    section_title("Checklist de demo")
    st.write(
        """
        - Datos sinteticos cargados en MySQL.
        - Score hibrido calculado con reglas, ML, anomalias y NLP.
        - Agente responde con tools controladas sobre datos procesados.
        - La salida es prioridad de revision humana, no conclusion legal.
        """
    )
