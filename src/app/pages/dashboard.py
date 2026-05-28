"""Página de dashboard ejecutivo."""

from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from src.app.components import ethics_notice, format_currency, kpi_card, page_header
from src.app.styles import RISK_COLORS


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Dashboard ejecutivo",
        "Vista consolidada de señales de posible riesgo en siniestros para priorización humana.",
    )
    ethics_notice()

    total = len(claims)
    red = int((claims["nivel_riesgo"] == "Rojo").sum())
    yellow = int((claims["nivel_riesgo"] == "Amarillo").sum())
    green = int((claims["nivel_riesgo"] == "Verde").sum())
    amount_total = float(claims["monto_reclamado"].sum())
    amount_red = float(claims.loc[claims["nivel_riesgo"] == "Rojo", "monto_reclamado"].sum())

    cols = st.columns(6)
    metrics = [
        ("Siniestros", str(total), "Casos en bandeja"),
        ("Rojos", str(red), "Revisión urgente"),
        ("Amarillos", str(yellow), "Revisión priorizada"),
        ("Verdes", str(green), "Revisión estándar"),
        ("Monto reclamado", format_currency(amount_total), "Total demo"),
        ("Monto rojo", format_currency(amount_red), "Exposición prioritaria"),
    ]
    for col, metric in zip(cols, metrics):
        with col:
            kpi_card(*metric)

    st.markdown("### Señales por nivel")
    chart_cols = st.columns([1, 1])
    level_counts = claims["nivel_riesgo"].value_counts().reset_index()
    level_counts.columns = ["nivel_riesgo", "casos"]
    with chart_cols[0]:
        fig = px.bar(
            level_counts,
            x="nivel_riesgo",
            y="casos",
            color="nivel_riesgo",
            color_discrete_map=RISK_COLORS,
            text="casos",
        )
        fig.update_layout(showlegend=False, height=360, margin=dict(l=10, r=10, t=25, b=10))
        st.plotly_chart(fig, use_container_width=True)

    with chart_cols[1]:
        fig = px.pie(
            level_counts,
            values="casos",
            names="nivel_riesgo",
            color="nivel_riesgo",
            color_discrete_map=RISK_COLORS,
            hole=0.55,
        )
        fig.update_layout(height=360, margin=dict(l=10, r=10, t=25, b=10))
        st.plotly_chart(fig, use_container_width=True)

    lower_cols = st.columns([1, 1, 1])
    with lower_cols[0]:
        city = claims.groupby("ciudad", as_index=False)["score_final"].mean()
        fig = px.bar(city, x="ciudad", y="score_final", title="Riesgo promedio por ciudad")
        fig.update_layout(height=320, margin=dict(l=10, r=10, t=45, b=10))
        st.plotly_chart(fig, use_container_width=True)
    with lower_cols[1]:
        ramo = claims.groupby("ramo", as_index=False)["score_final"].mean()
        fig = px.bar(ramo, x="ramo", y="score_final", title="Riesgo promedio por ramo")
        fig.update_layout(height=320, margin=dict(l=10, r=10, t=45, b=10))
        st.plotly_chart(fig, use_container_width=True)
    with lower_cols[2]:
        provider = claims.groupby("proveedor", as_index=False)["score_final"].mean()
        fig = px.bar(provider, x="proveedor", y="score_final", title="Riesgo promedio por proveedor")
        fig.update_layout(height=320, margin=dict(l=10, r=10, t=45, b=10), xaxis_tickangle=-25)
        st.plotly_chart(fig, use_container_width=True)
