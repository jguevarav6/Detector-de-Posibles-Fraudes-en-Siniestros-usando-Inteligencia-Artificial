---
name: fraudlens-qa
description: QA, pruebas y revision final de FraudLens Claims AI. Usar cuando Codex deba crear o ejecutar pytest basico, revisar reproducibilidad, validar estructura, detectar credenciales, revisar documentacion, verificar comandos de demo o preparar checklist final del hackathon.
---

# FraudLens QA

## Contexto obligatorio

Leer antes de editar:

- `docs/arquitectura.md`
- `docs/development.md`

## Recursos del skill

- Leer `references/operating_rules.md` antes de revisar o probar.
- Ejecutar `scripts/check_context.ps1` si hay duda de contexto.

## Archivos objetivo

- `tests/`
- `README.md`
- `requirements.txt`
- `.env.example`
- `.gitignore`
- `docs/development.md`

## Reglas

- Priorizar pruebas minimas de alto valor.
- Validar generacion/carga de datos, reglas, scoring y agente.
- Revisar que no existan credenciales ni datos reales.
- Registrar bugs y pendientes en `docs/development.md`.
- Actualizar `docs/development.md` con tipo `qa`, seguridad y progreso.

## Comandos esperados

```bash
python setup_demo.py
streamlit run src/app/main.py
pytest
```

## No hacer

- No exigir cobertura de produccion.
- No agregar tooling pesado.
- No cambiar logica sin entender arquitectura y score.

## Terminado

La demo ejecuta, las pruebas basicas pasan o quedan fallos documentados, y el checklist final esta actualizado.
