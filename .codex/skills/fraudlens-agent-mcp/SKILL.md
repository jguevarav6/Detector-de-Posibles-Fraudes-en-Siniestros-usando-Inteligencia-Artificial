---
name: fraudlens-agent-mcp
description: Agente consultivo local y MCP opcional para FraudLens Claims AI. Usar cuando Codex deba crear o revisar agent_tools, agent_router, preguntas del agente, respuestas sobre siniestros, proveedores, documentos, narrativas, resumen ejecutivo o servidor MCP opcional con tools controladas.
---

# FraudLens Agent/MCP

## Contexto obligatorio

Leer antes de editar:

- `docs/arquitectura.md`
- `docs/development.md`

## Recursos del skill

- Leer `references/operating_rules.md` antes de tocar agente o MCP.
- Ejecutar `scripts/check_context.ps1` si hay duda de contexto.

## Archivos objetivo

- `src/agent/agent_tools.py`
- `src/agent/agent_router.py`
- `src/mcp_server/server.py`
- `docs/agente_mcp.md`

## Reglas

- Implementar primero agente local.
- Usar funciones/tools controladas sobre DataFrames o SQLite.
- MCP es opcional y no bloquea el MVP.
- Las respuestas deben citar datos concretos.
- El agente no recalcula ni inventa scores.
- Actualizar `docs/development.md` con tipo `agente`, seguridad y progreso.

## Preguntas mínimas

- Top 10 siniestros con mayor riesgo.
- Por qué un siniestro es rojo o amarillo.
- Proveedores con más alertas.
- Ramos y ciudades con mayor concentración.
- Asegurados con mayor frecuencia.
- Documentos faltantes en casos críticos.
- Montos atípicos.
- Siniestros cerca del inicio de póliza.
- Narrativas similares.
- Resumen ejecutivo.
- Casos que el analista debe revisar primero.

## No hacer

- No depender obligatoriamente de LLM externo.
- No hacer consultas libres sin control.
- No dar conclusiones legales.

## Terminado

El agente responde las preguntas del reto desde datos procesados; MCP, si existe, envuelve las mismas tools.
