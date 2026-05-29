"""Features de riesgo desde datos sinteticos."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


SYNTHETIC_DIR = Path("data/synthetic")


def load_synthetic_tables(input_dir: Path = SYNTHETIC_DIR) -> dict[str, pd.DataFrame]:
    """Carga las tablas sinteticas requeridas para scoring."""
    tables = {}
    for name in ["claims", "policies", "insured", "vehicles", "providers", "documents"]:
        tables[name] = pd.read_csv(input_dir / f"{name}.csv")
    return tables


def build_claim_features(input_dir: Path = SYNTHETIC_DIR) -> pd.DataFrame:
    """Une entidades y calcula variables consumidas por reglas, ML, agente y UI."""
    tables = load_synthetic_tables(input_dir)
    claims = tables["claims"].copy()
    policies = tables["policies"].add_prefix("poliza_")
    providers = tables["providers"].add_prefix("proveedor_")
    insured = tables["insured"].add_prefix("asegurado_")
    documents = tables["documents"]

    features = claims.merge(policies, left_on="id_poliza", right_on="poliza_id_poliza", how="left")
    features = features.merge(providers, left_on="id_proveedor", right_on="proveedor_id_proveedor", how="left")
    features = features.merge(insured, left_on="id_asegurado", right_on="asegurado_id_asegurado", how="left")

    doc_summary = (
        documents.groupby("id_siniestro")
        .agg(
            documentos_total=("id_documento", "count"),
            documentos_faltantes=("entregado", lambda s: int((~s.astype(bool)).sum())),
            documentos_ilegibles=("legible", lambda s: int((~s.astype(bool)).sum())),
            documentos_inconsistentes=("inconsistencia_detectada", lambda s: int(s.astype(bool).sum())),
            documentos_observados=("observacion", lambda s: "; ".join(sorted(set(map(str, s)))[:3])),
        )
        .reset_index()
    )
    features = features.merge(doc_summary, on="id_siniestro", how="left")
    for column in ["documentos_total", "documentos_faltantes", "documentos_ilegibles", "documentos_inconsistentes"]:
        features[column] = features[column].fillna(0).astype(int)

    features["monto_vs_suma_asegurada"] = (
        features["monto_reclamado"] / features["poliza_suma_asegurada"].replace(0, pd.NA)
    ).fillna(0)
    features["proveedor"] = features["id_proveedor"] + " - " + features["proveedor_tipo"].fillna("Proveedor")
    features["asegurado"] = features["id_asegurado"]
    features["vehiculo"] = features["id_vehiculo"].fillna("")
    features["reclamos_vehiculo_18_meses"] = features.groupby("id_vehiculo")["id_siniestro"].transform("count")
    features.loc[features["id_vehiculo"].fillna("") == "", "reclamos_vehiculo_18_meses"] = 0
    return features
