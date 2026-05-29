"""Estilos y tokens visuales del dashboard Streamlit."""

from __future__ import annotations


RISK_COLORS = {
    "Verde": "#168a45",
    "Amarillo": "#c17a00",
    "Rojo": "#cf2e2e",
}


def inject_global_styles() -> None:
    import streamlit as st

    st.markdown(
        """
        <style>
        :root {
          --fl-surface: #ffffff;
          --fl-surface-2: #f8fafc;
          --fl-ink: #172033;
          --fl-muted: #667085;
          --fl-border: #d9dee8;
          --fl-blue: #1f5fbf;
          --fl-blue-soft: #eaf2ff;
          --fl-shadow: 0 10px 26px rgba(23, 32, 51, 0.07);
        }
        .main .block-container {
          max-width: 1360px;
          padding-top: 1.1rem;
          padding-bottom: 2.2rem;
        }
        h1, h2, h3, p { letter-spacing: 0; }
        [data-testid="stSidebar"] { background: #111827; }
        [data-testid="stSidebar"] * { color: #f9fafb; }
        [data-testid="stSidebar"] [role="radiogroup"] label {
          border-radius: 8px;
          padding: 6px 8px;
        }
        .fl-brand {
          border-bottom: 1px solid rgba(255,255,255,0.14);
          padding-bottom: 14px;
          margin-bottom: 14px;
        }
        .fl-brand-title {
          font-size: 1.28rem;
          font-weight: 800;
          line-height: 1.15;
        }
        .fl-brand-subtitle {
          color: #cbd5e1;
          font-size: 0.82rem;
          margin-top: 4px;
        }
        .fl-sidebar-card {
          border: 1px solid rgba(255,255,255,0.14);
          background: rgba(255,255,255,0.06);
          border-radius: 8px;
          padding: 11px 12px;
          margin-top: 12px;
          font-size: 0.82rem;
        }
        .fl-hero {
          border: 1px solid var(--fl-border);
          border-radius: 8px;
          padding: 20px 22px;
          background: var(--fl-surface);
          box-shadow: var(--fl-shadow);
          margin-bottom: 16px;
        }
        .fl-hero h1 {
          margin: 0;
          font-size: 1.9rem;
          line-height: 1.16;
          color: var(--fl-ink);
        }
        .fl-hero p {
          color: var(--fl-muted);
          margin: 8px 0 0;
          max-width: 980px;
        }
        .fl-alert {
          border: 1px solid #b7d4ff;
          border-left: 5px solid var(--fl-blue);
          background: var(--fl-blue-soft);
          color: #173f82;
          padding: 12px 14px;
          border-radius: 8px;
          margin: 12px 0 18px;
          font-size: 0.94rem;
        }
        .fl-kpi {
          border: 1px solid var(--fl-border);
          border-radius: 8px;
          padding: 14px 15px;
          background: var(--fl-surface);
          min-height: 112px;
          box-shadow: 0 5px 16px rgba(23, 32, 51, 0.04);
        }
        .fl-kpi .label {
          color: var(--fl-muted);
          font-size: 0.78rem;
          text-transform: uppercase;
          font-weight: 700;
          margin-bottom: 8px;
        }
        .fl-kpi .value {
          color: var(--fl-ink);
          font-size: 1.52rem;
          font-weight: 800;
          line-height: 1.1;
        }
        .fl-kpi .hint {
          color: var(--fl-muted);
          font-size: 0.8rem;
          margin-top: 8px;
        }
        .fl-pill {
          display: inline-block;
          border-radius: 999px;
          padding: 4px 10px;
          font-size: 0.78rem;
          font-weight: 800;
          color: white;
          white-space: nowrap;
        }
        .fl-section-title {
          font-size: 1rem;
          font-weight: 800;
          color: var(--fl-ink);
          margin: 8px 0 10px;
        }
        .fl-muted {
          color: var(--fl-muted);
          font-size: 0.88rem;
        }
        .fl-score-grid {
          display: grid;
          grid-template-columns: repeat(4, minmax(0, 1fr));
          gap: 10px;
        }
        .fl-score-item {
          border: 1px solid var(--fl-border);
          border-radius: 8px;
          padding: 10px 12px;
          background: var(--fl-surface-2);
        }
        .fl-score-item .label {
          color: var(--fl-muted);
          font-size: 0.76rem;
          font-weight: 700;
        }
        .fl-score-item .value {
          margin-top: 5px;
          font-weight: 800;
          font-size: 1.1rem;
          color: var(--fl-ink);
        }
        div[data-testid="stMetric"] {
          border: 1px solid var(--fl-border);
          border-radius: 8px;
          padding: 12px 14px;
          background: var(--fl-surface);
        }
        .stDataFrame, .stDataEditor { border-radius: 8px; }
        @media (max-width: 768px) {
          .main .block-container { padding-left: 0.8rem; padding-right: 0.8rem; }
          .fl-hero { padding: 15px; }
          .fl-hero h1 { font-size: 1.35rem; }
          .fl-kpi { min-height: auto; }
          .fl-kpi .value { font-size: 1.2rem; }
          .fl-score-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
