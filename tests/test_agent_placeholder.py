"""Pruebas de agente consultivo local."""

import pandas as pd

from src.agent.agent_router import answer_question


def test_agent_answers_top_risk_from_dataframe() -> None:
    claims = pd.DataFrame(
        [
            {
                "id_siniestro": "SIN-00001",
                "score_final": 90,
                "nivel_riesgo": "Rojo",
                "proveedor": "PRO-1",
                "ciudad": "Quito",
                "ramo": "Vehiculos",
                "documentos": "1 faltantes",
                "monto_reclamado": 1000,
                "dias_desde_inicio_poliza": 2,
                "similar_claim_id": "",
                "max_similarity": 0,
                "explicacion": "Caso con senales para revision humana.",
                "reglas_activadas": "R001",
            }
        ]
    )

    answer = answer_question("Top 10 siniestros de mayor riesgo", claims)

    assert "SIN-00001" in answer
    assert "revision" in answer.lower()
