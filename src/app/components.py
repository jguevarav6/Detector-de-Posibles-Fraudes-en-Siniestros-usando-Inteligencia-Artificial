"""Componentes visuales reutilizables para Streamlit."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.styles import (
    RISK_COLORS,
    icon_alert,
    icon_check,
    icon_info,
    icon_shield,
)


_KPI_ICONS = {
    "red": icon_alert,
    "amber": icon_alert,
    "green": icon_check,
    "blue": icon_shield,
    "": icon_shield,
}


def page_header(title: str, subtitle: str, badge: str = "Demo Hackathon | Aseguradora del Sur", icon_svg: str | None = None) -> None:
    icon = icon_svg if icon_svg is not None else icon_shield()
    badge_html = f'<div class="fl-hero-badge">{badge}</div>' if badge else ""
    st.html(
        f"""
        <div class="fl-hero">
          <div class="fl-hero-row">
            <div class="fl-hero-icon">{icon}</div>
            <div class="fl-hero-content">
              {badge_html}
              <h1>{title}</h1>
              <p>{subtitle}</p>
            </div>
          </div>
        </div>
        """
    )


def ethics_notice() -> None:
    st.html(
        f"""
        <div class="fl-alert">
          <div class="fl-alert-icon">{icon_info()}</div>
          <div>
            <strong>Aviso etico.</strong> FraudLens genera alertas explicables para revision humana.
            No acusa fraude, no rechaza siniestros y no reemplaza el criterio del analista.
          </div>
        </div>
        """
    )


def kpi_card(label: str, value: str, hint: str = "", accent: str = "", icon: str | None = None) -> None:
    """KPI con icono SVG y acento de color: 'red' | 'amber' | 'green' | 'blue' | ''."""
    accent_class = f" accent-{accent}" if accent else ""
    icon_svg = icon if icon is not None else _KPI_ICONS.get(accent, icon_shield)()
    st.html(
        f"""
        <div class="fl-kpi{accent_class}">
          <div class="fl-kpi-head">
            <div class="fl-kpi-label">{label}</div>
            <div class="fl-kpi-icon">{icon_svg}</div>
          </div>
          <div class="fl-kpi-value">{value}</div>
          <div class="fl-kpi-hint">{hint}</div>
        </div>
        """
    )


def section_title(title: str, hint: str = "") -> None:
    detail = f'<div class="fl-muted">{hint}</div>' if hint else ""
    st.html(f'<div class="fl-section-title">{title}</div>{detail}')


def score_breakdown(row: pd.Series) -> None:
    parts = [
        ("Reglas", float(row.get("score_reglas", 0))),
        ("ML", float(row.get("score_ml", 0))),
        ("Anomalia", float(row.get("score_anomalia", 0))),
        ("NLP", float(row.get("score_nlp", 0))),
    ]
    items = "".join(
        f"""
        <div class="fl-score-item">
          <div class="label">{label}</div>
          <div class="value">{value:.0f}</div>
          <div class="bar"><span style="width:{min(max(value, 0), 100):.0f}%"></span></div>
        </div>
        """
        for label, value in parts
    )
    st.html(f'<div class="fl-score-grid">{items}</div>')


def risk_pill(level: str) -> str:
    color = RISK_COLORS.get(level, "#5b6677")
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
