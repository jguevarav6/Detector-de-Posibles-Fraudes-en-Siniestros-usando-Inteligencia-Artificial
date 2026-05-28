# Modelo de Datos

El MVP usa datos 100% sintéticos. No se incluyen nombres, documentos, teléfonos, correos, placas reales ni información confidencial.

## Archivos generados

Los CSV se generan con:

```bash
python setup_demo.py
```

Salida prevista:

- `data/synthetic/claims.csv`
- `data/synthetic/policies.csv`
- `data/synthetic/insured.csv`
- `data/synthetic/vehicles.csv`
- `data/synthetic/providers.csv`
- `data/synthetic/documents.csv`
- `data/synthetic/watchlist.csv`
- `data/processed/fraudlens_demo.sqlite`

Los CSV y SQLite generados son artefactos locales y no se versionan.

## Entidades

### claims

Tabla principal de siniestros. Incluye identificadores anónimos, fechas, montos, descripción, cobertura, proveedor, indicadores de documentos y etiqueta simulada.

Campos clave: `id_siniestro`, `id_poliza`, `id_asegurado`, `id_vehiculo`, `id_proveedor`, `ramo`, `cobertura`, `fecha_ocurrencia`, `fecha_reporte`, `monto_reclamado`, `monto_estimado`, `monto_pagado`, `ciudad`, `descripcion`, `documentos_completos`, `dias_desde_inicio_poliza`, `dias_desde_fin_poliza`, `dias_entre_ocurrencia_reporte`, `historial_siniestros_asegurado`, `etiqueta_fraude_simulada`.

### policies

Pólizas sintéticas asociadas a asegurados.

Campos clave: `id_poliza`, `id_asegurado`, `ramo`, `fecha_inicio`, `fecha_fin`, `prima`, `suma_asegurada`, `deducible`, `canal_venta`, `ciudad`, `estado_poliza`.

### insured

Asegurados sintéticos anonimizados.

Campos clave: `id_asegurado`, `segmento`, `antiguedad_meses`, `ciudad`, `numero_polizas`, `reclamos_ultimos_12_meses`, `mora_actual`, `score_cliente_simulado`.

### vehicles

Vehículos sintéticos con hashes ficticios.

Campos clave: `id_vehiculo`, `id_asegurado`, `marca`, `modelo`, `anio`, `placa_hash`, `chasis_hash`, `motor_hash`, `valor_asegurado`.

### providers

Proveedores sintéticos como talleres, clínicas, peritos y asistencias.

Campos clave: `id_proveedor`, `tipo`, `ciudad`, `reclamos_asociados`, `monto_promedio_reclamado`, `porcentaje_casos_observados`, `antiguedad_meses`, `lista_restrictiva_simulada`.

### documents

Documentos sintéticos por siniestro.

Campos clave: `id_documento`, `id_siniestro`, `tipo_documento`, `entregado`, `legible`, `fecha_emision`, `inconsistencia_detectada`, `observacion`.

### risk_scores

Tabla preparada en SQLite para resultados de scoring. Se crea vacía en esta fase.

Campos clave: `id_siniestro`, `score_reglas`, `score_ml`, `score_anomalia`, `score_nlp`, `score_final`, `nivel_riesgo`, `reglas_activadas`, `explicacion`, `accion_sugerida`.

## Patrones sintéticos inyectados

- Reclamos al borde de vigencia.
- Reportes tardíos.
- Montos elevados respecto a suma asegurada.
- Proveedores con mayor porcentaje de casos observados.
- Documentos incompletos, ilegibles o inconsistentes.
- Narrativas similares.
- Tercero no identificado.
- Coberturas de robo con denuncia tardía.
