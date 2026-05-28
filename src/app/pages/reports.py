"""Página de reportes y descargas."""

from __future__ import annotations

import pandas as pd
import streamlit as st

from src.app.components import ethics_notice, page_header


def render(claims: pd.DataFrame) -> None:
    page_header(
        "Reportes",
        "Exportación de bandejas y resumen ejecutivo para revisión humana.",
    )
    ethics_notice()

    critical = claims[claims["nivel_riesgo"] == "Rojo"].sort_values("score_final", ascending=False)
    st.download_button(
        "Descargar casos rojos CSV",
        critical.to_csv(index=False).encode("utf-8"),
        file_name="casos_rojos_demo.csv",
        mime="text/csv",
        use_container_width=True,
    )
    st.download_button(
        "Descargar todos los scores CSV",
        claims.to_csv(index=False).encode("utf-8"),
        file_name="scores_demo.csv",
        mime="text/csv",
        use_container_width=True,
    )

    st.markdown("### Resumen ejecutivo")
    st.write(
        f"""
        La bandeja demo contiene {len(claims)} siniestros. Los casos rojos deben ser revisados
        primero por concentración de señales. La salida del sistema es una alerta operativa,
        no una conclusión legal ni una decisión automática.
        """
    )
