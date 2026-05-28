# Skills Operativas para Codex - FraudLens Claims AI

## Instrucciones generales

- Antes de modificar archivos, revisar `docs/arquitectura.md` y `docs/development.md`.
- Mantener código modular, reproducible y sin credenciales.
- Actualizar `docs/development.md` después de cada cambio importante.
- No usar datos reales.
- No agregar dependencias innecesarias.
- No cambiar el stack definido.
- No proponer login, roles, microservicios ni arquitectura pesada.
- Mantener el lenguaje del producto como alerta para revisión humana, no acusación de fraude.

## Skill de arquitecto técnico

### Rol

Definir y proteger la arquitectura del MVP.

### Responsabilidades

- Mantener separación entre datos, reglas, scoring, ML/NLP, agente y UI.
- Validar que las decisiones técnicas respeten el alcance del hackathon.
- Documentar cambios relevantes en arquitectura.

### Archivos donde debe trabajar

- `docs/arquitectura.md`
- `README.md`
- `requirements.txt`
- `.env.example`
- Estructura de carpetas del repo.

### Reglas que debe respetar

- Streamlit es el frontend.
- Python 3.11 es el lenguaje principal.
- CSV sintéticos y SQLite son la base de datos del MVP.
- MCP es opcional.
- FastAPI, Docker y bases corporativas reales no son obligatorios.

### Qué no debe hacer

- No introducir React.
- No imponer microservicios.
- No agregar login ni roles.
- No convertir el MVP en una arquitectura empresarial pesada.

### Criterios de terminado

- La arquitectura está documentada.
- La estructura del repo es clara.
- Las decisiones descartadas están justificadas.
- El MVP puede ejecutarse localmente.

## Skill de desarrollador Streamlit

### Rol

Construir el dashboard funcional para la demo.

### Responsabilidades

- Crear navegación clara.
- Mostrar KPIs, bandeja, detalle, proveedores, agente y reportes.
- Usar Plotly para visualizaciones.
- Mostrar advertencia ética visible.

### Archivos donde debe trabajar

- `src/app/main.py`
- `src/app/components.py`
- `src/app/styles.py`
- `src/app/pages/dashboard.py`
- `src/app/pages/claims_inbox.py`
- `src/app/pages/claim_detail.py`
- `src/app/pages/providers.py`
- `src/app/pages/agent_chat.py`
- `src/app/pages/reports.py`

### Reglas que debe respetar

- Consumir datos procesados, no recalcular todo en la UI.
- Ordenar casos por prioridad de revisión.
- Usar colores verde, amarillo y rojo solo como semáforo de riesgo.
- Evitar lenguaje acusatorio.

### Qué no debe hacer

- No crear frontend React.
- No depender de una API externa obligatoria.
- No pedir credenciales para usar la demo.

### Criterios de terminado

- `streamlit run src/app/main.py` abre la app.
- El dashboard permite revisar casos críticos.
- El detalle explica el score.
- El agente se puede usar desde la interfaz.

## Skill de ingeniero de datos sintéticos

### Rol

Crear datos sintéticos realistas y seguros para la demo.

### Responsabilidades

- Generar claims, policies, insured, vehicles, providers y documents.
- Inyectar patrones de posible riesgo.
- Crear datos suficientes para dashboard, reglas, ML y NLP.
- Garantizar anonimización completa.

### Archivos donde debe trabajar

- `src/data_generation/generate_synthetic_data.py`
- `src/database/build_database.py`
- `src/database/queries.py`
- `data/synthetic/`
- `data/processed/`

### Reglas que debe respetar

- Usar solo datos sintéticos.
- Usar IDs anónimos.
- Generar patrones normales y sospechosos.
- Mantener reproducibilidad con semilla controlada.

### Qué no debe hacer

- No usar nombres, documentos, teléfonos, correos o placas reales.
- No descargar datasets sensibles.
- No introducir bases externas obligatorias.

### Criterios de terminado

- Existen CSV sintéticos.
- La base SQLite puede reconstruirse.
- Las tablas mínimas están presentes.
- Los datos soportan reglas, ML y dashboard.

## Skill de ingeniero ML/NLP

### Rol

Implementar modelos de apoyo al score de riesgo.

### Responsabilidades

- Entrenar RandomForestClassifier.
- Mantener LogisticRegression como fallback.
- Implementar IsolationForest si hay tiempo.
- Implementar TF-IDF y cosine similarity para narrativas.
- Guardar métricas básicas.

### Archivos donde debe trabajar

- `src/features/build_features.py`
- `src/models/train_model.py`
- `src/models/fraud_classifier.py`
- `src/models/anomaly_detector.py`
- `src/nlp/narrative_similarity.py`
- `data/processed/model_metrics.json`

### Reglas que debe respetar

- El modelo no decide fraude.
- La etiqueta es simulada y debe documentarse como tal.
- Los scores deben integrarse al scoring final.
- Las métricas deben ser entendibles para jurado.

### Qué no debe hacer

- No usar LLM para decidir el score.
- No presentar predicciones como verdad legal.
- No agregar frameworks de deep learning innecesarios.

### Criterios de terminado

- Hay score ML disponible o fallback documentado.
- Hay score NLP de similitud de narrativas.
- Hay métricas guardadas.
- Las salidas alimentan `score_final`.

## Skill de explicabilidad y ética

### Rol

Garantizar que el sistema sea trazable, claro y responsable.

### Responsabilidades

- Explicar reglas activadas.
- Redactar explicaciones humanas por caso.
- Documentar límites, sesgos y falsos positivos.
- Revisar lenguaje de app y docs.

### Archivos donde debe trabajar

- `src/explainability/explain_score.py`
- `docs/arquitectura.md`
- `docs/etica_privacidad.md`
- `docs/limitaciones.md`
- `README.md`

### Reglas que debe respetar

- Usar "posible riesgo", "alerta" y "revisión humana".
- Aclarar que no hay acusación ni rechazo automático.
- Mantener trazabilidad entre score y señales.

### Qué no debe hacer

- No escribir "fraude confirmado".
- No recomendar rechazar un siniestro automáticamente.
- No ocultar limitaciones del dataset sintético.

### Criterios de terminado

- Cada caso crítico tiene explicación.
- La advertencia ética aparece en app y docs.
- Las limitaciones están documentadas.
- El score es defendible ante el jurado.

## Skill de agente IA/MCP

### Rol

Crear un agente consultivo controlado para explorar patrones.

### Responsabilidades

- Implementar tools locales.
- Implementar router por intención.
- Responder preguntas esperadas del reto.
- Evaluar MCP como capa opcional.

### Archivos donde debe trabajar

- `src/agent/agent_tools.py`
- `src/agent/agent_router.py`
- `src/mcp_server/server.py`
- `docs/agente_mcp.md`

### Reglas que debe respetar

- El agente consulta datos procesados mediante funciones.
- El agente no recalcula arbitrariamente el score.
- MCP no debe bloquear el MVP.
- Las respuestas deben usar datos concretos.

### Qué no debe hacer

- No depender obligatoriamente de un LLM externo.
- No dar recomendaciones legales.
- No ejecutar consultas libres sin control.

### Criterios de terminado

- El agente responde top riesgos, explicación de caso, proveedores, ciudades, documentos, narrativas y resumen ejecutivo.
- Las respuestas son claras y trazables.
- MCP, si existe, llama a las mismas tools locales.

## Skill de QA y revisión

### Rol

Validar que el proyecto sea ejecutable, coherente y listo para demo.

### Responsabilidades

- Crear pruebas pytest básicas.
- Probar generación de datos, reglas y scoring.
- Revisar que no existan credenciales ni datos reales.
- Verificar comandos de demo.
- Revisar consistencia de documentación.

### Archivos donde debe trabajar

- `tests/`
- `docs/development.md`
- `README.md`
- `.gitignore`
- `requirements.txt`

### Reglas que debe respetar

- Priorizar pruebas de alto valor para el MVP.
- Reportar riesgos sin bloquear avances menores.
- Mantener checklist actualizado.

### Qué no debe hacer

- No exigir cobertura extensa de producción.
- No introducir herramientas pesadas de QA.
- No modificar lógica sin entender reglas y score.

### Criterios de terminado

- `pytest` ejecuta pruebas básicas.
- La demo corre con comandos documentados.
- No hay secretos en archivos del repo.
- Los checklists finales están revisados.
