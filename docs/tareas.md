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
| Frontend Streamlit | Persona 1 | En progreso | 75% |
| Backend, datos y SQL | Persona 2 | En progreso | 70% |
| Reglas y scoring | Persona 2 | En progreso | 70% |
| ML/NLP | Persona 2 | En progreso | 55% |
| Agente local/MCP | Persona 2 | En progreso | 55% |
| QA, docs y demo | Ambos | En progreso | 60% |

Progreso global estimado de implementación: 70%.

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
- [x] Conectar con `src/agent/agent_router.py`.
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
- [x] Generar `data/synthetic/claims.csv`.
- [x] Generar `data/synthetic/policies.csv`.
- [x] Generar `data/synthetic/insured.csv`.
- [x] Generar `data/synthetic/vehicles.csv`.
- [x] Generar `data/synthetic/providers.csv`.
- [x] Generar `data/synthetic/documents.csv`.
- [x] Usar IDs anónimos.
- [x] Inyectar casos normales.
- [x] Inyectar casos con señales de posible riesgo.
- [x] Documentar supuestos del dataset.

## Fase 3: MySQL y consultas

- [x] Crear `src/database/build_database.py`.
- [x] Crear base MySQL local desde CSV.
- [x] Crear tablas `claims`.
- [x] Crear tablas `policies`.
- [x] Crear tablas `insured`.
- [x] Crear tablas `vehicles`.
- [x] Crear tablas `providers`.
- [x] Crear tablas `documents`.
- [x] Crear tabla `risk_scores`.
- [x] Crear `src/database/queries.py`.
- [ ] Crear consultas para dashboard.
- [ ] Crear consultas para agente.

## Fase 4: features

- [x] Crear `src/features/build_features.py`.
- [x] Calcular días desde inicio de póliza.
- [x] Calcular días hasta fin de póliza.
- [x] Calcular días entre ocurrencia y reporte.
- [x] Calcular frecuencia de reclamos por asegurado.
- [x] Calcular frecuencia de reclamos por vehículo.
- [x] Calcular recurrencia de proveedor.
- [x] Calcular relación monto reclamado vs suma asegurada.
- [x] Calcular indicadores de documentos incompletos.
- [x] Calcular indicadores de documentos inconsistentes.

## Fase 5: reglas de riesgo

- [x] Crear `src/rules/fraud_rules.py`.
- [x] Implementar regla borde de vigencia.
- [x] Implementar regla reporte tardío.
- [x] Implementar regla demora en robo.
- [x] Implementar regla frecuencia de asegurado.
- [x] Implementar regla frecuencia de vehículo.
- [x] Implementar regla proveedor recurrente.
- [x] Implementar regla documentos incompletos.
- [x] Implementar regla documentos inconsistentes.
- [x] Implementar regla dinámica sospechosa.
- [x] Implementar regla tercero no identificado.
- [x] Implementar regla narrativa similar.
- [x] Implementar regla monto atípico.
- [x] Cada regla debe devolver código, puntos, severidad, explicación y evidencia.

## Fase 6: scoring y explicabilidad

- [x] Crear `src/scoring/scoring_service.py`.
- [x] Calcular `score_reglas`.
- [x] Integrar `score_ml`.
- [x] Integrar `score_anomalia`.
- [x] Integrar `score_nlp`.
- [x] Calcular `score_final`.
- [x] Clasificar Verde, Amarillo y Rojo.
- [x] Crear `src/explainability/explain_score.py`.
- [x] Generar explicación humana por caso.
- [x] Guardar `data/processed/scored_claims.csv`.

## Fase 7: ML

- [x] Crear `src/models/train_model.py`.
- [x] Crear `src/models/fraud_classifier.py`.
- [x] Crear `src/models/anomaly_detector.py`.
- [x] Entrenar RandomForestClassifier.
- [x] Implementar LogisticRegression como fallback.
- [x] Implementar IsolationForest si hay tiempo.
- [x] Guardar modelo supervisado.
- [x] Guardar modelo de anomalías si aplica.
- [x] Guardar `data/processed/model_metrics.json`.
- [ ] Documentar que la etiqueta es simulada.

## Fase 8: NLP

- [x] Crear `src/nlp/narrative_similarity.py`.
- [x] Vectorizar descripciones con TF-IDF.
- [x] Calcular cosine similarity.
- [x] Detectar narrativas similares.
- [x] Calcular `score_nlp`.
- [x] Guardar `max_similarity`.
- [x] Guardar `similar_claim_id`.
- [x] Generar explicación NLP.

## Fase 9: agente local

- [x] Crear `src/agent/agent_tools.py`.
- [x] Crear `src/agent/agent_router.py`.
- [x] Implementar intención top riesgos.
- [x] Implementar intención explicar siniestro.
- [x] Implementar intención proveedores con alertas.
- [x] Implementar intención ramos con riesgo.
- [x] Implementar intención ciudades con alertas.
- [ ] Implementar intención asegurados frecuentes.
- [x] Implementar intención documentos faltantes.
- [x] Implementar intención montos atípicos.
- [x] Implementar intención siniestros cerca de inicio de póliza.
- [x] Implementar intención patrones repetidos.
- [x] Implementar resumen ejecutivo.
- [x] Implementar recomendación de casos para revisar.

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

- [x] Crear tests de generación de datos.
- [ ] Crear tests de reglas.
- [x] Crear tests de scoring.
- [ ] Crear tests de NLP.
- [x] Crear tests de agente.
- [x] Validar que `pytest` ejecuta.

---

# Tareas compartidas

## Documentación

- [x] Completar `README.md`.
- [x] Completar documentación de modelo de datos.
- [x] Completar documentación de reglas.
- [x] Completar documentación de uso de IA.
- [x] Completar documentación de ética y privacidad.
- [x] Completar documentación de limitaciones.
- [x] Mantener `docs/development.md` actualizado.
- [x] Mantener este archivo actualizado.

## Seguridad y ética

- [x] Confirmar que no hay datos reales.
- [x] Confirmar que no hay credenciales.
- [x] Confirmar que no hay API keys.
- [x] Confirmar que `.env` real no se versiona.
- [x] Confirmar que la app no acusa fraude.
- [x] Confirmar que la app no recomienda rechazo automático.
- [x] Confirmar que las explicaciones son trazables.

## Demo y pitch

- [x] Preparar script de demo.
- [ ] Preparar presentación ejecutiva.
- [ ] Ensayar demo de 10 minutos.
- [x] Preparar respuesta técnica sobre TF-IDF y cosine similarity.
- [x] Preparar respuesta ética sobre revisión humana.
- [x] Preparar respuesta de negocio sobre priorización de casos.
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
