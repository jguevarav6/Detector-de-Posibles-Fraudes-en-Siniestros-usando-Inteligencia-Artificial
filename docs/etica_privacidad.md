# Etica y Privacidad

FraudLens Claims AI es una herramienta de apoyo para analistas de siniestros. Su salida es una prioridad de revision, no una decision legal, contractual ni automatica.

## Principios

- No usar datos reales.
- No incluir informacion personal identificable.
- No guardar credenciales en el repositorio.
- No confirmar fraude.
- No rechazar siniestros automaticamente.
- No reemplazar el criterio del analista.
- Explicar las senales que influyen en el score.

## Datos sinteticos

Los datos se generan con `src/data_generation/generate_synthetic_data.py`.

Se usan identificadores anonimos:

- `SIN-xxxxx`.
- `POL-xxxx`.
- `ASE-xxxx`.
- `VEH-xxxx`.
- `PRO-xxxx`.

No se generan nombres, correos, telefonos, documentos reales ni placas reales.

## Etiqueta simulada

`etiqueta_fraude_simulada` es una etiqueta sintetica para entrenar modelos. No representa una verdad legal.

Debe explicarse como:

```txt
Etiqueta artificial usada para validar el funcionamiento del prototipo.
```

## Lenguaje permitido

Usar:

- Posible riesgo.
- Alerta.
- Prioridad de revision.
- Revision humana.
- Senales anomalas.

Evitar:

- Fraude confirmado.
- Cliente fraudulento.
- Rechazar automaticamente.
- Culpable.

## Manejo de falsos positivos

Un caso rojo puede ser legitimo. El sistema solo indica que contiene varias senales para revisar antes.

Mitigaciones:

- Mostrar reglas activadas.
- Mostrar componentes del score.
- Mantener explicacion humana.
- Descargar evidencia para revision.
- Conservar decision final en un analista.

## Credenciales

`.env.example` contiene valores de ejemplo. Las credenciales reales deben estar fuera de Git.

Para demo local se usan defaults de MySQL, pero no se debe publicar una `.env` real.
