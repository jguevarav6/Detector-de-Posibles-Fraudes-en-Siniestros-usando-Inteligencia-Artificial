"""Prepara la demo local de FraudLens Claims AI."""

from __future__ import annotations

from src.data_generation.generate_synthetic_data import generate_all
from src.database.build_database import build_database


def main() -> None:
    outputs = generate_all()
    database_path = build_database()
    print("Datos sintéticos generados:")
    for name, path in outputs.items():
        print(f"- {name}: {path}")
    print(f"SQLite local: {database_path}")
    print("Pendiente: features, scoring, ML/NLP y agente real se implementarán en fases posteriores.")


if __name__ == "__main__":
    main()
