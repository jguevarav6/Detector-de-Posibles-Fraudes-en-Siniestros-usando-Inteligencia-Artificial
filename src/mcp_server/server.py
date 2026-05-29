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
    return server


if __name__ == "__main__":
    create_mcp_server().run()
