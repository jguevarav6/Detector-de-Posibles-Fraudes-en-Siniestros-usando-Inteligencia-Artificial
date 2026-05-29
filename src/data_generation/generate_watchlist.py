"""Generador de datos sinteticos para la base de compliance fraudlens_watchlist.

Crea cuatro tablas que viven separadas del operacional, cruzando IDs con el
dataset principal para que el agente pueda devolver respuestas con sentido.
"""

from __future__ import annotations

import random
from datetime import date, timedelta
from pathlib import Path

import pandas as pd


WATCHLIST_DIR = Path("data/watchlist")
SOURCE_CLAIMS = Path("data/synthetic/claims.csv")
SOURCE_PROVIDERS = Path("data/synthetic/providers.csv")
SOURCE_INSURED = Path("data/synthetic/insured.csv")
SOURCE_VEHICLES = Path("data/synthetic/vehicles.csv")


PROVIDER_REASONS = (
    "Concentracion atipica de reclamos",
    "Casos repetidos en menos de 30 dias",
    "Documentacion irregular reportada",
    "Reclamos con narrativa duplicada",
    "Monto promedio superior al mercado",
    "Reportes anonimos de terceros",
)

INSURED_REASONS = (
    "Historico de reclamos por robo",
    "Antecedente de monto atipico",
    "Multiples polizas activas",
    "Reclamo dentro de los primeros 30 dias de cobertura",
    "Reincidencia en cobertura medica",
)

VEHICLE_REASONS = (
    "Vehiculo reportado robado previamente",
    "Placa asociada a multiples siniestros",
    "Cambio de propietario reciente",
    "Modelo con alto indice de fraude documentado",
)

NARRATIVE_PATTERNS = (
    "Vehiculo robado en zona insegura sin testigos.",
    "Choque contra objeto fijo sin reporte policial.",
    "Hurto sin denuncia inicial; reportado dias despues.",
    "Asistencia medica solicitada fuera de horario habitual.",
    "Perdida total con peritaje pendiente.",
    "Incendio domestico sin parte de bomberos.",
    "Atropello sin tercero identificado.",
    "Reparacion estimada por encima del valor del bien.",
    "Robo de mercaderia en transito sin guia.",
    "Danios por evento climatico sin reporte meteorologico.",
)


def generate_watchlist(
    output_dir: Path = WATCHLIST_DIR,
    seed: int = 7,
    providers_count: int = 60,
    insured_count: int = 35,
    vehicles_count: int = 22,
    narratives_count: int = 12,
) -> dict[str, int]:
    """Genera 4 CSV en `data/watchlist/` listos para cargar a fraudlens_watchlist.

    Cruza IDs reales del dataset operacional para que las queries que cruzan
    ambas bases tengan resultados visibles desde el primer click.
    """
    rng = random.Random(seed)
    output_dir.mkdir(parents=True, exist_ok=True)

    providers_df = _safe_read(SOURCE_PROVIDERS)
    insured_df = _safe_read(SOURCE_INSURED)
    vehicles_df = _safe_read(SOURCE_VEHICLES)
    claims_df = _safe_read(SOURCE_CLAIMS)

    today = date.today()
    counts: dict[str, int] = {}

    counts["proveedores_observados"] = _write_csv(
        output_dir / "proveedores_observados.csv",
        _build_provider_rows(providers_df, rng, today, providers_count),
    )
    counts["asegurados_antecedentes"] = _write_csv(
        output_dir / "asegurados_antecedentes.csv",
        _build_insured_rows(insured_df, rng, today, insured_count),
    )
    counts["vehiculos_marcados"] = _write_csv(
        output_dir / "vehiculos_marcados.csv",
        _build_vehicle_rows(vehicles_df, rng, today, vehicles_count),
    )
    counts["narrativas_recurrentes"] = _write_csv(
        output_dir / "narrativas_recurrentes.csv",
        _build_narrative_rows(claims_df, rng, today, narratives_count),
    )
    return counts


def _safe_read(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path)


def _write_csv(path: Path, rows: list[dict]) -> int:
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    return len(df)


def _build_provider_rows(providers_df: pd.DataFrame, rng: random.Random, today: date, target: int) -> list[dict]:
    base_ids = providers_df["id_proveedor"].tolist() if not providers_df.empty else [f"PRO-{i:04d}" for i in range(60)]
    sample = rng.sample(base_ids, min(target, len(base_ids)))
    rows: list[dict] = []
    for idx, pid in enumerate(sample):
        registered = today - timedelta(days=rng.randint(15, 540))
        nivel = rng.choice(["Alerta media", "Alerta media", "Alerta alta", "Critico"])
        rows.append(
            {
                "id_proveedor": pid,
                "nivel_alerta": nivel,
                "casos_relacionados": rng.randint(3, 24),
                "motivo": rng.choice(PROVIDER_REASONS),
                "fecha_registro": registered.isoformat(),
                "responsable_compliance": rng.choice(["CAR-01", "CAR-02", "CAR-03", "CAR-04"]),
                "estado": rng.choice(["Activo", "Activo", "Activo", "En revision"]),
            }
        )
    return rows


def _build_insured_rows(insured_df: pd.DataFrame, rng: random.Random, today: date, target: int) -> list[dict]:
    base_ids = insured_df["id_asegurado"].tolist() if not insured_df.empty else [f"ASE-{i:04d}" for i in range(80)]
    sample = rng.sample(base_ids, min(target, len(base_ids)))
    rows: list[dict] = []
    for aid in sample:
        registered = today - timedelta(days=rng.randint(30, 720))
        rows.append(
            {
                "id_asegurado": aid,
                "tipo_antecedente": rng.choice(["Patrimonial", "Salud", "Vehicular", "Vida"]),
                "reclamos_previos": rng.randint(2, 9),
                "fecha_ultimo_reclamo": (registered + timedelta(days=rng.randint(0, 180))).isoformat(),
                "motivo": rng.choice(INSURED_REASONS),
                "nivel_alerta": rng.choice(["Alerta baja", "Alerta media", "Alerta alta"]),
                "estado": rng.choice(["Activo", "Activo", "En revision"]),
            }
        )
    return rows


def _build_vehicle_rows(vehicles_df: pd.DataFrame, rng: random.Random, today: date, target: int) -> list[dict]:
    base_ids = vehicles_df["id_vehiculo"].tolist() if not vehicles_df.empty else [f"VEH-{i:04d}" for i in range(80)]
    sample = rng.sample(base_ids, min(target, len(base_ids)))
    rows: list[dict] = []
    for vid in sample:
        registered = today - timedelta(days=rng.randint(20, 600))
        rows.append(
            {
                "id_vehiculo": vid,
                "motivo": rng.choice(VEHICLE_REASONS),
                "casos_relacionados": rng.randint(1, 6),
                "fecha_registro": registered.isoformat(),
                "fuente": rng.choice(["Policia Nacional", "Reporte interno", "Aseguradora aliada", "Anonimo"]),
                "estado": rng.choice(["Activo", "Activo", "Cerrado"]),
            }
        )
    return rows


def _build_narrative_rows(claims_df: pd.DataFrame, rng: random.Random, today: date, target: int) -> list[dict]:
    rows: list[dict] = []
    base_claims = (
        claims_df["id_siniestro"].tolist() if not claims_df.empty else [f"SIN-{i:05d}" for i in range(200)]
    )
    for idx in range(target):
        patron = rng.choice(NARRATIVE_PATTERNS)
        casos = rng.sample(base_claims, k=rng.randint(2, 5))
        rows.append(
            {
                "id_patron": f"PAT-{idx + 1:03d}",
                "patron_texto": patron,
                "siniestros_relacionados": ", ".join(casos),
                "frecuencia": len(casos),
                "fecha_deteccion": (today - timedelta(days=rng.randint(7, 365))).isoformat(),
                "nivel_alerta": rng.choice(["Alerta media", "Alerta alta", "Critico"]),
            }
        )
    return rows


if __name__ == "__main__":
    summary = generate_watchlist()
    for table, count in summary.items():
        print(f"{table}: {count} filas")
