---
name: fraudlens-architect
description: Arquitectura técnica y organización de repositorio para FraudLens Claims AI. Usar cuando Codex deba crear, revisar o modificar estructura del proyecto, README, requirements, .env.example, documentación técnica, decisiones de stack, alcance MVP o planificación del hackathon usando Streamlit, Python 3.11, CSV sintéticos, SQLite, Pandas, Plotly, Scikit-learn, TF-IDF, agente local y MCP opcional.
---

# FraudLens Architect

## Contexto obligatorio

Antes de editar, leer:

- `docs/arquitectura.md`
- `docs/development.md`
- `FraudLens_Claims_AI_Plan_HackIAthon.md` solo si falta detalle.
- `Proyecto.md` solo si falta detalle del reto.

## Recursos del skill

- Leer `references/operating_rules.md` para reglas operativas de este rol.
- Ejecutar `scripts/check_context.ps1` si hay duda de que la sesion este en el repo correcto.

## Flujo

1. Confirmar que el cambio respeta el stack definido.
2. Mantener arquitectura liviana de hackathon.
3. Separar datos, reglas, scoring, ML/NLP, explicación, agente y UI.
4. Documentar decisiones relevantes en `docs/development.md`.
5. Informar tarea completada, tarea pendiente y porcentaje de progreso.

## Permitido

- Crear estructura de repo.
- Crear documentación Markdown.
- Crear archivos de configuración del proyecto.
- Ajustar `requirements.txt` solo con dependencias aprobadas.

## Prohibido

- No introducir React, login, roles, microservicios, Docker obligatorio, MySQL/Oracle real ni FastAPI obligatorio.
- No usar datos reales ni credenciales.
- No implementar lógica de negocio si el usuario pidió solo arquitectura.

## Criterio de terminado

El repo queda más claro, reproducible y alineado con el MVP: Streamlit + Python + CSV/SQLite + reglas + ML/NLP + agente local.
