# FraudLens Claims AI - Plan detallado del proyecto HackIAthon

Perfecto. Te lo redacto **como si tuvieran 3 días completos**, bien organizado para que se lo mandes a Codex y Claude. La idea es que Codex no se ponga creativo haciendo un castillo con piscina, sino que siga una arquitectura clara, modular y orientada a la rúbrica.

El proyecto será:

```txt id="3ifc0j"
FraudLens Claims AI
Detector de señales de posible fraude en siniestros de seguros usando IA explicable, dashboard y agente consultivo.
```

El PDF pide un prototipo funcional basado en IA que analice siniestros, genere un score de riesgo, muestre alertas explicables, patrones detectados y recomendaciones para revisión humana. También aclara que la solución no debe acusar fraude ni rechazar automáticamente un siniestro, solo priorizar casos sospechosos para revisión. fileciteturn10file0

## 1. Decisión final de tecnologías

Esta será la arquitectura definitiva:

```txt id="iwd19y"
Frontend / Dashboard:
- Streamlit
- Plotly
- CSS personalizado básico

Lenguaje principal:
- Python 3.11

Base de datos:
- SQLite para demo
- CSV sintéticos como respaldo
- Arquitectura preparada para migrar a MySQL/PostgreSQL/Oracle

Procesamiento:
- Pandas
- NumPy

Machine Learning:
- Scikit-learn
- RandomForestClassifier
- LogisticRegression como fallback
- IsolationForest para anomalías

NLP:
- TfidfVectorizer
- Cosine Similarity

Agente IA:
- Agent router local basado en herramientas
- MCP opcional pero recomendado como diferenciador

MCP:
- MCP Python SDK
- Tools controladas para consultar siniestros, proveedores, documentos, score y resumen ejecutivo

API opcional:
- FastAPI solo como capa futura o si sobra tiempo

Deploy:
- Demo local principal
- Streamlit Community Cloud como despliegue público
- GitHub como repositorio de entrega

Herramientas de desarrollo:
- Codex para construir código
- Claude para revisar arquitectura, README, pitch y documentación
- ChatGPT para estrategia, prompts y preparación de defensa
```

Esta combinación es la mejor porque el reto premia más **IA, explicabilidad, prototipo funcional, arquitectura y negocio** que una interfaz tradicional hecha en React. La matriz del PDF da mucho peso al uso de IA y prototipo, explicabilidad y ética, y análisis del caso. Para nivel excepcional pide un enfoque híbrido con ML, NLP y agente IA para consultas en lenguaje natural. fileciteturn10file2

## 2. Por qué Streamlit y no React

Streamlit será el “frontend”. Aunque técnicamente es Python, visualmente es una app web. Sirve para crear dashboards, tablas, filtros, gráficos, cards, formularios y chat sin tener que montar React, API, CORS, Vite, rutas, estados ni deploy frontend/backend separado.

Streamlit se define oficialmente como un framework open-source de Python para crear apps dinámicas de datos e IA con pocas líneas de código. ([docs.streamlit.io](https://docs.streamlit.io/?utm_source=chatgpt.com))

Para este hackathon, Streamlit es correcto porque el PDF permite entregar una aplicación, dashboard, notebook o sistema ejecutable. Lo importante no es que sea React, sino que el analista pueda revisar casos, ver score, entender alertas y consultar al agente. fileciteturn10file4

Comparación real:

```txt id="iq92gr"
React:
- Más bonito si hay tiempo.
- Requiere frontend + backend.
- Requiere API.
- Requiere manejar estados, rutas, build y errores.
- Más riesgo para 3 días.

Streamlit:
- Todo en Python.
- Se conecta directo a Pandas, SQLite y modelos.
- Permite dashboard rápido.
- Permite chat rápido.
- Ideal para demos de IA/datos.
```

Veredicto: **Streamlit para competir, React para un producto futuro**.

## 3. Por qué Python

Python es la tecnología central porque el proyecto es de datos e IA. El PDF incluso menciona Python entre las herramientas esperadas, junto con Claude, ChatGPT, GitHub, Oracle y R. fileciteturn10file0

Con Python pueden hacer todo:

```txt id="geq7dr"
- Generar datos sintéticos.
- Limpiar y cruzar siniestros, pólizas, proveedores y documentos.
- Calcular reglas de riesgo.
- Entrenar modelos ML.
- Detectar anomalías.
- Analizar texto.
- Crear dashboard.
- Crear agente.
- Exportar reportes.
```

Scikit-learn es adecuado porque ofrece herramientas simples y eficientes para análisis predictivo en Python. ([scikit-learn.org](https://scikit-learn.org/?utm_source=chatgpt.com))

## 4. Por qué SQLite y no MySQL/Oracle

Usaremos **SQLite** como base principal de demo y CSV como respaldo.

El PDF permite usar datos sintéticos o públicos y acepta base de datos Oracle, PostgreSQL, MySQL o archivos planos. También pide que el código sea reproducible, tenga README, `.env.example` y no exponga credenciales. fileciteturn10file6

SQLite gana porque:

```txt id="52hepk"
- No requiere servidor.
- No requiere Docker.
- No requiere usuarios ni contraseñas.
- Es un solo archivo .db.
- Es fácil de subir al repo.
- Es estable para demo.
```

Pero en la documentación diremos:

```txt id="uekw7n"
Para el prototipo usamos SQLite por reproducibilidad. La capa de acceso a datos está separada para permitir migración futura a MySQL, PostgreSQL u Oracle usando la misma estructura de tablas.
```

Eso cubre escalabilidad sin meter un monstruo técnico en la mochila.

## 5. Qué rol tendrá MCP

Aquí sí podemos diferenciarnos.

MCP no debe ser el corazón del sistema, sino la **capa de agente empresarial**. El sistema debe funcionar aunque MCP falle. Pero si logramos MCP, se ve más pro porque el agente consultará tools controladas en vez de “inventar” respuestas.

MCP permite que aplicaciones den contexto a modelos de lenguaje de forma estandarizada, separando el contexto del LLM. El SDK oficial permite crear servidores MCP que exponen tools, resources y prompts. ([github.com](https://github.com/modelcontextprotocol/python-sdk?utm_source=chatgpt.com))

Además, en MCP las tools permiten que los modelos interactúen con sistemas externos, por ejemplo consultar bases de datos, llamar APIs o ejecutar cálculos. ([modelcontextprotocol.io](https://modelcontextprotocol.io/specification/2025-06-18/server/tools?utm_source=chatgpt.com))

En nuestro proyecto:

```txt id="be27rb"
Streamlit Chat
↓
Agent Router
↓
MCP Client opcional
↓
MCP Server local
↓
Tools
↓
SQLite / CSV / modelos / servicios
```

Tools MCP:

```txt id="a2jgv2"
get_top_risk_claims(limit)
explain_claim_risk(id_siniestro)
get_provider_alert_summary()
get_city_risk_summary()
get_missing_documents_critical()
get_similar_narratives(id_siniestro)
simulate_claim_score(payload)
generate_executive_summary()
```

Pitch técnico:

```txt id="fmn6os"
El agente no consulta la base libremente ni toma decisiones autónomas. Usa herramientas MCP controladas, auditables y limitadas a consultas específicas. Esto reduce alucinaciones y permite trazabilidad.
```

Importante: si MCP se complica, se deja como módulo opcional. El agente local con funciones ya cumple la demo. MCP es la armadura brillante, no el motor del carro 🛠️.

## 6. FastAPI sí o no

FastAPI es un framework moderno de Python para construir APIs usando type hints. ([fastapi.tiangolo.com](https://fastapi.tiangolo.com/?utm_source=chatgpt.com))

Pero para este proyecto:

```txt id="5qolfv"
FastAPI no es obligatorio.
```

Lo usaría solo si sobran horas. El PDF menciona una API funcional como deseable, no como mínimo. fileciteturn10file4

Prioridad:

```txt id="s0nxgy"
Nivel 1 obligatorio:
Streamlit + SQLite + reglas + ML + NLP + agente local.

Nivel 2 diferenciador:
MCP.

Nivel 3 extra:
FastAPI con endpoints.
```

Endpoints opcionales:

```txt id="pjv7w8"
GET /claims
GET /claims/{id}
GET /claims/{id}/explanation
GET /analytics/providers
GET /analytics/cities
POST /claims/simulate
GET /reports/executive
```

Si no hay tiempo, no se hace.

# 7. Análisis completo del PDF convertido en requerimientos

## Página 1: Resumen del reto

El reto es del sector asegurador. Pide un prototipo funcional basado en IA, usando datos públicos o sintéticos, con entregables: prototipo, código fuente, dataset, documentación y demo. También establece el principio clave: generar alertas de revisión, no acusaciones automáticas. fileciteturn10file0

Implementación:

```txt id="fylnvq"
- Nombre: FraudLens Claims AI.
- Datos: sintéticos.
- Resultado: score de posible fraude.
- Lenguaje visual: “requiere revisión”, “posible riesgo”, “alerta”.
- Prohibido decir: “fraude confirmado”.
```

## Páginas 2 y 3: Problema y objetivos

El problema es que la revisión manual depende del analista y requiere cruzar pólizas, asegurados, proveedores, documentos, fechas, montos e historial. El objetivo es detectar patrones anómalos, asignar score, clasificar verde/amarillo/rojo, explicar alertas y permitir consultas en lenguaje natural. fileciteturn10file0

Implementación:

```txt id="a5cpkf"
- Motor de reglas.
- Modelo ML.
- NLP para narrativas.
- Dashboard.
- Agente consultivo.
```

## Página 4: Alcance

Incluye cargar dataset de siniestros, pólizas, asegurados, vehículos, beneficiarios, proveedores y documentos. También pide detección de anomalías, score, semáforo, explicación, dashboard y exportación o bandeja de casos sospechosos. No incluye acusar fraude, rechazar siniestros, sustituir análisis humano ni usar datos reales/confidenciales. fileciteturn10file6

Implementación:

```txt id="770jyh"
Tablas:
- claims
- policies
- insured
- vehicles
- providers
- documents
- risk_scores

Pantallas:
- Dashboard
- Bandeja de casos
- Detalle del caso
- Proveedores
- Agente
- Reporte
```

## Página 5: Datos mínimos

La tabla principal debe tener `id_siniestro`, `id_poliza`, `id_asegurado`, ramo, cobertura, fechas, montos, estado, sucursal, descripción, documentos completos, beneficiario, días desde inicio/fin de póliza, días entre ocurrencia y reporte, historial y etiqueta simulada. También sugiere tablas complementarias de pólizas, asegurados, proveedores y documentos. fileciteturn10file6

Implementación:

```txt id="2il036"
Generar CSVs:
- claims.csv
- policies.csv
- insured.csv
- vehicles.csv
- providers.csv
- documents.csv
```

## Páginas 6 y 7: Señales de posible fraude

El PDF sugiere señales como borde de vigencia, demora en denuncia por robo, alta frecuencia por asegurado, vehículo o conductor, proveedor recurrente, documentos incompletos, dinámica sospechosa, tercero no identificado, documentos inconsistentes, reporte tardío, narrativas similares y monto cercano o superior a suma asegurada. fileciteturn10file6

Implementación:

```txt id="ugk2dm"
Reglas:
- edge_policy_rule
- late_report_rule
- theft_delay_rule
- insured_frequency_rule
- vehicle_frequency_rule
- provider_recurrence_rule
- missing_documents_rule
- inconsistent_documents_rule
- suspicious_dynamics_rule
- no_third_party_rule
- narrative_similarity_rule
- high_amount_rule
```

## Página 7: Reglas críticas

Incluye reglas críticas como pérdida total por robo, falsificación documental evidente, coincidencia con lista restrictiva, accidente físicamente imposible, siniestro extremo al borde de vigencia, demora atípica en denuncia de robo y narrativa clonada. fileciteturn10file6

Implementación:

```txt id="8vt11d"
Si se activa una regla crítica, subir riesgo mínimo a:
- Rojo para falsificación, lista restrictiva, pérdida total por robo, dinámica imposible.
- Amarillo alto para borde de vigencia extremo, demora atípica o narrativa clonada.
```

## Página 7 y 8: Uso esperado de IA

El PDF espera ML supervisado, detección de anomalías, NLP, agente explicativo y enfoque híbrido. Dice que la mejor solución combina reglas, modelo de anomalías o clasificación, análisis textual, dashboard y explicación. fileciteturn10file0

Implementación:

```txt id="hcz6u5"
- ML supervisado: RandomForestClassifier.
- Anomalías: IsolationForest.
- NLP: TF-IDF + cosine similarity.
- Agente: funciones locales + MCP opcional.
- Reglas: score trazable.
```

## Página 8: Funcionalidades mínimas y deseables

Mínimas: carga de datos, cálculo de variables, alertas por reglas, modelo IA, clasificación, dashboard y explicación automática. Deseables: chat, análisis textual, red de relaciones, ranking de proveedores, simulación de ahorro, exportación y API. fileciteturn10file4

Implementación:

```txt id="vi5zcx"
Mínimas obligatorias:
- Carga/generación de datos.
- Score.
- Semáforo.
- Dashboard.
- Explicación.

Deseables a implementar:
- Chat agente.
- NLP.
- Ranking proveedores.
- Exportación CSV.
- Simulación de ahorro potencial.

Deseables opcionales:
- Red de relaciones.
- API FastAPI.
```

## Página 8 y 9: Casos de uso y preguntas del agente

El PDF pide que el sistema permita cargar siniestros, calcular score, priorizar casos, explicar alertas, consultar mediante IA y generar reporte. Además lista preguntas esperadas del agente: top 10 riesgos, por qué un caso es alto, proveedores con más alertas, ramos sospechosos, ciudades, asegurados frecuentes, documentos faltantes, montos atípicos, siniestros cerca del inicio, patrones repetidos, resumen ejecutivo y recomendación de casos a revisar. fileciteturn10file4

Implementación directa:

```txt id="lgnhwh"
Agent Router debe soportar esas preguntas exactas.
```

## Página 9: Score sugerido

El PDF sugiere rangos:

```txt id="vgjmpz"
0 - 40: Verde
41 - 75: Amarillo
76 - 100: Rojo
```

Y permite proponer otro esquema si se explica la lógica, validación y trazabilidad. fileciteturn10file4

Implementación:

```txt id="rirlde"
score_final = 0.55 * score_reglas + 0.25 * score_ml + 0.10 * score_anomalia + 0.10 * score_nlp
```

## Página 9 y 10: Entregables y repo

El PDF pide prototipo funcional, código fuente, dataset, README, arquitectura, modelo de datos, explicación del modelo IA, rúbrica de alertas, demo y presentación ejecutiva. También sugiere estructura de repo con README, requirements, data, notebooks, src, docs, tests y presentation. fileciteturn10file4

Implementación:

```txt id="izztie"
fraudlens-claims-ai/
├── README.md
├── requirements.txt
├── .env.example
├── data/
├── notebooks/
├── src/
├── docs/
├── tests/
└── presentation/
```

## Página 10: Requisitos técnicos

El PDF pide Python, R y SQL como lenguajes/estándares, base Oracle/PostgreSQL/MySQL o archivos planos, repo GitHub, documentación, código modular, interfaz funcional, dependencias y `.env.example`. fileciteturn10file4

Implementación:

```txt id="rz26pd"
- Python como lenguaje principal.
- SQL mediante SQLite.
- CSV como archivos planos.
- GitHub.
- requirements.txt.
- .env.example.
```

## Página 11: Seguridad, privacidad y ética

No usar datos personales reales, no usar información confidencial, anonimizar identificadores, no subir credenciales, no exponer API keys, documentar fuentes, aclarar que el resultado es alerta, mantener revisión humana y explicar limitaciones/falsos positivos. fileciteturn10file7

Implementación:

```txt id="27vjc8"
- Datos sintéticos.
- IDs anónimos.
- .env.example.
- No subir .env.
- Texto visible en app: “El sistema no acusa fraude”.
- docs/etica_privacidad.md.
```

## Página 11 y 12: Evaluación, métricas y riesgos

El PDF da pesos: entendimiento 15%, prototipo 20%, IA 20%, explicabilidad 15%, calidad técnica 10%, seguridad/ética 10%, impacto/escalabilidad 10%. También sugiere métricas: precision, recall, F1, matriz de confusión, AUC-ROC, score de rareza y calidad de similitud textual. fileciteturn10file7

Implementación:

```txt id="w9t106"
- Mostrar métricas del modelo en pantalla o docs.
- Guardar confusion_matrix.png opcional.
- Crear docs/uso_ia.md con métricas.
- Crear docs/limitaciones.md con sesgo, falsos positivos, dependencia de APIs y no decisión legal.
```

## Página 12 y 13: Pitch y pruebas de fuego

El PDF define pitch de 10 minutos: problema, solución, demo, arquitectura/IA, impacto, limitaciones y preguntas. También indica que el jurado puede pedir consultas agenticas, pruebas de score y verificación del repo. fileciteturn10file2

Implementación:

```txt id="apkpj9"
Preparar 3 demos:
1. Preguntar al agente: proveedores que concentran alertas rojas.
2. Simular un siniestro ocurrido 24 horas después de iniciar póliza.
3. Mostrar estructura GitHub y módulos.
```

# 8. Arquitectura propuesta

```txt id="4t9sl7"
┌──────────────────────────────────────────────┐
│              Streamlit Dashboard              │
│  KPIs | Bandeja | Detalle | Agente | Reporte  │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│              Application Services             │
│ claims_service | scoring_service | reports    │
└───────────────────────┬──────────────────────┘
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
┌─────────────┐ ┌─────────────┐ ┌────────────────┐
│ Fraud Rules │ │ ML Models   │ │ NLP Similarity │
│ Score       │ │ RF/IForest  │ │ TF-IDF Cosine  │
└─────────────┘ └─────────────┘ └────────────────┘
        │               │                │
        └───────────────┼────────────────┘
                        ▼
┌──────────────────────────────────────────────┐
│                SQLite / CSV                   │
│ claims, policies, insured, vehicles, docs     │
└──────────────────────────────────────────────┘

Opcional:
┌──────────────────────┐
│ MCP Server            │
│ tools consultivas     │
└──────────────────────┘
```

# 9. Estructura final del repositorio

```txt id="okr5sj"
fraudlens-claims-ai/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup_demo.py
├── data/
│   ├── synthetic/
│   │   ├── claims.csv
│   │   ├── policies.csv
│   │   ├── insured.csv
│   │   ├── vehicles.csv
│   │   ├── providers.csv
│   │   ├── documents.csv
│   │   └── watchlist.csv
│   └── processed/
│       ├── fraudlens.db
│       ├── scored_claims.csv
│       ├── model_metrics.json
│       └── executive_summary.txt
├── notebooks/
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_modelo_fraude.ipynb
│   └── 03_evaluacion_modelo.ipynb
├── src/
│   ├── app/
│   │   ├── main.py
│   │   ├── components.py
│   │   ├── styles.py
│   │   └── pages/
│   │       ├── dashboard.py
│   │       ├── claims_inbox.py
│   │       ├── claim_detail.py
│   │       ├── providers.py
│   │       ├── agent_chat.py
│   │       └── reports.py
│   ├── data_generation/
│   │   └── generate_synthetic_data.py
│   ├── database/
│   │   ├── build_database.py
│   │   ├── connection.py
│   │   └── queries.py
│   ├── features/
│   │   └── build_features.py
│   ├── rules/
│   │   └── fraud_rules.py
│   ├── models/
│   │   ├── train_model.py
│   │   ├── fraud_classifier.py
│   │   └── anomaly_detector.py
│   ├── nlp/
│   │   └── narrative_similarity.py
│   ├── scoring/
│   │   └── scoring_service.py
│   ├── explainability/
│   │   └── explain_score.py
│   ├── agent/
│   │   ├── agent_router.py
│   │   └── agent_tools.py
│   ├── mcp_server/
│   │   └── server.py
│   ├── reports/
│   │   └── report_service.py
│   └── utils/
│       ├── config.py
│       └── constants.py
├── tests/
│   ├── test_rules.py
│   ├── test_scoring.py
│   ├── test_nlp.py
│   └── test_agent_tools.py
├── docs/
│   ├── arquitectura.md
│   ├── modelo_datos.md
│   ├── reglas_negocio.md
│   ├── uso_ia.md
│   ├── agente_mcp.md
│   ├── etica_privacidad.md
│   ├── limitaciones.md
│   └── demo_script.md
└── presentation/
    └── pitch.pdf
```

# 10. Modelo de datos detallado

## claims

```txt id="fl0a2k"
id_siniestro
id_poliza
id_asegurado
id_vehiculo
id_proveedor
ramo
cobertura
fecha_ocurrencia
fecha_reporte
monto_reclamado
monto_estimado
monto_pagado
estado
sucursal
ciudad
descripcion
documentos_completos
dias_desde_inicio_poliza
dias_desde_fin_poliza
dias_entre_ocurrencia_reporte
historial_siniestros_asegurado
tipo_accidente
tercero_identificado
hora_evento
etiqueta_fraude_simulada
```

## policies

```txt id="2gcrcp"
id_poliza
id_asegurado
ramo
fecha_inicio
fecha_fin
prima
suma_asegurada
deducible
canal_venta
ciudad
estado_poliza
```

## insured

```txt id="tfrmq0"
id_asegurado
segmento
antiguedad_meses
ciudad
numero_polizas
reclamos_ultimos_12_meses
mora_actual
score_cliente_simulado
cambio_datos_reciente
```

## vehicles

```txt id="siiaiw"
id_vehiculo
placa_hash
chasis_hash
motor_hash
marca
modelo
anio
reclamos_ultimos_18_meses
```

## providers

```txt id="pnd3mf"
id_proveedor
nombre_proveedor
tipo
ciudad
reclamos_asociados
monto_promedio_reclamado
porcentaje_casos_observados
antiguedad_meses
en_lista_restrictiva
```

## documents

```txt id="mps8we"
id_documento
id_siniestro
tipo_documento
entregado
legible
fecha_emision
inconsistencia_detectada
observacion
```

## risk_scores

```txt id="q8rzwy"
id_siniestro
score_reglas
score_ml
score_anomalia
score_nlp
score_final
nivel_riesgo
reglas_activadas
explicacion
accion_sugerida
created_at
```

# 11. Score de riesgo

Fórmula:

```txt id="lm0ju0"
score_final = 
    0.55 * score_reglas
  + 0.25 * score_ml
  + 0.10 * score_anomalia
  + 0.10 * score_nlp
```

Clasificación:

```txt id="mq8hjl"
0 - 40    Verde
41 - 75   Amarillo
76 - 100  Rojo
```

Esto respeta el rango sugerido por el PDF. fileciteturn10file4

Reglas:

```txt id="cr48k7"
R001_BORDE_VIGENCIA:
- <= 2 días desde inicio o fin: crítico
- <= 10 días: +8
- 11 a 30 días: +4

R002_REPORTE_TARDIO:
- > 7 días: +5
- 4 a 7 días: +3

R003_DEMORA_ROBO:
- cobertura robo y reporte > 48 horas: +8
- cobertura robo y reporte 24-48 horas: +4

R004_FRECUENCIA_ASEGURADO:
- >= 3 siniestros en 18 meses: +8
- 2 siniestros: +4

R005_FRECUENCIA_VEHICULO:
- >= 3 siniestros en 18 meses: +6
- 2 siniestros: +3

R006_PROVEEDOR_RECURRENTE:
- proveedor en lista restrictiva: +10 y rojo mínimo
- proveedor con > 2 casos observados: +5

R007_DOCUMENTOS_INCOMPLETOS:
- falta denuncia/factura/informe obligatorio: +4

R008_DOCUMENTOS_INCONSISTENTES:
- fechas no coinciden, factura previa al evento o ilegible: +10 y rojo mínimo si es grave

R009_DINAMICA_SOSPECHOSA:
- relato ilógico vs tipo de impacto: +6
- accidente múltiple de madrugada: +3

R010_TERCERO_NO_IDENTIFICADO:
- daño severo sin tercero ni evidencia: +5

R011_NARRATIVA_SIMILAR:
- similitud > 0.85: +8
- similitud 0.70 a 0.84: +4

R012_MONTO_ATIPICO:
- monto > 95% de suma asegurada: +5
- monto > 150% del promedio del ramo/cobertura: +4
```

Explicación generada:

```txt id="w7p32q"
El siniestro SIN-0421 fue clasificado como Rojo con score 86/100 porque ocurrió 2 días después del inicio de la póliza, fue reportado 9 días después del evento, el proveedor aparece en múltiples casos observados y existen documentos inconsistentes. Esta clasificación no representa una acusación de fraude; recomienda revisión especializada por parte de la Unidad Antifraude.
```

# 12. IA y modelos

## ML supervisado

Modelo:

```txt id="p1p8xa"
RandomForestClassifier
```

Por qué:

```txt id="wh4mte"
- Funciona bien con variables tabulares.
- No necesita demasiada configuración.
- Permite medir importancia de variables.
- Es más defendible en hackathon que una red neuronal innecesaria.
```

Variables:

```txt id="bt2j8t"
dias_desde_inicio_poliza
dias_desde_fin_poliza
dias_entre_ocurrencia_reporte
monto_reclamado
monto_estimado
monto_pagado
monto_vs_suma_asegurada
historial_siniestros_asegurado
reclamos_ultimos_12_meses
reclamos_vehiculo_18_meses
proveedor_recurrente
proveedor_lista_restrictiva
documentos_incompletos
documentos_inconsistentes
similitud_narrativa_max
tercero_identificado
hora_evento
```

Métricas:

```txt id="zi62lx"
precision
recall
f1-score
matriz de confusión
AUC-ROC opcional
```

Estas métricas están alineadas con las sugerencias del PDF para modelo supervisado. fileciteturn10file7

## Detección de anomalías

Modelo:

```txt id="7uek3o"
IsolationForest
```

Uso:

```txt id="mdxa9b"
Detectar casos raros por monto, tiempo de reporte, frecuencia, suma asegurada y comportamiento del proveedor.
```

Salida:

```txt id="ube0wo"
score_anomalia de 0 a 100
```

## NLP

Técnica:

```txt id="vbz46j"
TF-IDF + cosine similarity
```

Uso:

```txt id="kka876"
Detectar reclamos con narrativas similares o clonadas.
```

Respuesta técnica para jurado:

```txt id="eks7t2"
Convertimos las descripciones de los reclamos en vectores TF-IDF y calculamos similitud coseno entre narrativas. Si la similitud supera 0.85, se activa una alerta alta de narrativa posiblemente clonada; entre 0.70 y 0.84 se activa alerta media.
```

# 13. Dashboard que tú harás

## Pantalla 1: Dashboard ejecutivo

Componentes:

```txt id="h8nds4"
KPIs:
- Total de siniestros
- Casos rojos
- Casos amarillos
- Casos verdes
- Monto total reclamado
- Monto en riesgo rojo
- Porcentaje de casos revisables

Gráficos:
- Distribución por nivel de riesgo
- Top 10 proveedores con alertas rojas
- Riesgo por ciudad
- Riesgo por ramo
- Evolución mensual de casos críticos
```

Texto fijo:

```txt id="wwgop2"
FraudLens Claims AI prioriza siniestros con señales de posible fraude. El sistema genera alertas explicables para revisión humana, no acusaciones automáticas.
```

## Pantalla 2: Bandeja de siniestros

Filtros:

```txt id="flg3hg"
nivel_riesgo
ciudad
ramo
cobertura
proveedor
estado
rango de monto
rango de fecha
```

Tabla:

```txt id="tyte37"
id_siniestro
fecha_ocurrencia
ciudad
ramo
cobertura
proveedor
monto_reclamado
score_final
nivel_riesgo
accion_sugerida
```

## Pantalla 3: Detalle del siniestro

Secciones:

```txt id="plhfha"
1. Resumen del caso
2. Score y semáforo
3. Reglas activadas
4. Explicación automática
5. Datos de póliza
6. Datos de proveedor
7. Documentos
8. Narrativas similares
9. Acción recomendada
```

## Pantalla 4: Proveedores

Mostrar:

```txt id="s2tg4j"
Top proveedores por alertas
Casos rojos por proveedor
Monto promedio reclamado
Porcentaje de casos observados
Lista restrictiva simulada
```

## Pantalla 5: Agente IA

Chat:

```txt id="yw1i0h"
Input libre:
“Pregúntale al agente antifraude... ”

Botones rápidos:
- Top 10 siniestros de mayor riesgo
- ¿Por qué este siniestro es rojo?
- Proveedores con más alertas
- Documentos faltantes en casos críticos
- Ciudades con mayor concentración
- Montos atípicos
- Generar resumen ejecutivo
```

Las preguntas vienen directamente del PDF. fileciteturn10file4

## Pantalla 6: Reporte

Opciones:

```txt id="bkvrvh"
- Descargar casos rojos CSV
- Descargar todos los scores CSV
- Ver resumen ejecutivo
- Copiar recomendaciones para auditoría
```

# 14. Deploy

Prioridad:

```txt id="004uhs"
1. Demo local.
2. Streamlit Community Cloud.
3. Video corto de respaldo.
```

Streamlit Community Cloud permite desplegar apps conectadas a GitHub y administrar apps desplegadas, con la plataforma encargándose de la containerización. ([docs.streamlit.io](https://docs.streamlit.io/?utm_source=chatgpt.com))

Comandos:

```bash id="9478r8"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python setup_demo.py
streamlit run src/app/main.py
```

`setup_demo.py` debe hacer:

```txt id="on3yn8"
1. Generar datos sintéticos.
2. Crear SQLite.
3. Calcular features.
4. Entrenar modelo.
5. Calcular scores.
6. Guardar CSVs finales.
```

# 15. División de tareas para 2 personas

Tú haces todo el frontend. Tu compañero hace datos, IA y backend lógico. Codex trabaja como albañil robótico bajo instrucciones precisas.

## Tú: Frontend, demo y presentación

Responsabilidades:

```txt id="z5fbbl"
- Crear app Streamlit.
- Crear layout general.
- Crear sidebar.
- Crear navegación.
- Crear dashboard ejecutivo.
- Crear bandeja de siniestros.
- Crear detalle del siniestro.
- Crear visual de semáforo.
- Crear gráficos Plotly.
- Crear pantalla de proveedores.
- Crear pantalla del agente.
- Crear pantalla de reporte.
- Pulir CSS.
- Preparar demo script.
- Preparar pitch visual.
```

Archivos tuyos:

```txt id="80e3c0"
src/app/main.py
src/app/components.py
src/app/styles.py
src/app/pages/dashboard.py
src/app/pages/claims_inbox.py
src/app/pages/claim_detail.py
src/app/pages/providers.py
src/app/pages/agent_chat.py
src/app/pages/reports.py
presentation/pitch.pdf
docs/demo_script.md
```

## Tu compañero: Datos, IA y lógica

Responsabilidades:

```txt id="lwyvv1"
- Generar dataset sintético.
- Crear SQLite.
- Crear reglas de fraude.
- Crear features.
- Crear NLP de similitud.
- Entrenar modelo ML.
- Crear detector de anomalías.
- Crear score final.
- Crear explicaciones.
- Crear agent tools.
- Crear tests.
- Documentar IA, reglas, ética y modelo de datos.
```

Archivos de tu compañero:

```txt id="l6orwj"
src/data_generation/generate_synthetic_data.py
src/database/build_database.py
src/database/queries.py
src/features/build_features.py
src/rules/fraud_rules.py
src/models/train_model.py
src/models/fraud_classifier.py
src/models/anomaly_detector.py
src/nlp/narrative_similarity.py
src/scoring/scoring_service.py
src/explainability/explain_score.py
src/agent/agent_tools.py
src/agent/agent_router.py
tests/
docs/modelo_datos.md
docs/reglas_negocio.md
docs/uso_ia.md
docs/etica_privacidad.md
docs/limitaciones.md
```

## Opcional conjunto: MCP

Si el MVP ya está listo:

```txt id="hr4omx"
src/mcp_server/server.py
docs/agente_mcp.md
```

# 16. Plan de 3 días

## Día 1: Base funcional

Objetivo: app abre, datos existen, score básico funciona.

Tú:

```txt id="uwged6"
- Crear proyecto Streamlit.
- Crear navegación.
- Crear layout con sidebar.
- Crear dashboard inicial con datos mock o CSV.
- Crear tabla de siniestros.
- Crear filtros básicos.
- Crear diseño inicial de cards KPI.
```

Tu compañero:

```txt id="lp3iei"
- Crear generador de datos sintéticos.
- Crear claims, policies, insured, vehicles, providers, documents.
- Crear build_database.py.
- Crear primeras reglas.
- Crear scored_claims.csv.
```

Entregable del día:

```txt id="y1f5g2"
streamlit run src/app/main.py
```

Debe abrir y mostrar siniestros con score.

## Día 2: IA, explicabilidad y agente

Objetivo: tener valor real para jurado.

Tú:

```txt id="3kxaxu"
- Crear pantalla detalle.
- Crear visual semáforo.
- Crear gráficos Plotly.
- Crear pantalla proveedores.
- Crear pantalla agente con botones rápidos.
- Crear pantalla reportes.
```

Tu compañero:

```txt id="bg1djk"
- Completar reglas.
- Crear NLP TF-IDF.
- Crear RandomForest.
- Crear IsolationForest.
- Crear score_final.
- Crear explicación por caso.
- Crear agent_router.
```

Entregable del día:

```txt id="1k3iag"
- Dashboard completo.
- Casos rojos explicados.
- Agente responde preguntas.
```

## Día 3: Diferenciador, docs y pitch

Objetivo: pulir, documentar y ensayar.

Tú:

```txt id="34ilmx"
- Pulir UI.
- Agregar textos ejecutivos.
- Crear pitch.
- Preparar demo script.
- Probar flujo completo.
- Intentar Streamlit Cloud.
```

Tu compañero:

```txt id="p8ccda"
- Crear README.
- Crear docs.
- Crear tests.
- Crear métricas.
- Crear MCP si sobra tiempo.
- Revisar seguridad.
```

Ambos:

```txt id="m64dr6"
- Ensayar pitch de 10 minutos.
- Preparar respuestas técnicas.
- Verificar repo.
- Grabar video de respaldo.
```

# 17. Prompt maestro para Codex

Copia esto tal cual a Codex:

```txt id="6s0ey5"
Actúa como arquitecto senior Python/IA y desarrollador fullstack de hackathon. Vamos a construir un MVP llamado FraudLens Claims AI para el reto “Detector de Posibles Fraudes en Siniestros usando Inteligencia Artificial” de Aseguradora del Sur.

Contexto del reto:
El sistema debe analizar siniestros de seguros con datos sintéticos o públicos, generar un score de riesgo de posible fraude, clasificar en verde/amarillo/rojo, explicar alertas, detectar patrones, permitir consultas en lenguaje natural y mostrar un dashboard funcional. La solución NO debe acusar fraude ni rechazar siniestros automáticamente; solo debe generar alertas para revisión humana.

Stack obligatorio:
- Python 3.11
- Streamlit para frontend/dashboard
- Pandas y NumPy para procesamiento
- Plotly para gráficos
- SQLite como base de datos local
- CSV sintéticos como respaldo
- Scikit-learn para ML
- TF-IDF + cosine similarity para NLP
- Agent router local basado en herramientas
- MCP opcional como diferenciador
- Pytest para tests mínimos

No usar:
- React
- Angular
- Login
- Roles
- Docker obligatorio
- Oracle real
- MySQL obligatorio
- Microservicios
- LLM decidiendo directamente el score

Estructura del repositorio:
fraudlens-claims-ai/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup_demo.py
├── data/
│   ├── synthetic/
│   └── processed/
├── notebooks/
├── src/
│   ├── app/
│   ├── data_generation/
│   ├── database/
│   ├── features/
│   ├── rules/
│   ├── models/
│   ├── nlp/
│   ├── scoring/
│   ├── explainability/
│   ├── agent/
│   ├── mcp_server/
│   ├── reports/
│   └── utils/
├── tests/
├── docs/
└── presentation/

Primera tarea:
Crea la estructura completa del proyecto, requirements.txt, .env.example, .gitignore, README inicial y setup_demo.py. No implementes todo todavía. Deja placeholders claros y ejecutables.
```

# 18. Prompt para que Codex haga los datos

```txt id="2gori3"
Implementa el módulo de generación de datos sintéticos para FraudLens Claims AI.

Crear:
src/data_generation/generate_synthetic_data.py

Debe generar:
- data/synthetic/claims.csv
- data/synthetic/policies.csv
- data/synthetic/insured.csv
- data/synthetic/vehicles.csv
- data/synthetic/providers.csv
- data/synthetic/documents.csv
- data/synthetic/watchlist.csv

Requisitos:
- 1000 siniestros
- 400 pólizas
- 350 asegurados
- 250 vehículos
- 80 proveedores
- 3000 documentos aproximados
- Datos 100% sintéticos, sin información personal real
- IDs anónimos
- Incluir casos normales y casos sospechosos

Campos claims:
id_siniestro, id_poliza, id_asegurado, id_vehiculo, id_proveedor, ramo, cobertura, fecha_ocurrencia, fecha_reporte, monto_reclamado, monto_estimado, monto_pagado, estado, sucursal, ciudad, descripcion, documentos_completos, dias_desde_inicio_poliza, dias_desde_fin_poliza, dias_entre_ocurrencia_reporte, historial_siniestros_asegurado, tipo_accidente, tercero_identificado, hora_evento, etiqueta_fraude_simulada.

Inyecta patrones sospechosos:
- siniestros cerca del inicio o fin de póliza
- reportes tardíos
- montos atípicos
- proveedores recurrentes
- documentos incompletos
- documentos inconsistentes
- narrativas similares
- terceros no identificados
- cobertura robo con denuncia tardía

El script debe poder ejecutarse con:
python src/data_generation/generate_synthetic_data.py
```

# 19. Prompt para Codex de reglas y score

```txt id="gbf5kh"
Implementa el motor de reglas y score para FraudLens Claims AI.

Crear:
src/rules/fraud_rules.py
src/scoring/scoring_service.py
src/explainability/explain_score.py

Reglas:
R001_BORDE_VIGENCIA
R002_REPORTE_TARDIO
R003_DEMORA_ROBO
R004_FRECUENCIA_ASEGURADO
R005_FRECUENCIA_VEHICULO
R006_PROVEEDOR_RECURRENTE
R007_DOCUMENTOS_INCOMPLETOS
R008_DOCUMENTOS_INCONSISTENTES
R009_DINAMICA_SOSPECHOSA
R010_TERCERO_NO_IDENTIFICADO
R011_NARRATIVA_SIMILAR
R012_MONTO_ATIPICO

Cada regla debe devolver:
- code
- name
- points
- severity
- explanation
- evidence

El score final debe ser:
score_final = 0.55 * score_reglas + 0.25 * score_ml + 0.10 * score_anomalia + 0.10 * score_nlp

Clasificación:
0-40 Verde
41-75 Amarillo
76-100 Rojo

El sistema debe generar explicación humana:
“No es una acusación de fraude, es una alerta para revisión humana.”

Guardar resultado en:
data/processed/scored_claims.csv
```

# 20. Prompt para Codex del NLP

```txt id="tdabei"
Implementa el módulo NLP para detectar narrativas similares.

Crear:
src/nlp/narrative_similarity.py

Usar:
- sklearn.feature_extraction.text.TfidfVectorizer
- sklearn.metrics.pairwise.cosine_similarity

Funciones:
- compute_similarity_matrix(df)
- get_similar_claims(id_siniestro, df, threshold=0.70)
- add_nlp_scores(df)

Reglas:
- similitud > 0.85: score_nlp alto y alerta fuerte
- similitud 0.70 a 0.84: alerta media
- debajo de 0.70: sin alerta

Debe devolver para cada siniestro:
- max_similarity
- similar_claim_id
- nlp_alert
- nlp_explanation
```

# 21. Prompt para Codex del modelo ML

```txt id="tgck8h"
Implementa el modelo ML para FraudLens Claims AI.

Crear:
src/models/train_model.py
src/models/fraud_classifier.py
src/models/anomaly_detector.py

Usar:
- RandomForestClassifier para clasificación supervisada con etiqueta_fraude_simulada
- LogisticRegression como fallback simple
- IsolationForest para anomalías

Features:
dias_desde_inicio_poliza, dias_desde_fin_poliza, dias_entre_ocurrencia_reporte, monto_reclamado, monto_estimado, monto_pagado, monto_vs_suma_asegurada, historial_siniestros_asegurado, reclamos_ultimos_12_meses, reclamos_vehiculo_18_meses, proveedor_recurrente, proveedor_lista_restrictiva, documentos_incompletos, documentos_inconsistentes, similitud_narrativa_max, tercero_identificado, hora_evento.

Guardar:
- data/processed/fraud_model.joblib
- data/processed/anomaly_model.joblib
- data/processed/model_metrics.json

Métricas:
- accuracy
- precision
- recall
- f1
- confusion matrix
- roc_auc si aplica

El modelo no debe decidir fraude automáticamente. Solo entrega score_ml para apoyar priorización.
```

# 22. Prompt para Codex del frontend Streamlit

```txt id="zetktn"
Implementa el frontend Streamlit de FraudLens Claims AI.

Crear:
src/app/main.py
src/app/components.py
src/app/styles.py
src/app/pages/dashboard.py
src/app/pages/claims_inbox.py
src/app/pages/claim_detail.py
src/app/pages/providers.py
src/app/pages/agent_chat.py
src/app/pages/reports.py

Requisitos visuales:
- Interfaz limpia, moderna y ejecutiva.
- Sidebar con navegación.
- Cards KPI.
- Colores de semáforo: verde, amarillo, rojo.
- Tablas con filtros.
- Gráficos Plotly.
- Textos claros para jurado.
- Advertencia ética visible: “El sistema genera alertas para revisión humana; no acusa fraude.”

Pantalla Dashboard:
- Total siniestros
- Casos verdes, amarillos, rojos
- Monto total reclamado
- Monto en casos rojos
- Gráficos por nivel, ciudad, proveedor y ramo

Pantalla Bandeja:
- Filtros por nivel, ciudad, ramo, proveedor, cobertura
- Tabla ordenada por score_final descendente

Pantalla Detalle:
- Selector de id_siniestro
- Score
- Nivel
- Reglas activadas
- Explicación
- Datos de póliza/proveedor/documentos
- Narrativas similares

Pantalla Proveedores:
- Ranking de proveedores con alertas
- Monto promedio
- Casos rojos
- Lista restrictiva simulada

Pantalla Agente:
- st.chat_input
- Botones de preguntas rápidas
- Respuestas usando agent_router.py

Pantalla Reportes:
- Descargar CSV casos rojos
- Descargar CSV todos los scores
- Mostrar resumen ejecutivo
```

# 23. Prompt para Codex del agente

```txt id="ev3raz"
Implementa el agente consultivo local.

Crear:
src/agent/agent_tools.py
src/agent/agent_router.py

El agente debe responder:
1. ¿Cuáles son los 10 siniestros con mayor riesgo?
2. ¿Por qué este siniestro fue marcado como alto riesgo?
3. ¿Qué proveedores concentran más alertas?
4. ¿Qué ramos tienen mayor porcentaje de casos sospechosos?
5. ¿Qué ciudades presentan mayor concentración de alertas?
6. ¿Qué asegurados tienen mayor frecuencia de reclamos?
7. ¿Qué documentos faltan en los casos críticos?
8. ¿Qué casos tienen montos atípicos?
9. ¿Qué siniestros ocurrieron cerca del inicio de la póliza?
10. ¿Qué patrones se repiten en los reclamos sospechosos?
11. Genera un resumen ejecutivo de los casos críticos.
12. Recomienda qué casos debería revisar primero el analista.

No usar LLM obligatorio. Usar detección de intención por keywords y funciones controladas sobre el DataFrame.

Debe devolver respuestas en lenguaje natural, con datos concretos.
```

# 24. Prompt para Codex del MCP opcional

```txt id="d1k3nc"
Implementa un servidor MCP opcional para FraudLens Claims AI.

Crear:
src/mcp_server/server.py

Usar MCP Python SDK.

Exponer tools:
- get_top_risk_claims(limit: int)
- explain_claim_risk(id_siniestro: str)
- get_provider_alert_summary()
- get_city_risk_summary()
- get_missing_documents_critical()
- get_similar_narratives(id_siniestro: str)
- simulate_claim_score(payload: dict)
- generate_executive_summary()

Las tools deben llamar a src/agent/agent_tools.py y devolver JSON serializable.

Debe existir documentación en docs/agente_mcp.md explicando que MCP permite conectar el agente a herramientas controladas y auditable, y que para el prototipo se conecta a una base sintética SQLite.
```

# 25. Prompt para Claude

```txt id="eoq364"
Necesito que revises la arquitectura y documentación de un proyecto de hackathon llamado FraudLens Claims AI.

Contexto:
Es un detector de señales de posible fraude en siniestros de seguros. Usa datos sintéticos, reglas de negocio, ML, NLP y un agente consultivo. La solución no acusa fraude ni rechaza reclamos; solo genera alertas explicables para revisión humana.

Revisa:
1. Si la arquitectura es clara.
2. Si el README explica instalación y demo.
3. Si la explicación del modelo IA es entendible para jurado.
4. Si la ética está bien planteada.
5. Si el pitch de 10 minutos es convincente.
6. Si hay riesgos técnicos o puntos débiles.

Mejora el lenguaje para que suene profesional, ejecutivo y defendible.
```

# 26. README mínimo que debe existir

```txt id="q60k5j"
# FraudLens Claims AI

Sistema de apoyo para analistas de siniestros que detecta señales de posible fraude mediante reglas, machine learning, análisis textual y un agente consultivo.

## Importante
El sistema no acusa fraude ni rechaza siniestros automáticamente. Solo genera alertas de revisión humana.

## Stack
Python, Streamlit, Pandas, Scikit-learn, SQLite, Plotly, TF-IDF, Cosine Similarity, MCP opcional.

## Instalación
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Ejecutar demo
python setup_demo.py
streamlit run src/app/main.py

## Entregables
- Prototipo funcional
- Dataset sintético
- Código fuente
- Documentación
- Modelo de datos
- Reglas de negocio
- Explicación IA
- Pitch
```

# 27. Checklist final

Antes de entregar:

```txt id="2dlyfk"
[ ] App abre con streamlit run src/app/main.py
[ ] setup_demo.py corre desde cero
[ ] Hay CSVs sintéticos
[ ] Hay SQLite o al menos CSV procesado
[ ] Dashboard muestra KPIs
[ ] Bandeja ordena por score
[ ] Detalle muestra explicación
[ ] Agente responde preguntas del PDF
[ ] Exporta CSV de casos críticos
[ ] README completo
[ ] requirements.txt completo
[ ] .env.example existe
[ ] No hay .env real
[ ] No hay API keys
[ ] Docs de arquitectura
[ ] Docs de modelo de datos
[ ] Docs de reglas
[ ] Docs de IA
[ ] Docs de ética
[ ] Pitch PDF
[ ] Demo ensayada
[ ] Video backup grabado
```

# 28. Veredicto final

La apuesta ganadora no es “hacer muchas tecnologías”. Es mostrar un sistema coherente:

```txt id="87re3c"
Datos sintéticos tipo aseguradora
+ score explicable
+ ML
+ NLP
+ agente consultivo
+ dashboard claro
+ ética visible
+ repo ordenado
+ pitch sólido
```

Con 3 días, sí metería MCP como diferenciador, pero después de tener el MVP. Con eso pueden decir algo potente:

```txt id="csh2zg"
FraudLens Claims AI no reemplaza al analista. Le entrega una bandeja priorizada de casos, explicaciones trazables y un agente conectado a herramientas controladas para investigar patrones en siniestros, proveedores, documentos y narrativas.
```

Eso calza con la rúbrica y no se siente improvisado. El proyecto queda como bisturí, no como licuadora con luces. 🧠
