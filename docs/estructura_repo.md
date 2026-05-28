# Estructura del Repositorio

Este documento describe la arquitectura de archivos de FraudLens Claims AI. La estructura está preparada para desarrollo modular, demo local y crecimiento controlado sin microservicios.

## Árbol principal

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
| `data/synthetic/` | CSV sintéticos generados para la demo. |
| `data/processed/` | Salidas procesadas: scores, métricas, SQLite local y modelos. |
| `src/app/` | Dashboard Streamlit y páginas visuales. |
| `src/data_generation/` | Generación reproducible de datos sintéticos. |
| `src/database/` | Construcción de SQLite y consultas controladas. |
| `src/features/` | Variables derivadas para reglas, ML y dashboard. |
| `src/rules/` | Reglas explicables de señales de posible riesgo. |
| `src/models/` | Clasificación supervisada y anomalías opcionales. |
| `src/nlp/` | Similitud de narrativas con TF-IDF y cosine similarity. |
| `src/scoring/` | Integración del score final y niveles Verde/Amarillo/Rojo. |
| `src/explainability/` | Explicaciones humanas y trazabilidad. |
| `src/agent/` | Tools y router local del agente consultivo. |
| `src/mcp_server/` | MCP opcional como diferenciador. |
| `src/reports/` | Exportaciones y resúmenes de demo. |
| `src/utils/` | Configuración, rutas y validaciones compartidas. |
| `tests/` | Pruebas básicas de estructura y módulos críticos. |
| `docs/` | Arquitectura, bitácora, tareas, ética, límites y demo. |
| `presentation/` | Material de pitch. |
| `scripts/` | Scripts de soporte para Codex y operación local. |

## Reglas de arquitectura

- La UI no debe calcular reglas ni entrenar modelos.
- El score debe vivir en `src/scoring/`.
- Las reglas deben vivir en `src/rules/`.
- El agente debe usar tools controladas en `src/agent/`.
- MCP debe envolver tools existentes y seguir siendo opcional.
- Los datos reales y credenciales están prohibidos.
- Toda salida debe hablar de alertas para revisión humana, no de fraude confirmado.

## Estado actual

La arquitectura de archivos está creada con placeholders. La lógica de negocio, datos sintéticos, scoring, ML/NLP, dashboard funcional y agente se implementarán en fases posteriores.
