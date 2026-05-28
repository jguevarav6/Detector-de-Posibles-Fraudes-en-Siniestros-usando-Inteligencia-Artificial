# Tareas del Proyecto - FraudLens Claims AI

## Propósito

Este archivo es el tablero operativo del equipo. Aquí se marcan las tareas pendientes, en progreso y completadas durante el desarrollo.

Roles principales:

- Persona 1: Frontend / Dashboard / Demo visual.
- Persona 2: Backend / Datos / SQL / Reglas / IA / Agente.

Reglas:

- Marcar cada tarea con `[ ]`, `[~]` o `[x]`.
- `[ ]` pendiente.
- `[~]` en progreso.
- `[x]` completada.
- Registrar avances importantes en `docs/development.md`.
- Antes de implementar, revisar `docs/arquitectura.md` y `docs/development.md`.
- No usar datos reales, credenciales ni lenguaje acusatorio.

## Estado general

| Área | Responsable | Estado | Progreso |
|---|---|---|---:|
| Configuración base | Ambos | Completo | 100% |
| Frontend Streamlit | Persona 1 | En progreso | 55% |
| Backend, datos y SQL | Persona 2 | Estructura creada | 15% |
| Reglas y scoring | Persona 2 | Pendiente | 0% |
| ML/NLP | Persona 2 | Pendiente | 0% |
| Agente local/MCP | Persona 2 | Pendiente | 0% |
| QA, docs y demo | Ambos | En progreso | 25% |

Progreso global estimado de implementación: 34%.

---

# Persona 1 - Frontend / Streamlit / Demo

## Fase 1: base visual de la app

- [x] Crear `src/app/main.py`.
- [x] Crear navegación principal en sidebar.
- [x] Crear estructura de páginas en `src/app/pages/`.
- [x] Crear `src/app/components.py`.
- [x] Crear `src/app/styles.py`.
- [x] Cargar datos procesados desde `data/processed/scored_claims.csv`.
- [x] Mostrar aviso ético fijo: el sistema genera alertas para revisión humana.

## Fase 2: dashboard ejecutivo

- [x] Mostrar total de siniestros.
- [x] Mostrar cantidad de casos verdes.
- [x] Mostrar cantidad de casos amarillos.
- [x] Mostrar cantidad de casos rojos.
- [x] Mostrar monto total reclamado.
- [x] Mostrar monto asociado a casos rojos.
- [x] Crear gráfico de distribución por nivel de riesgo.
- [x] Crear gráfico de riesgo por ciudad.
- [x] Crear gráfico de riesgo por ramo.
- [x] Crear gráfico de top proveedores con alertas.

## Fase 3: bandeja de siniestros

- [x] Crear página `claims_inbox.py`.
- [x] Agregar filtros por nivel de riesgo.
- [x] Agregar filtros por ciudad.
- [x] Agregar filtros por ramo.
- [ ] Agregar filtros por cobertura.
- [x] Agregar filtros por proveedor.
- [ ] Agregar filtro por rango de monto.
- [x] Mostrar tabla ordenada por `score_final` descendente.
- [x] Mostrar acción sugerida para revisión.

## Fase 4: detalle de siniestro

- [x] Crear página `claim_detail.py`.
- [x] Agregar selector de `id_siniestro`.
- [x] Mostrar score final y semáforo.
- [x] Mostrar reglas activadas.
- [x] Mostrar explicación humana.
- [ ] Mostrar datos de póliza.
- [x] Mostrar datos del asegurado sintético.
- [x] Mostrar datos del vehículo.
- [x] Mostrar datos del proveedor.
- [x] Mostrar documentos entregados/faltantes.
- [x] Mostrar narrativas similares si existen.

## Fase 5: proveedores

- [x] Crear página `providers.py`.
- [x] Mostrar ranking de proveedores por alertas.
- [x] Mostrar casos rojos por proveedor.
- [x] Mostrar monto promedio reclamado.
- [ ] Mostrar porcentaje de casos observados.
- [ ] Mostrar indicador de lista restrictiva simulada.

## Fase 6: agente en interfaz

- [x] Crear página `agent_chat.py`.
- [ ] Conectar con `src/agent/agent_router.py`.
- [x] Agregar `st.chat_input`.
- [x] Agregar botones de preguntas rápidas.
- [x] Mostrar respuestas del agente con datos concretos.
- [x] Evitar que el agente use lenguaje acusatorio.

## Fase 7: reportes

- [x] Crear página `reports.py`.
- [x] Agregar descarga CSV de casos rojos.
- [x] Agregar descarga CSV de todos los scores.
- [x] Mostrar resumen ejecutivo.
- [x] Mostrar recomendaciones de revisión.

## Fase 8: pulido de demo

- [x] Revisar responsividad básica.
- [x] Revisar que textos no se corten.
- [x] Revisar colores del semáforo.
- [ ] Ensayar flujo: dashboard -> bandeja -> detalle -> agente -> reporte.
- [ ] Preparar capturas o video backup si aplica.

---

# Persona 2 - Backend / Datos / SQL / IA / Agente

## Fase 1: estructura base del proyecto

- [x] Crear carpetas `src/`, `data/`, `tests/`, `presentation/`.
- [x] Crear `README.md`.
- [x] Crear `requirements.txt`.
- [x] Crear `.env.example` sin credenciales.
- [x] Crear `.gitignore`.
- [x] Crear `setup_demo.py`.
- [x] Validar que no se agregue `.env` real.

## Fase 2: datos sintéticos

- [x] Crear `src/data_generation/generate_synthetic_data.py`.
- [ ] Generar `data/synthetic/claims.csv`.
- [ ] Generar `data/synthetic/policies.csv`.
- [ ] Generar `data/synthetic/insured.csv`.
- [ ] Generar `data/synthetic/vehicles.csv`.
- [ ] Generar `data/synthetic/providers.csv`.
- [ ] Generar `data/synthetic/documents.csv`.
- [ ] Usar IDs anónimos.
- [ ] Inyectar casos normales.
- [ ] Inyectar casos con señales de posible riesgo.
- [ ] Documentar supuestos del dataset.

## Fase 3: SQLite y consultas

- [x] Crear `src/database/build_database.py`.
- [ ] Crear base SQLite local desde CSV.
- [ ] Crear tablas `claims`.
- [ ] Crear tablas `policies`.
- [ ] Crear tablas `insured`.
- [ ] Crear tablas `vehicles`.
- [ ] Crear tablas `providers`.
- [ ] Crear tablas `documents`.
- [ ] Crear tabla `risk_scores`.
- [x] Crear `src/database/queries.py`.
- [ ] Crear consultas para dashboard.
- [ ] Crear consultas para agente.

## Fase 4: features

- [x] Crear `src/features/build_features.py`.
- [ ] Calcular días desde inicio de póliza.
- [ ] Calcular días hasta fin de póliza.
- [ ] Calcular días entre ocurrencia y reporte.
- [ ] Calcular frecuencia de reclamos por asegurado.
- [ ] Calcular frecuencia de reclamos por vehículo.
- [ ] Calcular recurrencia de proveedor.
- [ ] Calcular relación monto reclamado vs suma asegurada.
- [ ] Calcular indicadores de documentos incompletos.
- [ ] Calcular indicadores de documentos inconsistentes.

## Fase 5: reglas de riesgo

- [x] Crear `src/rules/fraud_rules.py`.
- [ ] Implementar regla borde de vigencia.
- [ ] Implementar regla reporte tardío.
- [ ] Implementar regla demora en robo.
- [ ] Implementar regla frecuencia de asegurado.
- [ ] Implementar regla frecuencia de vehículo.
- [ ] Implementar regla proveedor recurrente.
- [ ] Implementar regla documentos incompletos.
- [ ] Implementar regla documentos inconsistentes.
- [ ] Implementar regla dinámica sospechosa.
- [ ] Implementar regla tercero no identificado.
- [ ] Implementar regla narrativa similar.
- [ ] Implementar regla monto atípico.
- [ ] Cada regla debe devolver código, puntos, severidad, explicación y evidencia.

## Fase 6: scoring y explicabilidad

- [x] Crear `src/scoring/scoring_service.py`.
- [ ] Calcular `score_reglas`.
- [ ] Integrar `score_ml`.
- [ ] Integrar `score_anomalia`.
- [ ] Integrar `score_nlp`.
- [ ] Calcular `score_final`.
- [ ] Clasificar Verde, Amarillo y Rojo.
- [x] Crear `src/explainability/explain_score.py`.
- [ ] Generar explicación humana por caso.
- [ ] Guardar `data/processed/scored_claims.csv`.

## Fase 7: ML

- [x] Crear `src/models/train_model.py`.
- [x] Crear `src/models/fraud_classifier.py`.
- [x] Crear `src/models/anomaly_detector.py`.
- [ ] Entrenar RandomForestClassifier.
- [ ] Implementar LogisticRegression como fallback.
- [ ] Implementar IsolationForest si hay tiempo.
- [ ] Guardar modelo supervisado.
- [ ] Guardar modelo de anomalías si aplica.
- [ ] Guardar `data/processed/model_metrics.json`.
- [ ] Documentar que la etiqueta es simulada.

## Fase 8: NLP

- [x] Crear `src/nlp/narrative_similarity.py`.
- [ ] Vectorizar descripciones con TF-IDF.
- [ ] Calcular cosine similarity.
- [ ] Detectar narrativas similares.
- [ ] Calcular `score_nlp`.
- [ ] Guardar `max_similarity`.
- [ ] Guardar `similar_claim_id`.
- [ ] Generar explicación NLP.

## Fase 9: agente local

- [x] Crear `src/agent/agent_tools.py`.
- [x] Crear `src/agent/agent_router.py`.
- [ ] Implementar intención top riesgos.
- [ ] Implementar intención explicar siniestro.
- [ ] Implementar intención proveedores con alertas.
- [ ] Implementar intención ramos con riesgo.
- [ ] Implementar intención ciudades con alertas.
- [ ] Implementar intención asegurados frecuentes.
- [ ] Implementar intención documentos faltantes.
- [ ] Implementar intención montos atípicos.
- [ ] Implementar intención siniestros cerca de inicio de póliza.
- [ ] Implementar intención patrones repetidos.
- [ ] Implementar resumen ejecutivo.
- [ ] Implementar recomendación de casos para revisar.

## Fase 10: MCP opcional

- [x] Crear `src/mcp_server/server.py`.
- [ ] Exponer tool `get_top_risk_claims`.
- [ ] Exponer tool `explain_claim_risk`.
- [ ] Exponer tool `get_provider_alert_summary`.
- [ ] Exponer tool `get_city_risk_summary`.
- [ ] Exponer tool `get_missing_documents_critical`.
- [ ] Exponer tool `get_similar_narratives`.
- [ ] Exponer tool `simulate_claim_score`.
- [ ] Exponer tool `generate_executive_summary`.
- [x] Crear `docs/agente_mcp.md`.

## Fase 11: tests

- [ ] Crear tests de generación de datos.
- [ ] Crear tests de reglas.
- [ ] Crear tests de scoring.
- [ ] Crear tests de NLP.
- [ ] Crear tests de agente.
- [x] Validar que `pytest` ejecuta.

---

# Tareas compartidas

## Documentación

- [x] Completar `README.md`.
- [~] Completar documentación de modelo de datos.
- [~] Completar documentación de reglas.
- [~] Completar documentación de uso de IA.
- [~] Completar documentación de ética y privacidad.
- [~] Completar documentación de limitaciones.
- [ ] Mantener `docs/development.md` actualizado.
- [ ] Mantener este archivo actualizado.

## Seguridad y ética

- [ ] Confirmar que no hay datos reales.
- [ ] Confirmar que no hay credenciales.
- [ ] Confirmar que no hay API keys.
- [ ] Confirmar que `.env` real no se versiona.
- [ ] Confirmar que la app no acusa fraude.
- [ ] Confirmar que la app no recomienda rechazo automático.
- [ ] Confirmar que las explicaciones son trazables.

## Demo y pitch

- [ ] Preparar script de demo.
- [ ] Preparar presentación ejecutiva.
- [ ] Ensayar demo de 10 minutos.
- [ ] Preparar respuesta técnica sobre TF-IDF y cosine similarity.
- [ ] Preparar respuesta ética sobre revisión humana.
- [ ] Preparar respuesta de negocio sobre priorización de casos.
- [ ] Preparar video backup si hay tiempo.

---

# Registro rápido de avances

Usar esta sección para notas cortas. Los cambios importantes van también en `docs/development.md`.

```md
## YYYY-MM-DD

- Responsable:
- Área:
- Tarea marcada:
- Estado anterior:
- Estado nuevo:
- Bloqueo:
- Próximo paso:
```
