"""Página de bandeja priorizada de siniestros."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.components import ethics_notice, level_order, page_header


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Bandeja de siniestros",
        "Filtra, ordena y prioriza casos por nivel de riesgo para revisión del analista.",
    )
    ethics_notice()

    with st.container(border=True):
        c1, c2, c3, c4 = st.columns(4)
        levels = c1.multiselect("Nivel", sorted(claims["nivel_riesgo"].unique()), default=list(claims["nivel_riesgo"].unique()))
        cities = c2.multiselect("Ciudad", sorted(claims["ciudad"].unique()), default=list(claims["ciudad"].unique()))
        branches = c3.multiselect("Ramo", sorted(claims["ramo"].unique()), default=list(claims["ramo"].unique()))
        providers = c4.multiselect("Proveedor", sorted(claims["proveedor"].unique()), default=list(claims["proveedor"].unique()))

    filtered = claims[
        claims["nivel_riesgo"].isin(levels)
        & claims["ciudad"].isin(cities)
        & claims["ramo"].isin(branches)
        & claims["proveedor"].isin(providers)
    ]
    filtered = level_order(filtered)

    st.caption(f"{len(filtered)} casos encontrados")
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
    )

    st.markdown("### Vista móvil")
    for _, row in filtered.head(8).iterrows():
        with st.container(border=True):
            st.markdown(f"**{row['id_siniestro']}** · {row['nivel_riesgo']} · Score {row['score_final']}")
            st.caption(f"{row['ciudad']} · {row['ramo']} · {row['proveedor']}")
            st.write(row["accion_sugerida"])
