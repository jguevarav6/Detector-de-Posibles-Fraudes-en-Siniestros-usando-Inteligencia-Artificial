"""Pagina de dashboard ejecutivo."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.app.components import ethics_notice, format_currency, kpi_card, page_header, section_title
from src.app.styles import RISK_COLORS


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Dashboard ejecutivo",
        "Priorizacion operativa de siniestros con senales explicables para revision humana.",
    )
    ethics_notice()

    total = len(claims)
    red = int((claims["nivel_riesgo"] == "Rojo").sum())
    yellow = int((claims["nivel_riesgo"] == "Amarillo").sum())
    green = int((claims["nivel_riesgo"] == "Verde").sum())
    amount_total = float(claims["monto_reclamado"].sum())
    amount_red = float(claims.loc[claims["nivel_riesgo"] == "Rojo", "monto_reclamado"].sum())
    review_rate = (red + yellow) / total * 100 if total else 0

    cols = st.columns(6)
    metrics = [
        ("Siniestros", f"{total:,}", "Dataset sintetico procesado"),
        ("Rojos", str(red), "Revision urgente"),
        ("Amarillos", str(yellow), "Revision priorizada"),
        ("Verdes", str(green), "Revision estandar"),
        ("Monto reclamado", format_currency(amount_total), "Total de la bandeja"),
        ("Tasa revisable", f"{review_rate:.1f}%", "Rojo + amarillo"),
    ]
    for col, metric in zip(cols, metrics):
        with col:
            kpi_card(*metric)

    section_title("Lectura ejecutiva", "Distribucion de prioridad, exposicion y concentraciones relevantes.")
    top_left, top_right = st.columns([1.05, 0.95])
    level_counts = claims["nivel_riesgo"].value_counts().rename_axis("nivel_riesgo").reset_index(name="casos")
    level_counts["nivel_riesgo"] = pd.Categorical(level_counts["nivel_riesgo"], ["Rojo", "Amarillo", "Verde"], ordered=True)
    level_counts = level_counts.sort_values("nivel_riesgo")

    with top_left:
        fig = px.bar(
            level_counts,
            x="nivel_riesgo",
            y="casos",
            color="nivel_riesgo",
            color_discrete_map=RISK_COLORS,
            text="casos",
            title="Casos por prioridad de revision",
        )
        _clean_chart(fig, height=360)
        st.plotly_chart(fig, use_container_width=True)

    with top_right:
        amount_by_level = claims.groupby("nivel_riesgo", as_index=False)["monto_reclamado"].sum()
        fig = px.pie(
            amount_by_level,
            values="monto_reclamado",
            names="nivel_riesgo",
            color="nivel_riesgo",
            color_discrete_map=RISK_COLORS,
            hole=0.55,
            title=f"Exposicion roja: {format_currency(amount_red)}",
        )
        _clean_chart(fig, height=360)
        st.plotly_chart(fig, use_container_width=True)

    lower_cols = st.columns([1, 1, 1])
    with lower_cols[0]:
        city = claims.groupby("ciudad", as_index=False).agg(score_final=("score_final", "mean"), casos=("id_siniestro", "count"))
        fig = px.bar(city.sort_values("score_final", ascending=False), x="ciudad", y="score_final", text="casos", title="Score promedio por ciudad")
        _clean_chart(fig, height=330)
        st.plotly_chart(fig, use_container_width=True)
    with lower_cols[1]:
        branch = claims.groupby("ramo", as_index=False).agg(score_final=("score_final", "mean"), casos=("id_siniestro", "count"))
        fig = px.bar(branch.sort_values("score_final", ascending=False), x="ramo", y="score_final", text="casos", title="Score promedio por ramo")
        _clean_chart(fig, height=330)
        st.plotly_chart(fig, use_container_width=True)
    with lower_cols[2]:
        provider = (
            claims.groupby("proveedor", as_index=False)
            .agg(score_final=("score_final", "mean"), rojos=("nivel_riesgo", lambda s: int((s == "Rojo").sum())))
            .sort_values(["rojos", "score_final"], ascending=False)
            .head(10)
        )
        fig = px.bar(provider, x="proveedor", y="rojos", color="score_final", title="Top proveedores por alertas rojas")
        _clean_chart(fig, height=330)
        fig.update_layout(xaxis_tickangle=-30)
        st.plotly_chart(fig, use_container_width=True)

    section_title("Cola priorizada", "Primeros casos que un analista deberia revisar.")
    st.dataframe(
        claims.sort_values("score_final", ascending=False).head(12)[
            ["id_siniestro", "nivel_riesgo", "score_final", "ciudad", "ramo", "proveedor", "monto_reclamado", "accion_sugerida"]
        ],
        hide_index=True,
        use_container_width=True,
        column_config={
            "score_final": st.column_config.ProgressColumn("Score", min_value=0, max_value=100),
            "monto_reclamado": st.column_config.NumberColumn("Monto reclamado", format="$ %.0f"),
        },
    )


def _clean_chart(fig, height: int) -> None:
    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=48, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#172033"),
    )
