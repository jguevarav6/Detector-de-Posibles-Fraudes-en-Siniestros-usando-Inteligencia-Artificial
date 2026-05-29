"""Router local de intenciones para el agente consultivo.

El router clasifica preguntas en lenguaje natural a tools controladas sobre
`scored_claims.csv`. No usa LLM externo, no recalcula scores y no acusa fraude.
"""

from __future__ import annotations

import re

import pandas as pd

from src.agent import agent_tools as tools


# Diccionario de intenciones con sinonimos en espanol/ingles para clasificar
# preguntas libres del usuario sin depender de palabras exactas.
INTENT_KEYWORDS: dict[str, tuple[str, ...]] = {
    "help_what_is_watchlist": ("que es watchlist", "que es la watchlist", "que es watchlsit", "que es un watchlist", "para que sirve la watchlist", "que es compliance"),
    "help_how_it_works":      ("como funciona", "como trabaja", "que hace el sistema", "que hace fraudlens", "como esta hecho", "explicame el sistema", "como funciona esto"),
    "watchlist_summary": ("watchlist", "compliance", "lista restrictiva", "lista negra", "observados", "antecedentes", "cuantos cruzan", "cruce"),
    "pareto_providers":  ("80", "ochenta", "pareto", "concentran", "concentracion 80"),
    "explain":          ("por que", "por qué", "porque", "explica", "explicar", "explicacion", "explicación", "detalle", "razon", "razón", "motivo"),
    "provider":         ("proveedor", "taller", "clinica", "clínica", "perito", "peritaje", "centro medico", "centro médico"),
    "city":             ("ciudad", "ciudades", "sucursal", "guayaquil", "quito", "cuenca", "manta", "loja"),
    "branch":           ("ramo", "ramos", "cobertura", "coberturas", "linea", "línea"),
    "insured":          ("asegurado", "asegurados", "cliente", "clientes", "frecuencia", "recurrente"),
    "documents":        ("document", "documental", "papeles", "factura", "denuncia"),
    "amount":           ("monto", "montos", "valor", "atipico", "atípico", "atipicos", "atípicos", "alto", "elevado"),
    "policy_start":     ("inicio", "vigencia", "borde", "poliza", "póliza", "recien", "recién"),
    "narrative":        ("narrativa", "narrativas", "similar", "similares", "patron", "patrón", "patrones", "texto", "descripcion", "descripción"),
    "summary":          ("resumen", "ejecutivo", "panorama", "estado general", "overview", "sintesis", "síntesis"),
    "recommend":        ("recomienda", "recomendacion", "recomendación", "revisar primero", "priorizar", "primero", "urgente"),
    "top":              ("top", "mayor riesgo", "mas riesgo", "más riesgo", "criticos", "críticos", "rojos", "ranking"),
}


GREETINGS = ("hola", "buenas", "buenos dias", "buenos días", "buen dia", "buen día", "saludos", "hey", "hi", "hello")


def answer_question(question: str, claims: pd.DataFrame | None = None) -> str:
    """Responde preguntas operativas con tools controladas.

    El router primero busca un id de siniestro explicito. Si no hay, intenta
    clasificar la intencion por palabras clave. Si la pregunta no encaja en
    ninguna intencion, devuelve un mensaje guia con las opciones disponibles
    en lugar del fallback silencioso de top riesgos.
    """
    df = claims if claims is not None else tools.load_scored_claims()
    if df.empty:
        return "No hay datos procesados. Ejecuta primero `python setup_demo.py`."

    raw = (question or "").strip()
    if not raw:
        return _guidance_message()

    normalized = raw.lower()

    if any(g == normalized or normalized.startswith(g + " ") for g in GREETINGS):
        return (
            "Hola. Soy el agente consultivo de FraudLens. Puedo responder sobre "
            "top de riesgos, proveedores, ciudades, ramos, asegurados frecuentes, "
            "documentos faltantes, montos atipicos, casos cerca del inicio de poliza, "
            "narrativas similares y resumen ejecutivo. Tambien puedo explicar un caso "
            "especifico si me das el ID (ejemplo: SIN-00012)."
        )

    claim_id = _extract_claim_id(raw)
    if claim_id:
        # Si la pregunta menciona compliance/watchlist, usar cross_reference
        if any(k in normalized for k in ("watchlist", "compliance", "cruz", "antecedente")):
            return _format_cross_reference(tools.cross_reference_claim(claim_id))
        return tools.explain_claim(df, claim_id)

    matched = _match_intent(normalized)
    if matched is None:
        return _guidance_message(question=raw)

    dispatch = {
        "help_what_is_watchlist": lambda: _meta_what_is_watchlist(),
        "help_how_it_works":      lambda: _meta_how_it_works(),
        "watchlist_summary": lambda: _format_watchlist_summary(tools.watchlist_summary()),
        "pareto_providers":  lambda: _format_pareto(tools.pareto_red_providers(0.8)),
        "explain":      lambda: tools.explain_claim(df, None),
        "provider":     lambda: tools.provider_alert_summary(df),
        "city":         lambda: tools.city_risk_summary(df),
        "branch":       lambda: tools.branch_risk_summary(df),
        "insured":      lambda: tools.frequent_insured_summary(df),
        "documents":    lambda: tools.missing_documents_summary(df),
        "amount":       lambda: tools.atypical_amounts(df),
        "policy_start": lambda: tools.near_policy_start(df),
        "narrative":    lambda: tools.similar_narratives(df),
        "summary":      lambda: tools.executive_summary(df),
        "recommend":    lambda: tools.top_risk_claims(df, limit=5),
        "top":          lambda: tools.top_risk_claims(df),
    }
    return dispatch[matched]()


def _format_watchlist_summary(data: dict) -> str:
    if "error" in data:
        return "No hay datos suficientes para cruzar con la watchlist."
    return (
        f"Cruce operacional vs watchlist: {data['claims_con_alerta_compliance']} de "
        f"{data['claims_total']} siniestros cruzan con compliance; "
        f"{data['claims_rojos_con_alerta']} son rojos. "
        f"Watchlist activa: {data['watchlist_proveedores']} proveedores observados, "
        f"{data['watchlist_asegurados']} asegurados con antecedentes y "
        f"{data['watchlist_vehiculos']} vehiculos marcados."
    )


def _format_pareto(data: dict) -> str:
    if "error" in data:
        return "No hay alertas rojas suficientes para calcular concentracion."
    nombres = ", ".join(f"{p['proveedor']} ({p['rojos']} rojos)" for p in data["proveedores"][:8])
    return (
        f"El {data['porcentaje_cubierto']:.0%} de las {data['rojos_totales']} alertas rojas "
        f"se concentra en {data['n_proveedores']} proveedores: {nombres}."
    )


def _meta_what_is_watchlist() -> str:
    return (
        "Una **watchlist** es una lista interna de compliance. Toda aseguradora real "
        "mantiene dos bases separadas:\n\n"
        "1. **Base operacional** (`fraudlens_claims_ai`): los siniestros que entran "
        "cada dia, con sus polizas, asegurados, vehiculos y proveedores.\n"
        "2. **Base watchlist** (`fraudlens_watchlist`): proveedores, asegurados y "
        "vehiculos que ya tuvieron problemas antes, marcados por auditoria o por "
        "casos previos.\n\n"
        "Cuando llega un siniestro nuevo, FraudLens lo cruza automaticamente contra "
        "la watchlist. Si el proveedor o asegurado ya esta marcado, sube la prioridad "
        "de revision. En el demo actual hay 60 proveedores observados, 35 asegurados "
        "con antecedentes, 22 vehiculos marcados y 12 patrones narrativos recurrentes. "
        "Puedes ver los cruces en la pagina **Watchlist (DB2)** del menu."
    )


def _meta_how_it_works() -> str:
    return (
        "FraudLens analiza siniestros en cuatro capas y combina los resultados en un "
        "score final de 0 a 100:\n\n"
        "- **Reglas (55%)**: 13 reglas explicables como borde de vigencia, reporte "
        "tardio, monto atipico, documentos incompletos o proveedor recurrente.\n"
        "- **Machine Learning (25%)**: RandomForest entrenado sobre features tabulares "
        "(LogisticRegression como fallback).\n"
        "- **Anomalia (10%)**: IsolationForest detecta casos atipicos sin etiqueta.\n"
        "- **NLP (10%)**: TF-IDF + cosine similarity para detectar narrativas similares.\n\n"
        "El resultado se clasifica en Verde (<41), Amarillo (41-75) y Rojo (76+). "
        "El sistema **no decide pagos ni acusa fraude**: solo prioriza casos para "
        "revision humana. Ademas el **MCP** consulta dos bases MySQL en paralelo "
        "(operacional y watchlist) para responder preguntas que cruzan ambos sistemas."
    )


def _format_cross_reference(data: dict) -> str:
    if data.get("error"):
        return f"No encuentro el siniestro {data.get('id_siniestro', '')} en la base operacional."
    hits = data.get("watchlist_hits", [])
    if not hits:
        return f"{data['id_siniestro']} no cruza con la watchlist de compliance."
    lineas = [f"{data['id_siniestro']} ({data['nivel_riesgo']}, score {data['score_final']:.0f}) cruza con compliance:"]
    for hit in hits:
        if hit["tipo"] == "proveedor":
            lineas.append(f"  - Proveedor {hit.get('id_proveedor')} {hit.get('nivel_alerta')}: {hit.get('motivo')}.")
        elif hit["tipo"] == "asegurado":
            lineas.append(f"  - Asegurado {hit.get('id_asegurado')} con antecedente {hit.get('tipo_antecedente')}: {hit.get('motivo')}.")
        elif hit["tipo"] == "vehiculo":
            lineas.append(f"  - Vehiculo {hit.get('id_vehiculo')} marcado: {hit.get('motivo')}.")
    return "\n".join(lineas)


def _match_intent(normalized: str) -> str | None:
    """Devuelve la intencion con mas coincidencias de keywords, o None."""
    scores: dict[str, int] = {}
    for intent, keywords in INTENT_KEYWORDS.items():
        hits = sum(1 for kw in keywords if kw in normalized)
        if hits:
            scores[intent] = hits
    if not scores:
        return None
    return max(scores, key=scores.get)


def _guidance_message(question: str | None = None) -> str:
    quoted = f' "{question}"' if question else ""
    return (
        f"No identifique una consulta operativa clara{quoted}. Algunas opciones:\n\n"
        "- Top de mayor riesgo: \"cuales son los siniestros mas criticos\"\n"
        "- Proveedores: \"que proveedores concentran alertas\"\n"
        "- Ciudades: \"que ciudades tienen mas casos rojos\"\n"
        "- Ramos: \"que ramos tienen mas riesgo\"\n"
        "- Asegurados frecuentes: \"asegurados con mas siniestros\"\n"
        "- Documentos: \"casos con documentos faltantes\"\n"
        "- Montos atipicos: \"siniestros con monto elevado\"\n"
        "- Inicio de poliza: \"casos cerca del inicio de la poliza\"\n"
        "- Narrativas: \"casos con narrativa similar\"\n"
        "- Resumen ejecutivo: \"dame el resumen\"\n"
        "- Explicar un caso especifico: escribe el ID, por ejemplo \"SIN-00012\"."
    )


def _extract_claim_id(text: str) -> str | None:
    match = re.search(r"SIN-\d{3,6}", text.upper())
    return match.group(0) if match else None
