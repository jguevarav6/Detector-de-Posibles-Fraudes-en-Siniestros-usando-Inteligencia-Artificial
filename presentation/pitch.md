# FraudLens Claims AI - Pitch Ejecutivo

## 1. Problema

Las areas de siniestros revisan grandes volumenes de reclamos con informacion dispersa en polizas, asegurados, vehiculos, proveedores, documentos y narrativas.

El reto no es acusar fraude. El reto es priorizar casos que merecen revision humana antes de que consuman tiempo operativo o generen exposicion innecesaria.

## 2. Solucion

FraudLens Claims AI genera una bandeja priorizada de siniestros con:

- Score hibrido de posible riesgo.
- Semaforo Verde, Amarillo y Rojo.
- Reglas activadas con evidencia.
- ML supervisado sobre etiqueta sintetica.
- Deteccion de anomalias.
- NLP para narrativas similares.
- Agente consultivo con tools controladas.
- Dashboard Streamlit y reportes CSV.

## 3. Arquitectura

```txt
CSV sinteticos -> MySQL -> Features -> Reglas + ML + Anomalias + NLP
                                      -> Score final + Explicacion
                                      -> Streamlit + Agente local
```

## 4. Uso de IA

Formula:

```txt
score_final = 0.55 * score_reglas
            + 0.25 * score_ml
            + 0.10 * score_anomalia
            + 0.10 * score_nlp
```

La IA no decide. La IA prioriza y explica.

## 5. Demo

Flujo:

1. Dashboard ejecutivo.
2. Bandeja filtrada por casos rojos.
3. Detalle de un siniestro con reglas y score.
4. Pregunta al agente: proveedores con mas alertas.
5. Reporte descargable de casos revisables.

## 6. Impacto

- Reduce tiempo de triage inicial.
- Ordena la revision por prioridad.
- Explica por que un caso sube en la bandeja.
- Permite consultas ejecutivas y operativas.
- Mantiene la decision final en manos humanas.

## 7. Etica

FraudLens no confirma fraude, no rechaza siniestros y no reemplaza al analista.

Usa datos sinteticos e identificadores anonimos. Las metricas del modelo son demostrativas y no representan desempeno productivo.

## 8. Proximos pasos

- Conectar fuentes historicas anonimizadas.
- Ajustar umbrales con analistas.
- Implementar MCP completo como integracion externa.
- Preparar despliegue Streamlit Cloud o entorno interno.
