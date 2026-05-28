# FraudLens Claims AI

Detector de señales de posible fraude en siniestros de seguros usando datos sintéticos, reglas explicables, score de riesgo, dashboard Streamlit y agente consultivo.

## Importante

FraudLens Claims AI no acusa fraude, no rechaza siniestros y no toma decisiones automáticas de pago. El sistema solo genera alertas de posible riesgo para revisión humana especializada.

## Contexto del reto

Proyecto desarrollado para el hackIAthon Ecuador, reto Aseguradora del Sur: Detector de Posibles Fraudes en Siniestros usando Inteligencia Artificial.

El reto solicita un prototipo funcional que analice información de siniestros, pólizas, asegurados, vehículos, proveedores y documentos para:

- identificar patrones anómalos;
- calcular un score de riesgo;
- clasificar casos en Verde, Amarillo y Rojo;
- explicar las señales detectadas;
- priorizar casos para revisión humana;
- permitir consultas mediante un agente consultivo.

## Objetivo

Apoyar al analista de siniestros con una bandeja priorizada de casos, explicaciones trazables y consultas operativas sobre patrones de riesgo. La solución está orientada a demo funcional de hackathon, no a producción.

## Alcance del MVP

Incluye:

- Datos sintéticos de siniestros, pólizas, asegurados, vehículos, proveedores y documentos.
- Persistencia local con CSV y SQLite.
- Reglas explicables de posible riesgo.
- Score final de riesgo.
- Dashboard Streamlit.
- Visualizaciones Plotly.
- Modelo ML con Scikit-learn.
- NLP con TF-IDF y cosine similarity.
- Agente local basado en funciones/tools.
- MCP opcional como diferenciador.
- Pruebas básicas con pytest.

No incluye:

- Datos personales reales.
- Credenciales o API keys.
- Acusación formal de fraude.
- Rechazo automático de siniestros.
- Login, roles o microservicios.
- Docker obligatorio.
- Base Oracle/MySQL real obligatoria.
- React o frontend separado.

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| Lenguaje | Python 3.11 |
| Dashboard | Streamlit |
| Datos | CSV sintéticos + SQLite |
| Procesamiento | Pandas, NumPy |
| Visualización | Plotly |
| ML | Scikit-learn |
| Modelo supervisado | RandomForestClassifier |
| Fallback ML | LogisticRegression |
| Anomalías | IsolationForest opcional |
| NLP | TF-IDF + cosine similarity |
| Agente | Router local basado en tools |
| MCP | Opcional |
| Testing | pytest |

## Estructura del repositorio

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

## Instalación

Requisito recomendado: Python 3.11.

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno en Windows:

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución prevista de la demo

Preparar datos, base local y salidas procesadas:

```bash
python setup_demo.py
```

Ejecutar dashboard:

```bash
streamlit run src/app/main.py
```

Ejecutar pruebas:

```bash
pytest
```

Nota: actualmente el repositorio tiene la arquitectura de archivos y placeholders. La lógica de datos, scoring, dashboard funcional y agente se implementará por fases.

## Score de riesgo

La fórmula definida para el MVP es:

```txt
score_final = 0.55 * score_reglas
            + 0.25 * score_ml
            + 0.10 * score_anomalia
            + 0.10 * score_nlp
```

Clasificación:

| Rango | Nivel | Uso |
|---:|---|---|
| 0-40 | Verde | Baja prioridad de revisión |
| 41-75 | Amarillo | Revisión priorizada |
| 76-100 | Rojo | Revisión urgente |

La clasificación expresa prioridad de revisión, no culpabilidad.

## Entregables del proyecto

- Prototipo funcional.
- Código fuente en GitHub.
- Dataset sintético.
- README con instalación y ejecución.
- Arquitectura técnica.
- Modelo de datos.
- Reglas de negocio.
- Explicación del uso de IA.
- Documentación de ética, privacidad y limitaciones.
- Dashboard y demo.
- Presentación ejecutiva.

## Documentación principal

- [Arquitectura](docs/arquitectura.md)
- [Estructura del repo](docs/estructura_repo.md)
- [Bitácora de desarrollo](docs/development.md)
- [Tareas por rol](docs/tareas.md)
- [Modelo de datos](docs/modelo_datos.md)
- [Reglas de negocio](docs/reglas_negocio.md)
- [Uso de IA](docs/uso_ia.md)
- [Ética y privacidad](docs/etica_privacidad.md)
- [Limitaciones](docs/limitaciones.md)
- [Demo script](docs/demo_script.md)

## Seguridad y privacidad

- Usar únicamente datos sintéticos.
- No versionar `.env`.
- No incluir credenciales.
- No incluir API keys.
- No usar información personal real.
- No usar lenguaje acusatorio.
- Mantener revisión humana obligatoria.

## Estado actual

Arquitectura base creada y publicada en `main`.

Siguiente fase: generación de datos sintéticos y preparación local de SQLite desde `setup_demo.py`.
