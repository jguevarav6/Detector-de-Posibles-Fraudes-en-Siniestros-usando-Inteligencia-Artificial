---
name: fraudlens-ethics
description: Explicabilidad, privacidad y ética para FraudLens Claims AI. Usar cuando Codex deba redactar o revisar explicaciones de score, mensajes de interfaz, documentación de sesgos, falsos positivos, privacidad, no acusación, revisión humana o límites del sistema antifraude.
---

# FraudLens Ethics

## Contexto obligatorio

Leer antes de editar:

- `docs/arquitectura.md`
- `docs/development.md`

## Recursos del skill

- Leer `references/operating_rules.md` antes de revisar textos, privacidad o explicabilidad.
- Ejecutar `scripts/check_context.ps1` si hay duda de contexto.

## Archivos objetivo

- `src/explainability/explain_score.py`
- `docs/etica_privacidad.md`
- `docs/limitaciones.md`
- `README.md`
- Textos visibles de Streamlit.

## Reglas de lenguaje

Usar:

- “posible riesgo”
- “alerta”
- “prioridad de revisión”
- “revisión humana”
- “señales anómalas”

Evitar:

- “fraude confirmado”
- “cliente fraudulento”
- “rechazar automáticamente”
- “culpable”

## Reglas técnicas

- No usar datos reales.
- No incluir credenciales.
- Mantener trazabilidad entre score y señales.
- Documentar falsos positivos y límites de datos sintéticos.
- Actualizar `docs/development.md` con tipo `seguridad`, `documentacion` o `frontend`, y progreso.

## Terminado

La app y docs dejan claro que FraudLens prioriza revisión humana y no acusa ni decide automáticamente.
