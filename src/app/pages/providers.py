"""Página de análisis de proveedores."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.app.components import ethics_notice, page_header
from src.app.styles import RISK_COLORS


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Proveedores",
        "Concentración de alertas por proveedor para apoyar revisión operativa.",
    )
    ethics_notice()

    summary = (
        claims.groupby("proveedor")
        .agg(
            casos=("id_siniestro", "count"),
            score_promedio=("score_final", "mean"),
            monto_promedio=("monto_reclamado", "mean"),
            casos_rojos=("nivel_riesgo", lambda s: int((s == "Rojo").sum())),
        )
        .reset_index()
        .sort_values(["casos_rojos", "score_promedio"], ascending=False)
    )

    c1, c2 = st.columns([1, 1])
    with c1:
        fig = px.bar(summary, x="proveedor", y="casos_rojos", title="Casos rojos por proveedor")
        fig.update_layout(height=360, margin=dict(l=10, r=10, t=45, b=10), xaxis_tickangle=-25)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        risk_by_provider = claims.groupby(["proveedor", "nivel_riesgo"], as_index=False).size()
        fig = px.bar(
            risk_by_provider,
            x="proveedor",
            y="size",
            color="nivel_riesgo",
            color_discrete_map=RISK_COLORS,
            title="Distribución de riesgo",
        )
        fig.update_layout(height=360, margin=dict(l=10, r=10, t=45, b=10), xaxis_tickangle=-25)
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(summary, use_container_width=True, hide_index=True)
