"""Entrada del dashboard Streamlit de FraudLens Claims AI."""

from __future__ import annotations

import streamlit as st

from src.app.demo_data import load_claims
from src.app.views import (
    agent_chat,
    claim_detail,
    claims_inbox,
    dashboard,
    providers,
    reports,
    simulator,
    watchlist,
)
from src.app.styles import inject_global_styles


PAGES = {
    "Dashboard": dashboard.render,
    "Bandeja": claims_inbox.render,
    "Detalle": claim_detail.render,
    "Watchlist (DB2)": watchlist.render,
    "Simulador": simulator.render,
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
        st.markdown(_brand_html(), unsafe_allow_html=True)
        selected_page = st.radio("Navegacion", list(PAGES.keys()), label_visibility="collapsed")
        st.markdown('<hr style="border-color:rgba(255,255,255,.10); margin:14px 0;">', unsafe_allow_html=True)
        total = len(claims)
        red = int((claims["nivel_riesgo"] == "Rojo").sum())
        yellow = int((claims["nivel_riesgo"] == "Amarillo").sum())
        st.markdown(_sidebar_stats_html(total, red, yellow), unsafe_allow_html=True)

    PAGES[selected_page](claims)


_SHIELD_DATA_URI = (
    "data:image/svg+xml;utf8,"
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' "
    "stroke='%23ffffff' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'>"
    "<path d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/>"
    "<path d='m9 12 2 2 4-4'/></svg>"
)


def _brand_html() -> str:
    return f"""
    <div style="padding:4px 0 18px; border-bottom:1px solid rgba(255,255,255,.10);
                margin-bottom:14px;">
      <div style="display:flex; align-items:center; gap:12px;">
        <div style="width:44px; height:44px; border-radius:11px;
                    background-image:url('{_SHIELD_DATA_URI}'),
                                     linear-gradient(135deg, #2563eb 0%, #06b6d4 100%);
                    background-repeat:no-repeat;
                    background-position:center;
                    background-size:24px 24px, cover;
                    box-shadow:0 6px 20px rgba(37,99,235,.45),
                               inset 0 0 0 1px rgba(255,255,255,.18);
                    flex-shrink:0;"></div>
        <div>
          <div style="font-size:1.18rem; font-weight:800; line-height:1.1;
                      color:#ffffff; letter-spacing:-.02em;">FraudLens</div>
          <div style="color:#94a0b3; font-size:.72rem; margin-top:3px;
                      font-weight:700; text-transform:uppercase;
                      letter-spacing:.10em;">Claims AI</div>
        </div>
      </div>
    </div>
    """


def _sidebar_stats_html(total: int, red: int, yellow: int) -> str:
    def stat(label: str, value: str, dot_color: str, dot_shadow: str) -> str:
        return f"""
        <div style="display:flex; align-items:center; justify-content:space-between;
                    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08);
                    border-radius:12px; padding:10px 14px; margin-top:10px;">
          <div style="display:flex; flex-direction:column;">
            <span style="color:#94a0b3; font-size:.68rem; font-weight:700;
                         text-transform:uppercase; letter-spacing:.08em;">{label}</span>
            <span style="color:#ffffff; font-weight:800; font-size:1.05rem;
                         margin-top:2px; font-feature-settings:'tnum';">{value}</span>
          </div>
          <span style="width:8px; height:8px; border-radius:50%; background:{dot_color};
                       box-shadow:0 0 0 4px {dot_shadow};"></span>
        </div>
        """

    blocks = (
        stat("Procesados",      f"{total:,}", "#60a5fa", "rgba(96,165,250,.20)")
        + stat("Casos rojos",   str(red),     "#ef4444", "rgba(239,68,68,.20)")
        + stat("Casos amarillos", str(yellow), "#f59e0b", "rgba(245,158,11,.20)")
        + """
        <div style="margin-top:16px;
                    background:linear-gradient(135deg, rgba(37,99,235,.18), rgba(6,182,212,.10));
                    border:1px solid rgba(96,165,250,.30); border-radius:12px;
                    padding:12px 14px; color:#d6e3fb; font-size:.78rem; line-height:1.55;">
          <strong style="color:#ffffff; display:block; margin-bottom:4px;
                         font-size:.82rem;">Revision humana obligatoria</strong>
          El score prioriza casos para el analista. No decide pagos ni acusa fraude.
        </div>
        """
    )
    return blocks


if __name__ == "__main__":
    main()
