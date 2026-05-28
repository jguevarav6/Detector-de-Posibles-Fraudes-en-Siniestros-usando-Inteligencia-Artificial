"""Página de detalle explicable de un siniestro."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.components import ethics_notice, format_currency, page_header, risk_pill


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Detalle del siniestro",
        "Explicación trazable del score, reglas activadas, documentos y señales textuales.",
    )
    ethics_notice()

    selected = st.selectbox("Seleccionar siniestro", claims["id_siniestro"].tolist())
    claim = claims.loc[claims["id_siniestro"] == selected].iloc[0]

    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        st.metric("Score final", int(claim["score_final"]))
    with c2:
        st.markdown("Nivel")
        st.markdown(risk_pill(str(claim["nivel_riesgo"])), unsafe_allow_html=True)
    with c3:
        st.markdown("Acción sugerida")
        st.info(str(claim["accion_sugerida"]))

    st.divider()
    left, right = st.columns([1.15, 0.85])
    with left:
        st.markdown("### Explicación")
        st.write(claim["explicacion"])
        st.markdown("### Reglas activadas")
        st.warning(claim["reglas_activadas"])
        st.markdown("### Narrativa similar")
        if claim["similar_claim_id"]:
            st.write(f"Caso relacionado: `{claim['similar_claim_id']}` · similitud {claim['max_similarity']:.0%}")
        else:
            st.write("No se observan narrativas similares relevantes en los datos demo.")

    with right:
        st.markdown("### Resumen del caso")
        st.write(f"**Ciudad:** {claim['ciudad']}")
        st.write(f"**Ramo:** {claim['ramo']}")
        st.write(f"**Cobertura:** {claim['cobertura']}")
        st.write(f"**Proveedor:** {claim['proveedor']}")
        st.write(f"**Monto reclamado:** {format_currency(float(claim['monto_reclamado']))}")
        st.write(f"**Asegurado:** {claim['asegurado']}")
        st.write(f"**Vehículo:** {claim['vehiculo'] or 'No aplica'}")
        st.write(f"**Días desde inicio de póliza:** {claim['dias_desde_inicio_poliza']}")
        st.write(f"**Documentos:** {claim['documentos']}")
