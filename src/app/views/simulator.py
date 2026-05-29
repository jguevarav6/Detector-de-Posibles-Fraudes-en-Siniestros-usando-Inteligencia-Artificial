"""Simulador de score para un siniestro hipotetico.

Responde la prueba de fuego del jurado:
'Cargue este siniestro ocurrido 24 horas despues de la poliza y explique
el riesgo asignado.'

Soporta dos modos:
1. **Formulario manual:** ingresar campos directamente.
2. **Carga de archivo:** subir CSV o JSON con uno o varios siniestros.

Aplica las reglas explicables en vivo y devuelve el desglose. No persiste
en la base.
"""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from src.agent import agent_tools
from src.app.components import ethics_notice, page_header, section_title
from src.app.styles import RISK_COLORS


REQUIRED_FIELDS = (
    "monto_reclamado",
    "suma_asegurada",
    "dias_desde_inicio_poliza",
    "dias_entre_ocurrencia_reporte",
)

TEMPLATE_CSV = (
    "id_siniestro,ramo,monto_reclamado,suma_asegurada,"
    "dias_desde_inicio_poliza,dias_entre_ocurrencia_reporte,documentos_completos\n"
    "TEST-001,Vehiculos,15000,20000,1,12,false\n"
    "TEST-002,Salud,4500,8000,210,3,true\n"
)

TEMPLATE_JSON = json.dumps(
    [
        {
            "id_siniestro": "TEST-001",
            "ramo": "Vehiculos",
            "monto_reclamado": 15000,
            "suma_asegurada": 20000,
            "dias_desde_inicio_poliza": 1,
            "dias_entre_ocurrencia_reporte": 12,
            "documentos_completos": False,
        }
    ],
    indent=2,
)


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Simulador de siniestro",
        "Carga un caso hipotetico o sube tu propio archivo. El motor aplica las reglas explicables en vivo y devuelve nivel, score y motivos. No se persiste nada en la base.",
    )
    ethics_notice()

    tab_form, tab_upload = st.tabs(["Ingreso manual", "Cargar archivo (CSV / JSON)"])

    with tab_form:
        _render_manual_form()

    with tab_upload:
        _render_upload_panel()


def _render_manual_form() -> None:
    section_title("Datos del siniestro hipotetico", "Modifica cualquier campo para ver como cambia el riesgo en tiempo real.")
    c1, c2 = st.columns(2)
    with c1:
        monto = st.number_input("Monto reclamado ($)", min_value=0, value=15000, step=500, key="sim_monto")
        suma = st.number_input("Suma asegurada de la poliza ($)", min_value=1, value=20000, step=500, key="sim_suma")
        ramo = st.selectbox("Ramo", ["Vehiculos", "Salud", "Hogar", "Vida", "Comercial"], key="sim_ramo")
    with c2:
        dias_inicio = st.number_input("Dias desde el inicio de la poliza", min_value=0, value=1, key="sim_dias_ini")
        dias_reporte = st.number_input("Dias entre ocurrencia y reporte", min_value=0, value=12, key="sim_dias_rep")
        docs = st.toggle("Documentos completos", value=False, key="sim_docs")

    st.divider()
    result = agent_tools.simulate_claim_score(
        monto_reclamado=float(monto),
        suma_asegurada=float(suma),
        dias_desde_inicio_poliza=int(dias_inicio),
        dias_entre_ocurrencia_reporte=int(dias_reporte),
        documentos_completos=bool(docs),
        ramo=ramo,
    )
    _render_result(result)


def _render_upload_panel() -> None:
    section_title("Subir siniestro(s) para evaluacion", "Acepta CSV o JSON. Si subes varias filas, evalua todas y muestra ranking.")

    cols = st.columns([1, 1])
    with cols[0]:
        st.download_button(
            "Plantilla CSV",
            TEMPLATE_CSV,
            file_name="siniestro_plantilla.csv",
            mime="text/csv",
            width="stretch",
        )
    with cols[1]:
        st.download_button(
            "Plantilla JSON",
            TEMPLATE_JSON,
            file_name="siniestro_plantilla.json",
            mime="application/json",
            width="stretch",
        )

    st.html(
        """
        <div style="background:#eef4ff; border:1px solid #c7d8f9;
                    border-left:4px solid #2563eb; border-radius:10px;
                    padding:12px 16px; margin:10px 0;
                    color:#1a3a7d; font-size:.88rem; line-height:1.55;">
          <strong>Campos requeridos:</strong>
          <code>monto_reclamado</code>, <code>suma_asegurada</code>,
          <code>dias_desde_inicio_poliza</code>, <code>dias_entre_ocurrencia_reporte</code>.<br>
          <strong>Opcionales:</strong>
          <code>id_siniestro</code>, <code>ramo</code>, <code>documentos_completos</code> (true/false).
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded = st.file_uploader(
        "Sube tu archivo",
        type=["csv", "json"],
        help="Acepta un siniestro o un lote. Maximo 200 filas para mantener la demo agil.",
    )

    if uploaded is None:
        st.info("Sube un CSV o JSON o usa la pestana 'Ingreso manual'.")
        return

    try:
        df = _parse_upload(uploaded)
    except Exception as exc:
        st.error(f"No pude leer el archivo: {exc}")
        return

    missing = [c for c in REQUIRED_FIELDS if c not in df.columns]
    if missing:
        st.error(f"Faltan columnas requeridas: {', '.join(missing)}.")
        return

    if not _coerce_numeric(df, REQUIRED_FIELDS):
        return

    if len(df) > 200:
        st.warning(f"El archivo tiene {len(df)} filas. Procesando solo las primeras 200.")
        df = df.head(200)

    section_title("Resultados de la evaluacion", f"{len(df)} siniestro(s) evaluado(s) por el motor de reglas.")

    results: list[dict] = []
    for _, row in df.iterrows():
        result = agent_tools.simulate_claim_score(
            monto_reclamado=float(row["monto_reclamado"]),
            suma_asegurada=float(row["suma_asegurada"]),
            dias_desde_inicio_poliza=int(row["dias_desde_inicio_poliza"]),
            dias_entre_ocurrencia_reporte=int(row["dias_entre_ocurrencia_reporte"]),
            documentos_completos=_truthy(row.get("documentos_completos", True)),
            ramo=str(row.get("ramo", "Vehiculos")),
        )
        results.append(
            {
                "id":              str(row.get("id_siniestro", f"UP-{len(results) + 1:03d}")),
                "ramo":            str(row.get("ramo", "Vehiculos")),
                "monto_reclamado": float(row["monto_reclamado"]),
                "nivel_riesgo":    result["nivel_riesgo"],
                "score_final":     result["score_final"],
                "reglas_activadas": len(result["reglas_activadas"]),
                "accion":          result["accion_sugerida"],
            }
        )

    out = pd.DataFrame(results)
    out.index = df.index
    out = out.sort_values("score_final", ascending=False)

    c1, c2, c3 = st.columns(3)
    c1.metric("Casos evaluados", len(out))
    c2.metric("Rojos detectados", int((out["nivel_riesgo"] == "Rojo").sum()))
    c3.metric("Score promedio", f"{out['score_final'].mean():.0f}")

    st.dataframe(
        out,
        width="stretch",
        hide_index=True,
        column_config={
            "score_final":     st.column_config.ProgressColumn("Score", min_value=0, max_value=100),
            "monto_reclamado": st.column_config.NumberColumn("Monto", format="$ %.0f"),
        },
    )

    st.download_button(
        "Descargar resultado de evaluacion",
        out.to_csv(index=False).encode("utf-8"),
        file_name="evaluacion_simulador.csv",
        mime="text/csv",
    )

    # Detalle ampliado del primer caso (el de mayor score)
    if not out.empty:
        top_idx = out.index[0]
        first = out.iloc[0]
        st.divider()
        section_title(f"Desglose del caso con mayor score: {first['id']}")
        detail = agent_tools.simulate_claim_score(
            monto_reclamado=float(first["monto_reclamado"]),
            suma_asegurada=float(df.loc[top_idx, "suma_asegurada"]),
            dias_desde_inicio_poliza=int(df.loc[top_idx, "dias_desde_inicio_poliza"]),
            dias_entre_ocurrencia_reporte=int(df.loc[top_idx, "dias_entre_ocurrencia_reporte"]),
            documentos_completos=_truthy(df.loc[top_idx].get("documentos_completos", True)),
            ramo=str(df.loc[top_idx].get("ramo", "Vehiculos")),
        )
        _render_result(detail)


def _render_result(result: dict) -> None:
    nivel = result["nivel_riesgo"]
    color = RISK_COLORS.get(nivel, "#5b6677")
    score = int(result["score_final"])
    st.markdown(
        f"""
        <div style="background:#ffffff; border:1px solid {color}33;
                    border-left:5px solid {color}; border-radius:14px;
                    padding:18px 22px; margin-bottom:14px;
                    box-shadow:0 4px 14px rgba(10,22,40,.06);">
          <div style="display:flex; justify-content:space-between; align-items:flex-start;
                      gap:18px; flex-wrap:wrap;">
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
            <div style="height:100%; width:{score}%;
                        background:linear-gradient(90deg,{color}88,{color});
                        border-radius:6px;"></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_title("Desglose de reglas", "Cada regla aporta puntos al score y es trazable.")
    if not result["reglas_activadas"]:
        st.markdown(
            """<div style="background:#e6f5ed; border:1px solid #c4e3d3; color:#0f8a55;
                    border-radius:10px; padding:12px 16px;">
                  Ninguna regla se activo con esos datos. El caso entra como verde.
                </div>""",
            unsafe_allow_html=True,
        )
    else:
        for regla in result["reglas_activadas"]:
            st.markdown(
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
                """,
                unsafe_allow_html=True,
            )

    st.info(
        "Esta simulacion NO acusa fraude ni decide pagos. Es una herramienta para que un analista vea "
        "como el motor de reglas habria evaluado un caso hipotetico antes de cargarlo a la base."
    )


def _parse_upload(uploaded) -> pd.DataFrame:
    name = uploaded.name.lower()
    if name.endswith(".csv"):
        return pd.read_csv(uploaded)
    if name.endswith(".json"):
        raw = uploaded.read()
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8")
        data = json.loads(raw)
        if isinstance(data, dict):
            data = [data]
        return pd.DataFrame(data)
    raise ValueError("Solo se aceptan archivos .csv o .json.")


def _coerce_numeric(df: pd.DataFrame, columns) -> bool:
    # Convierte columnas requeridas a numerico; reporta y aborta si hay no-numericos.
    for col in columns:
        coerced = pd.to_numeric(df[col], errors="coerce")
        if coerced.isna().any():
            st.error(f"La columna {col} contiene valores no numericos. Revisa el archivo.")
            return False
        df[col] = coerced
    return True


def _truthy(value) -> bool:
    if isinstance(value, bool):
        return value
    if pd.isna(value):
        return True
    return str(value).strip().lower() in {"true", "1", "si", "sí", "yes", "y"}
