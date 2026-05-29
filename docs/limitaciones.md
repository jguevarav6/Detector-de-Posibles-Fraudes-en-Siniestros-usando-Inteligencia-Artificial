# Limitaciones

## Dataset sintetico

El dataset no representa una cartera real de una aseguradora. Fue creado para demostrar:

- Cruce de entidades.
- Reglas explicables.
- ML supervisado.
- Deteccion de anomalias.
- NLP de narrativas.
- Agente consultivo.

Las metricas del modelo no deben interpretarse como desempeno en produccion.

## Sesgos y falsos positivos

Como los patrones son sinteticos, el modelo puede aprender relaciones demasiado limpias. En produccion se requeriria:

- Validacion con datos historicos anonimizados.
- Revision de sesgos por ciudad, ramo, proveedor o segmento.
- Monitoreo de falsos positivos.
- Ajuste de umbrales con analistas.

## Alcance del MVP

Incluye:

- Generacion de datos sinteticos.
- Carga en MySQL.
- Score hibrido.
- Dashboard Streamlit.
- Agente local por tools controladas.
- Reportes CSV.

No incluye:

- Decision automatica de pago.
- Rechazo automatico.
- Login o roles.
- Integracion con sistemas reales.
- Oracle corporativo.
- API productiva.

## Riesgo tecnico

MySQL debe estar levantado para ejecutar la demo completa.

Defaults locales:

```txt
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=fraudlens_claims_ai
MYSQL_USER=<usuario_local>
MYSQL_PASSWORD=<password_local>
```

Si el entorno cambia, ajustar variables de entorno antes de ejecutar `setup_demo.py`.

## MCP

MCP esta documentado como diferenciador opcional. El MVP no depende de MCP porque el agente local ya responde las preguntas clave del reto.
