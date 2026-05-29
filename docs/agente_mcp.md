# Agente Local y MCP

## Estado actual

El MVP implementa agente local con tools controladas.

Archivos:

- `src/agent/agent_tools.py`.
- `src/agent/agent_router.py`.
- `src/app/pages/agent_chat.py`.

La interfaz Streamlit usa `answer_question()` para responder preguntas sobre `data/processed/scored_claims.csv`.

## Preguntas soportadas

- Top 10 siniestros con mayor riesgo.
- Explicacion de un siniestro por ID.
- Proveedores con mas alertas.
- Ramos con mayor prioridad.
- Ciudades con mayor concentracion.
- Documentos faltantes en casos criticos.
- Montos atipicos.
- Siniestros cerca del inicio de poliza.
- Narrativas similares.
- Resumen ejecutivo.
- Casos que el analista deberia revisar primero.

## Control de seguridad

El agente:

- No recalcula el score.
- No modifica datos.
- No ejecuta SQL libre.
- No toma decisiones de pago.
- No confirma fraude.
- Responde con datos concretos de la bandeja procesada.

## MCP opcional

MCP queda como diferenciador futuro para exponer las mismas tools de forma estandarizada.

Tools candidatas:

- `get_top_risk_claims(limit)`.
- `explain_claim_risk(id_siniestro)`.
- `get_provider_alert_summary()`.
- `get_city_risk_summary()`.
- `get_missing_documents_critical()`.
- `get_similar_narratives(id_siniestro)`.
- `generate_executive_summary()`.

## Decision de MVP

El agente local ya cumple el reto porque responde preguntas clave con funciones controladas. MCP no bloquea la demo ni la presentacion.
