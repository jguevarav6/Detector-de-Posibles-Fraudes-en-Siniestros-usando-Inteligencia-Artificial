"""Servidor MCP opcional para exponer tools controladas de FraudLens."""

from __future__ import annotations

from src.agent import agent_tools


try:
    from mcp.server.fastmcp import FastMCP
except ImportError:  # pragma: no cover - depende de instalacion opcional
    FastMCP = None


def get_top_risk_claims(limit: int = 10) -> list[dict]:
    return agent_tools.top_risk_claims_json(limit=limit)


def explain_claim_risk(id_siniestro: str) -> dict:
    return agent_tools.explain_claim_json(id_siniestro)


def get_provider_alert_summary(limit: int = 10) -> list[dict]:
    return agent_tools.provider_alert_summary_json(limit=limit)


def get_city_risk_summary(limit: int = 10) -> list[dict]:
    return agent_tools.city_risk_summary_json(limit=limit)


def get_missing_documents_critical(limit: int = 10) -> list[dict]:
    return agent_tools.missing_documents_critical_json(limit=limit)


def get_similar_narratives(id_siniestro: str | None = None, limit: int = 10) -> list[dict]:
    return agent_tools.similar_narratives_json(id_siniestro=id_siniestro, limit=limit)


def generate_executive_summary() -> dict:
    return agent_tools.executive_summary_json()


# Tools que cruzan DB operacional con DB de compliance (watchlist).
def check_watchlist(id_siniestro: str) -> str:
    return agent_tools.check_watchlist(id_siniestro)


def cross_reference_claim(id_siniestro: str) -> dict:
    return agent_tools.cross_reference_claim(id_siniestro)


def get_watchlist_summary() -> dict:
    return agent_tools.watchlist_summary()


def pareto_red_providers(coverage: float = 0.8) -> dict:
    return agent_tools.pareto_red_providers(coverage=coverage)


def simulate_claim_score(
    monto_reclamado: float,
    suma_asegurada: float,
    dias_desde_inicio_poliza: int,
    dias_entre_ocurrencia_reporte: int,
    documentos_completos: bool = True,
    ramo: str = "Vehiculos",
) -> dict:
    return agent_tools.simulate_claim_score(
        monto_reclamado=monto_reclamado,
        suma_asegurada=suma_asegurada,
        dias_desde_inicio_poliza=dias_desde_inicio_poliza,
        dias_entre_ocurrencia_reporte=dias_entre_ocurrencia_reporte,
        documentos_completos=documentos_completos,
        ramo=ramo,
    )


MCP_TOOLS_REGISTRY = [
    ("get_top_risk_claims",          "claims_ai",        "Top siniestros por score final."),
    ("explain_claim_risk",           "claims_ai",        "Explicacion humana de un siniestro."),
    ("get_provider_alert_summary",   "claims_ai",        "Ranking de proveedores con mas alertas."),
    ("get_city_risk_summary",        "claims_ai",        "Concentracion de riesgo por ciudad."),
    ("get_missing_documents_critical","claims_ai",       "Casos rojos con documentos faltantes."),
    ("get_similar_narratives",       "claims_ai",        "Narrativas similares por TF-IDF + cosine."),
    ("generate_executive_summary",   "claims_ai",        "Resumen ejecutivo del dataset."),
    ("check_watchlist",              "claims_ai+watchlist","Verifica si un siniestro cruza con compliance."),
    ("cross_reference_claim",        "claims_ai+watchlist","Expediente cruzado claim + watchlist."),
    ("get_watchlist_summary",        "claims_ai+watchlist","Cruces totales operacional vs watchlist."),
    ("pareto_red_providers",         "claims_ai",        "Proveedores que concentran el 80% de rojos."),
    ("simulate_claim_score",         "stateless",        "Aplica reglas a un siniestro hipotetico."),
]


def create_mcp_server():
    """Crea servidor FastMCP si el SDK esta instalado."""
    if FastMCP is None:
        raise RuntimeError("Instala mcp para ejecutar el servidor MCP opcional.")
    server = FastMCP("fraudlens-claims-ai")
    server.tool()(get_top_risk_claims)
    server.tool()(explain_claim_risk)
    server.tool()(get_provider_alert_summary)
    server.tool()(get_city_risk_summary)
    server.tool()(get_missing_documents_critical)
    server.tool()(get_similar_narratives)
    server.tool()(generate_executive_summary)
    server.tool()(check_watchlist)
    server.tool()(cross_reference_claim)
    server.tool()(get_watchlist_summary)
    server.tool()(pareto_red_providers)
    server.tool()(simulate_claim_score)
    return server


if __name__ == "__main__":
    create_mcp_server().run()
