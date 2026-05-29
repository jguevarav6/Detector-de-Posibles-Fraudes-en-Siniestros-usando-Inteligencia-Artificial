"""Entrada del dashboard Streamlit de FraudLens Claims AI."""

from __future__ import annotations

import streamlit as st

from src.app.demo_data import load_claims
from src.app.views import agent_chat, claim_detail, claims_inbox, dashboard, providers, reports
from src.app.styles import icon_shield, inject_global_styles


PAGES = {
    "Dashboard": dashboard.render,
    "Bandeja": claims_inbox.render,
    "Detalle": claim_detail.render,
    "Proveedores": providers.render,
    "Agente": agent_chat.render,
    "Reportes": reports.render,
}


def main() -> None:
    st.set_page_config(
        page_title="FraudLens Claims AI",
        page_icon="FL",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    inject_global_styles()

    claims = load_claims()

    with st.sidebar:
        st.html(
            f"""
            <div class="fl-brand">
              <div class="fl-brand-row">
                <div class="fl-brand-mark">{icon_shield()}</div>
                <div>
                  <div class="fl-brand-title">FraudLens</div>
                  <div class="fl-brand-subtitle">Claims AI</div>
                </div>
              </div>
            </div>
            """
        )
        selected_page = st.radio("Navegacion", list(PAGES.keys()), label_visibility="collapsed")
        st.divider()
        total = len(claims)
        red = int((claims["nivel_riesgo"] == "Rojo").sum())
        yellow = int((claims["nivel_riesgo"] == "Amarillo").sum())
        st.html(
            f"""
            <div class="fl-sidebar-stat blue">
              <div class="left">
                <span class="label">Procesados</span>
                <span class="value">{total:,}</span>
              </div>
              <span class="dot"></span>
            </div>
            <div class="fl-sidebar-stat red">
              <div class="left">
                <span class="label">Casos rojos</span>
                <span class="value">{red}</span>
              </div>
              <span class="dot"></span>
            </div>
            <div class="fl-sidebar-stat amber">
              <div class="left">
                <span class="label">Casos amarillos</span>
                <span class="value">{yellow}</span>
              </div>
              <span class="dot"></span>
            </div>
            <div class="fl-ethics-card">
              <strong>Revision humana obligatoria</strong>
              El score prioriza casos para analista. No decide pagos ni acusa fraude.
            </div>
            """
        )

    PAGES[selected_page](claims)


if __name__ == "__main__":
    main()
