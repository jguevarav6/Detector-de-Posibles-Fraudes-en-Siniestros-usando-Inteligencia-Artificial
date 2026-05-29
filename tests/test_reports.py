"""Pruebas de reportes exportables."""

from pathlib import Path

import pandas as pd

from src.reports.export_reports import critical_cases, executive_summary, export_demo_reports, review_queue


def test_report_helpers_filter_and_export(tmp_path: Path) -> None:
    df = pd.DataFrame(
        [
            {"id_siniestro": "SIN-1", "nivel_riesgo": "Rojo", "score_final": 90, "monto_reclamado": 1000},
            {"id_siniestro": "SIN-2", "nivel_riesgo": "Amarillo", "score_final": 60, "monto_reclamado": 500},
            {"id_siniestro": "SIN-3", "nivel_riesgo": "Verde", "score_final": 20, "monto_reclamado": 100},
        ]
    )

    outputs = export_demo_reports(df, output_dir=tmp_path)

    assert len(critical_cases(df)) == 1
    assert len(review_queue(df)) == 2
    assert executive_summary(df)["casos_revisables"] == 2
    assert all(path.exists() for path in outputs.values())
