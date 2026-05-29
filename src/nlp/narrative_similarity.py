"""Similitud de narrativas con TF-IDF y cosine similarity."""

from __future__ import annotations

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def add_nlp_scores(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega similitud maxima, caso similar y score_nlp por siniestro."""
    result = df.copy()
    texts = result["descripcion"].fillna("").astype(str)
    if len(result) < 2 or texts.str.strip().eq("").all():
        result["max_similarity"] = 0.0
        result["similar_claim_id"] = ""
        result["score_nlp"] = 0.0
        result["nlp_alert"] = "Sin alerta textual"
        result["nlp_explanation"] = "No hay suficientes narrativas comparables."
        return result

    matrix = cosine_similarity(TfidfVectorizer(ngram_range=(1, 2), min_df=1).fit_transform(texts))
    ids = result["id_siniestro"].tolist()
    max_values = []
    similar_ids = []
    for idx in range(len(result)):
        row = matrix[idx].copy()
        row[idx] = -1
        best_idx = int(row.argmax())
        best_value = float(row[best_idx])
        max_values.append(round(best_value, 4))
        similar_ids.append(ids[best_idx] if best_value >= 0.70 else "")

    result["max_similarity"] = max_values
    result["similar_claim_id"] = similar_ids
    result["score_nlp"] = result["max_similarity"].apply(_score_similarity)
    result["nlp_alert"] = result["score_nlp"].apply(
        lambda score: "Narrativa muy similar" if score >= 85 else ("Narrativa similar" if score >= 60 else "Sin alerta textual")
    )
    result["nlp_explanation"] = result.apply(
        lambda row: f"Narrativa comparable con {row['similar_claim_id']} ({row['max_similarity']:.0%})."
        if row["similar_claim_id"]
        else "No se observan narrativas similares relevantes.",
        axis=1,
    )
    return result


def get_similar_claims(id_siniestro: str, df: pd.DataFrame, threshold: float = 0.70) -> pd.DataFrame:
    """Devuelve el caso similar precomputado cuando supera el umbral."""
    row = df.loc[df["id_siniestro"] == id_siniestro]
    if row.empty or float(row.iloc[0].get("max_similarity", 0)) < threshold:
        return pd.DataFrame()
    similar_id = row.iloc[0].get("similar_claim_id", "")
    return df.loc[df["id_siniestro"] == similar_id]


def _score_similarity(value: float) -> float:
    if value >= 0.85:
        return 90.0
    if value >= 0.70:
        return 65.0
    return 0.0
