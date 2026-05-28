"""Estilos y tokens visuales del dashboard Streamlit."""

from __future__ import annotations


RISK_COLORS = {
    "Verde": "#15803d",
    "Amarillo": "#ca8a04",
    "Rojo": "#dc2626",
}


def inject_global_styles() -> None:
    import streamlit as st

    st.markdown(
        """
        <style>
        :root {
          --fl-bg: #f7f8fb;
          --fl-surface: #ffffff;
          --fl-ink: #111827;
          --fl-muted: #64748b;
          --fl-border: #e5e7eb;
          --fl-blue: #1d4ed8;
          --fl-green: #15803d;
          --fl-yellow: #ca8a04;
          --fl-red: #dc2626;
        }
        .main .block-container {
          max-width: 1280px;
          padding-top: 1.2rem;
          padding-bottom: 2rem;
        }
        h1, h2, h3 {
          letter-spacing: 0;
        }
        .fl-hero {
          border: 1px solid var(--fl-border);
          border-radius: 8px;
          padding: 18px 20px;
          background: var(--fl-surface);
          box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
          margin-bottom: 18px;
        }
        .fl-hero h1 {
          margin: 0;
          font-size: 1.85rem;
          line-height: 1.2;
        }
        .fl-hero p {
          color: var(--fl-muted);
          margin: 8px 0 0;
          max-width: 920px;
        }
        .fl-alert {
          border-left: 4px solid var(--fl-blue);
          background: #eff6ff;
          color: #1e3a8a;
          padding: 12px 14px;
          border-radius: 6px;
          margin: 12px 0 18px;
          font-size: 0.95rem;
        }
        .fl-kpi {
          border: 1px solid var(--fl-border);
          border-radius: 8px;
          padding: 14px 16px;
          background: var(--fl-surface);
          min-height: 112px;
        }
        .fl-kpi .label {
          color: var(--fl-muted);
          font-size: 0.82rem;
          margin-bottom: 6px;
        }
        .fl-kpi .value {
          color: var(--fl-ink);
          font-size: 1.55rem;
          font-weight: 700;
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
          padding: 4px 9px;
          font-size: 0.8rem;
          font-weight: 700;
          color: white;
        }
        .fl-section {
          margin-top: 10px;
          margin-bottom: 8px;
        }
        .stDataFrame, .stDataEditor {
          border-radius: 8px;
        }
        @media (max-width: 768px) {
          .main .block-container {
            padding-left: 0.8rem;
            padding-right: 0.8rem;
          }
          .fl-hero {
            padding: 14px;
          }
          .fl-hero h1 {
            font-size: 1.35rem;
          }
          .fl-kpi {
            min-height: auto;
          }
          .fl-kpi .value {
            font-size: 1.25rem;
          }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
