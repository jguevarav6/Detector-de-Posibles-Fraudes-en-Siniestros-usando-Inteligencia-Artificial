"""Prepara la demo local de FraudLens Claims AI."""

from __future__ import annotations

from src.data_generation.generate_synthetic_data import generate_all
from src.database.build_database import build_database
from src.scoring.scoring_service import run_scoring_pipeline


def main() -> None:
    outputs = generate_all()
    database_target = build_database()
    scored_claims = run_scoring_pipeline()
    print("Datos sinteticos generados:")
    for name, path in outputs.items():
        print(f"- {name}: {path}")
    print(f"MySQL: {database_target}")
    print(f"Siniestros procesados con score: {len(scored_claims)}")
    print("Artefactos: data/processed/scored_claims.csv, risk_scores.csv, model_metrics.json")


if __name__ == "__main__":
    main()
