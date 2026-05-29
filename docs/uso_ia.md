# Uso de IA - FraudLens Claims AI

## Objetivo

La IA se usa para apoyar la priorizacion de siniestros que requieren revision humana. No decide fraude, no rechaza reclamos y no reemplaza al analista.

## Componentes implementados

### 1. Reglas explicables

Archivo: `src/rules/fraud_rules.py`

Las reglas detectan senales de posible riesgo como borde de vigencia, reporte tardio, proveedor recurrente, documentos incompletos, documentos inconsistentes, monto atipico y narrativa similar.

Cada regla entrega:

- Codigo.
- Nombre.
- Puntos.
- Severidad.
- Explicacion.
- Evidencia.

### 2. Machine Learning supervisado

Archivo: `src/models/train_model.py`

Se entrena un `RandomForestClassifier` sobre `etiqueta_fraude_simulada`. Esta etiqueta es sintetica y sirve solo para entrenar y validar el prototipo.

Si el entrenamiento principal falla, existe fallback con `LogisticRegression`.

Salidas:

- `score_ml`.
- `data/processed/fraud_model.joblib`.
- `data/processed/model_metrics.json`.

Metricas guardadas:

- Accuracy.
- Precision.
- Recall.
- F1.
- Matriz de confusion.
- ROC-AUC cuando aplica.

### 3. Deteccion de anomalias

Archivo: `src/models/train_model.py`

Se usa `IsolationForest` para identificar casos atipicos dentro del dataset sintetico.

Salida:

- `score_anomalia`.
- `data/processed/anomaly_model.joblib`.

### 4. NLP de narrativas

Archivo: `src/nlp/narrative_similarity.py`

Se usa `TfidfVectorizer` con similitud coseno para comparar descripciones de reclamos.

Criterios:

- Similitud >= 0.85: alerta fuerte.
- Similitud >= 0.70 y < 0.85: alerta media.
- Similitud < 0.70: sin alerta textual.

Salidas:

- `max_similarity`.
- `similar_claim_id`.
- `score_nlp`.
- `nlp_alert`.
- `nlp_explanation`.

### 5. Agente consultivo local

Archivos:

- `src/agent/agent_tools.py`.
- `src/agent/agent_router.py`.

El agente responde preguntas usando funciones controladas sobre `data/processed/scored_claims.csv`. No consulta libremente la base ni inventa scores.

Preguntas soportadas:

- Top de siniestros de mayor riesgo.
- Explicacion de un siniestro.
- Proveedores con mas alertas.
- Ramos y ciudades con mayor concentracion.
- Documentos faltantes en casos criticos.
- Montos atipicos.
- Siniestros cerca del inicio de poliza.
- Narrativas similares.
- Resumen ejecutivo.
- Recomendacion de casos a revisar primero.

## Formula del score

```txt
score_final = 0.55 * score_reglas
            + 0.25 * score_ml
            + 0.10 * score_anomalia
            + 0.10 * score_nlp
```

## Clasificacion

| Score | Nivel | Uso |
|---:|---|---|
| 0-40 | Verde | Revision estandar |
| 41-75 | Amarillo | Revision priorizada |
| 76-100 | Rojo | Revision urgente |

## Artefactos generados

Al ejecutar:

```bash
python setup_demo.py
```

Se generan:

- CSV sinteticos en `data/synthetic/`.
- Tablas MySQL en `fraudlens_claims_ai`.
- `data/processed/scored_claims.csv`.
- `data/processed/risk_scores.csv`.
- `data/processed/model_metrics.json`.
- Modelos `.joblib`.

## Limitacion importante

Los modelos aprenden de datos sinteticos. Sus metricas demuestran el funcionamiento tecnico, no desempeno real en produccion.
