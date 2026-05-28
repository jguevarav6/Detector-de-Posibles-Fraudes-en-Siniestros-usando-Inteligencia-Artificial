---
name: fraudlens-streamlit
description: Desarrollo del dashboard Streamlit de FraudLens Claims AI. Usar cuando Codex deba crear o modificar pantallas, componentes, navegacion, KPIs, bandeja de siniestros, detalle de caso, vista de proveedores, agente en UI, reportes, Plotly o estilos de la app Streamlit respetando el alcance etico del reto.
---

# FraudLens Streamlit

## Contexto obligatorio

Leer antes de editar:

- `docs/arquitectura.md`
- `docs/development.md`

## Recursos del skill

- Leer `references/operating_rules.md` para reglas operativas de frontend.
- Ejecutar `scripts/check_context.ps1` si hay duda de contexto.

## Archivos objetivo

- `src/app/main.py`
- `src/app/components.py`
- `src/app/styles.py`
- `src/app/pages/dashboard.py`
- `src/app/pages/claims_inbox.py`
- `src/app/pages/claim_detail.py`
- `src/app/pages/providers.py`
- `src/app/pages/agent_chat.py`
- `src/app/pages/reports.py`

## Reglas

- Streamlit es el frontend definitivo.
- Usar Plotly para graficos.
- Consumir datos procesados; no concentrar scoring en la UI.
- Mostrar siempre que el sistema genera alertas para revision humana.
- Usar niveles Verde, Amarillo y Rojo como prioridad de revision.
- Actualizar `docs/development.md` con tipo `frontend`, seguridad y progreso.

## No hacer

- No crear React ni API obligatoria.
- No pedir login ni credenciales.
- No escribir "fraude confirmado" o "rechazar siniestro".

## Terminado

La app abre con `streamlit run src/app/main.py`, muestra KPIs, bandeja, detalle, proveedores, agente y reportes con datos procesados.
