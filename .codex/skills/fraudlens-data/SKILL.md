---
name: fraudlens-data
description: Ingeniería de datos sintéticos para FraudLens Claims AI. Usar cuando Codex deba generar, validar, cargar o documentar claims, policies, insured, vehicles, providers, documents, SQLite, CSV sintéticos, features base o dataset reproducible sin datos reales.
---

# FraudLens Data

## Contexto obligatorio

Leer antes de editar:

- `docs/arquitectura.md`
- `docs/development.md`

## Recursos del skill

- Leer `references/operating_rules.md` antes de generar o modificar datos.
- Ejecutar `scripts/check_context.ps1` si hay duda de contexto.

## Archivos objetivo

- `src/data_generation/generate_synthetic_data.py`
- `src/database/build_database.py`
- `src/database/queries.py`
- `src/features/build_features.py`
- `data/synthetic/`
- `data/processed/`

## Reglas

- Usar solo datos sintéticos.
- Usar IDs anónimos.
- Mantener semilla reproducible.
- Incluir patrones normales y de posible riesgo.
- Cubrir claims, policies, insured, vehicles, providers, documents y risk_scores.
- Actualizar `docs/development.md` con tipo `datos` o `backend`, seguridad y progreso.

## Patrones a inyectar

- Borde de vigencia.
- Reporte tardío.
- Montos atípicos.
- Proveedores recurrentes.
- Documentos incompletos o inconsistentes.
- Narrativas similares.
- Tercero no identificado.
- Robo con denuncia tardía.

## No hacer

- No usar nombres, teléfonos, correos, documentos o placas reales.
- No descargar datos sensibles.
- No depender de bases externas.

## Terminado

Los CSV sintéticos y SQLite se pueden reconstruir desde cero y soportan reglas, ML, NLP, dashboard y agente.
