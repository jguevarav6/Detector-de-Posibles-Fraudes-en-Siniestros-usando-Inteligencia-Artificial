"""Pagina de cruce operacional vs compliance (DB1 + DB2)."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.agent import agent_tools
from src.app.components import ethics_notice, format_currency, kpi_card, page_header, section_title
from src.app.styles import icon_alert, icon_check, icon_search, icon_shield
from src.database import watchlist_repo


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Watchlist y cruce de bases",
        "Watchlist = lista interna de compliance con proveedores, asegurados y vehiculos que ya tuvieron problemas. El sistema cruza siniestros nuevos contra esa lista para priorizar revision.",
    )
    ethics_notice()

    st.markdown(
        """
        <div style="background:#ffffff; border:1px solid #e3e8f0;
                    border-left:4px solid #2563eb; border-radius:12px;
                    padding:16px 20px; margin-bottom:18px;">
          <div style="font-weight:800; color:#0a1628; font-size:1rem; margin-bottom:6px;">
            &iquest;Que es esta pantalla y para que sirve?
          </div>
          <div style="color:#28344a; font-size:.92rem; line-height:1.6;">
            En una aseguradora real existen <strong>dos bases separadas</strong>:
            la base <strong>operacional</strong> (siniestros que entran cada dia)
            y la base de <strong>compliance / watchlist</strong> (proveedores,
            asegurados y vehiculos marcados por auditoria o casos previos).
            <br><br>
            FraudLens conecta las dos via MCP. Cuando llega un siniestro nuevo,
            el sistema lo <strong>cruza automaticamente</strong> con la watchlist
            y prioriza casos donde el proveedor, asegurado o vehiculo ya tenia
            historial. Aqui ves esos cruces en tiempo real.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    summary = agent_tools.watchlist_summary()
    cols = st.columns(4)
    with cols[0]:
        kpi_card("Cruces totales", str(summary["claims_con_alerta_compliance"]), f"de {summary['claims_total']} siniestros", "blue", icon_search())
    with cols[1]:
        kpi_card("Rojos con alerta", str(summary["claims_rojos_con_alerta"]), "Casos criticos a priorizar", "red", icon_alert())
    with cols[2]:
        kpi_card("Proveedores watchlist", str(summary["watchlist_proveedores"]), "Base de compliance", "amber", icon_shield())
    with cols[3]:
        kpi_card("Asegurados antecedentes", str(summary["watchlist_asegurados"]), "Historial registrado", "", icon_check())

    section_title("Bases conectadas", "Lectura en tiempo real. Si MySQL no esta disponible, cae a CSV versionado.")
    status = watchlist_repo.watchlist_status()
    st.html(
        f"""
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:14px;">
          <div style="background:#ffffff; border:1px solid #e3e8f0; border-left:4px solid #2563eb;
                      border-radius:12px; padding:16px 18px;">
            <div style="color:#5b6677; font-size:.7rem; font-weight:800; letter-spacing:.08em;
                        text-transform:uppercase;">DB 1 - Operacional</div>
            <div style="font-size:1.1rem; font-weight:800; color:#0a1628; margin-top:4px;
                        font-family:'JetBrains Mono',monospace;">fraudlens_claims_ai</div>
            <div style="color:#5b6677; font-size:.85rem; margin-top:6px;">
              {summary['claims_total']:,} siniestros con score y semaforo.
            </div>
          </div>
          <div style="background:#ffffff; border:1px solid #e3e8f0; border-left:4px solid #d68a00;
                      border-radius:12px; padding:16px 18px;">
            <div style="color:#5b6677; font-size:.7rem; font-weight:800; letter-spacing:.08em;
                        text-transform:uppercase;">DB 2 - Compliance &middot; {status['source']}</div>
            <div style="font-size:1.1rem; font-weight:800; color:#0a1628; margin-top:4px;
                        font-family:'JetBrains Mono',monospace;">fraudlens_watchlist</div>
            <div style="color:#5b6677; font-size:.85rem; margin-top:6px;">
              {status['proveedores_observados']} proveedores &middot;
              {status['asegurados_antecedentes']} asegurados &middot;
              {status['vehiculos_marcados']} vehiculos &middot;
              {status['narrativas_recurrentes']} patrones.
            </div>
          </div>
        </div>
        """
    )

    tab_cross, tab_pareto, tab_provs, tab_aseg = st.tabs([
        "Expediente cruzado",
        "Pareto 80/20",
        "Proveedores observados",
        "Asegurados con antecedentes",
    ])

    with tab_cross:
        section_title("Expediente cruzado claim + compliance", "Selecciona un siniestro para ver si activa alertas en la watchlist.")
        c1, c2 = st.columns([1.5, 1])
        with c1:
            options = claims.sort_values("score_final", ascending=False)["id_siniestro"].tolist()
            selected = st.selectbox("Siniestro", options, key="watchlist_claim_pick")
        result = agent_tools.cross_reference_claim(selected)
        hits = result.get("watchlist_hits", [])
        with c2:
            color = "#d33232" if hits else "#0f8a55"
            label = f"{len(hits)} alerta(s) compliance" if hits else "Sin cruces"
            st.html(
                f"""
                <div style="margin-top:24px; background:#ffffff; border:1px solid {color}33;
                            border-left:4px solid {color}; border-radius:10px; padding:12px 14px;">
                  <div style="color:{color}; font-size:.72rem; font-weight:800;
                              letter-spacing:.08em; text-transform:uppercase;">Resultado del cruce</div>
                  <div style="color:{color}; font-size:1.05rem; font-weight:800; margin-top:2px;">{label}</div>
                </div>
                """
            )

        if not hits:
            st.html(
                """<div style="background:#e6f5ed; border:1px solid #c4e3d3; color:#0f8a55;
                        border-radius:10px; padding:14px 16px; margin-top:8px;">
                      Este siniestro no aparece en la watchlist de compliance.
                    </div>"""
            )
        else:
            for hit in hits:
                _render_hit_card(hit)

    with tab_pareto:
        section_title("Concentracion de alertas rojas (Pareto)", "Tool MCP: pareto_red_providers. Responde literalmente la pregunta del jurado.")
        pareto = agent_tools.pareto_red_providers(0.8)
        if "error" in pareto:
            st.warning("No hay rojos suficientes para calcular el Pareto.")
        else:
            top1, top2, top3 = st.columns(3)
            top1.metric("Rojos totales", pareto["rojos_totales"])
            top2.metric("Proveedores", f"{pareto['n_proveedores']}")
            top3.metric("Cobertura", f"{pareto['porcentaje_cubierto']:.0%}")
            st.html(
                """<div style="background:#fbf1da; border:1px solid #f0d68a; color:#7d4f00;
                        border-left:4px solid #d68a00; border-radius:10px; padding:12px 16px; margin:10px 0;">
                      <strong>Lectura ejecutiva:</strong>
                      Concentrar el equipo de revision en estos proveedores cubre el 80% de las alertas rojas.
                    </div>"""
            )
            st.dataframe(
                pd.DataFrame(pareto["proveedores"]),
                width="stretch",
                hide_index=True,
                column_config={
                    "rojos":     st.column_config.NumberColumn("Rojos"),
                    "acumulado": st.column_config.NumberColumn("Acumulado"),
                },
            )

    with tab_provs:
        section_title("Watchlist · proveedores", "Lectura directa de la tabla `proveedores_observados`.")
        st.dataframe(watchlist_repo.proveedores_observados(), width="stretch", hide_index=True)

    with tab_aseg:
        section_title("Watchlist · asegurados", "Lectura directa de la tabla `asegurados_antecedentes`.")
        st.dataframe(watchlist_repo.asegurados_antecedentes(), width="stretch", hide_index=True)


def _render_hit_card(hit: dict) -> None:
    tipo = hit.get("tipo", "")
    icon_color = {"proveedor": "#d33232", "asegurado": "#d68a00", "vehiculo": "#1d4ed8"}.get(tipo, "#5b6677")
    titulo_map = {
        "proveedor": f"Proveedor {hit.get('id_proveedor', '')} en watchlist",
        "asegurado": f"Asegurado {hit.get('id_asegurado', '')} con antecedente",
        "vehiculo":  f"Vehiculo {hit.get('id_vehiculo', '')} marcado",
    }
    detail_map = {
        "proveedor": f"Nivel: <strong>{hit.get('nivel_alerta', '')}</strong> &middot; {hit.get('casos_relacionados', '')} casos relacionados.",
        "asegurado": f"Tipo: <strong>{hit.get('tipo_antecedente', '')}</strong> &middot; {hit.get('reclamos_previos', '')} reclamos previos.",
        "vehiculo":  f"Fuente: <strong>{hit.get('fuente', '')}</strong> &middot; {hit.get('casos_relacionados', '')} casos relacionados.",
    }
    st.html(
        f"""
        <div style="background:#ffffff; border:1px solid {icon_color}33;
                    border-left:5px solid {icon_color}; border-radius:12px;
                    padding:14px 18px; margin:8px 0; box-shadow:0 2px 6px rgba(10,22,40,.04);">
          <div style="color:{icon_color}; font-weight:800; font-size:.95rem;">{titulo_map.get(tipo, tipo)}</div>
          <div style="color:#28344a; font-size:.88rem; margin-top:6px;">{detail_map.get(tipo, '')}</div>
          <div style="color:#5b6677; font-size:.82rem; margin-top:6px;">
            Motivo: {hit.get('motivo', 'No registrado')}.
          </div>
        </div>
        """
    )
