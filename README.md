# FraudLens Claims AI

Sistema de apoyo para analistas de siniestros que prioriza casos con señales de posible riesgo usando reglas explicables, datos sintéticos, ML/NLP y un agente consultivo.

## Principio ético

FraudLens Claims AI no acusa fraude, no rechaza siniestros y no toma decisiones automáticas. Solo genera alertas para revisión humana.

## Stack

- Python 3.11
- Streamlit
- Pandas, NumPy
- Plotly
- SQLite + CSV sintéticos
- Scikit-learn
- TF-IDF + cosine similarity
- Agent router local
- MCP opcional
- pytest básico

## Estructura

```txt
data/                 Datos sintéticos y procesados
docs/                 Documentación técnica y bitácoras
src/app/              Dashboard Streamlit
src/data_generation/  Generación de datos sintéticos
src/database/         SQLite y consultas
src/features/         Variables de riesgo
src/rules/            Reglas explicables
src/models/           ML supervisado y anomalías
src/nlp/              Similitud de narrativas
src/scoring/          Score final
src/explainability/   Explicaciones humanas
src/agent/            Agente local
src/mcp_server/       MCP opcional
src/reports/          Reportes
tests/                Pruebas básicas
presentation/         Pitch y demo
```

## Estado

Arquitectura de archivos creada. La lógica de negocio aún no está implementada.

## Comandos previstos

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python setup_demo.py
streamlit run src/app/main.py
pytest
```
