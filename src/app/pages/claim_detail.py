"""Pagina de detalle explicable de un siniestro."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.components import ethics_notice, format_currency, page_header, risk_pill, score_breakdown, section_title


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Detalle del siniestro",
        "Explicacion trazable del score, reglas activadas, documentos y senales textuales.",
    )
    ethics_notice()

    ordered = claims.sort_values("score_final", ascending=False)
    selected = st.selectbox("Seleccionar siniestro", ordered["id_siniestro"].tolist())
    claim = claims.loc[claims["id_siniestro"] == selected].iloc[0]

    c1, c2, c3, c4 = st.columns([1, 1, 1.2, 2])
    c1.metric("Score final", f"{float(claim['score_final']):.0f}")
    with c2:
        st.markdown("Nivel")
        st.markdown(risk_pill(str(claim["nivel_riesgo"])), unsafe_allow_html=True)
    c3.metric("Monto", format_currency(float(claim["monto_reclamado"])))
    with c4:
        st.markdown("Accion sugerida")
        st.info(str(claim["accion_sugerida"]))

    tab_summary, tab_score, tab_evidence = st.tabs(["Resumen", "Score", "Evidencia"])
    with tab_summary:
        left, right = st.columns([1.25, 0.75])
        with left:
            section_title("Explicacion para analista")
            st.write(claim["explicacion"])
            section_title("Reglas activadas")
            for rule in str(claim["reglas_activadas"]).split(";"):
                if rule.strip():
                    st.warning(rule.strip())
        with right:
            section_title("Ficha del caso")
            st.write(f"**Ciudad:** {claim['ciudad']}")
            st.write(f"**Ramo:** {claim['ramo']}")
            st.write(f"**Cobertura:** {claim['cobertura']}")
            st.write(f"**Proveedor:** {claim['proveedor']}")
            st.write(f"**Asegurado:** {claim['asegurado']}")
            st.write(f"**Vehiculo:** {claim['vehiculo'] or 'No aplica'}")
            st.write(f"**Ocurrencia:** {claim['fecha_ocurrencia']}")
            st.write(f"**Reporte:** {claim['fecha_reporte']}")

    with tab_score:
        section_title("Componentes del score", "Formula: 55% reglas, 25% ML, 10% anomalia, 10% NLP.")
        score_breakdown(claim)
        st.divider()
        st.progress(float(claim["score_final"]) / 100, text=f"Score final {float(claim['score_final']):.0f}/100")
        st.write(
            f"El monto reclamado representa {float(claim.get('monto_vs_suma_asegurada', 0)):.0%} "
            f"de la suma asegurada registrada."
        )

    with tab_evidence:
        left, right = st.columns([1, 1])
        with left:
            section_title("Documentos")
            st.write(claim["documentos"])
            st.write(f"**Dias desde inicio de poliza:** {claim['dias_desde_inicio_poliza']}")
            st.write(f"**Dias hasta fin de poliza:** {claim['dias_desde_fin_poliza']}")
            st.write(f"**Dias entre ocurrencia y reporte:** {claim['dias_entre_ocurrencia_reporte']}")
        with right:
            section_title("Narrativa")
            st.write(str(claim.get("descripcion", "")))
            if claim["similar_claim_id"]:
                st.info(f"Caso relacionado: {claim['similar_claim_id']} · similitud {float(claim['max_similarity']):.0%}")
            else:
                st.write("No se observan narrativas similares relevantes.")
