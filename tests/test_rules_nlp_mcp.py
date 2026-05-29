"""Pruebas de reglas, NLP y tools MCP opcionales."""

import pandas as pd

from src.agent import agent_tools
from src.mcp_server.server import explain_claim_risk, generate_executive_summary, get_top_risk_claims
from src.nlp.narrative_similarity import add_nlp_scores
from src.rules.fraud_rules import add_rule_scores


def test_rules_activate_on_high_risk_row() -> None:
    row = pd.DataFrame(
        [
            {
                "id_siniestro": "SIN-TEST",
                "dias_desde_inicio_poliza": 1,
                "dias_desde_fin_poliza": 360,
                "dias_entre_ocurrencia_reporte": 12,
                "cobertura": "Robo total",
                "historial_siniestros_asegurado": 4,
                "asegurado_reclamos_ultimos_12_meses": 4,
                "reclamos_vehiculo_18_meses": 3,
                "proveedor_reclamos_asociados": 70,
                "proveedor_porcentaje_casos_observados": 0.3,
                "documentos_completos": False,
                "documentos_faltantes": 1,
                "documentos_inconsistentes": 1,
                "documentos_ilegibles": 0,
                "hora_evento": 2,
                "tercero_identificado": False,
                "ramo": "Vehiculos",
                "score_nlp": 80,
                "max_similarity": 0.9,
                "monto_vs_suma_asegurada": 0.9,
                "proveedor_lista_restrictiva": True,
                "id_proveedor": "PRO-TEST",
            }
        ]
    )

    scored = add_rule_scores(row)

    assert scored.loc[0, "score_reglas"] == 100
    assert "R001_BORDE_VIGENCIA" in scored.loc[0, "reglas_activadas"]


def test_nlp_detects_similar_narratives() -> None:
    df = pd.DataFrame(
        [
            {"id_siniestro": "SIN-00001", "descripcion": "Robo ocurrido cerca del inicio de vigencia con denuncia tardia."},
            {"id_siniestro": "SIN-00002", "descripcion": "Robo ocurrido cerca del inicio de vigencia con denuncia tardia."},
            {"id_siniestro": "SIN-00003", "descripcion": "Reclamo normal con documentos completos."},
        ]
    )

    result = add_nlp_scores(df)

    assert result.loc[0, "score_nlp"] >= 65
    assert result.loc[0, "similar_claim_id"] == "SIN-00002"


def test_mcp_tool_functions_return_serializable_shapes(monkeypatch) -> None:
    claims = pd.DataFrame(
        [
            {
                "id_siniestro": "SIN-00001",
                "nivel_riesgo": "Rojo",
                "score_final": 91.0,
                "ciudad": "Quito",
                "ramo": "Vehiculos",
                "proveedor": "PRO-1",
                "monto_reclamado": 12000.0,
                "reglas_activadas": "R001_BORDE_VIGENCIA",
                "explicacion": "Caso para revision humana.",
                "accion_sugerida": "Priorizar revision documental",
            }
        ]
    )
    monkeypatch.setattr(agent_tools, "load_scored_claims", lambda: claims)

    top = get_top_risk_claims(limit=3)
    summary = generate_executive_summary()
    explanation = explain_claim_risk("SIN-00001")
    missing = explain_claim_risk("SIN-99999")

    assert top[0]["id_siniestro"] == "SIN-00001"
    assert summary["casos"] == 1
    assert explanation["score_final"] == 91.0
    assert missing["error"] == "siniestro_no_encontrado"
