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
| Documentación base | En progreso | 90% |
| Integración Codex skills/agentes | Completo | 100% |
| Tablero de tareas por rol | Completo | 100% |
| Estructura de repo ejecutable | Completo | 100% |
| Datos sintéticos | Pendiente | 0% |
| Reglas y score | Pendiente | 0% |
| ML/NLP | Pendiente | 0% |
| Dashboard Streamlit | Pendiente | 0% |
| Agente local/MCP | Pendiente | 0% |
| QA/demo/pitch | Estructura creada | 20% |

Progreso global estimado: 28%.

## Plan de trabajo por fases

### Fase 1: estructura base y datos sintéticos

- Crear estructura de carpetas.
- Crear `requirements.txt`, `.env.example`, `.gitignore` y `README.md`.
- Generar CSV sintéticos.
- Crear SQLite local.
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
- [ ] Existe SQLite local o CSV procesado equivalente.
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
- La persistencia será CSV + SQLite.
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
- [ ] Crear SQLite.
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
- Decisión tomada: Mantener arquitectura liviana con Streamlit, Python, CSV, SQLite, reglas, ML/NLP y agente local.
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
- Decisión tomada: Crear placeholders por módulo para conectar arquitectura, responsabilidades y futuras fases, manteniendo Streamlit + Python + CSV/SQLite + Scikit-learn + agente local.
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
- Revisión de seguridad: Antes del commit se confirma que no existe `.env` real, credenciales, bases SQLite, CSV generados ni datos reales.
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
- Tarea pendiente: Confirmar si se usará entorno virtual local `venv` para aislar dependencias antes de implementar datos.
- Progreso estimado: 28%.
- Siguiente paso: Commit y push de la rama `docs/readme-install-deps`.
