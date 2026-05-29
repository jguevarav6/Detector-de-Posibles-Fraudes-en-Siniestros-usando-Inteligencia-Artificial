# Script de Demo

Duracion sugerida: 4 minutos dentro del pitch.

## 1. Preparar demo

```bash
python setup_demo.py
streamlit run src/app/main.py
```

Validar:

- MySQL contiene `claims` y `risk_scores`.
- Streamlit abre en `http://localhost:8501`.
- La bandeja muestra 1000 siniestros procesados.

## 2. Dashboard ejecutivo

Mostrar:

- Total de siniestros.
- Cantidad de rojos, amarillos y verdes.
- Tasa revisable.
- Exposicion por prioridad.
- Top proveedores con alertas rojas.

Mensaje:

```txt
FraudLens no acusa fraude. Prioriza casos con senales explicables para que un analista revise primero.
```

## 3. Bandeja de siniestros

Filtrar:

- Nivel: Rojo.
- Ramo: Vehiculos.
- Monto alto.

Mostrar que la tabla ordena por prioridad y score.

## 4. Detalle de caso

Abrir un caso rojo.

Mostrar tabs:

- Resumen.
- Score.
- Evidencia.

Explicar:

- Reglas activadas.
- Score de reglas, ML, anomalia y NLP.
- Documentos.
- Narrativa similar si existe.

## 5. Agente

Preguntar:

```txt
Proveedores con mas alertas
```

Luego:

```txt
Generar resumen ejecutivo
```

Explicar que el agente usa tools controladas y datos procesados, no un LLM tomando decisiones.

## 6. Reportes

Mostrar descargas:

- Casos rojos.
- Bandeja revisable.
- Todos los scores.

Cerrar con:

```txt
El analista recibe una cola priorizada, explicaciones y evidencia exportable. La decision final sigue siendo humana.
```
