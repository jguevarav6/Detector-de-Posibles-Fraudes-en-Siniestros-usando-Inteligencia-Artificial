# Reglas de Negocio

Las reglas generan alertas explicables para revision humana. No confirman fraude ni recomiendan rechazo automatico.

## Reglas implementadas

| Codigo | Regla | Senal | Severidad base |
|---|---|---|---|
| R001_BORDE_VIGENCIA | Evento cerca de vigencia | Ocurrencia cerca del inicio o fin de poliza | Alta |
| R002_REPORTE_TARDIO | Reporte tardio | Demora relevante entre ocurrencia y reporte | Media |
| R003_DEMORA_ROBO | Demora en robo | Cobertura de robo reportada con demora | Alta |
| R004_FRECUENCIA_ASEGURADO | Frecuencia del asegurado | Varios reclamos recientes del mismo asegurado | Media |
| R005_FRECUENCIA_VEHICULO | Frecuencia del vehiculo | Vehiculo asociado a multiples reclamos | Media |
| R006_PROVEEDOR_RECURRENTE | Proveedor recurrente | Proveedor con reclamos o casos observados altos | Media |
| R007_DOCUMENTOS_INCOMPLETOS | Documentos incompletos | Faltan respaldos para validar el caso | Media |
| R008_DOCUMENTOS_INCONSISTENTES | Documentos inconsistentes | Documentos ilegibles o inconsistentes | Alta |
| R009_DINAMICA_SOSPECHOSA | Dinamica a validar | Evento nocturno sin tercero identificado | Media |
| R010_TERCERO_NO_IDENTIFICADO | Tercero no identificado | Caso vehicular sin tercero identificado | Baja |
| R011_NARRATIVA_SIMILAR | Narrativa similar | Texto parecido a otro reclamo | Alta |
| R012_MONTO_ATIPICO | Monto atipico | Monto alto frente a suma asegurada | Alta |
| R013_PROVEEDOR_OBSERVADO | Proveedor en lista simulada | Proveedor marcado en lista restrictiva sintetica | Alta |

## Salida de cada regla

Cada regla entrega:

- `code`.
- `name`.
- `points`.
- `severity`.
- `explanation`.
- `evidence`.

## Score de reglas

El `score_reglas` suma puntos de reglas activadas y se limita a 100.

Este score es el componente principal del score final porque es trazable y defendible ante analistas y jurado.

## Mensaje operativo

Una regla activada significa:

```txt
Este siniestro contiene una senal que requiere validacion humana.
```

No significa:

```txt
Fraude confirmado.
```
