"""Datos demo sintéticos para que el frontend funcione antes del backend."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


PROCESSED_CLAIMS_PATH = Path("data/processed/scored_claims.csv")


def load_claims() -> pd.DataFrame:
    """Carga datos procesados si existen; si no, usa datos sintéticos de UI."""
    if PROCESSED_CLAIMS_PATH.exists():
        return pd.read_csv(PROCESSED_CLAIMS_PATH)
    return _demo_claims()


def _demo_claims() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "id_siniestro": "SIN-0001",
                "fecha_ocurrencia": "2026-05-03",
                "ciudad": "Guayaquil",
                "ramo": "Vehículos",
                "cobertura": "Robo total",
                "proveedor": "Taller Norte",
                "monto_reclamado": 18500,
                "score_final": 88,
                "nivel_riesgo": "Rojo",
                "accion_sugerida": "Revisión documental urgente",
                "reglas_activadas": "Borde de vigencia; denuncia tardía; documentos incompletos",
                "explicacion": "El caso concentra señales de revisión por ocurrir cerca del inicio de póliza, presentar demora de reporte y documentos incompletos.",
                "documentos": "Denuncia pendiente, factura ilegible",
                "asegurado": "ASE-104",
                "vehiculo": "VEH-081",
                "dias_desde_inicio_poliza": 2,
                "similar_claim_id": "SIN-0028",
                "max_similarity": 0.89,
            },
            {
                "id_siniestro": "SIN-0002",
                "fecha_ocurrencia": "2026-04-28",
                "ciudad": "Quito",
                "ramo": "Salud",
                "cobertura": "Atención médica",
                "proveedor": "Clínica Central",
                "monto_reclamado": 4200,
                "score_final": 67,
                "nivel_riesgo": "Amarillo",
                "accion_sugerida": "Validar documentos clínicos",
                "reglas_activadas": "Proveedor recurrente; monto atípico",
                "explicacion": "El monto se ubica por encima del patrón esperado y el proveedor concentra alertas medias.",
                "documentos": "Historia clínica completa",
                "asegurado": "ASE-218",
                "vehiculo": "",
                "dias_desde_inicio_poliza": 183,
                "similar_claim_id": "",
                "max_similarity": 0.34,
            },
            {
                "id_siniestro": "SIN-0003",
                "fecha_ocurrencia": "2026-04-18",
                "ciudad": "Cuenca",
                "ramo": "Vehículos",
                "cobertura": "Choque",
                "proveedor": "Taller Andino",
                "monto_reclamado": 2100,
                "score_final": 32,
                "nivel_riesgo": "Verde",
                "accion_sugerida": "Revisión estándar",
                "reglas_activadas": "Sin alertas críticas",
                "explicacion": "No se observan señales relevantes fuera del comportamiento esperado.",
                "documentos": "Documentos completos",
                "asegurado": "ASE-044",
                "vehiculo": "VEH-012",
                "dias_desde_inicio_poliza": 248,
                "similar_claim_id": "",
                "max_similarity": 0.21,
            },
            {
                "id_siniestro": "SIN-0004",
                "fecha_ocurrencia": "2026-05-11",
                "ciudad": "Manta",
                "ramo": "Hogar",
                "cobertura": "Incendio",
                "proveedor": "Peritaje Costa",
                "monto_reclamado": 12500,
                "score_final": 74,
                "nivel_riesgo": "Amarillo",
                "accion_sugerida": "Solicitar validación pericial",
                "reglas_activadas": "Monto alto; reporte tardío",
                "explicacion": "El caso requiere revisión por monto elevado y demora entre ocurrencia y reporte.",
                "documentos": "Informe pericial pendiente",
                "asegurado": "ASE-301",
                "vehiculo": "",
                "dias_desde_inicio_poliza": 41,
                "similar_claim_id": "",
                "max_similarity": 0.42,
            },
            {
                "id_siniestro": "SIN-0005",
                "fecha_ocurrencia": "2026-05-15",
                "ciudad": "Guayaquil",
                "ramo": "Vehículos",
                "cobertura": "Robo parcial",
                "proveedor": "Taller Norte",
                "monto_reclamado": 7600,
                "score_final": 81,
                "nivel_riesgo": "Rojo",
                "accion_sugerida": "Priorizar revisión antifraude",
                "reglas_activadas": "Narrativa similar; proveedor recurrente; tercero no identificado",
                "explicacion": "Se detectan similitudes narrativas con otro reclamo y concentración de alertas en el proveedor.",
                "documentos": "Denuncia completa",
                "asegurado": "ASE-147",
                "vehiculo": "VEH-203",
                "dias_desde_inicio_poliza": 9,
                "similar_claim_id": "SIN-0001",
                "max_similarity": 0.86,
            },
            {
                "id_siniestro": "SIN-0006",
                "fecha_ocurrencia": "2026-03-20",
                "ciudad": "Loja",
                "ramo": "Vida",
                "cobertura": "Incapacidad",
                "proveedor": "Centro Médico Sur",
                "monto_reclamado": 3300,
                "score_final": 45,
                "nivel_riesgo": "Amarillo",
                "accion_sugerida": "Revisión priorizada baja",
                "reglas_activadas": "Documentos incompletos",
                "explicacion": "Falta documentación de respaldo para completar validación del caso.",
                "documentos": "Certificado pendiente",
                "asegurado": "ASE-082",
                "vehiculo": "",
                "dias_desde_inicio_poliza": 92,
                "similar_claim_id": "",
                "max_similarity": 0.18,
            },
        ]
    )
