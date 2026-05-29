"""Entrada del dashboard Streamlit de FraudLens Claims AI."""

from __future__ import annotations

import streamlit as st

from src.app.demo_data import load_claims
from src.app.pages import agent_chat, claim_detail, claims_inbox, dashboard, providers, reports
from src.app.styles import inject_global_styles


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
        st.markdown(
            """
            <div class="fl-brand">
              <div class="fl-brand-title">FraudLens</div>
              <div class="fl-brand-subtitle">Claims AI · MySQL demo</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        selected_page = st.radio("Navegacion", list(PAGES.keys()), label_visibility="collapsed")
        st.divider()
        red = int((claims["nivel_riesgo"] == "Rojo").sum())
        yellow = int((claims["nivel_riesgo"] == "Amarillo").sum())
        st.markdown(
            f"""
            <div class="fl-sidebar-card">
              <strong>{len(claims):,}</strong> siniestros procesados<br>
              {red} rojos · {yellow} amarillos<br>
              Fuente: MySQL + CSV procesado
            </div>
            <div class="fl-sidebar-card">
              Revision humana obligatoria. El score prioriza casos, no decide pagos.
            </div>
            """,
            unsafe_allow_html=True,
        )

    PAGES[selected_page](claims)


if __name__ == "__main__":
    main()
