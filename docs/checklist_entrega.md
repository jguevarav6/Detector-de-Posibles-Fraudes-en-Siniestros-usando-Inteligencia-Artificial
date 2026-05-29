# Checklist de Entrega Final

## Estado

Progreso del MVP: 100%.

## Validacion tecnica

- [x] `python setup_demo.py` genera datos sinteticos, carga MySQL y produce scores.
- [x] MySQL contiene tablas principales y `risk_scores`.
- [x] `data/processed/scored_claims.csv` alimenta Streamlit.
- [x] `python -m pytest` pasa.
- [x] Streamlit responde en `http://localhost:8501`.
- [x] El agente local responde preguntas clave.
- [x] MCP opcional envuelve tools controladas.
- [x] Reportes CSV disponibles desde la app y `src/reports/export_reports.py`.

## Entregables

- [x] README.
- [x] Arquitectura.
- [x] Modelo de datos.
- [x] Reglas de negocio.
- [x] Uso de IA.
- [x] Etica y privacidad.
- [x] Limitaciones.
- [x] Script de demo.
- [x] Pitch ejecutivo en `presentation/pitch.md`.
- [x] Tablero de tareas actualizado.

## Seguridad y etica

- [x] Sin datos reales.
- [x] Sin `.env` real versionado.
- [x] Sin API keys.
- [x] Sin credenciales productivas.
- [x] Sin lenguaje de acusacion.
- [x] Revision humana obligatoria en UI y documentacion.

## Respaldo de demo

Si la demo en vivo falla:

1. Mostrar `presentation/pitch.md`.
2. Abrir `docs/demo_script.md`.
3. Mostrar `data/processed/scored_claims.csv`.
4. Ejecutar consulta del agente desde Streamlit o Python.
5. Mostrar capturas o grabacion si el equipo las genera antes de presentar.
