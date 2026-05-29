# Bitácora de Desarrollo - FraudLens Claims AI

## Propósito

Este archivo registra avances, decisiones, problemas y pendientes del proyecto. Debe permitir entender qué se hizo, por qué se hizo y qué falta para completar la demo del hackathon.

Actualizar este documento después de cada cambio importante.

## Cómo registrar avances diarios

Cada entrada debe ser breve, concreta y trazable. Registrar solo cambios relevantes para arquitectura, datos, reglas, IA, dashboard, agente, pruebas, documentación o demo.

Regla obligatoria: toda entrada debe indicar si el cambio fue `frontend`, `backend`, `datos`, `ml-nlp`, `agente`, `documentacion`, `qa`, `seguridad` o `repo/config`. Si toca varias áreas, listarlas todas.

Regla de seguridad: antes de cerrar una tarea, confirmar que no se agregaron datos reales, credenciales, API keys, `.env` real ni lenguaje acusatorio.

Regla de progreso: cada actualización importante debe indicar porcentaje estimado de avance del MVP y qué tarea se completó o falta.

Regla de ramas y commits: cada tarea debe trabajarse en una rama separada, indicando nombre de rama y descripción detallada del commit esperado. La rama `main` queda como rama estable de integración.

Flujo obligatorio de Git:

1. Cambiar a `main`.
2. Actualizar con `git pull origin main`.
3. Crear una rama nueva desde `main`.
4. Hacer cambios y commit en la rama.
5. Subir la rama al remoto.
6. Crear PR hacia `main` cuando haya GitHub CLI o hacerlo desde GitHub web.
7. Integrar a `main` solo después de revisar el cambio.
8. Actualizar `main` local después del merge.

## Plantilla de entrada

```md
## YYYY-MM-DD - Título breve

- Responsable:
- Tipo de cambio:
- Rama:
- Descripción de commit:
- Tarea:
- Archivos modificados:
- Decisión tomada:
- Revisión de seguridad:
- Problema encontrado:
- Solución aplicada:
- Tarea completada:
- Tarea pendiente:
- Progreso estimado:
- Siguiente paso:
```

## Estado de progreso del MVP

| Área | Estado | Progreso |
|---|---|---:|
| Documentación base | En progreso | 95% |
| Integración Codex skills/agentes | Completo | 100% |
| Tablero de tareas por rol | Completo | 100% |
| Estructura de repo ejecutable | Completo | 100% |
| Datos sintéticos | En progreso | 80% |
| Reglas y score | En progreso | 70% |
| ML/NLP | En progreso | 55% |
| Dashboard Streamlit | En progreso | 85% |
| Agente local/MCP | En progreso | 82% |
| QA/demo/pitch | En progreso | 85% |

Progreso global estimado: 85%.

## Plan de trabajo por fases

### Fase 1: estructura base y datos sintéticos

- Crear estructura de carpetas.
- Crear `requirements.txt`, `.env.example`, `.gitignore` y `README.md`.
- Generar CSV sintéticos.
- Crear MySQL local.
- Validar que no existan datos reales ni credenciales.

### Fase 2: reglas y score

- Implementar reglas de posible riesgo.
- Calcular `score_reglas`.
- Definir reglas críticas.
- Crear `score_final` inicial aunque ML/NLP no estén listos.
- Generar explicación por caso.

### Fase 3: ML/NLP

- Entrenar RandomForestClassifier con etiqueta simulada.
- Implementar LogisticRegression como fallback.
- Implementar IsolationForest si hay tiempo.
- Calcular similitud de narrativas con TF-IDF y cosine similarity.
- Guardar métricas básicas.

### Fase 4: dashboard

- Construir app Streamlit.
- Crear dashboard ejecutivo.
- Crear bandeja de siniestros priorizados.
- Crear detalle del caso.
- Crear vista de proveedores.
- Crear reportes descargables.
- Mostrar advertencia ética visible.

### Fase 5: agente

- Crear tools locales.
- Crear `agent_router` por intención y keywords.
- Responder preguntas esperadas del reto.
- Conectar el agente al dashboard.
- Evaluar MCP solo si el MVP ya funciona.

### Fase 6: documentación, demo y pitch

- Completar README.
- Completar documentación técnica.
- Preparar script de demo.
- Crear pitch ejecutivo.
- Ejecutar pruebas básicas.
- Ensayar flujo completo.
- Preparar Streamlit Community Cloud solo como backup.

## Checklist diario

- [ ] Se revisó `docs/arquitectura.md`.
- [ ] Se revisó `docs/development.md`.
- [ ] Si hubo duda de alcance, se revisaron los MD base: `FraudLens_Claims_AI_Plan_HackIAthon.md` y `Proyecto.md`.
- [ ] La app o scripts principales siguen ejecutando.
- [ ] No se agregaron dependencias innecesarias.
- [ ] No se usaron datos reales.
- [ ] No se agregaron credenciales.
- [ ] No se agregó lenguaje acusatorio ni decisión automática.
- [ ] Se clasificó el cambio como frontend/backend/datos/ml-nlp/agente/documentación/qa/seguridad/repo-config.
- [ ] Se informó tarea realizada, tarea pendiente y porcentaje de progreso.
- [ ] Los cambios respetan `docs/arquitectura.md`.
- [ ] Las decisiones relevantes quedaron registradas aquí.
- [ ] Hay siguiente paso claro.

## Checklist final antes de entrega

- [ ] `setup_demo.py` prepara datos y resultados desde cero.
- [ ] `streamlit run src/app/main.py` abre la demo.
- [ ] Existen CSV sintéticos.
- [ ] Existe MySQL local o CSV procesado equivalente.
- [ ] El dashboard muestra KPIs.
- [ ] La bandeja ordena casos por `score_final`.
- [ ] El detalle muestra reglas, score y explicación.
- [ ] El agente responde preguntas clave.
- [ ] Se pueden exportar casos críticos.
- [ ] Hay README con instalación y ejecución.
- [ ] Hay `requirements.txt`.
- [ ] Hay `.env.example` sin secretos.
- [ ] Hay pruebas pytest básicas.
- [ ] La documentación explica arquitectura, score, datos, IA y ética.
- [ ] La app aclara que no acusa fraude.
- [ ] No existe `.env` real versionado.
- [ ] No hay API keys ni credenciales.
- [ ] Pitch y demo están ensayados.

## Registro inicial de decisiones técnicas

- El frontend será Streamlit.
- El lenguaje principal será Python 3.11.
- Los datos serán sintéticos.
- La persistencia será MySQL + CSV procesados.
- El procesamiento usará Pandas y NumPy.
- Los gráficos usarán Plotly.
- El modelo supervisado principal será RandomForestClassifier.
- LogisticRegression queda como fallback.
- IsolationForest es opcional.
- NLP usará TF-IDF y cosine similarity.
- El agente será local, basado en funciones/tools.
- MCP es opcional y no bloquea el MVP.
- La demo local tiene prioridad sobre deploy externo.
- No se implementarán login, roles, microservicios ni Docker obligatorio.

## Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Dataset sintético poco creíble | Debilita demo y ML | Inyectar patrones claros y documentar supuestos. |
| Score difícil de explicar | Reduce confianza del jurado | Priorizar reglas trazables y explicación textual. |
| ML no mejora el resultado | Puede parecer accesorio | Mostrarlo como apoyo al score, no como juez. |
| MCP consume demasiado tiempo | Retrasa MVP | Implementarlo solo después del agente local. |
| Dashboard incompleto | Afecta demo | Priorizar KPIs, bandeja, detalle y agente. |
| Lenguaje acusatorio | Riesgo ético | Usar "alerta", "posible riesgo" y "revisión humana". |
| Dependencias o entorno fallan | Demo bloqueada | Mantener demo local simple y documentar comandos. |

## Bugs conocidos

Registrar aquí errores detectados que aún no estén resueltos.

```md
- [ ] Descripción:
  - Impacto:
  - Archivo:
  - Estado:
```

## Pendientes

- [ ] Crear estructura base del repo.
- [ ] Crear generador de datos sintéticos.
- [ ] Crear MySQL.
- [ ] Implementar reglas.
- [ ] Implementar scoring.
- [ ] Implementar ML/NLP.
- [ ] Implementar Streamlit.
- [ ] Implementar agente local.
- [ ] Agregar pruebas.
- [ ] Completar README.
- [ ] Preparar pitch.

## Comandos útiles

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python setup_demo.py
streamlit run src/app/main.py
pytest
```

## 2026-05-27 - Inicio de documentación técnica

- Responsable: Codex.
- Tipo de cambio: documentación, repo/config.
- Tarea: Crear documentación base para orientar desarrollo del MVP.
- Archivos modificados: `docs/arquitectura.md`, `docs/development.md`, `docs/skills_codex_fraudlens.md`.
- Decisión tomada: Mantener arquitectura liviana con Streamlit, Python, CSV, MySQL, reglas, ML/NLP y agente local.
- Revisión de seguridad: No se agregaron datos reales, credenciales ni decisiones automáticas.
- Problema encontrado: Los documentos base son extensos y contienen contenido repetido.
- Solución aplicada: Consolidar decisiones y estructura sin reescribir todo el material fuente.
- Tarea completada: Documentación inicial de arquitectura y bitácora.
- Tarea pendiente: Convertir instrucciones de Codex en skills operativos.
- Progreso estimado: 8%.
- Siguiente paso: Crear estructura base del repositorio y archivos mínimos del proyecto.

## 2026-05-27 - Integración operativa de Codex

- Responsable: Codex.
- Tipo de cambio: repo/config, documentación, seguridad.
- Tarea: Crear skills reales, perfiles de agentes/subagentes, manifiesto de contexto y scripts de bootstrap para Codex.
- Archivos modificados: `.codex/fraudlens.yml`, `.codex/skills/`, `.codex/agents/`, `scripts/codex_context.ps1`, `scripts/codex_bootstrap.ps1`, `docs/development.md`.
- Decisión tomada: Mantener skills versionados dentro del repo y permitir instalación global con script.
- Revisión de seguridad: Los scripts no incluyen credenciales ni descargan datos; solo leen contexto o copian skills locales.
- Problema encontrado: Los resources `references/` y `scripts/` de los skills estaban vacíos y no había regla formal para reportar frontend/backend, seguridad y progreso.
- Solución aplicada: Agregar referencias operativas, scripts de verificación de contexto por skill, manifiesto `.codex/fraudlens.yml`, agentes YAML y plantilla reforzada de bitácora.
- Tarea completada: Capa operativa de Codex para cargar contexto y trabajar por rol.
- Tarea pendiente: Crear estructura base ejecutable del proyecto.
- Progreso estimado: 15%.
- Siguiente paso: Crear carpetas base, README, requirements, `.env.example`, `.gitignore` y `setup_demo.py`.

## 2026-05-27 - Tablero de tareas por persona

- Responsable: Codex.
- Tipo de cambio: documentacion, repo/config.
- Tarea: Crear un archivo dedicado para dividir y marcar tareas entre frontend y backend/datos/SQL/IA.
- Archivos modificados: `docs/tareas.md`, `docs/development.md`.
- Decisión tomada: Separar tareas por Persona 1 Frontend y Persona 2 Backend/Datos/SQL/IA, con tareas compartidas de documentación, seguridad y demo.
- Revisión de seguridad: No se agregaron datos reales, credenciales, API keys ni lógica de decisión automática.
- Problema encontrado: La bitácora general no era suficiente como tablero operativo diario para dos personas.
- Solución aplicada: Crear checklist específico por rol y fases.
- Tarea completada: Tablero de tareas creado.
- Tarea pendiente: Empezar estructura base ejecutable del repo.
- Progreso estimado: 17%.
- Siguiente paso: Crear carpetas base, README, requirements, `.env.example`, `.gitignore` y `setup_demo.py`.

## 2026-05-27 - Arquitectura de archivos del MVP

- Responsable: Codex.
- Tipo de cambio: repo/config, documentacion, backend, frontend, datos, ml-nlp, agente, qa, seguridad.
- Tarea: Crear toda la estructura de archivos del proyecto sin implementar lógica de negocio.
- Archivos modificados: `README.md`, `requirements.txt`, `.env.example`, `.gitignore`, `setup_demo.py`, `src/`, `data/`, `tests/`, `notebooks/`, `presentation/`, `docs/estructura_repo.md`, `docs/tareas.md`, `docs/development.md`.
- Decisión tomada: Crear placeholders por módulo para conectar arquitectura, responsabilidades y futuras fases, manteniendo Streamlit + Python + CSV/MySQL + Scikit-learn + agente local.
- Revisión de seguridad: No se agregaron datos reales, credenciales, API keys, `.env` real, lógica de acusación ni rechazo automático.
- Problema encontrado: El repo tenía documentación y configuración Codex, pero no la estructura ejecutable base del MVP.
- Solución aplicada: Crear carpetas y archivos mínimos por capa con docstrings y documentación de responsabilidad, sin lógica de negocio.
- Tarea completada: Arquitectura de archivos base creada y tablero de tareas actualizado.
- Tarea pendiente: Implementar generación de datos sintéticos y flujo `setup_demo.py`.
- Progreso estimado: 25%.
- Siguiente paso: Implementar Fase 1 de datos sintéticos o, si se desea mantener arquitectura pura, revisar nombres y responsabilidades antes de programar.

## 2026-05-27 - Publicación inicial en GitHub

- Responsable: Codex.
- Tipo de cambio: repo/config, documentacion, seguridad.
- Rama: main.
- Descripción de commit: Publicar estructura inicial de FraudLens Claims AI con arquitectura, documentación, tablero de tareas, skills Codex y placeholders del MVP.
- Tarea: Inicializar Git, crear rama `main`, configurar remoto GitHub y subir el estado actual del proyecto.
- Archivos modificados: `docs/development.md`, `.codex/fraudlens.yml`.
- Decisión tomada: Usar `main` como rama estable inicial; las siguientes tareas deben ir en ramas separadas por funcionalidad.
- Revisión de seguridad: Antes del commit se confirma que no existe `.env` real, credenciales, bases MySQL con datos reales, CSV generados ni datos reales.
- Problema encontrado: La carpeta local aún no estaba inicializada como repositorio Git.
- Solución aplicada: Inicializar repo local y preparar push al remoto indicado por el usuario.
- Tarea completada: Repo local inicializado en `main`, remoto configurado y commit inicial creado.
- Tarea pendiente: Completar publicación remota con credenciales autorizadas.
- Progreso estimado: 26%.
- Siguiente paso: Ejecutar commit inicial y subir a GitHub.

## 2026-05-27 - README e instalación de dependencias

- Responsable: Codex.
- Tipo de cambio: documentacion, repo/config, qa.
- Rama: docs/readme-install-deps.
- Descripción de commit: Ampliar README con contexto del reto, alcance, stack, estructura, instalación, ejecución, entregables, seguridad y estado del MVP; verificar instalación de dependencias del proyecto.
- Tarea: Ajustar `README.md` según los requisitos de `Proyecto.md` e instalar dependencias desde `requirements.txt`.
- Archivos modificados: `README.md`, `docs/development.md`, `docs/tareas.md`.
- Decisión tomada: Mantener instalación estándar con `pip install -r requirements.txt` y documentar que el proyecto aún está en fase de arquitectura/placeholders.
- Revisión de seguridad: No se agregaron datos reales, credenciales, API keys ni `.env` real. El README mantiene lenguaje de alerta para revisión humana.
- Problema encontrado: `pip install -r requirements.txt` falló inicialmente por bloqueo de red/permisos.
- Solución aplicada: Reintentar instalación con permisos de red aprobados; dependencias instaladas en user site-packages porque el site-packages global no es escribible.
- Tarea completada: README ampliado, dependencias instaladas y versiones importadas verificadas.
- Tarea pendiente: Integrar rama a `main` y confirmar si se usará entorno virtual local `venv` para aislar dependencias antes de implementar datos.
- Progreso estimado: 28%.
- Siguiente paso: Commit y push de la rama `docs/readme-install-deps`.

## 2026-05-27 - Integración de rama README a main

- Responsable: Codex.
- Tipo de cambio: repo/config, documentacion.
- Rama: docs/readme-install-deps -> main.
- Descripción de commit: Registrar flujo obligatorio de ramas desde `main`, integración por PR o merge revisado y actualización de `main` antes de crear nuevas ramas.
- Tarea: Integrar la rama `docs/readme-install-deps` a `main` después de subirla.
- Archivos modificados: `docs/development.md`.
- Decisión tomada: Como GitHub CLI no está instalado, se hará merge local controlado a `main` y push al remoto.
- Revisión de seguridad: No se agregaron datos reales, credenciales, API keys ni `.env` real.
- Problema encontrado: No existe `gh` en el entorno para crear PR desde terminal.
- Solución aplicada: Documentar flujo de PR y usar merge local revisado como alternativa.
- Tarea completada: Pendiente de merge a `main`.
- Tarea pendiente: Cambiar a `main`, actualizarla, mergear la rama y empujar `main`.
- Progreso estimado: 29%.
- Siguiente paso: Merge local de `docs/readme-install-deps` hacia `main`.

## 2026-05-27 - Frontend Streamlit inicial

- Responsable: Codex.
- Tipo de cambio: frontend, qa, seguridad.
- Rama: feature/frontend-streamlit-dashboard.
- Descripción de commit: Implementar dashboard Streamlit inicial con navegación, estilos responsive, datos demo sintéticos de fallback, KPIs, bandeja filtrable, detalle, proveedores, agente demo, reportes y pruebas mínimas del frontend.
- Tarea: Construir primera versión funcional del frontend sin implementar lógica backend, reglas, ML ni SQL.
- Archivos modificados: `src/app/`, `tests/test_frontend_demo_data.py`, `docs/development.md`, `docs/tareas.md`.
- Decisión tomada: Usar Streamlit + Plotly y datos demo sintéticos de fallback para permitir desarrollo visual antes de que backend genere `scored_claims.csv`.
- Revisión de seguridad: No se agregaron datos reales, credenciales, API keys ni `.env` real. La UI mantiene aviso de revisión humana y evita lenguaje acusatorio.
- Problema encontrado: `pytest` no ejecutaba pruebas porque los tests previos eran placeholders sin funciones.
- Solución aplicada: Agregar pruebas mínimas para validar el dataset demo del frontend.
- Tarea completada: UI inicial responsive, navegación multipágina, pruebas frontend y validación local de Streamlit en `http://localhost:8501`.
- Tarea pendiente: Conectar frontend con backend real cuando existan datos sintéticos procesados y agente local.
- Progreso estimado: 34%.
- Siguiente paso: Subir rama e integrar a `main`.

## 2026-05-27 - Datos sintéticos y base local

- Responsable: Codex.
- Tipo de cambio: datos, backend, qa, documentacion, seguridad.
- Rama: feature/datos-sinteticos.
- Descripción de commit: Implementar generador reproducible de CSV sintéticos, construcción de base local, consultas básicas, orquestación en `setup_demo.py`, documentación del modelo de datos y pruebas de generación/base.
- Tarea: Crear dataset sintético base y base local para reemplazar gradualmente el fallback demo del frontend.
- Archivos modificados: `src/data_generation/generate_synthetic_data.py`, `src/database/build_database.py`, `src/database/queries.py`, `setup_demo.py`, `tests/test_synthetic_data_generation.py`, `tests/test_database_build.py`, `docs/modelo_datos.md`, `docs/development.md`, `docs/tareas.md`.
- Decisión tomada: Generar artefactos locales reproducibles con semilla fija y mantener CSV procesados fuera de Git mediante `.gitignore`.
- Revisión de seguridad: No se usaron datos reales, credenciales, nombres, teléfonos, correos, documentos ni placas reales. Los identificadores son sintéticos y anónimos.
- Problema encontrado: El repo solo tenía placeholders de datos y la UI dependía de fallback demo.
- Solución aplicada: Crear generador con entidades mínimas, patrones de riesgo sintéticos y base local con tablas `claims`, `policies`, `insured`, `vehicles`, `providers`, `documents` y `risk_scores`.
- Tarea completada: `setup_demo.py` genera CSV sintéticos y base local; tests de datos/base pasan.
- Tarea pendiente: Construir features, reglas y `scored_claims.csv` para alimentar directamente el dashboard.
- Progreso estimado: 42%.
- Siguiente paso: Commit, subir rama e integrar a `main`.

## 2026-05-28 - Scoring hibrido, ML/NLP y agente local

- Responsable: Codex.
- Tipo de cambio: backend, datos, ml-nlp, agente, frontend, qa, documentacion, seguridad.
- Rama: feature/mysql-support.
- Descripción de commit: Implementar pipeline reproducible de features, reglas, ML, anomalias, NLP, score final, explicaciones, agente local y pruebas minimas.
- Tarea: Pasar de datos sinteticos sin score a una demo end-to-end con `scored_claims.csv` compatible con Streamlit.
- Archivos modificados: `setup_demo.py`, `src/database/build_database.py`, `src/features/build_features.py`, `src/rules/fraud_rules.py`, `src/nlp/narrative_similarity.py`, `src/models/`, `src/scoring/scoring_service.py`, `src/explainability/explain_score.py`, `src/agent/`, `src/app/pages/agent_chat.py`, `tests/`, `docs/tareas.md`, `docs/development.md`.
- Decisión tomada: Usar MySQL como ruta principal de demo y producir un contrato enriquecido para UI, no solo una tabla `risk_scores`.
- Revisión de seguridad: No se agregaron datos reales, credenciales, API keys ni `.env` real. Las explicaciones mantienen lenguaje de alerta para revisión humana y no confirman fraude.
- Problema encontrado: `src/database/build_database.py` estaba eliminado en el worktree y `risk_scores` estaba vacio; la UI fallaria si `scored_claims.csv` no incluia columnas enriquecidas.
- Solución aplicada: Restaurar `build_database.py`, crear features con joins, reglas trazables, TF-IDF, RandomForest con fallback LogisticRegression, IsolationForest, score ponderado, explicaciones, agente local y pruebas.
- Tarea completada: `python setup_demo.py` genera 1000 siniestros procesados, `data/processed/scored_claims.csv`, `risk_scores.csv`, modelos y `model_metrics.json`; `pytest` pasa.
- Tarea pendiente: Pulir reportes de dominio, ampliar docs de reglas/IA/etica, completar consultas SQL para dashboard/agente y decidir si MCP se implementa como diferenciador.
- Progreso estimado: 60%.
- Siguiente paso: Ensayar flujo Streamlit completo y preparar documentacion/pitch de uso de IA.

## 2026-05-28 - Correccion a MySQL y mejora visual de Streamlit

- Responsable: Codex.
- Tipo de cambio: backend, datos, frontend, qa, documentacion, seguridad.
- Rama: feature/mysql-support.
- Descripción de commit: Cambiar la base operativa de demo a MySQL, actualizar consultas y pruebas, y mejorar la experiencia visual del dashboard Streamlit.
- Tarea: Corregir la ruta de persistencia para usar MySQL y elevar la calidad del frontend.
- Archivos modificados: `.env.example`, `README.md`, `docs/arquitectura.md`, `docs/development.md`, `docs/tareas.md`, `setup_demo.py`, `src/database/`, `src/scoring/scoring_service.py`, `src/app/`, `tests/`.
- Decisión tomada: MySQL queda como base principal de la demo local; CSV procesado queda como contrato de lectura para Streamlit y respaldo reproducible.
- Revisión de seguridad: No se agregaron datos reales ni credenciales versionadas. Los defaults de MySQL son solo para demo local; `.env.example` mantiene placeholders.
- Problema encontrado: El avance anterior mantenia SQLite como ruta principal y el frontend tenia una presentacion demasiado basica para demo.
- Solución aplicada: `setup_demo.py` crea/carga `fraudlens_claims_ai` en MySQL, `risk_scores` queda poblada en MySQL, las consultas usan MySQL, y Streamlit incorpora sidebar de producto, KPIs, filtros avanzados, tabs de detalle, proveedores enriquecidos y reportes operativos.
- Tarea completada: MySQL verificado con 1000 `claims` y 1000 `risk_scores`; `pytest` pasa; Streamlit responde en `http://localhost:8501`.
- Tarea pendiente: Ensayar visualmente el flujo completo, preparar pitch y decidir si se implementa MCP como diferenciador.
- Progreso estimado: 65%.
- Siguiente paso: Documentar uso de IA/reglas y crear script de demo.

## 2026-05-28 - Documentacion de IA, reglas, etica y demo

- Responsable: Codex.
- Tipo de cambio: documentacion, ml-nlp, agente, qa, seguridad.
- Rama: feature/mysql-support.
- Descripción de commit: Completar documentacion de uso de IA, reglas, etica, limitaciones, agente y script de demo alineada con MySQL y Streamlit.
- Tarea: Reemplazar placeholders documentales por contenido real defendible ante jurado.
- Archivos modificados: `docs/uso_ia.md`, `docs/reglas_negocio.md`, `docs/etica_privacidad.md`, `docs/limitaciones.md`, `docs/demo_script.md`, `docs/agente_mcp.md`, `docs/development.md`, `docs/tareas.md`.
- Decisión tomada: Documentar MCP como diferenciador opcional y mantener agente local como capacidad principal del MVP.
- Revisión de seguridad: Los documentos refuerzan que el sistema prioriza revision humana, no confirma fraude y no rechaza siniestros automaticamente.
- Problema encontrado: La documentacion clave seguia como placeholder y no explicaba el estado real de reglas, ML, NLP, agente ni demo MySQL.
- Solución aplicada: Completar documentos con formula de score, reglas implementadas, metricas generadas, limites eticos, falsos positivos, flujo de demo y alcance MCP.
- Tarea completada: Documentacion tecnica y de demo alineada con el codigo actual.
- Tarea pendiente: Preparar presentacion ejecutiva y, si hay tiempo, implementar servidor MCP opcional.
- Progreso estimado: 70%.
- Siguiente paso: Commit, push y ensayo final de demo.

## 2026-05-28 - MCP opcional, pitch y QA ampliado

- Responsable: Codex.
- Tipo de cambio: agente, qa, documentacion, frontend, seguridad.
- Rama: feature/pitch-mcp-qa-85.
- Descripción de commit: Implementar wrappers MCP opcionales, completar intencion de asegurados frecuentes, agregar pitch ejecutivo y ampliar pruebas de reglas, NLP, MCP y estructura.
- Tarea: Avanzar el MVP de 70% a 85% con foco en diferenciador, demo y confiabilidad.
- Archivos modificados: `src/agent/`, `src/mcp_server/server.py`, `tests/`, `presentation/pitch.md`, `docs/agente_mcp.md`, `docs/tareas.md`, `docs/development.md`.
- Decisión tomada: Mantener MCP opcional para no bloquear Streamlit; exponer wrappers serializables que reutilizan las mismas tools auditables del agente local.
- Revisión de seguridad: No se agregaron datos reales, secretos ni lenguaje acusatorio. MCP no modifica datos ni recalcula scores.
- Problema encontrado: Faltaban pruebas para reglas/NLP/MCP y la presentacion ejecutiva seguia vacia.
- Solución aplicada: Agregar tests, pitch, tools MCP, intencion de asegurados frecuentes y actualizar tablero de progreso.
- Tarea completada: QA ampliado y demo documentada hasta 85%.
- Tarea pendiente: Convertir pitch Markdown a PDF y grabar video backup si el equipo lo requiere.
- Progreso estimado: 85%.
- Siguiente paso: Commit y push de la rama `feature/pitch-mcp-qa-85`.
