"""Simulador de score para un siniestro hipotetico.

Responde la prueba de fuego: 'cargue este siniestro ocurrido 24 horas despues
de la poliza y explique el riesgo'. Aplica las reglas explicables en vivo y
muestra el desglose de puntos sin tocar la base.
"""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.agent import agent_tools
from src.app.components import ethics_notice, page_header, section_title
from src.app.styles import RISK_COLORS


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Simulador de siniestro",
        "Ingresa un caso hipotetico. El sistema aplica las reglas explicables en vivo y devuelve nivel, score y motivo. No persiste nada en la base.",
    )
    ethics_notice()

    section_title("Datos del siniestro hipotetico")
    c1, c2 = st.columns(2)
    with c1:
        monto = st.number_input("Monto reclamado ($)", min_value=0, value=15000, step=500)
        suma = st.number_input("Suma asegurada de la poliza ($)", min_value=1, value=20000, step=500)
        ramo = st.selectbox("Ramo", ["Vehiculos", "Salud", "Hogar", "Vida", "Comercial"])
    with c2:
        dias_inicio = st.number_input("Dias desde el inicio de la poliza", min_value=0, value=1)
        dias_reporte = st.number_input("Dias entre ocurrencia y reporte", min_value=0, value=2)
        docs = st.toggle("Documentos completos", value=True)

    st.divider()
    result = agent_tools.simulate_claim_score(
        monto_reclamado=float(monto),
        suma_asegurada=float(suma),
        dias_desde_inicio_poliza=int(dias_inicio),
        dias_entre_ocurrencia_reporte=int(dias_reporte),
        documentos_completos=bool(docs),
        ramo=ramo,
    )

    nivel = result["nivel_riesgo"]
    color = RISK_COLORS.get(nivel, "#5b6677")
    score = int(result["score_final"])
    st.html(
        f"""
        <div style="background:#ffffff; border:1px solid {color}33;
                    border-left:5px solid {color}; border-radius:14px;
                    padding:18px 22px; margin-bottom:14px;
                    box-shadow:0 4px 14px rgba(10,22,40,.06);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:18px; flex-wrap:wrap;">
            <div>
              <div style="color:#5b6677; font-size:.72rem; font-weight:800; letter-spacing:.08em;
                          text-transform:uppercase;">Resultado de la simulacion</div>
              <div style="font-size:1.6rem; font-weight:900; color:{color}; letter-spacing:-.02em;">
                {nivel} &middot; {score}/100
              </div>
              <div style="color:#5b6677; font-size:.9rem; margin-top:4px;">
                Accion sugerida: <strong>{result['accion_sugerida']}</strong>
              </div>
            </div>
            <div style="text-align:right;">
              <div style="color:#5b6677; font-size:.72rem; font-weight:800; letter-spacing:.08em;
                          text-transform:uppercase;">Reglas activadas</div>
              <div style="font-size:1.6rem; font-weight:900; color:#0a1628;">
                {len(result['reglas_activadas'])}
              </div>
            </div>
          </div>
          <div style="margin-top:14px; height:10px; background:#eef1f6; border-radius:6px; overflow:hidden;">
            <div style="height:100%; width:{score}%; background:linear-gradient(90deg,{color}88,{color}); border-radius:6px;"></div>
          </div>
        </div>
        """
    )

    section_title("Desglose de reglas", "Cada regla aporta puntos al score y es trazable.")
    if not result["reglas_activadas"]:
        st.html(
            """<div style="background:#e6f5ed; border:1px solid #c4e3d3; color:#0f8a55;
                    border-radius:10px; padding:12px 16px;">
                  Ninguna regla se activo con esos datos. El caso entra como verde.
                </div>"""
        )
    else:
        for regla in result["reglas_activadas"]:
            st.html(
                f"""
                <div style="display:flex; align-items:center; gap:14px;
                            background:#fbf1da; border:1px solid #f0d68a;
                            border-left:3px solid #d68a00; border-radius:8px;
                            padding:12px 16px; margin-bottom:8px;">
                  <div style="background:#d68a00; color:white; font-weight:800;
                              border-radius:6px; padding:4px 10px; font-size:.75rem;
                              font-family:'JetBrains Mono',monospace;">{regla['codigo']}</div>
                  <div style="flex:1; color:#7d4f00; font-size:.92rem;">{regla['regla']}</div>
                  <div style="font-weight:800; color:#7d4f00; font-size:1.05rem;">+{regla['puntos']}</div>
                </div>
                """
            )

    st.info(
        "Esta simulacion NO acusa fraude ni decide pagos. Es una herramienta para que un analista "
        "vea como el motor de reglas habria evaluado un caso hipotetico antes de cargarlo a la base."
    )
