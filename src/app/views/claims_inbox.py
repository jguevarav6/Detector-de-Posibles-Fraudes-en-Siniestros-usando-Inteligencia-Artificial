"""Pagina de bandeja priorizada de siniestros."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.components import ethics_notice, format_currency, level_order, page_header, risk_pill, section_title


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Bandeja de siniestros",
        "Filtro operativo para ordenar casos por prioridad, monto, cobertura y concentracion de senales.",
    )
    ethics_notice()

    with st.container(border=True):
        c1, c2, c3, c4 = st.columns(4)
        levels = c1.multiselect("Nivel", sorted(claims["nivel_riesgo"].unique()), default=list(claims["nivel_riesgo"].unique()))
        cities = c2.multiselect("Ciudad", sorted(claims["ciudad"].unique()), default=list(claims["ciudad"].unique()))
        branches = c3.multiselect("Ramo", sorted(claims["ramo"].unique()), default=list(claims["ramo"].unique()))
        coverages = c4.multiselect("Cobertura", sorted(claims["cobertura"].unique()), default=list(claims["cobertura"].unique()))
        c5, c6, c7 = st.columns([1.2, 1.2, 1])
        providers = c5.multiselect("Proveedor", sorted(claims["proveedor"].unique()), default=list(claims["proveedor"].unique()))
        amount_range = c6.slider(
            "Monto reclamado",
            min_value=float(claims["monto_reclamado"].min()),
            max_value=float(claims["monto_reclamado"].max()),
            value=(float(claims["monto_reclamado"].min()), float(claims["monto_reclamado"].max())),
        )
        search = c7.text_input("Buscar ID", placeholder="SIN-00001")

    filtered = claims[
        claims["nivel_riesgo"].isin(levels)
        & claims["ciudad"].isin(cities)
        & claims["ramo"].isin(branches)
        & claims["cobertura"].isin(coverages)
        & claims["proveedor"].isin(providers)
        & claims["monto_reclamado"].between(amount_range[0], amount_range[1])
    ]
    if search:
        filtered = filtered[filtered["id_siniestro"].str.contains(search.strip(), case=False, na=False)]
    filtered = level_order(filtered)

    c1, c2, c3 = st.columns(3)
    c1.metric("Casos filtrados", len(filtered))
    c2.metric("Score promedio", f"{filtered['score_final'].mean():.1f}" if not filtered.empty else "0")
    c3.metric("Monto filtrado", format_currency(float(filtered["monto_reclamado"].sum())) if not filtered.empty else "$0")

    section_title("Tabla priorizada", "Orden rojo, amarillo y verde; dentro de cada nivel, score descendente.")
    st.dataframe(
        filtered[
            [
                "id_siniestro",
                "fecha_ocurrencia",
                "ciudad",
                "ramo",
                "cobertura",
                "proveedor",
                "monto_reclamado",
                "score_final",
                "nivel_riesgo",
                "accion_sugerida",
            ]
        ],
        use_container_width=True,
        hide_index=True,
        column_config={
            "score_final": st.column_config.ProgressColumn("Score", min_value=0, max_value=100),
            "monto_reclamado": st.column_config.NumberColumn("Monto", format="$ %.0f"),
        },
    )

    section_title("Vista rapida", "Tarjetas compactas para revisar los primeros casos filtrados.")
    for _, row in filtered.head(6).iterrows():
        with st.container(border=True):
            a, b, c = st.columns([1.1, 1.4, 2.2])
            a.markdown(f"**{row['id_siniestro']}**")
            a.markdown(risk_pill(str(row["nivel_riesgo"])), unsafe_allow_html=True)
            b.metric("Score", f"{row['score_final']:.0f}")
            b.caption(format_currency(float(row["monto_reclamado"])))
            c.caption(f"{row['ciudad']} · {row['ramo']} · {row['cobertura']}")
            c.write(row["accion_sugerida"])
