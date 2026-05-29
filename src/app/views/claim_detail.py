"""Pagina de detalle explicable de un siniestro."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.components import ethics_notice, format_currency, page_header, score_breakdown, section_title
from src.app.styles import RISK_COLORS, RISK_COLORS_SOFT


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Detalle del siniestro",
        "Explicacion trazable del score, reglas activadas, documentos y senales textuales para revision humana.",
    )
    ethics_notice()

    ordered = claims.sort_values("score_final", ascending=False)
    c_sel, c_info = st.columns([2, 1])
    with c_sel:
        selected = st.selectbox(
            "Seleccionar siniestro",
            ordered["id_siniestro"].tolist(),
            help="Listado ordenado por score descendente. Los primeros casos requieren revision prioritaria.",
        )
    claim = claims.loc[claims["id_siniestro"] == selected].iloc[0]
    nivel = str(claim["nivel_riesgo"])
    color = RISK_COLORS.get(nivel, "#5b6677")
    color_soft = RISK_COLORS_SOFT.get(nivel, "#eef1f6")
    with c_info:
        st.html(
            f"""
            <div style="background:{color_soft}; border:1px solid {color}33; border-left:4px solid {color};
                        border-radius:10px; padding:10px 14px; margin-top:28px;">
              <div style="font-size:0.72rem; font-weight:700; letter-spacing:.06em; text-transform:uppercase;
                          color:{color};">Prioridad de revision</div>
              <div style="font-size:1.05rem; font-weight:700; color:{color}; margin-top:2px;">
                {nivel} &middot; {float(claim['score_final']):.0f}/100
              </div>
            </div>
            """
        )

    st.html(
        f"""
        <div style="background:#ffffff; border:1px solid #e3e8f0; border-radius:14px;
                    padding:20px 24px; margin:14px 0 18px; box-shadow:0 2px 6px rgba(10,37,64,.05);
                    border-left:5px solid {color};">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:18px; flex-wrap:wrap;">
            <div>
              <div style="color:#5b6677; font-size:.72rem; font-weight:700; letter-spacing:.08em;
                          text-transform:uppercase;">Siniestro</div>
              <div style="font-size:1.5rem; font-weight:800; color:#0a2540; letter-spacing:-.02em;
                          font-family:'JetBrains Mono',monospace;">{claim['id_siniestro']}</div>
              <div style="color:#5b6677; font-size:.88rem; margin-top:6px;">
                {claim['ciudad']} &middot; {claim['ramo']} &middot; {claim['cobertura']}
              </div>
            </div>
            <div style="text-align:right;">
              <div style="color:#5b6677; font-size:.72rem; font-weight:700; letter-spacing:.08em;
                          text-transform:uppercase;">Monto reclamado</div>
              <div style="font-size:1.5rem; font-weight:800; color:#0a2540; letter-spacing:-.02em;
                          font-feature-settings:'tnum';">{format_currency(float(claim['monto_reclamado']))}</div>
              <div style="color:#5b6677; font-size:.82rem; margin-top:4px;">
                {float(claim.get('monto_vs_suma_asegurada', 0)):.0%} de la suma asegurada
              </div>
            </div>
          </div>
          <div style="margin-top:14px; padding:12px 14px; background:#f6f8fb; border-radius:10px;
                      border:1px dashed #c7d8f9;">
            <span style="color:#1748ab; font-weight:700; font-size:.78rem; letter-spacing:.06em;
                         text-transform:uppercase;">Accion sugerida</span><br>
            <span style="color:#0a2540; font-size:0.95rem;">{claim['accion_sugerida']}</span>
          </div>
        </div>
        """
    )

    tab_summary, tab_score, tab_evidence = st.tabs(["Resumen", "Score detallado", "Evidencia"])

    with tab_summary:
        left, right = st.columns([1.3, 0.9])
        with left:
            section_title("Explicacion para el analista", "Texto generado por reglas y NLP; sin lenguaje acusatorio.")
            st.html(
                f"""
                <div style="background:#ffffff; border:1px solid #e3e8f0; border-radius:10px;
                            padding:16px 18px; color:#28344a; font-size:.95rem; line-height:1.55;">
                  {claim['explicacion']}
                </div>
                """
            )
            section_title("Reglas activadas", "Cada regla aporta puntos al score y es trazable.")
            reglas = [r.strip() for r in str(claim["reglas_activadas"]).split(";") if r.strip()]
            if reglas:
                chips = "".join(
                    f"""<div style="display:flex; align-items:center; gap:10px; background:#fbf1da;
                            border:1px solid #f0d68a; border-left:3px solid #d68a00; border-radius:8px;
                            padding:10px 14px; margin-bottom:8px;">
                          <div style="width:24px; height:24px; border-radius:6px; background:#d68a00;
                                      color:white; display:flex; align-items:center; justify-content:center;
                                      font-weight:800; font-size:.72rem;">!</div>
                          <div style="color:#7d4f00; font-weight:600; font-size:.92rem;">{r}</div>
                        </div>"""
                    for r in reglas
                )
                st.html(chips)
            else:
                st.html(
                    """<div style="background:#e6f5ed; border:1px solid #c4e3d3; color:#0f8a55;
                            border-radius:8px; padding:12px 14px;">Sin reglas activadas. Caso dentro de patrones esperados.</div>"""
                )

        with right:
            section_title("Ficha del caso")
            ficha_rows = [
                ("Ciudad", claim["ciudad"]),
                ("Ramo", claim["ramo"]),
                ("Cobertura", claim["cobertura"]),
                ("Proveedor", claim["proveedor"]),
                ("Asegurado", claim["asegurado"]),
                ("Vehiculo", str(claim["vehiculo"]) if claim.get("vehiculo") else "No aplica"),
                ("Ocurrencia", claim["fecha_ocurrencia"]),
                ("Reporte", claim["fecha_reporte"]),
            ]
            rows = "".join(
                f"""<div style="display:flex; justify-content:space-between; padding:8px 12px;
                       border-bottom:1px solid #eef1f6;">
                      <span style="color:#5b6677; font-size:.82rem;">{k}</span>
                      <span style="color:#0a2540; font-weight:600; font-size:.88rem;">{v}</span>
                    </div>"""
                for k, v in ficha_rows
            )
            st.html(
                f"""<div style="background:#ffffff; border:1px solid #e3e8f0; border-radius:10px;
                        overflow:hidden;">{rows}</div>"""
            )

    with tab_score:
        section_title("Componentes del score", "Formula: 55% reglas, 25% ML, 10% anomalia, 10% NLP.")
        score_breakdown(claim)
        st.html("<div style='height:14px'></div>")
        sf = float(claim["score_final"])
        st.html(
            f"""
            <div style="background:#ffffff; border:1px solid #e3e8f0; border-radius:10px; padding:18px 20px;">
              <div style="display:flex; justify-content:space-between; margin-bottom:8px;">
                <span style="color:#5b6677; font-size:.78rem; font-weight:700; letter-spacing:.06em;
                             text-transform:uppercase;">Score final</span>
                <span style="color:{color}; font-weight:800; font-size:1.1rem;">{sf:.0f}/100</span>
              </div>
              <div style="height:10px; background:#eef1f6; border-radius:6px; overflow:hidden;">
                <div style="height:100%; width:{sf:.0f}%; background:linear-gradient(90deg,{color}88,{color});
                            border-radius:6px;"></div>
              </div>
              <div style="margin-top:14px; color:#5b6677; font-size:.88rem;">
                El monto reclamado representa
                <strong style="color:#0a2540;">{float(claim.get('monto_vs_suma_asegurada', 0)):.0%}</strong>
                de la suma asegurada registrada.
              </div>
            </div>
            """
        )

    with tab_evidence:
        left, right = st.columns([1, 1])
        with left:
            section_title("Documentos y plazos")
            timeline = [
                ("Documentos", str(claim["documentos"])),
                ("Dias desde inicio de poliza", str(claim["dias_desde_inicio_poliza"])),
                ("Dias hasta fin de poliza", str(claim["dias_desde_fin_poliza"])),
                ("Dias ocurrencia-reporte", str(claim["dias_entre_ocurrencia_reporte"])),
            ]
            rows = "".join(
                f"""<div style="padding:12px 14px; border-bottom:1px solid #eef1f6;">
                      <div style="color:#5b6677; font-size:.72rem; font-weight:700; letter-spacing:.06em;
                                  text-transform:uppercase; margin-bottom:4px;">{k}</div>
                      <div style="color:#0a2540; font-size:.95rem;">{v}</div>
                    </div>"""
                for k, v in timeline
            )
            st.html(
                f"""<div style="background:#ffffff; border:1px solid #e3e8f0; border-radius:10px;
                        overflow:hidden;">{rows}</div>"""
            )

        with right:
            section_title("Narrativa textual", "Vectorizada con TF-IDF; similitud por cosine similarity.")
            st.html(
                f"""<div style="background:#f9fbfd; border:1px solid #e3e8f0; border-radius:10px;
                        padding:14px 16px; color:#28344a; font-style:italic; min-height:80px;">
                      &laquo;{str(claim.get('descripcion', '')) or 'Sin descripcion registrada.'}&raquo;
                    </div>"""
            )
            if claim.get("similar_claim_id"):
                similar = float(claim["max_similarity"])
                st.html(
                    f"""<div style="margin-top:10px; background:#e8f0fe; border:1px solid #c7d8f9;
                            border-left:4px solid #1e5bd6; border-radius:10px; padding:12px 14px;">
                          <div style="color:#1748ab; font-weight:700; font-size:.82rem;">Caso narrativamente similar</div>
                          <div style="color:#0a2540; font-size:.95rem; margin-top:4px;">
                            <strong>{claim['similar_claim_id']}</strong> &middot; similitud {similar:.0%}
                          </div>
                        </div>"""
                )
            else:
                st.html(
                    """<div style="margin-top:10px; color:#5b6677; font-size:.88rem;">
                          No se observan narrativas similares relevantes en el dataset.
                        </div>"""
                )
