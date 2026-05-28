# Arquitectura - FraudLens Claims AI

## Resumen técnico

FraudLens Claims AI es un prototipo de apoyo para analistas de siniestros. Analiza datos sintéticos de reclamos, pólizas, asegurados, vehículos, proveedores y documentos para generar un score de posible riesgo, explicar señales relevantes y priorizar casos para revisión humana.

El sistema no acusa fraude, no rechaza siniestros y no toma decisiones automáticas de pago. Su salida es una alerta explicable para análisis especializado.

## Objetivo de la arquitectura

Construir una demo local, reproducible y defendible para hackathon, con foco en:

- Carga y generación de datos sintéticos.
- Cruce de información entre entidades de seguros.
- Score trazable combinando reglas, ML, anomalías y NLP.
- Dashboard Streamlit para análisis operativo.
- Agente consultivo local basado en funciones controladas.
- Documentación clara para jurado y desarrollo.

## Stack tecnológico definitivo

| Capa | Tecnología | Justificación |
|---|---|---|
| Lenguaje | Python 3.11 | Ecosistema maduro para datos, IA y prototipos rápidos. |
| Frontend/dashboard | Streamlit | Permite construir interfaz web de datos sin frontend separado. |
| Datos | CSV sintéticos + SQLite | Reproducible, sin servidor ni credenciales. |
| Procesamiento | Pandas, NumPy | Limpieza, cruces y cálculo de variables. |
| Visualización | Plotly | Gráficos interactivos para dashboard. |
| ML supervisado | Scikit-learn con RandomForestClassifier | Modelo robusto para datos tabulares sintéticos. |
| Fallback ML | LogisticRegression | Alternativa simple e interpretable si RandomForest falla. |
| Anomalías | IsolationForest opcional | Detección de casos atípicos sin etiqueta. |
| NLP | TF-IDF + cosine similarity | Detección simple y explicable de narrativas similares. |
| Agente | agent_router local | Consultas controladas sin depender de LLM externo. |
| MCP | Opcional | Diferenciador para exponer tools auditables, no requisito del MVP. |
| Testing | pytest básico | Validar reglas, scoring y carga de datos. |
| Deploy | Demo local, Streamlit Community Cloud como backup | Prioriza confiabilidad en presentación. |

## Diagrama textual

```txt
CSV sintéticos / SQLite
        |
        v
Carga y validación de datos
        |
        v
Features de riesgo
        |
        +--> Motor de reglas
        +--> Modelo ML supervisado
        +--> Detector de anomalías opcional
        +--> NLP de narrativas similares
        |
        v
Scoring service
        |
        +--> risk_scores
        +--> explicaciones
        |
        v
Streamlit Dashboard
        |
        +--> KPIs
        +--> bandeja priorizada
        +--> detalle de siniestro
        +--> proveedores
        +--> reportes
        +--> agente consultivo
```

## Flujo de datos

1. Generar o cargar CSV sintéticos.
2. Crear o actualizar SQLite local para la demo.
3. Unir claims, policies, insured, vehicles, providers y documents.
4. Calcular features: vigencia, demora de reporte, frecuencia, montos, documentos, proveedor, narrativa.
5. Aplicar reglas de negocio explicables.
6. Calcular score ML, score de anomalía y score NLP cuando estén disponibles.
7. Consolidar `score_final`, `nivel_riesgo` y explicación.
8. Guardar resultados en `risk_scores` y/o `data/processed/scored_claims.csv`.
9. Mostrar resultados en Streamlit.
10. Permitir consultas del agente sobre los datos procesados.

## Módulos principales

- `src/data_generation/`: generación de datos sintéticos.
- `src/database/`: creación de SQLite y consultas.
- `src/features/`: construcción de variables de riesgo.
- `src/rules/`: reglas explicables de posible riesgo.
- `src/models/`: entrenamiento y predicción ML.
- `src/nlp/`: similitud de narrativas.
- `src/scoring/`: combinación de scores.
- `src/explainability/`: explicación humana del resultado.
- `src/agent/`: tools y router local del agente.
- `src/mcp_server/`: servidor MCP opcional.
- `src/app/`: dashboard Streamlit.
- `tests/`: pruebas básicas.
- `docs/`: documentación técnica y de entrega.

## Estructura recomendada del repositorio

```txt
fraudlens-claims-ai/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup_demo.py
├── data/
│   ├── synthetic/
│   └── processed/
├── notebooks/
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
├── tests/
├── docs/
└── presentation/
```

## Modelo de datos resumido

### `claims`

Siniestros reportados. Campos clave: `id_siniestro`, `id_poliza`, `id_asegurado`, `id_vehiculo`, `id_proveedor`, `ramo`, `cobertura`, `fecha_ocurrencia`, `fecha_reporte`, `monto_reclamado`, `monto_estimado`, `monto_pagado`, `estado`, `sucursal`, `ciudad`, `descripcion`, `documentos_completos`, `dias_desde_inicio_poliza`, `dias_desde_fin_poliza`, `dias_entre_ocurrencia_reporte`, `historial_siniestros_asegurado`, `etiqueta_fraude_simulada`.

### `policies`

Pólizas asociadas. Campos clave: `id_poliza`, `id_asegurado`, `ramo`, `fecha_inicio`, `fecha_fin`, `prima`, `suma_asegurada`, `deducible`, `canal_venta`, `ciudad`, `estado_poliza`.

### `insured`

Asegurados sintéticos anonimizados. Campos clave: `id_asegurado`, `segmento`, `antiguedad`, `ciudad`, `numero_polizas`, `reclamos_ultimos_12_meses`, `mora_actual`, `score_cliente_simulado`.

### `vehicles`

Vehículos sintéticos. Campos clave: `id_vehiculo`, `id_asegurado`, `marca`, `modelo`, `anio`, `placa_hash`, `chasis_hash`, `motor_hash`, `valor_asegurado`.

### `providers`

Proveedores, talleres, clínicas o peritos sintéticos. Campos clave: `id_proveedor`, `tipo`, `ciudad`, `reclamos_asociados`, `monto_promedio_reclamado`, `porcentaje_casos_observados`, `antiguedad`, `lista_restrictiva_simulada`.

### `documents`

Documentos del siniestro. Campos clave: `id_documento`, `id_siniestro`, `tipo_documento`, `entregado`, `legible`, `fecha_emision`, `inconsistencia_detectada`, `observacion`.

### `risk_scores`

Resultado consolidado. Campos clave: `id_siniestro`, `score_reglas`, `score_ml`, `score_anomalia`, `score_nlp`, `score_final`, `nivel_riesgo`, `reglas_activadas`, `explicacion`, `accion_sugerida`.

## Fórmula del score final

```txt
score_final = 0.55 * score_reglas
            + 0.25 * score_ml
            + 0.10 * score_anomalia
            + 0.10 * score_nlp
```

Si una capa no está disponible en el MVP inicial, su valor debe ser `0` o un valor neutral documentado. Las reglas explicables son la base del sistema y no deben omitirse.

## Clasificación de riesgo

| Rango | Nivel | Interpretación |
|---:|---|---|
| 0-40 | Verde | Sin señales relevantes o riesgo bajo. |
| 41-75 | Amarillo | Señales que requieren revisión priorizada. |
| 76-100 | Rojo | Alta concentración de señales para revisión urgente. |

La clasificación expresa prioridad de revisión, no culpabilidad.

## Rol del agente IA

El agente es consultivo. Debe responder preguntas operativas usando funciones locales sobre datos procesados:

- Top de siniestros con mayor riesgo.
- Explicación de un caso específico.
- Proveedores con más alertas.
- Ciudades, ramos o coberturas con concentración de riesgo.
- Documentos faltantes o inconsistentes.
- Narrativas similares.
- Resumen ejecutivo de casos críticos.

El agente no modifica scores, no decide pagos y no consulta datos fuera de las tools definidas.

## Rol opcional del MCP

MCP puede exponerse como diferenciador si el MVP ya funciona. Su rol es publicar tools controladas y auditables para consultar siniestros, proveedores, documentos, narrativas y resúmenes.

MCP no es obligatorio. El sistema debe seguir funcionando con `agent_router` local si MCP no se implementa.

## Decisiones técnicas tomadas

- Usar Streamlit como interfaz principal.
- Usar Python 3.11 como único lenguaje de implementación.
- Usar datos 100% sintéticos.
- Usar SQLite para demo local y CSV como respaldo.
- Priorizar reglas explicables antes de ML.
- Usar RandomForestClassifier como modelo supervisado principal.
- Mantener LogisticRegression como fallback.
- Usar IsolationForest solo si no compromete el tiempo de entrega.
- Usar TF-IDF y similitud coseno para NLP.
- Implementar agente local antes que MCP.
- Mantener demo local como ruta principal de presentación.

## Decisiones descartadas

| Decisión descartada | Motivo |
|---|---|
| React | Aumenta complejidad de frontend, API, estado y deploy para una demo de datos. |
| FastAPI obligatorio | No es necesario para Streamlit local; puede quedar como mejora futura. |
| MySQL/Oracle real | Requiere servidor, credenciales y configuración innecesaria para datos sintéticos. |
| Docker obligatorio | Añade fricción operativa para hackathon; no aporta al MVP local. |
| Login | No es parte del alcance y desvía tiempo de IA, score y explicabilidad. |
| Roles | No se requiere control de acceso para demo sintética. |
| Microservicios | Arquitectura pesada para un prototipo de 3 días. |

## Seguridad, privacidad y ética

- No usar datos reales ni información personal identificable.
- Usar identificadores sintéticos o anonimizados.
- No incluir credenciales ni API keys.
- Mantener `.env.example` sin secretos.
- Evitar lenguaje acusatorio en app, docs y pitch.
- Mostrar que el sistema genera alertas para revisión humana.
- Documentar falsos positivos, sesgos y límites del dataset sintético.
- Mantener trazabilidad de reglas y factores del score.
- No permitir que un LLM decida el score final.

## Criterios mínimos de arquitectura lista

- Estructura de repo definida y documentada.
- Stack cerrado y sin dependencias innecesarias.
- Modelo de datos mínimo definido.
- Flujo de datos claro de CSV/SQLite a dashboard.
- Score final y rangos de riesgo documentados.
- Separación entre datos, reglas, ML/NLP, scoring, explicación, agente y UI.
- Decisiones descartadas documentadas.
- Límites éticos explícitos.
- MVP puede funcionar sin MCP, FastAPI, Docker ni login.
