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
        st.title("FraudLens")
        st.caption("Claims AI")
        selected_page = st.radio("Navegación", list(PAGES.keys()), label_visibility="collapsed")
        st.divider()
        st.caption("Demo local")
        st.caption("Datos sintéticos o procesados")
        st.caption("Revisión humana obligatoria")

    PAGES[selected_page](claims)


if __name__ == "__main__":
    main()
