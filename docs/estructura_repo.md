# Estructura del Repositorio

Este documento describe la arquitectura de archivos de FraudLens Claims AI. La estructura esta preparada para demo local, desarrollo modular y crecimiento controlado sin microservicios.

## Arbol principal

```txt
Detector-Fraudes/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup_demo.py
├── data/
│   ├── synthetic/
│   └── processed/
├── docs/
├── notebooks/
├── presentation/
├── scripts/
├── src/
│   ├── app/
│   │   └── pages/
│   ├── data_generation/
│   ├── database/
│   ├── features/
│   ├── rules/
│   ├── models/
│   ├── nlp/
│   ├── scoring/
│   ├── explainability/
│   ├── agent/
│   ├── mcp_server/
│   ├── reports/
│   └── utils/
└── tests/
```

## Responsabilidad por carpeta

| Ruta | Responsabilidad |
|---|---|
| `data/synthetic/` | CSV sinteticos generados para la demo. |
| `data/processed/` | Salidas procesadas: scores, metricas, reportes CSV y modelos. |
| `src/app/` | Dashboard Streamlit y paginas visuales. |
| `src/data_generation/` | Generacion reproducible de datos sinteticos. |
| `src/database/` | Construccion de MySQL y consultas controladas. |
| `src/features/` | Variables derivadas para reglas, ML y dashboard. |
| `src/rules/` | Reglas explicables de senales de posible riesgo. |
| `src/models/` | Clasificacion supervisada y anomalias. |
| `src/nlp/` | Similitud de narrativas con TF-IDF y cosine similarity. |
| `src/scoring/` | Integracion del score final y niveles Verde/Amarillo/Rojo. |
| `src/explainability/` | Explicaciones humanas y trazabilidad. |
| `src/agent/` | Tools y router local del agente consultivo. |
| `src/mcp_server/` | MCP opcional como diferenciador. |
| `src/reports/` | Exportaciones y resumenes de demo. |
| `tests/` | Pruebas basicas de estructura y modulos criticos. |
| `docs/` | Arquitectura, bitacora, tareas, etica, limites y demo. |
| `presentation/` | Material de pitch. |

## Reglas de arquitectura

- La UI no calcula reglas ni entrena modelos.
- El score vive en `src/scoring/`.
- Las reglas viven en `src/rules/`.
- El agente usa tools controladas en `src/agent/`.
- MCP envuelve tools existentes y sigue siendo opcional.
- MySQL es la base local principal de demo.
- CSV procesados son el contrato de lectura para Streamlit.
- Los datos reales y credenciales estan prohibidos.
- Toda salida habla de alertas para revision humana, no de fraude confirmado.

## Estado actual

La arquitectura de archivos ya soporta el MVP completo de hackathon: generacion de datos sinteticos, carga MySQL, features, reglas, ML/NLP, scoring, explicabilidad, dashboard Streamlit, agente local, MCP opcional, reportes y pruebas basicas.
