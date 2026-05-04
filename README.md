# StudyPlanner AI - Planificador de estudio con IA

### Alumno: Francisco Luis Campo

### Comisión: 86240

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://study-planner-ai.streamlit.app/)

## Problemática

Muchos estudiantes tienen dificultades para organizar su tiempo de estudio de manera eficiente. Esto genera mala distribución del tiempo, acumulación de contenido y estrés antes de exámenes. Además, no todos saben cómo armar un cronograma equilibrado según su disponibilidad.

## Solución propuesta

Se propone desarrollar una aplicación web que permite generar automáticamente un plan de estudio personalizado. El usuario ingresará:

- materias
- cantidad de días disponibles
- horas por día

A partir de estos datos, la aplicación utilizará IA para:

- distribuir el tiempo de estudio
- organizar las materias
- generar un cronograma semanal claro

Esto permite optimizar el estudio sin que el usuario tenga que planificar manualmente.

## Propuesta de Aplicación Web con IA

Para llevar a cabo esta solución, se desarrollará una aplicación web que se llamará StudyPlanner AI. La función principal de esta aplicación será generar planes de estudio personalizados en base a las necesidades del usuario. Además, esta aplicación ofrece ventajas significativas, como ahorrar tiempo en la organización del estudio, reducir el estrés previo a exámenes y mejorar la distribución de las materias.

El asistente utilizará inteligencia artificial para analizar la carga de materias, la disponibilidad de días y las horas de estudio, generando automáticamente un cronograma equilibrado y fácil de seguir. Asimismo, la aplicación permitirá visualizar el plan de estudio de forma clara, facilitando su comprensión y adaptación según las preferencias del usuario.

## Prompt Inicial

El prompt inicial será el siguiente:

“Actúa como un asistente académico.

Necesito que generes un plan de estudio semanal en formato claro y ordenado.

Datos:

- Materias: {materias}
- Días disponibles: {dias}
- Horas por día: {horas}

Requisitos:

- Distribuir las materias de forma equilibrada
- No repetir demasiadas veces la misma materia en un día
- Incluir descansos
- Mostrar el resultado en formato de tabla o lista por día
- Agregar sugerencia de recompensas luego de cada bloque de estudio

El resultado debe ser claro y fácil de seguir.”

Este prompt define un rol claro (asistente académico), da contexto, impone reglas (equilibrio, descansos) y específica formato de salida.

## Factibilidad económica

El proyecto es económicamente viable porque utilizará APIs de Google AI Studio con costo bajo por consulta, cada usuario genera pocos requests, puede implementarse en versión gratuita (limitada)

### Como ejecutarlo en tu propia maquina

1. Instalar dependencias

    ```
    $ pip install -r requirements.txt
    ```

2. Ejecutar la aplicación

    ```
    $ streamlit run streamlit_app.py
    ```
