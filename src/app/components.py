"""Componentes visuales reutilizables para Streamlit."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.styles import RISK_COLORS


def page_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="fl-hero">
          <h1>{title}</h1>
          <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def ethics_notice() -> None:
    st.markdown(
        """
        <div class="fl-alert">
        FraudLens genera alertas explicables para revisión humana. No acusa fraude,
        no rechaza siniestros y no reemplaza el criterio del analista.
        </div>
        """,
        unsafe_allow_html=True,
    )


def kpi_card(label: str, value: str, hint: str = "") -> None:
    st.markdown(
        f"""
        <div class="fl-kpi">
          <div class="label">{label}</div>
          <div class="value">{value}</div>
          <div class="hint">{hint}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def risk_pill(level: str) -> str:
    color = RISK_COLORS.get(level, "#64748b")
    return f'<span class="fl-pill" style="background:{color}">{level}</span>'


def format_currency(value: float) -> str:
    return f"${value:,.0f}".replace(",", ".")


def level_order(df: pd.DataFrame) -> pd.DataFrame:
    order = {"Rojo": 0, "Amarillo": 1, "Verde": 2}
    return df.assign(_risk_order=df["nivel_riesgo"].map(order).fillna(9)).sort_values(
        ["_risk_order", "score_final"], ascending=[True, False]
    )


def empty_state(title: str, body: str) -> None:
    st.info(f"{title}\n\n{body}")
