"""Entrenamiento y scoring ML basico sobre etiqueta sintetica."""

from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


MODEL_PATH = Path("data/processed/fraud_model.joblib")
ANOMALY_MODEL_PATH = Path("data/processed/anomaly_model.joblib")
METRICS_PATH = Path("data/processed/model_metrics.json")

FEATURE_COLUMNS = [
    "dias_desde_inicio_poliza",
    "dias_desde_fin_poliza",
    "dias_entre_ocurrencia_reporte",
    "monto_reclamado",
    "monto_estimado",
    "monto_pagado",
    "monto_vs_suma_asegurada",
    "historial_siniestros_asegurado",
    "asegurado_reclamos_ultimos_12_meses",
    "reclamos_vehiculo_18_meses",
    "proveedor_reclamos_asociados",
    "proveedor_porcentaje_casos_observados",
    "documentos_faltantes",
    "documentos_inconsistentes",
    "max_similarity",
    "hora_evento",
]


def add_ml_scores(df: pd.DataFrame, output_dir: Path = Path("data/processed")) -> pd.DataFrame:
    """Entrena modelos ligeros y agrega score_ml y score_anomalia."""
    output_dir.mkdir(parents=True, exist_ok=True)
    result = df.copy()
    x = _feature_matrix(result)
    y = result["etiqueta_fraude_simulada"].astype(int)

    model, metrics = _fit_classifier(x, y)
    result["score_ml"] = (model.predict_proba(x)[:, 1] * 100).round(2)
    joblib.dump(model, output_dir / MODEL_PATH.name)

    anomaly = IsolationForest(n_estimators=120, contamination=0.12, random_state=20260527)
    anomaly.fit(x)
    raw = -anomaly.decision_function(x)
    result["score_anomalia"] = _scale_0_100(pd.Series(raw)).round(2)
    joblib.dump(anomaly, output_dir / ANOMALY_MODEL_PATH.name)

    metrics["anomaly_model"] = {"type": "IsolationForest", "contamination": 0.12}
    (output_dir / METRICS_PATH.name).write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return result


def _fit_classifier(x: pd.DataFrame, y: pd.Series) -> tuple[Pipeline | RandomForestClassifier, dict]:
    stratify = y if y.nunique() > 1 else None
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=20260527, stratify=stratify)
    try:
        model: Pipeline | RandomForestClassifier = RandomForestClassifier(
            n_estimators=140,
            max_depth=8,
            min_samples_leaf=4,
            random_state=20260527,
            class_weight="balanced",
        )
        model.fit(x_train, y_train)
    except Exception:
        model = Pipeline([("scale", StandardScaler()), ("clf", LogisticRegression(max_iter=500, class_weight="balanced"))])
        model.fit(x_train, y_train)

    pred = model.predict(x_test)
    proba = model.predict_proba(x_test)[:, 1]
    metrics = {
        "model_type": type(model).__name__,
        "accuracy": round(float(accuracy_score(y_test, pred)), 4),
        "precision": round(float(precision_score(y_test, pred, zero_division=0)), 4),
        "recall": round(float(recall_score(y_test, pred, zero_division=0)), 4),
        "f1": round(float(f1_score(y_test, pred, zero_division=0)), 4),
        "confusion_matrix": confusion_matrix(y_test, pred).tolist(),
        "roc_auc": round(float(roc_auc_score(y_test, proba)), 4) if y_test.nunique() > 1 else None,
    }
    return model, metrics


def _feature_matrix(df: pd.DataFrame) -> pd.DataFrame:
    x = df.copy()
    x["tercero_identificado"] = x["tercero_identificado"].astype(int)
    x["proveedor_lista_restrictiva"] = x["proveedor_lista_restrictiva"].astype(int)
    for column in FEATURE_COLUMNS:
        if column not in x:
            x[column] = 0
    return x[FEATURE_COLUMNS].fillna(0)


def _scale_0_100(values: pd.Series) -> pd.Series:
    min_value = values.min()
    max_value = values.max()
    if max_value == min_value:
        return pd.Series([0.0] * len(values), index=values.index)
    return ((values - min_value) / (max_value - min_value) * 100).clip(0, 100)
