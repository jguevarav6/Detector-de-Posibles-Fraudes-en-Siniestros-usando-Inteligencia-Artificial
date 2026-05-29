"""Sistema visual FraudLens Claims AI.

Inspirado en cockpits operativos de antifraude: dark sidebar, hero con escudo,
gradientes corporativos sutiles, tarjetas con acento por riesgo, mobile-first.
"""

from __future__ import annotations


RISK_COLORS = {
    "Verde": "#0f8a55",
    "Amarillo": "#d68a00",
    "Rojo": "#d33232",
}

RISK_COLORS_SOFT = {
    "Verde": "#e6f5ed",
    "Amarillo": "#fbf1da",
    "Rojo": "#fbe6e6",
}


def inject_global_styles() -> None:
    import streamlit as st

    st.html(
        """
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
        <style>
        :root {
          --fl-ink:        #0a1628;
          --fl-ink-2:      #1a2942;
          --fl-muted:      #5b6677;
          --fl-muted-2:    #94a0b3;
          --fl-line:       #e3e8f0;
          --fl-line-soft:  #f0f3f8;
          --fl-bg:         #f4f6fa;
          --fl-bg-2:       #eef2f8;
          --fl-surface:    #ffffff;
          --fl-surface-2:  #fafbfd;

          --fl-blue:       #2563eb;
          --fl-blue-700:   #1d4ed8;
          --fl-blue-900:   #172554;
          --fl-blue-soft:  #eef4ff;
          --fl-cyan:       #06b6d4;
          --fl-violet:     #7c3aed;

          --fl-green:      #0f8a55;
          --fl-green-soft: #e6f5ed;
          --fl-amber:      #d68a00;
          --fl-amber-soft: #fbf1da;
          --fl-red:        #d33232;
          --fl-red-soft:   #fbe6e6;

          --fl-shadow-xs:  0 1px 2px rgba(10,22,40,.05);
          --fl-shadow-sm:  0 4px 10px rgba(10,22,40,.06);
          --fl-shadow-md:  0 10px 28px rgba(10,22,40,.09);
          --fl-shadow-lg:  0 20px 48px rgba(10,22,40,.14);

          --fl-r-sm: 8px;
          --fl-r-md: 12px;
          --fl-r-lg: 18px;
        }

        html, body, .stApp, .main, [class*="css"] {
          font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
          color: var(--fl-ink);
        }
        .stApp { background: var(--fl-bg); }
        .main .block-container {
          max-width: 1400px;
          padding-top: 1.4rem;
          padding-bottom: 3rem;
          animation: fl-fade-in .35s ease;
        }
        @keyframes fl-fade-in { from { opacity:0; transform: translateY(6px); } to { opacity:1; transform:none; } }
        @keyframes fl-pulse { 0%,100% { opacity:.55; } 50% { opacity:1; } }

        h1, h2, h3, h4 { color: var(--fl-ink); font-weight:800; letter-spacing:-.02em; }
        h1 { font-size: 1.95rem; line-height:1.15; }
        h2 { font-size: 1.35rem; }
        h3 { font-size: 1.1rem; }

        /* ============ SIDEBAR ============ */
        [data-testid="stSidebar"] {
          background: radial-gradient(120% 80% at 0% 0%, #1e3a8a 0%, #0a1628 55%, #050a15 100%);
          border-right: 1px solid rgba(255,255,255,.04);
        }
        [data-testid="stSidebar"] * { color:#e6ecf5; }
        [data-testid="stSidebar"] hr { border-color: rgba(255,255,255,.08); }
        [data-testid="stSidebar"] [role="radiogroup"] { gap:3px; }
        [data-testid="stSidebar"] [role="radiogroup"] label {
          border-radius: var(--fl-r-sm);
          padding: 10px 12px;
          font-weight:500;
          font-size:.93rem;
          border:1px solid transparent;
          transition: all .15s ease;
        }
        [data-testid="stSidebar"] [role="radiogroup"] label:hover { background: rgba(255,255,255,.05); }
        [data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] {
          background: linear-gradient(90deg, rgba(37,99,235,.30), rgba(37,99,235,.12));
          border-color: rgba(96,165,250,.45);
          font-weight:700;
          box-shadow: inset 2px 0 0 #60a5fa;
        }

        .fl-brand { padding: 6px 2px 20px; border-bottom:1px solid rgba(255,255,255,.10); margin-bottom:18px; }
        .fl-brand-row { display:flex; align-items:center; gap:12px; }
        .fl-brand-mark {
          width:44px; height:44px; border-radius:11px;
          background: linear-gradient(135deg, #2563eb 0%, #06b6d4 100%);
          display:flex; align-items:center; justify-content:center;
          box-shadow: 0 6px 20px rgba(37,99,235,.45), inset 0 0 0 1px rgba(255,255,255,.18);
          position:relative;
        }
        .fl-brand-mark svg { width:24px; height:24px; color:white; }
        .fl-brand-title { font-size:1.18rem; font-weight:800; line-height:1.1; color:#fff; letter-spacing:-.02em; }
        .fl-brand-subtitle {
          color:#94a0b3; font-size:.72rem; margin-top:3px; font-weight:600;
          text-transform:uppercase; letter-spacing:.1em;
        }

        .fl-sidebar-stat {
          display:flex; align-items:center; justify-content:space-between;
          background: rgba(255,255,255,.04);
          border:1px solid rgba(255,255,255,.08);
          border-radius: var(--fl-r-md);
          padding:10px 14px;
          margin-top:10px;
        }
        .fl-sidebar-stat .left { display:flex; flex-direction:column; }
        .fl-sidebar-stat .label { color:#94a0b3; font-size:.68rem; font-weight:700; text-transform:uppercase; letter-spacing:.08em; }
        .fl-sidebar-stat .value { color:#fff; font-weight:800; font-size:1.05rem; margin-top:1px; }
        .fl-sidebar-stat .dot {
          width:8px; height:8px; border-radius:50%;
          box-shadow: 0 0 0 4px rgba(255,255,255,.04);
          animation: fl-pulse 2s ease-in-out infinite;
        }
        .fl-sidebar-stat.red    .dot { background: #ef4444; box-shadow: 0 0 0 4px rgba(239,68,68,.18); }
        .fl-sidebar-stat.amber  .dot { background: #f59e0b; box-shadow: 0 0 0 4px rgba(245,158,11,.18); }
        .fl-sidebar-stat.blue   .dot { background: #60a5fa; box-shadow: 0 0 0 4px rgba(96,165,250,.18); }

        .fl-ethics-card {
          margin-top:18px;
          background: linear-gradient(135deg, rgba(37,99,235,.18), rgba(6,182,212,.10));
          border:1px solid rgba(96,165,250,.30);
          border-radius: var(--fl-r-md);
          padding:12px 14px;
          color:#d6e3fb;
          font-size:.78rem; line-height:1.55;
        }
        .fl-ethics-card strong { color:#fff; display:block; margin-bottom:4px; font-size:.82rem; }

        /* ============ HERO ============ */
        .fl-hero {
          position:relative;
          background:
            radial-gradient(120% 200% at 100% -10%, rgba(37,99,235,.13), transparent 55%),
            linear-gradient(135deg, #ffffff 0%, #f6f9ff 100%);
          border:1px solid var(--fl-line);
          border-radius: var(--fl-r-lg);
          padding: 28px 32px;
          margin-bottom:18px;
          box-shadow: var(--fl-shadow-sm);
          overflow:hidden;
        }
        .fl-hero::before {
          content:""; position:absolute; left:0; top:0; bottom:0; width:5px;
          background: linear-gradient(180deg, #2563eb, #06b6d4);
        }
        .fl-hero-row { display:flex; gap:18px; align-items:flex-start; }
        .fl-hero-icon {
          flex-shrink:0;
          width:56px; height:56px; border-radius:14px;
          background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
          display:flex; align-items:center; justify-content:center;
          box-shadow: 0 10px 24px rgba(37,99,235,.30);
          color:white;
        }
        .fl-hero-icon svg { width:28px; height:28px; }
        .fl-hero-content { flex:1; min-width:0; }
        .fl-hero-badge {
          display:inline-flex; align-items:center; gap:6px;
          font-size:.68rem; font-weight:800; letter-spacing:.12em; text-transform:uppercase;
          color: var(--fl-blue-700);
          background: var(--fl-blue-soft);
          padding:5px 11px; border-radius:999px; margin-bottom:10px;
          border:1px solid #cfddff;
        }
        .fl-hero-badge::before {
          content:""; width:6px; height:6px; border-radius:50%; background: var(--fl-blue);
          animation: fl-pulse 2.2s ease-in-out infinite;
        }
        .fl-hero h1 { margin:0; font-size:1.85rem; line-height:1.18; color: var(--fl-ink); }
        .fl-hero p {
          color: var(--fl-muted); margin:10px 0 0; max-width:940px;
          font-size:.97rem; line-height:1.55;
        }

        /* ============ ALERT ETICO ============ */
        .fl-alert {
          background: linear-gradient(90deg, #eef4ff 0%, #f3f6fd 100%);
          border:1px solid #d6e0f7;
          border-left:4px solid var(--fl-blue);
          color:#1a3a7d;
          padding:13px 16px;
          border-radius: var(--fl-r-md);
          margin: 12px 0 22px;
          font-size:.9rem; line-height:1.5;
          display:flex; gap:12px; align-items:flex-start;
        }
        .fl-alert .fl-alert-icon {
          flex-shrink:0;
          width:24px; height:24px; border-radius:7px;
          background: var(--fl-blue); color:white;
          display:flex; align-items:center; justify-content:center;
        }
        .fl-alert .fl-alert-icon svg { width:14px; height:14px; }

        /* ============ KPI CARDS ============ */
        .fl-kpi {
          background: var(--fl-surface);
          border:1px solid var(--fl-line);
          border-radius: var(--fl-r-md);
          padding: 16px 18px;
          min-height: 132px;
          box-shadow: var(--fl-shadow-xs);
          transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
          position:relative; overflow:hidden;
        }
        .fl-kpi::after {
          content:""; position:absolute; top:0; right:0; left:0; height:3px;
          background: var(--fl-line);
        }
        .fl-kpi.accent-red::after    { background: linear-gradient(90deg, #ef4444, #fca5a5); }
        .fl-kpi.accent-amber::after  { background: linear-gradient(90deg, #f59e0b, #fcd34d); }
        .fl-kpi.accent-green::after  { background: linear-gradient(90deg, #10b981, #6ee7b7); }
        .fl-kpi.accent-blue::after   { background: linear-gradient(90deg, #2563eb, #06b6d4); }
        .fl-kpi:hover {
          transform: translateY(-2px);
          box-shadow: var(--fl-shadow-md);
          border-color: #c7d5f1;
        }
        .fl-kpi-head { display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; }
        .fl-kpi-label {
          color: var(--fl-muted); font-size:.7rem; letter-spacing:.08em;
          text-transform:uppercase; font-weight:800;
        }
        .fl-kpi-icon {
          width:30px; height:30px; border-radius:8px;
          display:flex; align-items:center; justify-content:center;
          background: var(--fl-bg); color: var(--fl-muted);
        }
        .fl-kpi-icon svg { width:16px; height:16px; }
        .fl-kpi.accent-red    .fl-kpi-icon { background:#fee2e2; color:#b91c1c; }
        .fl-kpi.accent-amber  .fl-kpi-icon { background:#fef3c7; color:#b45309; }
        .fl-kpi.accent-green  .fl-kpi-icon { background:#d1fae5; color:#047857; }
        .fl-kpi.accent-blue   .fl-kpi-icon { background:#dbeafe; color:#1d4ed8; }
        .fl-kpi-value {
          color: var(--fl-ink); font-size:1.85rem; font-weight:900;
          line-height:1.05; letter-spacing:-.02em;
          font-feature-settings: "tnum";
        }
        .fl-kpi.accent-red    .fl-kpi-value { color: var(--fl-red); }
        .fl-kpi.accent-amber  .fl-kpi-value { color: var(--fl-amber); }
        .fl-kpi.accent-green  .fl-kpi-value { color: var(--fl-green); }
        .fl-kpi-hint {
          color: var(--fl-muted); font-size:.78rem; margin-top:8px; line-height:1.4;
        }

        /* ============ PILLS ============ */
        .fl-pill {
          display:inline-flex; align-items:center; gap:5px;
          border-radius:999px; padding:4px 12px;
          font-size:.74rem; font-weight:800; color:white; white-space:nowrap;
          letter-spacing:.02em;
          box-shadow: 0 1px 2px rgba(0,0,0,.10);
        }
        .fl-pill::before { content:""; width:6px; height:6px; border-radius:50%; background:rgba(255,255,255,.85); }

        /* ============ SECTION TITLE ============ */
        .fl-section-title {
          font-size:1.05rem; font-weight:800; color: var(--fl-ink);
          margin: 24px 0 4px; letter-spacing:-.01em;
          display:flex; align-items:center; gap:10px;
        }
        .fl-section-title::before {
          content:""; width:4px; height:18px;
          background: linear-gradient(180deg, var(--fl-blue), var(--fl-cyan));
          border-radius:2px;
        }
        .fl-muted {
          color: var(--fl-muted); font-size:.88rem;
          margin: 2px 0 14px 14px; line-height:1.45;
        }

        /* ============ SCORE BREAKDOWN ============ */
        .fl-score-grid {
          display:grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap:12px;
        }
        .fl-score-item {
          background: var(--fl-surface-2);
          border:1px solid var(--fl-line);
          border-radius: var(--fl-r-md);
          padding:14px 16px;
          transition: all .15s ease;
        }
        .fl-score-item:hover { background: var(--fl-surface); border-color:#c7d5f1; transform: translateY(-1px); }
        .fl-score-item .label {
          color: var(--fl-muted); font-size:.7rem;
          font-weight:800; letter-spacing:.08em; text-transform:uppercase;
        }
        .fl-score-item .value {
          margin-top:8px; font-weight:900; font-size:1.5rem;
          color: var(--fl-ink); font-feature-settings:"tnum"; letter-spacing:-.02em;
        }
        .fl-score-item .bar {
          margin-top:10px; height:5px; background: var(--fl-line-soft);
          border-radius:3px; overflow:hidden;
        }
        .fl-score-item .bar > span {
          display:block; height:100%; border-radius:3px;
          background: linear-gradient(90deg, var(--fl-blue), var(--fl-cyan));
          transition: width .4s ease;
        }

        /* ============ STREAMLIT OVERRIDES ============ */
        div[data-testid="stMetric"] {
          background: var(--fl-surface); border:1px solid var(--fl-line);
          border-radius: var(--fl-r-md); padding:14px 16px;
          box-shadow: var(--fl-shadow-xs);
        }
        div[data-testid="stMetric"] label {
          color: var(--fl-muted); font-size:.7rem !important;
          letter-spacing:.08em; text-transform:uppercase; font-weight:800;
        }
        div[data-testid="stMetricValue"] {
          color: var(--fl-ink); font-weight:900; font-size:1.55rem;
          font-feature-settings:"tnum";
        }

        .stDataFrame, .stDataEditor {
          border-radius: var(--fl-r-md); border:1px solid var(--fl-line); overflow:hidden;
        }

        .stButton > button {
          border-radius: var(--fl-r-sm) !important;
          font-weight:600 !important;
          border:1px solid var(--fl-line) !important;
          background: var(--fl-surface) !important;
          color: var(--fl-ink) !important;
          transition: all .15s ease !important;
          padding: 8px 14px !important;
        }
        .stButton > button:hover {
          border-color: var(--fl-blue) !important;
          color: var(--fl-blue) !important;
          background: var(--fl-blue-soft) !important;
          transform: translateY(-1px);
        }
        .stDownloadButton > button {
          background: linear-gradient(135deg, var(--fl-blue), var(--fl-blue-700)) !important;
          color:white !important;
          border:1px solid var(--fl-blue-700) !important;
          font-weight:700 !important;
          box-shadow: 0 4px 12px rgba(37,99,235,.25) !important;
        }
        .stDownloadButton > button:hover {
          box-shadow: 0 6px 18px rgba(37,99,235,.35) !important;
          transform: translateY(-1px);
        }

        div[data-testid="stChatMessage"] {
          background: var(--fl-surface);
          border:1px solid var(--fl-line);
          border-radius: var(--fl-r-md);
          padding:14px 16px;
        }

        div[data-baseweb="tab-list"] { border-bottom:1px solid var(--fl-line); gap:4px; }
        button[data-baseweb="tab"] {
          color: var(--fl-muted) !important; font-weight:600 !important;
          padding: 10px 16px !important;
        }
        button[data-baseweb="tab"][aria-selected="true"] {
          color: var(--fl-blue) !important; font-weight:700 !important;
        }

        div[data-testid="stExpander"] {
          border:1px solid var(--fl-line); border-radius: var(--fl-r-md);
          background: var(--fl-surface);
        }
        div[data-testid="stAlert"] { border-radius: var(--fl-r-md); }

        hr { border-color: var(--fl-line); margin: 18px 0; }

        /* ============ MOBILE ============ */
        @media (max-width: 1024px) {
          .main .block-container { max-width:100%; padding-left:.8rem; padding-right:.8rem; }
        }
        @media (max-width: 820px) {
          .fl-hero { padding:18px 20px; }
          .fl-hero-row { flex-direction:column; gap:14px; }
          .fl-hero-icon { width:48px; height:48px; }
          .fl-hero h1 { font-size:1.45rem; }
          .fl-hero p { font-size:.9rem; }
          .fl-kpi { min-height:auto; padding:13px 14px; }
          .fl-kpi-value { font-size:1.45rem; }
          .fl-score-grid { grid-template-columns: repeat(2, minmax(0,1fr)); }
          .fl-section-title { font-size:1rem; }
          [data-testid="stMetricValue"] { font-size:1.25rem !important; }
        }
        @media (max-width: 520px) {
          .fl-hero { padding:14px 16px; border-radius:12px; }
          .fl-hero h1 { font-size:1.25rem; }
          .fl-hero p { font-size:.85rem; }
          .fl-kpi-value { font-size:1.3rem; }
          .fl-kpi-icon { width:26px; height:26px; }
          .fl-score-grid { grid-template-columns: 1fr 1fr; gap:8px; }
        }
        </style>
        """
    )


def _svg(body: str, color: str = "#ffffff", width: int = 24, stroke: float = 2.0) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" '
        f'width="{width}" height="{width}" fill="none" stroke="{color}" '
        f'stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" '
        f'style="display:block">{body}</svg>'
    )


def icon_shield(color: str = "#ffffff", width: int = 26) -> str:
    return _svg('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>', color, width, 2.1)


def icon_search(color: str = "#1d4ed8", width: int = 16) -> str:
    return _svg('<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>', color, width, 2)


def icon_alert(color: str = "#b91c1c", width: int = 16) -> str:
    return _svg('<path d="m10.29 3.86-8.55 14.83A2 2 0 0 0 3.46 22h17.08a2 2 0 0 0 1.72-3.31L13.71 3.86a2 2 0 0 0-3.42 0Z"/><path d="M12 9v4"/><path d="M12 17h.01"/>', color, width, 2)


def icon_alert_circle(color: str = "#b45309", width: int = 16) -> str:
    return _svg('<circle cx="12" cy="12" r="10"/><path d="M12 8v4"/><path d="M12 16h.01"/>', color, width, 2)


def icon_check(color: str = "#047857", width: int = 16) -> str:
    return _svg('<circle cx="12" cy="12" r="10"/><path d="m9 12 2 2 4-4"/>', color, width, 2)


def icon_dollar(color: str = "#5b6677", width: int = 16) -> str:
    return _svg('<line x1="12" x2="12" y1="2" y2="22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>', color, width, 2)


def icon_trending(color: str = "#1d4ed8", width: int = 16) -> str:
    return _svg('<polyline points="22 7 13.5 15.5 8.5 10.5 2 17"/><polyline points="16 7 22 7 22 13"/>', color, width, 2)


def icon_info(color: str = "#ffffff", width: int = 14) -> str:
    return _svg('<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>', color, width, 2.5)
