import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="StudyPlanner AI", page_icon="📚")

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL (Configuración) ---
with st.sidebar:
    st.title("Configuración")
    api_key = st.text_input("Ingresa tu Google API Key:", type="password")
    st.info("Obtén tu llave en [Google AI Studio](https://aistudio.google.com/)")
    
    st.divider()
    st.markdown(f"**Alumno:** Francisco Luis Campo")
    st.markdown(f"**Comisión:** 86240")

# --- CUERPO PRINCIPAL ---
st.title("📚 StudyPlanner AI")
st.subheader("Tu planificador de estudio inteligente")

st.markdown("""
Esta herramienta utiliza Inteligencia Artificial para organizar tus materias de forma 
equilibrada según tu disponibilidad real.
""")

# Formulario de entrada
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        materias = st.text_area("Materias (separadas por coma):", 
                                placeholder="Ej: Matemática, Historia, Programación Python")
        dias = st.slider("Días disponibles a la semana:", 1, 7, 5)
    
    with col2:
        horas = st.number_input("Horas de estudio por día:", min_value=1, max_value=12, value=4)
        enfoque = st.selectbox("Enfoque del plan:", ["Equilibrado", "Intensivo (Examen pronto)", "Relajado"])

# Botón de generación
if st.button("Generar mi Plan de Estudio"):
    if not api_key:
        st.error("Por favor, ingresa tu API Key en la barra lateral.")
    elif not materias:
        st.warning("Debes ingresar al menos una materia.")
    else:
        try:
            # Configurar la IA
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-3-flash-preview')
            
            with st.spinner("La IA está organizando tu cronograma..."):
                # Definición del Prompt
                prompt = f"""
                Actúa como un asistente académico experto en técnicas de estudio (Pomodoro, Active Recall).

                Necesito que generes un plan de estudio semanal en formato claro y ordenado.

                Datos del usuario:
                - Materias: {materias}
                - Días disponibles: {dias} días a la semana
                - Horas por día: {horas} horas
                - Enfoque: {enfoque}

                Requisitos estrictos:
                1. Distribuir las materias de forma equilibrada.
                2. No repetir la misma materia más de 2 horas seguidas.
                3. Incluir bloques de descanso (ej: 10 min por cada 50 min de estudio).
                4. Mostrar el resultado en formato de TABLA Markdown para el cronograma.
                5. Agregar una sección de "Sugerencias de Recompensas" después de los bloques.
                6. Incluir un consejo breve de técnica de estudio según las materias mencionadas.

                El resultado debe ser profesional, motivador y fácil de leer.
                """
                
                response = model.generate_content(prompt)
                
                st.success("¡Plan generado con éxito!")
                st.markdown("---")
                st.markdown(response.text)
                
                # Opción para descargar (Simulada con el texto)
                st.download_button(
                    label="Descargar Plan como Texto",
                    data=response.text,
                    file_name="mi_plan_de_estudio.txt",
                    mime="text/plain"
                )
                
        except Exception as e:
            st.error(f"Ocurrió un error: {e}")

# Pie de página
st.markdown("---")
st.caption("StudyPlanner AI - Proyecto Final Comisión 86240")