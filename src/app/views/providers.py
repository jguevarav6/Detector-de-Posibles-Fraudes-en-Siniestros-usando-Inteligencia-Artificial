"""Pagina de analisis de proveedores."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.app.components import ethics_notice, format_currency, page_header, section_title
from src.app.styles import RISK_COLORS


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Concentracion por proveedor",
        "Talleres, clinicas y peritos con mayor volumen de alertas. Util para detectar redes recurrentes.",
    )
    ethics_notice()

    summary = (
        claims.groupby("proveedor")
        .agg(
            casos=("id_siniestro", "count"),
            score_promedio=("score_final", "mean"),
            monto_promedio=("monto_reclamado", "mean"),
            monto_total=("monto_reclamado", "sum"),
            casos_rojos=("nivel_riesgo", lambda s: int((s == "Rojo").sum())),
            porcentaje_observado=("proveedor_porcentaje_casos_observados", "max"),
            lista_restrictiva=("proveedor_lista_restrictiva", "max"),
        )
        .reset_index()
        .sort_values(["casos_rojos", "score_promedio"], ascending=False)
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Proveedores", len(summary))
    c2.metric("Con alertas rojas", int((summary["casos_rojos"] > 0).sum()))
    c3.metric("Mayor concentracion", int(summary["casos_rojos"].max()))
    c4.metric("Monto total", format_currency(float(summary["monto_total"].sum())))

    c1, c2 = st.columns([1, 1])
    with c1:
        top = summary.head(12)
        fig = px.bar(top, x="proveedor", y="casos_rojos", color="score_promedio", title="Casos rojos por proveedor")
        _clean_chart(fig)
        fig.update_layout(xaxis_tickangle=-30)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        risk_by_provider = claims.groupby(["proveedor", "nivel_riesgo"], as_index=False).size()
        risk_by_provider = risk_by_provider[risk_by_provider["proveedor"].isin(summary.head(12)["proveedor"])]
        fig = px.bar(
            risk_by_provider,
            x="proveedor",
            y="size",
            color="nivel_riesgo",
            color_discrete_map=RISK_COLORS,
            title="Distribucion de prioridad",
        )
        _clean_chart(fig)
        fig.update_layout(xaxis_tickangle=-30)
        st.plotly_chart(fig, use_container_width=True)

    section_title("Ranking operativo", "Incluye porcentaje observado y lista restrictiva simulada.")
    display = summary.copy()
    display["porcentaje_observado"] = (display["porcentaje_observado"] * 100).round(1)
    display["lista_restrictiva"] = display["lista_restrictiva"].map({True: "Si", False: "No", 1: "Si", 0: "No"})
    st.dataframe(
        display,
        use_container_width=True,
        hide_index=True,
        column_config={
            "score_promedio": st.column_config.ProgressColumn("Score promedio", min_value=0, max_value=100),
            "monto_promedio": st.column_config.NumberColumn("Monto promedio", format="$ %.0f"),
            "monto_total": st.column_config.NumberColumn("Monto total", format="$ %.0f"),
            "porcentaje_observado": st.column_config.NumberColumn("% observado", format="%.1f%%"),
        },
    )


def _clean_chart(fig) -> None:
    fig.update_layout(
        height=360,
        margin=dict(l=10, r=10, t=48, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
