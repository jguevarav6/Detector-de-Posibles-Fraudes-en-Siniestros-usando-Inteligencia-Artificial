"""Generación reproducible de datos sintéticos para FraudLens Claims AI."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


SYNTHETIC_DIR = Path("data/synthetic")
DEFAULT_SEED = 20260527


@dataclass(frozen=True)
class DatasetSizes:
    insured: int = 350
    policies: int = 400
    vehicles: int = 250
    providers: int = 80
    claims: int = 1000


def generate_all(output_dir: Path = SYNTHETIC_DIR, seed: int = DEFAULT_SEED) -> dict[str, Path]:
    """Genera CSV sintéticos y devuelve las rutas escritas."""
    output_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    sizes = DatasetSizes()

    insured = _build_insured(rng, sizes.insured)
    policies = _build_policies(rng, insured, sizes.policies)
    vehicles = _build_vehicles(rng, insured, sizes.vehicles)
    providers = _build_providers(rng, sizes.providers)
    claims = _build_claims(rng, policies, insured, vehicles, providers, sizes.claims)
    documents = _build_documents(rng, claims)
    watchlist = providers.loc[providers["lista_restrictiva_simulada"], ["id_proveedor", "tipo", "ciudad"]].copy()

    outputs = {
        "insured": output_dir / "insured.csv",
        "policies": output_dir / "policies.csv",
        "vehicles": output_dir / "vehicles.csv",
        "providers": output_dir / "providers.csv",
        "claims": output_dir / "claims.csv",
        "documents": output_dir / "documents.csv",
        "watchlist": output_dir / "watchlist.csv",
    }
    insured.to_csv(outputs["insured"], index=False)
    policies.to_csv(outputs["policies"], index=False)
    vehicles.to_csv(outputs["vehicles"], index=False)
    providers.to_csv(outputs["providers"], index=False)
    claims.to_csv(outputs["claims"], index=False)
    documents.to_csv(outputs["documents"], index=False)
    watchlist.to_csv(outputs["watchlist"], index=False)
    return outputs


def _build_insured(rng: np.random.Generator, n: int) -> pd.DataFrame:
    cities = ["Guayaquil", "Quito", "Cuenca", "Manta", "Loja", "Ambato", "Machala"]
    segments = ["Individual", "Familiar", "Pyme", "Corporativo"]
    return pd.DataFrame(
        {
            "id_asegurado": [f"ASE-{i:04d}" for i in range(1, n + 1)],
            "segmento": rng.choice(segments, n, p=[0.48, 0.28, 0.18, 0.06]),
            "antiguedad_meses": rng.integers(1, 96, n),
            "ciudad": rng.choice(cities, n),
            "numero_polizas": rng.integers(1, 5, n),
            "reclamos_ultimos_12_meses": rng.poisson(0.7, n).clip(0, 7),
            "mora_actual": rng.choice([False, True], n, p=[0.88, 0.12]),
            "score_cliente_simulado": rng.integers(45, 96, n),
        }
    )


def _build_policies(rng: np.random.Generator, insured: pd.DataFrame, n: int) -> pd.DataFrame:
    branches = ["Vehículos", "Salud", "Vida", "Hogar", "Generales"]
    channels = ["Agente", "Digital", "Broker", "Sucursal"]
    start_dates = pd.Timestamp("2025-01-01") + pd.to_timedelta(rng.integers(0, 470, n), unit="D")
    policy_insured = rng.choice(insured["id_asegurado"], n)
    insured_city = insured.set_index("id_asegurado").loc[policy_insured, "ciudad"].to_numpy()
    sums = rng.integers(8_000, 80_000, n)
    return pd.DataFrame(
        {
            "id_poliza": [f"POL-{i:04d}" for i in range(1, n + 1)],
            "id_asegurado": policy_insured,
            "ramo": rng.choice(branches, n, p=[0.42, 0.22, 0.12, 0.14, 0.10]),
            "fecha_inicio": start_dates.date.astype(str),
            "fecha_fin": (start_dates + pd.to_timedelta(365, unit="D")).date.astype(str),
            "prima": (sums * rng.uniform(0.025, 0.09, n)).round(2),
            "suma_asegurada": sums,
            "deducible": rng.choice([100, 250, 500, 1000], n),
            "canal_venta": rng.choice(channels, n),
            "ciudad": insured_city,
            "estado_poliza": rng.choice(["Vigente", "Vigente", "Vigente", "Renovación"], n),
        }
    )


def _build_vehicles(rng: np.random.Generator, insured: pd.DataFrame, n: int) -> pd.DataFrame:
    brands = ["Andes", "Pacífico", "Cóndor", "Sierra", "Costa"]
    return pd.DataFrame(
        {
            "id_vehiculo": [f"VEH-{i:04d}" for i in range(1, n + 1)],
            "id_asegurado": rng.choice(insured["id_asegurado"], n),
            "marca": rng.choice(brands, n),
            "modelo": [f"Modelo-{rng.integers(1, 9)}" for _ in range(n)],
            "anio": rng.integers(2012, 2026, n),
            "placa_hash": [f"PLH-{rng.integers(100000, 999999)}" for _ in range(n)],
            "chasis_hash": [f"CHH-{rng.integers(1000000, 9999999)}" for _ in range(n)],
            "motor_hash": [f"MTH-{rng.integers(1000000, 9999999)}" for _ in range(n)],
            "valor_asegurado": rng.integers(8_000, 55_000, n),
        }
    )


def _build_providers(rng: np.random.Generator, n: int) -> pd.DataFrame:
    cities = ["Guayaquil", "Quito", "Cuenca", "Manta", "Loja", "Ambato", "Machala"]
    types = ["Taller", "Clínica", "Perito", "Proveedor documentos", "Asistencia"]
    observed = rng.uniform(0.02, 0.35, n).round(3)
    restricted = observed > 0.29
    return pd.DataFrame(
        {
            "id_proveedor": [f"PRO-{i:04d}" for i in range(1, n + 1)],
            "tipo": rng.choice(types, n, p=[0.40, 0.24, 0.16, 0.10, 0.10]),
            "ciudad": rng.choice(cities, n),
            "reclamos_asociados": rng.integers(2, 90, n),
            "monto_promedio_reclamado": rng.integers(700, 14_000, n),
            "porcentaje_casos_observados": observed,
            "antiguedad_meses": rng.integers(2, 120, n),
            "lista_restrictiva_simulada": restricted,
        }
    )


def _build_claims(
    rng: np.random.Generator,
    policies: pd.DataFrame,
    insured: pd.DataFrame,
    vehicles: pd.DataFrame,
    providers: pd.DataFrame,
    n: int,
) -> pd.DataFrame:
    coverage_by_branch = {
        "Vehículos": ["Choque", "Robo total", "Robo parcial", "Daño"],
        "Salud": ["Atención médica", "Emergencia", "Cirugía"],
        "Vida": ["Incapacidad", "Fallecimiento"],
        "Hogar": ["Incendio", "Daño por agua", "Robo"],
        "Generales": ["Responsabilidad civil", "Daño", "Pérdida"],
    }
    suspicious_templates = [
        "Evento reportado con tercero no identificado y documentos pendientes.",
        "Robo ocurrido cerca del inicio de vigencia con denuncia tardía.",
        "Daño reportado con narrativa similar a otros reclamos revisados.",
    ]
    normal_templates = [
        "Siniestro reportado con documentación completa para revisión estándar.",
        "Evento ocurrido durante vigencia regular con respaldo documental.",
        "Reclamo presentado dentro del plazo esperado con proveedor habitual.",
    ]
    selected_policies = policies.sample(n=n, replace=True, random_state=int(rng.integers(1, 999999))).reset_index(drop=True)
    provider_ids = rng.choice(providers["id_proveedor"], n)
    provider_lookup = providers.set_index("id_proveedor")
    insured_lookup = insured.set_index("id_asegurado")
    vehicle_by_insured = vehicles.groupby("id_asegurado")["id_vehiculo"].first()

    suspicious_mask = rng.random(n) < 0.22
    start = pd.to_datetime(selected_policies["fecha_inicio"])
    end = pd.to_datetime(selected_policies["fecha_fin"])
    normal_offsets = rng.integers(30, 335, n)
    edge_offsets = rng.choice([1, 2, 3, 358, 362, 364], n)
    occurrence = start + pd.to_timedelta(np.where(suspicious_mask, edge_offsets, normal_offsets), unit="D")
    occurrence = occurrence.where(occurrence <= end, end - pd.to_timedelta(1, unit="D"))
    report_delay = np.where(suspicious_mask, rng.integers(8, 31, n), rng.integers(0, 7, n))
    report = occurrence + pd.to_timedelta(report_delay, unit="D")
    claimed_amount = np.where(
        suspicious_mask,
        selected_policies["suma_asegurada"].to_numpy() * rng.uniform(0.62, 1.08, n),
        selected_policies["suma_asegurada"].to_numpy() * rng.uniform(0.04, 0.38, n),
    ).round(2)
    estimated = (claimed_amount * rng.uniform(0.72, 0.96, n)).round(2)
    paid = np.where(rng.random(n) < 0.35, estimated * rng.uniform(0.2, 0.9, n), 0).round(2)
    ramo = selected_policies["ramo"].to_numpy()
    coverage = [rng.choice(coverage_by_branch[item]) for item in ramo]
    insured_ids = selected_policies["id_asegurado"].to_numpy()
    vehicle_ids = [vehicle_by_insured.get(item, "") if branch == "Vehículos" else "" for item, branch in zip(insured_ids, ramo)]

    return pd.DataFrame(
        {
            "id_siniestro": [f"SIN-{i:05d}" for i in range(1, n + 1)],
            "id_poliza": selected_policies["id_poliza"],
            "id_asegurado": insured_ids,
            "id_vehiculo": vehicle_ids,
            "id_proveedor": provider_ids,
            "ramo": ramo,
            "cobertura": coverage,
            "fecha_ocurrencia": occurrence.dt.date.astype(str),
            "fecha_reporte": report.dt.date.astype(str),
            "monto_reclamado": claimed_amount,
            "monto_estimado": estimated,
            "monto_pagado": paid,
            "estado": rng.choice(["Reserva", "Pago Parcial", "Liquidado", "En revisión", "Anticipo"], n),
            "sucursal": rng.choice(["Sucursal Norte", "Sucursal Centro", "Sucursal Costa", "Sucursal Austro"], n),
            "ciudad": [insured_lookup.loc[item, "ciudad"] for item in insured_ids],
            "descripcion": [rng.choice(suspicious_templates if flag else normal_templates) for flag in suspicious_mask],
            "documentos_completos": ~suspicious_mask | (rng.random(n) > 0.45),
            "beneficiario": provider_lookup.loc[provider_ids, "tipo"].to_numpy(),
            "dias_desde_inicio_poliza": (occurrence - start).dt.days,
            "dias_desde_fin_poliza": (end - occurrence).dt.days,
            "dias_entre_ocurrencia_reporte": report_delay,
            "historial_siniestros_asegurado": [insured_lookup.loc[item, "reclamos_ultimos_12_meses"] for item in insured_ids],
            "tipo_accidente": rng.choice(["Colisión", "Robo", "Daño material", "Atención médica", "Otro"], n),
            "tercero_identificado": np.where(suspicious_mask, rng.random(n) > 0.55, rng.random(n) > 0.12),
            "hora_evento": rng.integers(0, 24, n),
            "proveedor_lista_restrictiva": provider_lookup.loc[provider_ids, "lista_restrictiva_simulada"].to_numpy(),
            "etiqueta_fraude_simulada": suspicious_mask.astype(int),
        }
    )


def _build_documents(rng: np.random.Generator, claims: pd.DataFrame) -> pd.DataFrame:
    doc_types = ["Formulario", "Denuncia", "Factura", "Informe técnico", "Foto evidencia", "Certificado"]
    rows = []
    for claim in claims.itertuples(index=False):
        required = rng.choice(doc_types, size=rng.integers(3, 6), replace=False)
        risky = bool(claim.etiqueta_fraude_simulada)
        for doc_type in required:
            delivered = rng.random() > (0.28 if risky else 0.06)
            legible = delivered and (rng.random() > (0.18 if risky else 0.04))
            inconsistent = delivered and (rng.random() < (0.22 if risky else 0.03))
            rows.append(
                {
                    "id_documento": f"DOC-{len(rows) + 1:06d}",
                    "id_siniestro": claim.id_siniestro,
                    "tipo_documento": doc_type,
                    "entregado": delivered,
                    "legible": legible,
                    "fecha_emision": claim.fecha_reporte,
                    "inconsistencia_detectada": inconsistent,
                    "observacion": "Revisar respaldo" if inconsistent or not delivered else "Sin observación",
                }
            )
    return pd.DataFrame(rows)


if __name__ == "__main__":
    paths = generate_all()
    for name, path in paths.items():
        print(f"{name}: {path}")
