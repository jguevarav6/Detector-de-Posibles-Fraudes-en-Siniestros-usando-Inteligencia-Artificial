"""Motor de reglas explicables para prioridad de revision humana."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class RuleHit:
    code: str
    name: str
    points: int
    severity: str
    explanation: str
    evidence: str


def evaluate_claim(row: pd.Series) -> list[RuleHit]:
    """Evalua reglas de posible riesgo para un siniestro."""
    hits: list[RuleHit] = []
    if row["dias_desde_inicio_poliza"] <= 7 or row["dias_desde_fin_poliza"] <= 7:
        hits.append(_hit("R001_BORDE_VIGENCIA", "Evento cerca de vigencia", 22, "alta", "Ocurrio muy cerca del inicio o fin de poliza.", f"inicio={row['dias_desde_inicio_poliza']} fin={row['dias_desde_fin_poliza']}"))
    if row["dias_entre_ocurrencia_reporte"] >= 10:
        hits.append(_hit("R002_REPORTE_TARDIO", "Reporte tardio", 14, "media", "Existe demora relevante entre ocurrencia y reporte.", f"dias={row['dias_entre_ocurrencia_reporte']}"))
    if "Robo" in str(row["cobertura"]) and row["dias_entre_ocurrencia_reporte"] >= 5:
        hits.append(_hit("R003_DEMORA_ROBO", "Demora en robo", 18, "alta", "Robo reportado con demora atipica.", f"cobertura={row['cobertura']}"))
    if row["historial_siniestros_asegurado"] >= 3 or row.get("asegurado_reclamos_ultimos_12_meses", 0) >= 3:
        hits.append(_hit("R004_FRECUENCIA_ASEGURADO", "Frecuencia del asegurado", 13, "media", "El asegurado concentra varios reclamos recientes.", f"historial={row['historial_siniestros_asegurado']}"))
    if row.get("reclamos_vehiculo_18_meses", 0) >= 3:
        hits.append(_hit("R005_FRECUENCIA_VEHICULO", "Frecuencia del vehiculo", 10, "media", "El vehiculo aparece en multiples reclamos.", f"reclamos={row['reclamos_vehiculo_18_meses']}"))
    if row.get("proveedor_reclamos_asociados", 0) >= 60 or row.get("proveedor_porcentaje_casos_observados", 0) >= 0.25:
        hits.append(_hit("R006_PROVEEDOR_RECURRENTE", "Proveedor recurrente", 14, "media", "El proveedor concentra reclamos o casos observados.", f"proveedor={row['id_proveedor']}"))
    if not bool(row["documentos_completos"]) or row.get("documentos_faltantes", 0) > 0:
        hits.append(_hit("R007_DOCUMENTOS_INCOMPLETOS", "Documentos incompletos", 12, "media", "Faltan documentos para completar validacion.", f"faltantes={row.get('documentos_faltantes', 0)}"))
    if row.get("documentos_inconsistentes", 0) > 0 or row.get("documentos_ilegibles", 0) > 0:
        hits.append(_hit("R008_DOCUMENTOS_INCONSISTENTES", "Documentos inconsistentes", 18, "alta", "Hay documentos ilegibles o inconsistentes.", f"inconsistentes={row.get('documentos_inconsistentes', 0)}"))
    if row["hora_evento"] <= 4 and not bool(row["tercero_identificado"]):
        hits.append(_hit("R009_DINAMICA_SOSPECHOSA", "Dinamica a validar", 11, "media", "Evento nocturno sin tercero identificado.", f"hora={row['hora_evento']}"))
    if not bool(row["tercero_identificado"]) and str(row["ramo"]).replace("í", "i") == "Vehiculos":
        hits.append(_hit("R010_TERCERO_NO_IDENTIFICADO", "Tercero no identificado", 9, "baja", "No consta tercero identificado en un caso vehicular.", "tercero=False"))
    if row.get("score_nlp", 0) >= 70:
        hits.append(_hit("R011_NARRATIVA_SIMILAR", "Narrativa similar", 16, "alta", "La descripcion es muy similar a otro reclamo.", f"similitud={row.get('max_similarity', 0):.2f}"))
    if row.get("monto_vs_suma_asegurada", 0) >= 0.75:
        hits.append(_hit("R012_MONTO_ATIPICO", "Monto atipico", 17, "alta", "El monto reclamado es alto frente a la suma asegurada.", f"ratio={row.get('monto_vs_suma_asegurada', 0):.2f}"))
    if bool(row.get("proveedor_lista_restrictiva", False)):
        hits.append(_hit("R013_PROVEEDOR_OBSERVADO", "Proveedor en lista simulada", 20, "alta", "El proveedor aparece en lista restrictiva simulada.", f"proveedor={row['id_proveedor']}"))
    return hits


def add_rule_scores(df: pd.DataFrame) -> pd.DataFrame:
    """Agrega score_reglas, reglas activadas y explicacion base."""
    rows = []
    for _, row in df.iterrows():
        hits = evaluate_claim(row)
        points = min(sum(hit.points for hit in hits), 100)
        rows.append(
            {
                "score_reglas": points,
                "reglas_activadas": "; ".join(f"{hit.code}: {hit.name}" for hit in hits) or "Sin alertas relevantes",
                "evidencia_reglas": "; ".join(hit.evidence for hit in hits),
                "explicacion_reglas": " ".join(hit.explanation for hit in hits) or "No se observan senales relevantes fuera del comportamiento esperado.",
            }
        )
    return pd.concat([df.reset_index(drop=True), pd.DataFrame(rows)], axis=1)


def _hit(code: str, name: str, points: int, severity: str, explanation: str, evidence: str) -> RuleHit:
    return RuleHit(code, name, points, severity, explanation, evidence)
