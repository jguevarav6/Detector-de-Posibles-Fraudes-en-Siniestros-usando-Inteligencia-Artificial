# Análisis completo del PDF - hackIAthon Ecuador: Reto Aseguradora del Sur

**Documento base:** `hackIAthon - reto Aseguradora del Sur`  
**Tema:** Detector de Posibles Fraudes en Siniestros usando Inteligencia Artificial  
**Tipo de documento:** Levantamiento funcional, alcance técnico, entregables y criterios de evaluación  
**Objetivo de este archivo:** Convertir el PDF completo a un documento Markdown organizado, explicando página por página el contenido, los requisitos, las implicaciones técnicas y cómo debe orientar el desarrollo del prototipo.

> Nota importante: el PDF cargado contiene **14 páginas**. Las páginas 1 a 13 contienen el contenido principal del reto. La página 14 es principalmente visual, con logos de organizadores, coorganizadores, partners y sponsors. Aunque pediste 13 páginas, se incluye también la página 14 para no dejar nada fuera.

---

# Índice general del análisis

1. [Página 1 - Portada y ficha del reto](#pagina-1---portada-y-ficha-del-reto)
2. [Página 2 - Contenido del documento](#pagina-2---contenido-del-documento)
3. [Página 3 - Resumen ejecutivo, problema y objetivos](#pagina-3---resumen-ejecutivo-problema-y-objetivos)
4. [Página 4 - Alcance, exclusiones y usuarios beneficiarios](#pagina-4---alcance-exclusiones-y-usuarios-beneficiarios)
5. [Página 5 - Datos mínimos requeridos](#pagina-5---datos-minimos-requeridos)
6. [Página 6 - Señales de posible fraude, primera parte](#pagina-6---senales-de-posible-fraude-primera-parte)
7. [Página 7 - Señales restantes, reglas críticas y uso esperado de IA](#pagina-7---senales-restantes-reglas-criticas-y-uso-esperado-de-ia)
8. [Página 8 - Funcionalidades del prototipo, casos de uso y preguntas del agente](#pagina-8---funcionalidades-del-prototipo-casos-de-uso-y-preguntas-del-agente)
9. [Página 9 - Preguntas del agente, score sugerido y entregables](#pagina-9---preguntas-del-agente-score-sugerido-y-entregables)
10. [Página 10 - Estructura del repositorio y requisitos técnicos](#pagina-10---estructura-del-repositorio-y-requisitos-tecnicos)
11. [Página 11 - Seguridad, evaluación, métricas y riesgos](#pagina-11---seguridad-evaluacion-metricas-y-riesgos)
12. [Página 12 - Formato de presentación y matriz de evaluación](#pagina-12---formato-de-presentacion-y-matriz-de-evaluacion)
13. [Página 13 - Pitch, pruebas de fuego y entregables obligatorios](#pagina-13---pitch-pruebas-de-fuego-y-entregables-obligatorios)
14. [Página 14 - Organizadores, aliados y sponsors](#pagina-14---organizadores-aliados-y-sponsors)
15. [Requerimientos consolidados del proyecto](#requerimientos-consolidados-del-proyecto)
16. [Arquitectura recomendada para el hackathon](#arquitectura-recomendada-para-el-hackathon)
17. [Plan de implementación](#plan-de-implementacion)
18. [Checklist final para entrega](#checklist-final-para-entrega)

---

# Página 1 - Portada y ficha del reto

## Contenido identificado

La página 1 presenta la portada del reto:

**hackIAthon**  
**Reto Aseguradora del Sur**  
**Detector de Posibles Fraudes en Siniestros usando Inteligencia Artificial**

También indica que el documento es un:

**Documento de levantamiento funcional, alcance técnico, entregables y criterios de evaluación.**

La página incluye una ficha resumen con los elementos principales:

| Elemento | Definición |
|---|---|
| Sector | Asegurador |
| Tipo de solución | Prototipo funcional basado en Inteligencia Artificial |
| Datos permitidos | Datos públicos reales o datos sintéticos |
| Entregables | Prototipo funcional, código fuente, dataset, documentación y demo |
| Herramientas esperadas | Claude, ChatGPT, GitHub, Python, Oracle y R |
| Principio clave | La solución genera alertas de revisión, no acusaciones automáticas de fraude |

Al pie de página aparecen referencias visuales a los organizadores/coorganizadores:

- Organiza: Viamatica.
- Coorganiza: iT ahora y Citytech.
- También se muestran elementos visuales de Innovation Leader y Aseguradora del Sur.

## Análisis detallado de la página

Esta página define el marco completo del reto. Hay varios puntos críticos que deben guiar la solución:

### 1. El sector es asegurador

El proyecto no debe parecer un detector genérico de fraude financiero. Debe hablar el lenguaje de seguros:

- Siniestros.
- Pólizas.
- Asegurados.
- Beneficiarios.
- Proveedores.
- Talleres.
- Clínicas.
- Documentos de respaldo.
- Reclamos.
- Coberturas.
- Vigencia.

La solución debe demostrar que entiende cómo opera una aseguradora, especialmente en el proceso de revisión de siniestros.

### 2. El entregable es un prototipo funcional

No se espera un sistema de producción completo. Se espera algo que funcione, se pueda ejecutar y se pueda demostrar. Esto permite usar una arquitectura de demo siempre que sea clara, reproducible y defendible.

### 3. La solución debe usar Inteligencia Artificial

No basta con un dashboard con filtros. El PDF deja claro desde la portada que el prototipo debe estar basado en IA. La IA puede aparecer de varias formas:

- Machine Learning supervisado.
- Detección de anomalías.
- NLP para descripciones de reclamos.
- Agente consultivo.
- Explicaciones generadas automáticamente.

### 4. Se pueden usar datos sintéticos

Esto es clave. No necesitan datos reales de aseguradora. Pueden generar un dataset sintético bien diseñado, siempre que documente su estructura, supuestos y limitaciones.

### 5. La ética es central

El principio clave indica que la solución debe generar **alertas de revisión**, no acusaciones automáticas. Esto debe aparecer en:

- La interfaz.
- El README.
- La presentación.
- La explicación del score.
- La documentación de limitaciones.

Frase recomendada para la app:

> El sistema no determina fraude ni rechaza reclamos automáticamente. Solo prioriza casos con señales de riesgo para revisión humana especializada.

## Implicación para el desarrollo

La solución debe construirse como un sistema de apoyo a analistas, no como un juez automático. El lenguaje visual y textual debe evitar palabras como:

- “Fraude confirmado”.
- “Cliente fraudulento”.
- “Rechazar siniestro”.
- “Culpable”.

En su lugar se debe usar:

- “Posible riesgo”.
- “Caso para revisión”.
- “Alerta”.
- “Señal anómala”.
- “Priorización”.
- “Revisión humana”.

---

# Página 2 - Contenido del documento

## Contenido identificado

La página 2 presenta el índice del documento:

1. Resumen ejecutivo.
2. Planteamiento del problema.
3. Objetivos.
4. Alcance del reto.
5. Usuarios beneficiarios.
6. Datos mínimos requeridos.
7. Señales de posible fraude.
8. Reglas de negocio sugeridas.
9. Uso esperado de Inteligencia Artificial.
10. Funcionalidades del prototipo.
11. Casos de uso.
12. Preguntas que el agente de IA debe responder.
13. Score de riesgo sugerido.
14. Entregables obligatorios.
15. Estructura del repositorio.
16. Requisitos técnicos y estándares.
17. Seguridad, privacidad y ética.
18. Criterios de evaluación.
19. Métricas sugeridas.
20. Riesgos y mitigaciones.
21. Formato de presentación.

## Análisis detallado de la página

La estructura del índice permite entender que el reto no evalúa solo código. Evalúa un producto completo de hackathon:

- Entendimiento del problema.
- Diseño funcional.
- Datos.
- IA.
- Explicabilidad.
- Arquitectura.
- Ética.
- Demo.
- Presentación.

Esto significa que el equipo debe entregar más que una app. Debe entregar un paquete completo:

```txt
prototipo + dataset + repositorio + documentación + pitch + demo defendible
```

## Implicación para el desarrollo

Cada sección del PDF debe transformarse en una parte del repositorio:

| Sección del PDF | Artefacto del proyecto |
|---|---|
| Resumen ejecutivo | README y pitch |
| Problema | README, pitch, dashboard inicial |
| Objetivos | README y documentación funcional |
| Alcance | docs/arquitectura.md y docs/limitaciones.md |
| Datos mínimos | data/synthetic y docs/modelo_datos.md |
| Señales de fraude | src/rules/fraud_rules.py |
| Reglas de negocio | src/rules/fraud_rules.py y docs/reglas_negocio.md |
| Uso de IA | src/models, src/nlp, src/agent y docs/uso_ia.md |
| Funcionalidades | Streamlit app |
| Casos de uso | demo_script.md |
| Preguntas del agente | src/agent/agent_router.py |
| Score | src/scoring/scoring_service.py |
| Entregables | Checklist de entrega |
| Repositorio | Estructura GitHub |
| Seguridad y ética | docs/etica_privacidad.md |
| Evaluación | Estrategia de pitch |
| Métricas | model_metrics.json y docs/uso_ia.md |
| Riesgos | docs/limitaciones.md |
| Presentación | presentation/pitch.pdf |

---

# Página 3 - Resumen ejecutivo, problema y objetivos

## 1. Resumen ejecutivo

El documento explica que el sector asegurador enfrenta el reto de identificar oportunamente posibles patrones irregulares en siniestros reportados. La detección manual depende de:

- Experiencia del analista.
- Reglas dispersas.
- Revisión documental.
- Cruces de información.
- Tiempo disponible para revisar casos.

El reto consiste en desarrollar un prototipo funcional basado en Inteligencia Artificial que analice información de siniestros y genere:

- Un score de riesgo de posible fraude.
- Alertas explicables.
- Patrones detectados.
- Recomendaciones para revisión humana.

El documento enfatiza que la solución no debe emitir una acusación de fraude ni rechazar automáticamente un siniestro. Su propósito es identificar casos sospechosos, anómalos o de mayor riesgo para que sean revisados por un analista especializado.

## 2. Planteamiento del problema

El PDF explica que en una aseguradora los siniestros pueden presentar señales de riesgo que no siempre son evidentes en una revisión individual. Algunas alertas aparecen al cruzar variables como:

- Pólizas.
- Asegurados.
- Proveedores.
- Documentos.
- Fechas.
- Montos.
- Historial de reclamos.

Las señales mencionadas son:

- Frecuencia inusual de reclamos por asegurado o póliza.
- Montos reclamados superiores al promedio del ramo o del tipo de siniestro.
- Repetición de beneficiarios, proveedores, talleres o intermediarios asociados a casos observados.
- Reclamos ocurridos muy cerca de la fecha de inicio o fin de vigencia de la póliza.
- Documentos incompletos, ilegibles o inconsistentes.
- Narrativas similares entre diferentes reclamos.
- Cambios recientes en datos del asegurado antes del siniestro.
- Reporte tardío del evento frente a la fecha de ocurrencia.

## 3. Objetivos

### 3.1 Objetivo general

Desarrollar un prototipo funcional de Inteligencia Artificial que permita analizar siniestros de seguros, detectar patrones anómalos o señales de posible fraude, asignar un score de riesgo y generar explicaciones para apoyar la revisión del analista.

### 3.2 Objetivos específicos visibles en esta página

1. Cargar y procesar información sintética o pública de siniestros.
2. Identificar patrones atípicos en reclamos.
3. Calcular un score de riesgo por siniestro.
4. Clasificar casos en niveles de riesgo: verde, amarillo, rojo.
5. Generar alertas explicables para el analista.
6. Permitir consultas en lenguaje natural sobre los casos detectados.

## Análisis detallado de la página

Esta página contiene el núcleo funcional del reto. El sistema debe resolver un problema operativo real: los analistas no pueden revisar todos los casos con la misma profundidad. Por eso el sistema debe priorizar.

El valor del producto no es “decir quién hizo fraude”. El valor es reducir el ruido, ordenar los casos y explicar por qué algunos merecen revisión.

## Requerimientos funcionales derivados

De esta página salen estos requerimientos:

### RF-001: Carga de datos

El sistema debe cargar o generar datos de siniestros.

### RF-002: Cruce de información

El sistema debe cruzar datos entre siniestros, pólizas, asegurados, proveedores, documentos y vehículos.

### RF-003: Cálculo de score

Cada siniestro debe recibir un score de riesgo.

### RF-004: Clasificación visual

Cada siniestro debe clasificarse en verde, amarillo o rojo.

### RF-005: Explicabilidad

El sistema debe explicar por qué se asignó un determinado nivel de riesgo.

### RF-006: Consultas en lenguaje natural

El usuario debe poder preguntar por patrones, top de casos, proveedores, ciudades, documentos o motivos de alerta.

## Requerimientos no funcionales derivados

### RNF-001: Trazabilidad

Cada score debe tener reglas o factores asociados.

### RNF-002: Ética

El sistema debe evitar acusaciones automáticas.

### RNF-003: Reproducibilidad

El prototipo debe poder ejecutarse con instrucciones claras.

## Implicación para el dashboard

La pantalla principal debe mostrar:

- Cantidad total de siniestros.
- Casos por color de riesgo.
- Casos ordenados por prioridad.
- Top de alertas.
- Explicación de casos rojos.

---

# Página 4 - Alcance, exclusiones y usuarios beneficiarios

## Continuación de objetivos específicos

La página inicia con los objetivos específicos restantes:

7. Presentar un dashboard o interfaz funcional.
8. Documentar el modelo, reglas, datos y limitaciones.
9. Entregar código fuente ejecutable y reproducible.
10. Proponer una arquitectura escalable para una implementación futura.

## 4. Alcance del reto

### 4.1 Incluye

El reto incluye:

- Carga de un dataset de siniestros, pólizas, asegurados, vehículos, beneficiarios, proveedores y documentos.
- Los vehículos deben contemplar datos como placa, chasis, motor, marca, modelo y año.
- Análisis de variables del reclamo, pólizas, asegurados, vehículos, beneficiarios, proveedores y documentos.
- Detección de anomalías o señales de riesgo.
- Generación de score de posible fraude.
- Priorización de casos para revisión mediante semáforo: verde, amarillo, rojo.
- Explicación del motivo de cada alerta.
- Interfaz, dashboard, aplicación o notebook funcional para la demo.
- Exportación o visualización de un resumen o bandeja de casos sospechosos.

### 4.2 No incluye

El reto no incluye:

- Acusar formalmente a un asegurado de fraude.
- Rechazar automáticamente un siniestro.
- Sustituir el análisis humano.
- Usar datos personales reales o información confidencial.
- Tomar decisiones automáticas de pago o rechazo.
- Presentar conclusiones legales definitivas.

## 5. Usuarios beneficiarios

| Usuario | Beneficio esperado |
|---|---|
| Analista de siniestros | Priorización de casos y explicación de alertas. |
| Analista antifraude | Identificación temprana de patrones sospechosos. |
| Jefatura de siniestros | Visión consolidada de riesgos operativos. |
| Riesgos | Monitoreo de exposición y comportamiento anómalo. |
| Auditoría interna | Evidencia y trazabilidad para revisión. |
| Tecnología | Base para prototipo escalable e integrable. |
| Gerencia | Reducción potencial de pérdidas y mejora del control. |

## Análisis detallado de la página

Esta página define qué se debe construir y qué no se debe construir. Es una página de control de alcance.

La parte de “incluye” obliga a que el proyecto no sea solo una tabla de siniestros. Debe tener varias entidades:

- Siniestros.
- Pólizas.
- Asegurados.
- Vehículos.
- Beneficiarios/proveedores.
- Documentos.

La parte de “no incluye” es igual de importante. El jurado probablemente valorará que el equipo respete los límites éticos y legales.

## Implicaciones técnicas

### Entidades mínimas del modelo de datos

El sistema debería tener estas tablas o CSVs:

```txt
claims
policies
insured
vehicles
providers
documents
risk_scores
```

### Pantallas mínimas

El dashboard debe tener:

1. Dashboard ejecutivo.
2. Bandeja de casos.
3. Detalle de siniestro.
4. Análisis de proveedores.
5. Documentos y alertas.
6. Agente o consultas.
7. Exportación de reporte.

### Mensajes éticos en la interfaz

Se recomienda incluir un bloque visible:

> Esta herramienta genera alertas de posible riesgo para revisión humana. No acusa fraude, no rechaza siniestros y no reemplaza el criterio del analista.

## Implicación para el pitch

En la presentación se debe hablar de varios usuarios, no solo del analista. Por ejemplo:

- Para analistas: priorización.
- Para jefatura: tablero consolidado.
- Para auditoría: trazabilidad.
- Para tecnología: arquitectura escalable.
- Para gerencia: impacto operativo.

---

# Página 5 - Datos mínimos requeridos

## 6. Datos mínimos requeridos

El documento indica que se recomienda trabajar con datos sintéticos o públicos. Si se representa información interna de una aseguradora, los datos deben ser sintéticos y no contener información personal identificable.

## 6.1 Tabla: Siniestros

| Campo | Descripción |
|---|---|
| id_siniestro | Identificador único del siniestro. |
| id_poliza | Identificador de la póliza. |
| id_asegurado | Identificador anónimo del asegurado. |
| ramo | Vehículos, salud, vida, generales, hogar u otro. |
| cobertura | Choque, robo, atención médica, incendio, daño u otro. |
| fecha_ocurrencia | Fecha del evento. |
| fecha_reporte | Fecha de notificación. |
| monto_reclamado | Valor solicitado por el asegurado o proveedor. |
| monto_estimado | Valor estimado por la aseguradora. |
| monto_pagado | Valor pagado, si aplica. |
| estado | Reserva, Pago Total, Pago Parcial, Anticipo, Negativa, Cierre Sin Consecuencia, Liquidado. |
| sucursal | Sucursal del siniestro. |
| descripcion | Texto libre del reclamo. |
| documentos_completos | Indicador Sí/No. |
| beneficiario | Taller, clínica, perito u otro. |
| dias_desde_inicio_poliza | Días entre inicio de póliza y siniestro. |
| dias_desde_fin_poliza | Días entre fin de póliza y siniestro. |
| dias_entre_ocurrencia_reporte | Diferencia entre ocurrencia y reporte. |
| historial_siniestros_asegurado | Número de siniestros previos del asegurado. |
| etiqueta_fraude_simulada | 0/1, solo para entrenamiento o evaluación si aplica. |

## 6.2 Tablas complementarias sugeridas

| Tabla | Campos mínimos |
|---|---|
| Pólizas | id_poliza, id_asegurado, ramo, fecha_inicio, fecha_fin, prima, suma_asegurada, deducible, canal_venta, ciudad, estado_poliza. |
| Asegurados sintéticos | id_asegurado, segmento, antigüedad, ciudad, número de pólizas, reclamos últimos 12 meses, mora actual, score cliente simulado. |
| Beneficiarios / Proveedores | id_proveedor, tipo, ciudad, reclamos asociados, monto promedio reclamado, porcentaje de casos observados, antigüedad. |
| Documentos | id_documento, id_siniestro, tipo_documento, entregado, legible, fecha_emision, inconsistencia_detectada, observacion. |

## Análisis detallado de la página

Esta página es la guía del dataset. De aquí deben salir los CSV o tablas de la base de datos.

El campo `etiqueta_fraude_simulada` es especialmente importante porque permite entrenar un modelo supervisado sin usar datos reales. Esto se puede explicar así:

> Debido a que no se utilizan datos reales ni información confidencial, el dataset sintético incluye una etiqueta simulada generada a partir de patrones de riesgo conocidos. Esta etiqueta se usa únicamente para entrenamiento y evaluación del modelo, no como verdad legal.

## Modelo de datos recomendado

### Tabla `claims`

```txt
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
beneficiario
dias_desde_inicio_poliza
dias_desde_fin_poliza
dias_entre_ocurrencia_reporte
historial_siniestros_asegurado
etiqueta_fraude_simulada
```

### Tabla `policies`

```txt
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

### Tabla `insured`

```txt
id_asegurado
segmento
antiguedad_meses
ciudad
numero_polizas
reclamos_ultimos_12_meses
mora_actual
score_cliente_simulado
```

### Tabla `providers`

```txt
id_proveedor
tipo
ciudad
reclamos_asociados
monto_promedio_reclamado
porcentaje_casos_observados
antiguedad_meses
en_lista_restrictiva
```

### Tabla `documents`

```txt
id_documento
id_siniestro
tipo_documento
entregado
legible
fecha_emision
inconsistencia_detectada
observacion
```

## Implicación para generación de datos sintéticos

El generador de datos debe crear casos normales y casos sospechosos. Para que el modelo y las reglas tengan sentido, deben inyectarse patrones:

- Reclamos cerca del inicio o fin de póliza.
- Reportes tardíos.
- Montos anormalmente altos.
- Proveedores repetidos.
- Documentos incompletos o inconsistentes.
- Narrativas similares.
- Asegurados con múltiples reclamos.

---

# Página 6 - Señales de posible fraude, primera parte

## 7. Señales de posible fraude

La página 6 contiene una tabla extensa con señales, ejemplos y puntuaciones sugeridas.

| Señal | Ejemplo | Puntuación |
|---|---|---|
| Reclamo cercano al borde de vigencia | Siniestro ocurrido pocos días después de contratar la póliza o antes del fin de vigencia, menor o igual a 30 días. | Hasta 8 pts. Menor o igual a 10 días: 8 pts. 11 a 30 días: 4 pts. Mayor a 30 días: 0 pts. |
| Demora denuncia por robo | Tiempos prolongados entre la ocurrencia del evento y la denuncia formal en casos de robo. | Hasta 8 pts. Mayor a 48 horas: 8 pts. 24 a 48 horas: 4 pts. Menor a 24 horas: 0 pts. |
| Alta frecuencia de reclamos asegurado | Asegurado con múltiples siniestros en un periodo menor o igual a 18 meses. | Hasta 8 pts. 3 o más siniestros: 8 pts. 2 siniestros: 4 pts. 0-1 siniestros: 0 pts. |
| Alta frecuencia de reclamos vehículo | Vehículo con múltiples siniestros en un periodo menor o igual a 18 meses. | Hasta 6 pts. 3 o más siniestros: 6 pts. 2 siniestros: 3 pts. 0-1 siniestros: 0 pts. |
| Alta frecuencia de conductor vehículo | Conductor presente en múltiples siniestros en un periodo menor o igual a 18 meses. | Hasta 8 pts. 3 o más siniestros: 8 pts. 2 siniestros: 4 pts. 0-1 siniestros: 0 pts. |
| Alta frecuencia reclamos solo RC | Frecuencia atípica de siniestros donde solo se afecta la cobertura de Responsabilidad Civil. | Hasta 6 pts. Más de 2 eventos previos de solo RC: 6 pts. 1 evento previo: 3 pts. |
| Beneficiario / Proveedor recurrente | Proveedor asociado a varios casos observados. | Hasta 10 pts. En lista restrictiva: 10 pts. En más de 2 casos observados este año: 5 pts. |
| Documentos incompletos | Falta denuncia, factura, informe o evidencia requerida. | Hasta 4 pts. Falta documento legal obligatorio: 4 pts. |
| Dinámica sospechosa | Tipos de accidentes que requieren revisión minuciosa cruzada, como frontal, posterior, volcadura o múltiple. | Hasta 6 pts. Relato ilógico vs tipo de impacto: 6 pts. Accidente múltiple de madrugada: 3 pts. |
| Eventos sin tercero identificado | Siniestros donde el vehículo asegurado resulta afectado, pero no existe o huye el tercer involucrado. | Hasta 6 pts. Daño severo sin rastro del tercero ni cámaras: 5 pts. |
| Documentos inconsistentes | Fechas no coinciden, valores diferentes o documentos ilegibles. | Hasta 10 pts. Alteración confirmada o fechas de factura previas al evento: 10 pts. |
| Reporte tardío | El siniestro se reporta muchos días después del evento. | Hasta 5 pts. Mayor a 7 días: 5 pts. 4 a 7 días: 3 pts. Menor o igual a 3 días: 0 pts. |

## Análisis detallado de la página

Esta página es la base del motor de reglas. Aquí el PDF entrega una rúbrica explícita de señales y puntos. El sistema debe implementar estas señales para ser defendible.

## Reglas técnicas derivadas

### R001 - Reclamo cercano al borde de vigencia

Condición:

```txt
Si dias_desde_inicio_poliza <= 10 o dias_desde_fin_poliza <= 10: +8
Si está entre 11 y 30 días: +4
Si es mayor a 30 días: +0
```

Explicación:

> El siniestro ocurrió muy cerca del inicio o fin de vigencia de la póliza, lo que puede requerir revisión adicional.

### R002 - Demora en denuncia por robo

Condición:

```txt
Si cobertura = Robo y dias_entre_ocurrencia_reporte > 2: +8
Si cobertura = Robo y el reporte está entre 1 y 2 días: +4
```

Explicación:

> En casos de robo, una demora prolongada entre la ocurrencia y la denuncia puede ser una señal de revisión.

### R003 - Alta frecuencia por asegurado

Condición:

```txt
Si historial_siniestros_asegurado >= 3: +8
Si historial_siniestros_asegurado = 2: +4
```

Explicación:

> El asegurado registra múltiples reclamos en un periodo reciente.

### R004 - Alta frecuencia por vehículo

Condición:

```txt
Si reclamos_vehiculo_18_meses >= 3: +6
Si reclamos_vehiculo_18_meses = 2: +3
```

Explicación:

> El vehículo presenta múltiples siniestros recientes.

### R005 - Alta frecuencia por conductor

Condición:

```txt
Si conductor aparece en 3 o más siniestros: +8
Si conductor aparece en 2 siniestros: +4
```

Explicación:

> El conductor aparece asociado a múltiples reclamos.

### R006 - Reclamos solo RC

Condición:

```txt
Si hay más de 2 eventos previos de solo Responsabilidad Civil: +6
Si hay 1 evento previo: +3
```

Explicación:

> Existe una frecuencia atípica de reclamos donde solo se afecta RC.

### R007 - Proveedor recurrente

Condición:

```txt
Si proveedor está en lista restrictiva: +10
Si proveedor aparece en más de 2 casos observados: +5
```

Explicación:

> El proveedor está asociado a varios casos observados o forma parte de una lista restrictiva simulada.

### R008 - Documentos incompletos

Condición:

```txt
Si falta documento obligatorio: +4
```

Explicación:

> El expediente no cuenta con todos los documentos requeridos para revisión.

### R009 - Dinámica sospechosa

Condición:

```txt
Si relato ilógico contra tipo de impacto: +6
Si accidente múltiple de madrugada: +3
```

Explicación:

> La dinámica del evento requiere validación adicional por inconsistencias o condiciones atípicas.

### R010 - Sin tercero identificado

Condición:

```txt
Si daño severo y no hay tercero identificado ni evidencia: +5
```

Explicación:

> El evento indica daño relevante sin tercero identificado ni evidencia complementaria.

### R011 - Documentos inconsistentes

Condición:

```txt
Si hay alteración confirmada, fechas imposibles, factura previa al evento o documento ilegible: +10
```

Explicación:

> Se detectaron inconsistencias documentales que requieren revisión especializada.

### R012 - Reporte tardío

Condición:

```txt
Si dias_entre_ocurrencia_reporte > 7: +5
Si dias_entre_ocurrencia_reporte entre 4 y 7: +3
```

Explicación:

> El siniestro fue reportado varios días después de la fecha de ocurrencia.

## Implicación para el sistema

El sistema debe guardar por cada caso:

```json
{
  "id_siniestro": "SIN-001",
  "score_reglas": 37,
  "reglas_activadas": [
    "R001 - Reclamo cercano al borde de vigencia",
    "R007 - Proveedor recurrente",
    "R011 - Documentos inconsistentes"
  ],
  "explicacion": "El caso requiere revisión por cercanía a la vigencia, recurrencia del proveedor e inconsistencias documentales."
}
```

---

# Página 7 - Señales restantes, reglas críticas y uso esperado de IA

## Señales restantes de posible fraude

La página continúa la tabla de señales:

| Señal | Ejemplo | Puntuación |
|---|---|---|
| Narrativas similares | Descripciones parecidas entre varios reclamos. | Hasta 8 pts. Más de 85% de similitud textual con otro reclamo: 8 pts. 70% - 84%: 4 pts. |
| Monto cercano o superior a suma asegurada | Valor reclamado representa una proporción muy alta de la cobertura. | Hasta 5 pts. Reclamo mayor a 95% de la suma asegurada o 50% por encima del promedio de reparación: 4 pts. |

## 8. Reglas de negocio sugeridas críticas

| Código | Regla | Clasificación |
|---|---|---|
| RF-01 | Cobertura Pérdida Total por Robo (PTxRB) | Rojo |
| RF-02 | Evidencia de Falsificación o Adulteración Documental Evidente | Rojo |
| RF-03 | Asegurado, Beneficiario o APS con coincidencia exacta con “Lista Restrictiva” | Rojo |
| RF-04 | Dinámica del accidente físicamente imposible | Rojo |
| RF-05 | Siniestro extremo al borde de vigencia menor a 48 horas | Amarillo |
| RF-06 | Demora atípica en denuncia de robo mayor a 4 días | Amarillo |
| RF-07 | Narrativa idéntica o clonada | Amarillo |

## 9. Uso esperado de Inteligencia Artificial

| Enfoque | Aplicación esperada |
|---|---|
| Machine Learning supervisado | Predicción de probabilidad de posible fraude usando etiqueta simulada. |
| Detección de anomalías | Identificación de casos fuera del comportamiento esperado. |
| Procesamiento de lenguaje natural | Análisis de descripciones, similitud textual, extracción de entidades y resúmenes. |
| Agente de IA explicativo | Consultas en lenguaje natural sobre casos, alertas, proveedores y patrones. |
| Enfoque híbrido | Combinación de reglas de negocio, modelo de anomalías, análisis textual, dashboard y explicación. |

El documento indica que la mejor solución combinaría:

- Reglas de negocio.
- Modelo de anomalías o clasificación.
- Análisis de texto.
- Dashboard.
- Agente de explicación.

## Análisis detallado de la página

Esta página es clave para diferenciar un proyecto básico de uno competitivo.

El PDF no quiere únicamente reglas `if/else`. Tampoco quiere un modelo caja negra sin explicación. La frase más importante es que la mejor solución combina varios enfoques.

## Implicaciones técnicas

La arquitectura debe ser híbrida:

```txt
Score final = reglas + ML supervisado + anomalías + NLP + explicación
```

### Modelo supervisado

Se puede usar:

- RandomForestClassifier.
- LogisticRegression como alternativa simple.

Entrada:

- Días desde inicio/fin de póliza.
- Días entre ocurrencia y reporte.
- Monto reclamado.
- Relación monto/suma asegurada.
- Historial del asegurado.
- Frecuencia del proveedor.
- Inconsistencias documentales.
- Similitud textual.

Salida:

- `score_ml`.
- Probabilidad simulada de riesgo.

### Detección de anomalías

Se puede usar:

- IsolationForest.

Objetivo:

- Identificar casos raros aunque no coincidan exactamente con reglas.

### NLP

Se debe implementar:

- TF-IDF.
- Cosine Similarity.

Objetivo:

- Detectar narrativas similares.
- Identificar reclamos clonados o parecidos.

### Agente IA explicativo

Debe responder consultas como:

- Top casos de mayor riesgo.
- Motivo de un caso rojo.
- Proveedores con alertas.
- Documentos faltantes.
- Patrones repetidos.

## Fórmula de score recomendada

```txt
score_final = 0.55 * score_reglas + 0.25 * score_ml + 0.10 * score_anomalia + 0.10 * score_nlp
```

Justificación:

- Las reglas pesan más porque son explicables.
- El modelo ML aporta priorización probabilística.
- El modelo de anomalías detecta rarezas.
- El NLP aporta señales de narrativas parecidas.

## Reglas críticas como override

Algunas reglas deben subir el nivel mínimo:

```txt
Si RF-01, RF-02, RF-03 o RF-04 se activa: nivel mínimo Rojo.
Si RF-05, RF-06 o RF-07 se activa: nivel mínimo Amarillo.
```

Esto permite alinear el sistema con las reglas críticas del documento.

---

# Página 8 - Funcionalidades del prototipo, casos de uso y preguntas del agente

## 10. Funcionalidades del prototipo

### 10.1 Funcionalidades mínimas

El documento lista como funcionalidades mínimas:

1. Carga de datos de siniestros.
2. Cálculo de variables de riesgo.
3. Detección de alertas por reglas.
4. Modelo de IA para score de posible fraude.
5. Clasificación de riesgo: bajo, medio, alto o crítico.
6. Dashboard o interfaz para revisar casos.
7. Explicación automática del motivo de la alerta.

### 10.2 Funcionalidades deseables

- Chat con los casos y consultas en lenguaje natural.
- Análisis del texto del reclamo.
- Red de relaciones entre asegurados, proveedores y casos.
- Ranking de proveedores con mayor concentración de alertas.
- Simulación de ahorro potencial.
- Exportación de reporte para auditoría.
- API funcional para integración futura.

## 11. Casos de uso

| Código | Caso de uso | Resultado esperado |
|---|---|---|
| CU-01 | Cargar siniestros | El sistema valida estructura y procesa la información. |
| CU-02 | Calcular score de riesgo | Cada siniestro recibe un puntaje de riesgo. |
| CU-03 | Priorizar casos | El analista visualiza los casos ordenados por riesgo. |
| CU-04 | Explicar alerta | El sistema muestra factores como monto atípico, proveedor recurrente o documentos incompletos. |
| CU-05 | Consultar mediante IA | El usuario obtiene respuestas basadas en los datos. |
| CU-06 | Generar reporte | El sistema genera un resumen ejecutivo de casos de mayor riesgo. |

## 12. Preguntas que el agente de IA debe responder

La página inicia la lista de preguntas:

18. ¿Cuáles son los 10 siniestros con mayor riesgo de posible fraude?
19. ¿Por qué este siniestro fue marcado como alto riesgo?
20. ¿Qué proveedores concentran más alertas?
21. ¿Qué ramos tienen mayor porcentaje de casos sospechosos?

## Análisis detallado de la página

Esta página separa lo obligatorio de lo deseable. Para el hackathon, el proyecto debe cubrir todas las funcionalidades mínimas y escoger varias deseables de alto impacto.

## Funcionalidades obligatorias para el MVP

```txt
- Cargar/generar dataset.
- Procesar variables de riesgo.
- Aplicar reglas.
- Calcular score.
- Clasificar riesgo.
- Mostrar dashboard.
- Explicar alertas.
```

## Funcionalidades deseables que sí conviene implementar

Con alto impacto y dificultad razonable:

```txt
- Chat/agente consultivo.
- Análisis textual con TF-IDF.
- Ranking de proveedores.
- Exportación CSV de casos críticos.
- Resumen ejecutivo.
```

## Funcionalidades deseables opcionales

Solo si hay tiempo:

```txt
- Red de relaciones visual.
- Simulación de ahorro potencial avanzada.
- API FastAPI.
- MCP real.
```

## Pantallas derivadas

### Pantalla 1: Dashboard ejecutivo

Debe mostrar:

- KPIs.
- Distribución de riesgos.
- Monto total reclamado.
- Monto en casos rojos.
- Top proveedores.
- Top ciudades.

### Pantalla 2: Bandeja de siniestros

Debe permitir:

- Filtrar casos.
- Ordenar por score.
- Seleccionar un caso.

### Pantalla 3: Detalle del caso

Debe mostrar:

- Score.
- Semáforo.
- Reglas activadas.
- Explicación.
- Documentos.
- Proveedor.
- Narrativas similares.

### Pantalla 4: Agente

Debe responder las preguntas del PDF.

### Pantalla 5: Reporte

Debe exportar:

- Casos rojos.
- Todos los scores.
- Resumen ejecutivo.

---

# Página 9 - Preguntas del agente, score sugerido y entregables

## Continuación de preguntas que el agente debe responder

22. ¿Qué ciudades presentan mayor concentración de alertas?
23. ¿Qué asegurados tienen mayor frecuencia de reclamos?
24. ¿Qué documentos faltan en los casos críticos?
25. ¿Qué casos tienen montos atípicos?
26. ¿Qué siniestros ocurrieron cerca del inicio de la póliza?
27. ¿Qué patrones se repiten en los reclamos sospechosos?
28. Genera un resumen ejecutivo de los casos críticos.
29. Recomienda qué casos debería revisar primero el analista.

## 13. Score de riesgo sugerido

| Rango | Nivel | Acción sugerida |
|---|---|---|
| 0 - 40 | Verde Bajo | Continuar flujo normal. |
| 41 - 75 | Amarillo Medio | Escala a Unidad Antifraude para revisión documental. |
| 76 - 100 | Rojo Alto | Escala Unidad Antifraude para revisión especializada de campo. |

El documento indica que los pesos son referenciales. Los equipos pueden proponer otro esquema si explican:

- La lógica.
- La validación.
- La trazabilidad del score.

## 14. Entregables obligatorios

| Entregable | Descripción |
|---|---|
| Prototipo funcional | Aplicación, dashboard, notebook o sistema ejecutable. |
| Código fuente | Repositorio GitHub disponible para revisión del jurado. |
| Dataset | Sintético o público, con explicación de origen y estructura. |
| README | Instrucciones de instalación, ejecución y demo. |
| Arquitectura | Diagrama o explicación técnica. |
| Modelo de datos | Tablas, campos y relaciones. |
| Explicación del modelo IA | Algoritmo, variables, lógica, métricas y limitaciones. |
| Rúbrica de alertas | Reglas o criterios usados para generar alertas. |
| Demo funcional | Presentación en vivo durante el evento. |
| Presentación ejecutiva | Problema, solución, impacto y próximos pasos. |

## Análisis detallado de la página

Esta página define dos cosas críticas:

1. Cómo debe clasificarse el riesgo.
2. Qué debe entregarse sí o sí.

## Implementación del agente

El agente debe tener herramientas/funciones para responder las preguntas exactas.

Funciones recomendadas:

```python
get_top_risk_claims(limit=10)
explain_claim_risk(id_siniestro)
get_provider_alert_summary()
get_branch_or_line_risk_summary()
get_city_risk_summary()
get_high_frequency_insured()
get_missing_documents_critical()
get_outlier_amount_claims()
get_claims_near_policy_start()
get_repeated_patterns()
generate_executive_summary()
recommend_priority_cases()
```

## Implementación del score

El sistema debe mapear el score así:

```txt
0 - 40: Verde
41 - 75: Amarillo
76 - 100: Rojo
```

Y asignar acción sugerida:

```txt
Verde: continuar flujo normal.
Amarillo: revisión documental antifraude.
Rojo: revisión especializada de campo.
```

## Entregables como carpetas del repo

| Entregable | Carpeta/archivo sugerido |
|---|---|
| Prototipo funcional | `src/app/main.py` |
| Código fuente | GitHub repo |
| Dataset | `data/synthetic/` |
| README | `README.md` |
| Arquitectura | `docs/arquitectura.md` |
| Modelo de datos | `docs/modelo_datos.md` |
| Explicación IA | `docs/uso_ia.md` |
| Rúbrica de alertas | `docs/reglas_negocio.md` |
| Demo funcional | `docs/demo_script.md` |
| Presentación ejecutiva | `presentation/pitch.pdf` |

---

# Página 10 - Estructura del repositorio y requisitos técnicos

## 15. Estructura sugerida del repositorio GitHub

El PDF sugiere la siguiente estructura:

```txt
fraudia-claims/
├── README.md
├── requirements.txt
├── .env.example
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
├── notebooks/
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_modelo_fraude.ipynb
│   └── 03_evaluacion_modelo.ipynb
├── src/
│   ├── ingestion/load_data.py
│   ├── features/build_features.py
│   ├── rules/fraud_rules.py
│   ├── models/fraud_model.py
│   ├── explainability/explain_score.py
│   ├── ai_agent/claims_agent.py
│   └── app/main.py
├── docs/
│   ├── arquitectura.md
│   ├── modelo_datos.md
│   ├── reglas_negocio.md
│   ├── uso_ia.md
│   └── limitaciones.md
├── tests/
│   └── test_rules.py
└── presentation/
    └── pitch.pdf
```

## 16. Requisitos técnicos y estándares

| Categoría | Estándar mínimo |
|---|---|
| Lenguajes | Python, R y SQL. |
| Base de datos | Oracle, PostgreSQL, MySQL o archivos planos. |
| Repositorio | GitHub público o privado con acceso al jurado. |
| Documentación | README, arquitectura, modelo de datos, reglas y uso de IA. |
| Código | Modular, comentado, ejecutable y reproducible. |
| Interfaz | Aplicación web, dashboard, notebook o consola funcional con demo clara. |
| Dependencias | requirements.txt, renv.lock u otro mecanismo equivalente. |
| Configuración | Uso de .env.example; no credenciales reales. |

## Análisis detallado de la página

La página 10 es una guía directa para organizar el repositorio. Conviene seguirla casi exactamente porque el jurado podría revisar estructura.

## Estructura recomendada adaptada

```txt
fraudlens-claims-ai/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── setup_demo.py
├── data/
│   ├── raw/
│   ├── synthetic/
│   └── processed/
├── notebooks/
│   ├── 01_exploracion_datos.ipynb
│   ├── 02_modelo_fraude.ipynb
│   └── 03_evaluacion_modelo.ipynb
├── src/
│   ├── app/
│   │   └── main.py
│   ├── data_generation/
│   │   └── generate_synthetic_data.py
│   ├── database/
│   │   ├── build_database.py
│   │   └── connection.py
│   ├── features/
│   │   └── build_features.py
│   ├── rules/
│   │   └── fraud_rules.py
│   ├── models/
│   │   ├── fraud_model.py
│   │   ├── train_model.py
│   │   └── anomaly_detector.py
│   ├── nlp/
│   │   └── narrative_similarity.py
│   ├── scoring/
│   │   └── scoring_service.py
│   ├── explainability/
│   │   └── explain_score.py
│   ├── agent/
│   │   ├── claims_agent.py
│   │   ├── agent_router.py
│   │   └── agent_tools.py
│   └── reports/
│       └── report_service.py
├── docs/
│   ├── arquitectura.md
│   ├── modelo_datos.md
│   ├── reglas_negocio.md
│   ├── uso_ia.md
│   ├── etica_privacidad.md
│   └── limitaciones.md
├── tests/
│   ├── test_rules.py
│   ├── test_scoring.py
│   └── test_agent.py
└── presentation/
    └── pitch.pdf
```

## Decisión sobre tecnologías

Aunque el PDF menciona Python, R y SQL, no es obligatorio usar R si Python cubre todo. Se puede documentar que:

- Python se usa como lenguaje principal.
- SQL se usa mediante SQLite.
- R se considera compatible para análisis futuro, pero no se implementa por alcance del prototipo.

## Base de datos

El PDF permite archivos planos. Por eso se puede usar:

- CSV sintéticos.
- SQLite local.

Y explicar:

> Para facilitar reproducibilidad en el hackathon se usa SQLite y CSV. La arquitectura puede migrarse a Oracle, PostgreSQL o MySQL mediante una capa de acceso a datos.

---

# Página 11 - Seguridad, evaluación, métricas y riesgos

## 17. Seguridad, privacidad y ética

El documento exige:

- No usar datos personales reales.
- No usar información confidencial de aseguradoras.
- Usar datos sintéticos o públicos.
- Anonimizar cualquier identificador.
- No subir credenciales a GitHub.
- No exponer llaves de API.
- Documentar fuentes de datos.
- Aclarar que el resultado es una alerta, no una acusación.
- Mantener revisión humana antes de cualquier decisión.
- Explicar limitaciones del modelo y posibles falsos positivos.

## 18. Criterios de evaluación

| Criterio | Peso |
|---|---:|
| Entendimiento del problema de fraude en seguros | 15% |
| Calidad del prototipo funcional | 20% |
| Uso efectivo de IA | 20% |
| Explicabilidad y trazabilidad del score | 15% |
| Calidad técnica del código y arquitectura | 10% |
| Seguridad, privacidad y ética | 10% |
| Impacto de negocio y escalabilidad | 10% |

## 19. Métricas sugeridas

| Tipo de enfoque | Métricas sugeridas |
|---|---|
| Modelo supervisado | Precision, recall, F1-score, matriz de confusión y AUC-ROC. |
| Modelo de anomalías | Porcentaje de casos marcados, ranking de anomalías, score de rareza y validación con reglas. |
| NLP | Calidad de extracción, similitud textual, coherencia de resúmenes y explicación de narrativas repetidas. |

## 20. Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Confundir alerta con acusación | Usar lenguaje de posible fraude o requiere revisión. |
| Sesgo en datos | Usar variables explicables y análisis de sesgo. |
| Falsos positivos | Mantener revisión humana y explicar factores. |
| Datos sensibles | Usar datos sintéticos o públicos. |
| Modelo caja negra | Exigir explicación del score y reglas activadas. |
| Sobreajuste | Validar con datos separados o explicar la validación. |
| Mal uso legal | Declarar limitaciones y alcance no decisorio. |
| Dependencia de APIs externas | Documentar dependencias y tener una alternativa de demo. |

## Análisis detallado de la página

Esta página define cómo ganar puntos. El peso más alto acumulado está en:

- Prototipo funcional: 20%.
- Uso efectivo de IA: 20%.
- Explicabilidad: 15%.
- Entendimiento del problema: 15%.

Eso suma 70% del puntaje. La solución debe priorizar:

```txt
funciona + usa IA + explica + entiende seguros
```

## Implicación para documentación ética

Debe existir un archivo `docs/etica_privacidad.md` con:

- Datos sintéticos.
- IDs anonimizados.
- No uso de datos personales reales.
- No credenciales.
- No acusación automática.
- Revisión humana.
- Falsos positivos.
- Limitaciones del modelo.

## Implicación para métricas

Debe generarse un archivo:

```txt
data/processed/model_metrics.json
```

Con algo como:

```json
{
  "accuracy": 0.86,
  "precision": 0.82,
  "recall": 0.78,
  "f1_score": 0.80,
  "confusion_matrix": [[160, 14], [20, 56]],
  "roc_auc": 0.88
}
```

Incluso si los datos son sintéticos, sirve para demostrar método.

## Implicación para interfaz

Agregar una advertencia visible:

```txt
⚠️ Esta herramienta no determina fraude. Genera alertas explicables para revisión humana.
```

---

# Página 12 - Formato de presentación y matriz de evaluación

## 21. Formato de presentación del día del evento

| Tiempo | Contenido |
|---:|---|
| 1 min | Problema y oportunidad. |
| 1 min | Solución propuesta. |
| 4 min | Demo funcional. |
| 2 min | Arquitectura y uso de IA. |
| 1 min | Impacto de negocio. |
| 1 min | Limitaciones y próximos pasos. |
| 5 min | Preguntas del jurado. |

## 22. Matriz de evaluación para el hackIAthon 2026: Reto Aseguradora del Sur

La página explica que la tabla fue diseñada para que los equipos comprendan qué se espera de la solución y cómo alcanzar la máxima puntuación.

### Dimensión: Tecnología y Arquitectura - 10%

| Nivel | Descripción |
|---|---|
| 1 Limitado | Código desordenado, sin requirements.txt o falla al ejecutar. |
| 2 Básico | Scripts aislados sin arquitectura clara; sin uso de .env. |
| 3 Funcional | Repositorio organizado según el estándar solicitado. |
| 4 Avanzado | Arquitectura robusta, escalable y manejo correcto de excepciones. |
| 5 Excepcional | Código de nivel producción, modular, con documentación técnica profunda. |

### Dimensión: Análisis del Caso y Lógica - 15%

| Nivel | Descripción |
|---|---|
| 1 Limitado | No identifica señales de riesgo mínimas como fechas o montos. |
| 2 Básico | Reglas simples, por ejemplo solo vigencia, sin score ponderado. |
| 3 Funcional | Implementa el semáforo de riesgo verde/amarillo/rojo solicitado. |
| 4 Avanzado | Cruza múltiples variables como asegurado, proveedor y narrativa. |
| 5 Excepcional | Detecta patrones complejos como redes de relación o anomalías no evidentes. |

### Dimensión: Uso de IA y Prototipo - 40%

| Nivel | Descripción |
|---|---|
| 1 Limitado | Solo utiliza lógica de reglas rígidas IF/ELSE. |
| 2 Básico | Implementa un modelo de ML básico sobre datos sintéticos. |
| 3 Funcional | Prototipo funcional que integra modelos de IA, ML o NLP. |
| 4 Avanzado | Uso eficiente de APIs de IA como Claude/ChatGPT para análisis de texto. |
| 5 Excepcional | Enfoque híbrido: ML + NLP + Agente de IA para consultas en lenguaje natural. |

### Dimensión: Explicabilidad y Ética - 25%

| Nivel | Descripción |
|---|---|
| 1 Limitado | El modelo es una caja negra; no explica el porqué del score. |
| 2 Básico | Indica qué regla se activó, pero de forma técnica o poco clara. |
| 3 Funcional | Genera una explicación textual simple del motivo de la alerta. |
| 4 Avanzado | El agente de IA redacta un resumen justificando el nivel de riesgo. |
| 5 Excepcional | Documenta riesgos, sesgos y garantiza que la IA sea solo una alerta. |

## Análisis detallado de la página

Esta página es casi una receta para ganar.

Para aspirar a nivel alto:

```txt
- Repositorio organizado.
- Score ponderado.
- Cruce de múltiples variables.
- ML + NLP + agente.
- Explicaciones claras.
- Ética documentada.
```

## Estrategia para puntuar alto

### Tecnología y arquitectura

Hacer:

- `requirements.txt`.
- `.env.example`.
- README claro.
- Estructura modular.
- Manejo de errores básico.
- Código ejecutable con `setup_demo.py`.

### Análisis y lógica

Hacer:

- Score ponderado.
- Variables de póliza, asegurado, proveedor, documentos, narrativa y monto.
- Semáforo.
- Reglas críticas.

### Uso de IA

Hacer:

- RandomForest.
- IsolationForest.
- TF-IDF.
- Agente de consultas.

### Explicabilidad y ética

Hacer:

- Explicación por caso.
- Resumen del agente.
- Archivo de ética.
- Advertencia en dashboard.

---

# Página 13 - Pitch, pruebas de fuego y entregables obligatorios

## Continuación de la matriz: Pitch, Impacto y Negocio - 10%

| Nivel | Descripción |
|---|---|
| 1 Limitado | No explica la solución en tiempo o no realiza demo en vivo. |
| 2 Básico | Presentación técnica que olvida el impacto de negocio. |
| 3 Funcional | Estructura clara: problema, solución, demo y arquitectura. |
| 4 Avanzado | Comunicación fluida con visión clara de impacto operativo. |
| 5 Excepcional | Pitch persuasivo que demuestra valor real y escalabilidad futura. |

## 23. Guía de preparación para el Pitch - 10 minutos

El documento indica que los equipos deben prepararse para evaluaciones dinámicas del jurado.

### 1. Cuestionario crítico

Los equipos deben estar listos para preguntas como:

- Técnica: ¿Cómo detectan específicamente la similitud entre dos narrativas de reclamo?
- Negocio: ¿Cómo ayuda su solución a que un analista humano tome una decisión más rápida?
- Ética: ¿Qué medidas tomaron para evitar que la IA acuse a un cliente de fraude injustamente?

### 2. Pruebas de fuego - Live Demo

Durante el pitch, el jurado podrá solicitar:

- Consulta agentica: “Pregúntele a su sistema: ¿Qué proveedores concentran el 80% de las alertas rojas?”
- Prueba de score: “Cargue este siniestro ocurrido 24 horas después de la póliza y explíquenos el riesgo asignado”.
- Verificación de repositorio: “Muestre la estructura de su GitHub para verificar la modularidad del código”.

### 3. Entregables obligatorios para calificar

- Prototipo funcional: aplicación, dashboard o notebook ejecutable.
- Código fuente: repositorio en GitHub con README.md detallado.
- Dataset: datos sintéticos o públicos utilizados para la prueba.
- Presentación ejecutiva: PDF con el pitch del equipo.

## Análisis detallado de la página

Esta página indica cómo será la defensa. No basta con tener una app. Hay que preparar respuestas y escenarios de demo.

## Respuestas preparadas para el jurado

### Pregunta técnica: ¿Cómo detectan similitud entre narrativas?

Respuesta sugerida:

> Convertimos cada descripción de reclamo en un vector TF-IDF, que representa la importancia de los términos dentro del conjunto de narrativas. Luego calculamos similitud coseno entre los vectores. Si dos reclamos superan 0.85 de similitud, se activa una alerta fuerte de narrativa posiblemente clonada; entre 0.70 y 0.84 se activa una alerta media. Esta señal no confirma fraude, solo recomienda revisión.

### Pregunta de negocio: ¿Cómo ayuda al analista?

Respuesta sugerida:

> El sistema reduce el tiempo de revisión inicial porque ordena los siniestros por prioridad, muestra el motivo de cada alerta y permite consultar patrones por proveedor, ciudad, ramo o documentos. El analista no revisa a ciegas; empieza por los casos con mayor concentración de señales.

### Pregunta ética: ¿Cómo evitan acusaciones injustas?

Respuesta sugerida:

> La solución no usa lenguaje de fraude confirmado. Clasifica como riesgo de revisión, no como culpabilidad. Además, muestra los factores del score, usa datos sintéticos anonimizados, documenta limitaciones y mantiene la decisión final en manos de un analista humano.

## Pruebas de fuego que la app debe soportar

### Prueba 1: Proveedores con 80% de alertas rojas

El agente debe poder responder:

```txt
Los proveedores que concentran la mayor parte de alertas rojas son X, Y y Z. En conjunto representan N casos rojos, asociados principalmente a documentos inconsistentes, montos atípicos y recurrencia de reclamos.
```

### Prueba 2: Siniestro ocurrido 24 horas después de la póliza

La app debe permitir simular o mostrar un caso así:

```txt
Siniestro: SIN-TEST-001
Días desde inicio de póliza: 1
Regla activada: Reclamo extremo al borde de vigencia
Puntaje adicional: alto
Nivel sugerido: Amarillo o Rojo según otros factores
Explicación: requiere revisión documental por ocurrir 24 horas después de contratar la póliza.
```

### Prueba 3: Mostrar repositorio

La estructura debe verse ordenada:

```txt
README.md
requirements.txt
.env.example
data/
src/
docs/
tests/
presentation/
```

## Implicación final para el equipo

Antes de presentar, deben ensayar estos 3 flujos:

1. Dashboard general → caso rojo → explicación.
2. Agente → pregunta de proveedores → respuesta.
3. GitHub → estructura → README → docs.

---

# Página 14 - Organizadores, aliados y sponsors

## Contenido visual identificado

La página 14 es principalmente visual. Muestra logos y categorías de entidades relacionadas con el evento.

Se identifican las siguientes categorías:

- hackIAthon.
- Innovation Leader.
- Aseguradora del Sur.
- Organizador: Viamatica.
- Coorganizadores: iT ahora y Citytech.
- International Partners: Notion, TD Synnex y AWS.
- Academic Partner: UTEG.
- Sponsor Corporativo: Futuro Casa de Valores.
- Sponsor Aliado: Qualtic e Ianexo.
- Aliado Estratégico: Solog, CITEC, Aranas, Costa Rica, Procomer, Mensis y FullRestack.

En la parte inferior vuelve a aparecer:

- Organiza: Viamatica.
- Coorganiza: iT ahora y Citytech.

## Análisis detallado de la página

Esta página no agrega requisitos funcionales, pero sí ayuda a entender el contexto del evento. Al haber sponsors y partners tecnológicos, el pitch debe sonar profesional y empresarial.

## Implicación para el pitch

Conviene usar lenguaje de impacto corporativo:

- Reducción de tiempo de revisión.
- Priorización de casos.
- Trazabilidad de alertas.
- Escalabilidad futura.
- Integración con fuentes corporativas.
- Gobierno de datos.
- Revisión humana.

---

# Requerimientos consolidados del proyecto

## Requerimientos funcionales

| Código | Requerimiento |
|---|---|
| RF-001 | El sistema debe cargar o generar datos sintéticos de siniestros. |
| RF-002 | El sistema debe manejar datos de pólizas, asegurados, vehículos, proveedores y documentos. |
| RF-003 | El sistema debe calcular variables de riesgo. |
| RF-004 | El sistema debe aplicar reglas de negocio de posible fraude. |
| RF-005 | El sistema debe calcular un score de riesgo por siniestro. |
| RF-006 | El sistema debe clasificar los casos en verde, amarillo y rojo. |
| RF-007 | El sistema debe explicar las reglas o factores que generaron la alerta. |
| RF-008 | El sistema debe mostrar una bandeja de casos priorizados. |
| RF-009 | El sistema debe tener dashboard o interfaz funcional. |
| RF-010 | El sistema debe permitir consultas mediante agente o lenguaje natural controlado. |
| RF-011 | El sistema debe generar o exportar reportes de casos críticos. |
| RF-012 | El sistema debe analizar narrativas similares entre reclamos. |
| RF-013 | El sistema debe identificar proveedores recurrentes o concentradores de alertas. |
| RF-014 | El sistema debe mostrar documentos faltantes o inconsistentes. |
| RF-015 | El sistema debe recomendar casos que el analista debe revisar primero. |

## Requerimientos no funcionales

| Código | Requerimiento |
|---|---|
| RNF-001 | El código debe ser modular. |
| RNF-002 | El proyecto debe ser ejecutable y reproducible. |
| RNF-003 | Debe existir README con instrucciones. |
| RNF-004 | Debe existir requirements.txt. |
| RNF-005 | Debe existir .env.example sin credenciales reales. |
| RNF-006 | No se deben usar datos personales reales. |
| RNF-007 | El sistema debe aclarar que no acusa fraude. |
| RNF-008 | El score debe ser trazable. |
| RNF-009 | El modelo IA debe documentar variables, métricas y limitaciones. |
| RNF-010 | La solución debe tener arquitectura escalable futura. |

---

# Arquitectura recomendada para el hackathon

## Stack recomendado

```txt
Frontend / Dashboard:
- Streamlit
- Plotly
- CSS básico personalizado

Lenguaje principal:
- Python 3.11

Datos:
- CSV sintéticos
- SQLite para demo

Procesamiento:
- Pandas
- NumPy

IA / ML:
- Scikit-learn
- RandomForestClassifier
- IsolationForest

NLP:
- TF-IDF
- Cosine Similarity

Agente:
- Agent router local
- Tools controladas
- MCP opcional

Documentación:
- Markdown
- README
- Pitch PDF

Control de versiones:
- GitHub
```

## Diagrama lógico

```txt
┌─────────────────────────────────────────┐
│          Streamlit Dashboard             │
│  Dashboard | Bandeja | Detalle | Agente  │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│          Servicios de Aplicación         │
│ Claims | Scoring | Reports | Agent       │
└───────────────┬─────────────┬───────────┘
                │             │
                ▼             ▼
┌───────────────────────┐  ┌───────────────────────┐
│ Motor de reglas        │  │ Modelos IA/NLP         │
│ fraud_rules.py         │  │ ML + Anomalías + NLP   │
└───────────────┬───────┘  └───────────────┬───────┘
                │                          │
                └──────────────┬───────────┘
                               ▼
┌─────────────────────────────────────────┐
│              SQLite / CSV                │
│ claims, policies, insured, providers     │
└─────────────────────────────────────────┘
```

## Fórmula de score recomendada

```txt
score_final = 0.55 * score_reglas + 0.25 * score_ml + 0.10 * score_anomalia + 0.10 * score_nlp
```

## Clasificación

```txt
0 - 40    Verde
41 - 75   Amarillo
76 - 100  Rojo
```

---

# Plan de implementación

## Día 1 - Base de datos, reglas y dashboard inicial

Objetivo:

```txt
Que la app abra, tenga datos sintéticos y muestre score básico.
```

Tareas:

- Crear repo.
- Crear estructura de carpetas.
- Crear generador de datos sintéticos.
- Crear CSVs.
- Crear SQLite.
- Crear reglas base.
- Crear score inicial.
- Crear dashboard Streamlit.
- Mostrar tabla de siniestros.
- Mostrar semáforo.

## Día 2 - IA, NLP, explicabilidad y agente

Objetivo:

```txt
Que el sistema tenga enfoque híbrido y explicaciones claras.
```

Tareas:

- Implementar TF-IDF y similitud coseno.
- Implementar RandomForest.
- Implementar IsolationForest.
- Calcular score final.
- Generar explicaciones por caso.
- Crear pantalla detalle.
- Crear ranking de proveedores.
- Crear agente con preguntas del PDF.
- Crear exportación CSV.

## Día 3 - Documentación, pitch, pruebas y diferenciador

Objetivo:

```txt
Que el proyecto esté listo para entregar y defender.
```

Tareas:

- Crear README.
- Crear docs de arquitectura.
- Crear docs de modelo de datos.
- Crear docs de reglas.
- Crear docs de IA.
- Crear docs de ética y limitaciones.
- Crear presentación PDF.
- Ensayar demo.
- Grabar video backup.
- Opcional: MCP.
- Opcional: deploy en Streamlit Cloud.

---

# Checklist final para entrega

## Prototipo

- [ ] La app abre con `streamlit run src/app/main.py`.
- [ ] El dashboard muestra KPIs.
- [ ] La bandeja muestra siniestros ordenados por score.
- [ ] El detalle muestra explicación.
- [ ] El agente responde preguntas clave.
- [ ] Se pueden exportar casos críticos.

## Datos

- [ ] Existen CSVs sintéticos.
- [ ] No hay datos personales reales.
- [ ] Hay explicación del dataset.
- [ ] Hay tabla de siniestros, pólizas, asegurados, proveedores, vehículos y documentos.

## IA

- [ ] Hay score por reglas.
- [ ] Hay modelo ML.
- [ ] Hay NLP de narrativas similares.
- [ ] Hay métricas.
- [ ] Hay explicación de variables.

## Documentación

- [ ] README completo.
- [ ] requirements.txt.
- [ ] .env.example.
- [ ] docs/arquitectura.md.
- [ ] docs/modelo_datos.md.
- [ ] docs/reglas_negocio.md.
- [ ] docs/uso_ia.md.
- [ ] docs/etica_privacidad.md.
- [ ] docs/limitaciones.md.

## Pitch

- [ ] Presentación ejecutiva PDF.
- [ ] Demo ensayada.
- [ ] Respuestas preparadas para preguntas técnicas.
- [ ] Respuestas preparadas para preguntas de negocio.
- [ ] Respuestas preparadas para ética.
- [ ] Video de respaldo.

## Seguridad

- [ ] No hay `.env` real en GitHub.
- [ ] No hay API keys.
- [ ] No hay credenciales.
- [ ] La app aclara que no acusa fraude.
- [ ] Se documentan falsos positivos.

---

# Conclusión general

El PDF plantea un reto muy claro: construir un prototipo de IA para apoyar la revisión de siniestros sospechosos. La solución ganadora no debe ser únicamente un dashboard ni únicamente un modelo de ML. Debe combinar:

```txt
Reglas de negocio + ML + anomalías + NLP + agente + explicación + ética + demo clara
```

La idea central debe ser:

> FraudLens Claims AI prioriza siniestros con señales de posible fraude, explica los factores de riesgo y permite al analista consultar patrones mediante un agente, manteniendo siempre la revisión humana como paso obligatorio.

El proyecto debe evitar el error de sonar acusatorio. La palabra clave es **alerta**, no sentencia. La IA debe actuar como linterna, no como juez. 🔎

