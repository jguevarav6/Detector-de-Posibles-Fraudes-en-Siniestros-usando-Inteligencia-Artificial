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
        return tools.explain_claim(df, claim_id)

    matched = _match_intent(normalized)
    if matched is None:
        return _guidance_message(question=raw)

    dispatch = {
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
