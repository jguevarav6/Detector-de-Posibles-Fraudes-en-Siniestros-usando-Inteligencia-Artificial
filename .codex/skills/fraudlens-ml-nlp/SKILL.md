---
name: fraudlens-ml-nlp
description: Modelos ML y NLP de FraudLens Claims AI. Usar cuando Codex deba implementar o revisar RandomForestClassifier, LogisticRegression fallback, IsolationForest opcional, TF-IDF, cosine similarity, métricas, features de riesgo o scores ML/NLP integrados al score final.
---

# FraudLens ML/NLP

## Contexto obligatorio

Leer antes de editar:

- `docs/arquitectura.md`
- `docs/development.md`

## Recursos del skill

- Leer `references/operating_rules.md` antes de tocar modelos o NLP.
- Ejecutar `scripts/check_context.ps1` si hay duda de contexto.

## Archivos objetivo

- `src/features/build_features.py`
- `src/models/train_model.py`
- `src/models/fraud_classifier.py`
- `src/models/anomaly_detector.py`
- `src/nlp/narrative_similarity.py`
- `data/processed/model_metrics.json`

## Reglas

- El modelo no decide fraude.
- `etiqueta_fraude_simulada` es solo una etiqueta sintética de entrenamiento.
- RandomForestClassifier es el modelo principal.
- LogisticRegression es fallback.
- IsolationForest es opcional.
- NLP debe usar TF-IDF + cosine similarity.
- Actualizar `docs/development.md` con tipo `ml-nlp`, seguridad y progreso.

## Score

Integrar salidas al esquema:

```txt
score_final = 0.55 * score_reglas + 0.25 * score_ml + 0.10 * score_anomalia + 0.10 * score_nlp
```

## No hacer

- No agregar deep learning.
- No usar LLM para calcular el score.
- No presentar predicciones como verdad legal.

## Terminado

Hay scores ML/NLP trazables, métricas básicas y salida compatible con `risk_scores`.
