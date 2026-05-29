"""Demo interactiva del servidor MCP de FraudLens.

Ejecuta las 7 tools controladas y muestra el JSON que devolveria a un cliente
MCP externo (Claude Desktop, Cursor, IDEs compatibles). Sirve para presentar
el MCP en la demo sin necesidad de configurar un cliente real.

Uso:
    python scripts/demo_mcp.py
    python scripts/demo_mcp.py --tool top --limit 5
    python scripts/demo_mcp.py --tool explain --id SIN-00012
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.mcp_server import server  # noqa: E402


TOOLS = {
    "top":          ("get_top_risk_claims",          lambda a: server.get_top_risk_claims(limit=a.limit)),
    "explain":      ("explain_claim_risk",           lambda a: server.explain_claim_risk(id_siniestro=a.id)),
    "providers":    ("get_provider_alert_summary",   lambda a: server.get_provider_alert_summary(limit=a.limit)),
    "cities":       ("get_city_risk_summary",        lambda a: server.get_city_risk_summary(limit=a.limit)),
    "documents":    ("get_missing_documents_critical", lambda a: server.get_missing_documents_critical(limit=a.limit)),
    "narratives":   ("get_similar_narratives",       lambda a: server.get_similar_narratives(id_siniestro=a.id, limit=a.limit)),
    "summary":      ("generate_executive_summary",   lambda a: server.generate_executive_summary()),
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Demo del MCP de FraudLens")
    parser.add_argument(
        "--tool",
        choices=list(TOOLS.keys()) + ["all"],
        default="all",
        help="Tool MCP a invocar (default: all)",
    )
    parser.add_argument("--id", default=None, help="ID de siniestro para explain / narratives")
    parser.add_argument("--limit", type=int, default=5, help="Limite de resultados (default: 5)")
    args = parser.parse_args()

    selected = list(TOOLS.items()) if args.tool == "all" else [(args.tool, TOOLS[args.tool])]

    for key, (tool_name, fn) in selected:
        _print_header(key, tool_name)
        try:
            result = fn(args)
            print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
        except Exception as exc:  # pragma: no cover - demo defensiva
            print(f"ERROR ejecutando {tool_name}: {exc}")
        print()


def _print_header(key: str, tool_name: str) -> None:
    line = "=" * 72
    print(line)
    print(f"  MCP TOOL  ->  {tool_name}   [alias: {key}]")
    print(line)


if __name__ == "__main__":
    main()
