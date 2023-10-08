import streamlit as st
from PIL import Image
import pytesseract
from gtts import gTTS
import os
import glob
import time
import wikipediaapi

# Función para extraer texto de una imagen
@st.cache
def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Función para generar audio a partir de texto
def text_to_speech(text, tld):
    tts = gTTS(text, lang="es", tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name

# Función para eliminar archivos antiguos
def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted", f)

# Configuración de la página
st.set_page_config(
    page_title="Aplicación de Diagnóstico Médico",
    page_icon="✅",
    layout="wide"
)

# Crear una barra de navegación para cambiar entre las secciones
selected_page = st.sidebar.radio("Selecciona una opción:", ["Transcripción y Audio", "Reconocimiento de Paciente"])

# Contenido de la página principal
if selected_page == "Transcripción y Audio":
    # Título de la aplicación
    st.title("Transcripción y Generación de Audio")

    # Subir la imagen del diagnóstico
    image_file = st.file_uploader("Cargar imagen del diagnóstico (formato compatible: PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

    # Variable para almacenar el texto extraído
    text = ""

    if image_file is not None:
        # Mostrar la imagen cargada
        st.image(image_file, caption="Imagen del diagnóstico", use_column_width=True)

        # Botón para extraer el texto de la imagen
        if st.button("Extraer texto de la imagen"):
            # Leer la imagen
            image = Image.open(image_file)

            # Extraer el texto utilizando la función y guardar en caché
            text = extract_text(image)

            # Mostrar el texto extraído
            st.subheader("Texto extraído de la imagen:")
            st.write(text)

    # Botón para generar un audio con el texto
    if text:
        if st.button("Generar audio"):
            result = text_to_speech(text, "com")  # Cambia esto al dominio TLD deseado
            audio_file = open(f"temp/{result}.mp3", "rb")
            audio_bytes = audio_file.read()
            st.markdown(f"## Audio del diagnóstico:")
            st.audio(audio_bytes, format="audio/mp3", start_time=0)

            # Botón para eliminar el audio generado
            if st.button("Eliminar audio generado"):
                os.remove(f"temp/{result}.mp3")
                st.success("Audio eliminado correctamente.")

# Reconocimiento de Paciente
elif selected_page == "Reconocimiento de Paciente":
     # Título de la sección
    st.title("Reconocimiento de Paciente")

    # Formulario para ingresar el nombre del paciente
    patient_name = st.text_input("Nombre del Paciente:")
    
    # Botón para buscar información médica en Wikipedia
    if st.button("Buscar Información Médica"):
        if patient_name:
            # Conexión a la API de Wikipedia
            wiki_wiki = wikipediaapi.Wikipedia("es")
            
            # Realizar la búsqueda en Wikipedia
            page = wiki_wiki.page(patient_name)
            
            # Mostrar el resumen de la página de Wikipedia (si existe)
            if page.exists():
                st.subheader(f"Información médica sobre {patient_name}:")
                st.write(page.summary)
            else:
                st.warning(f"No se encontró información médica sobre {patient_name}.")
        else:
            st.warning("Por favor, ingresa el nombre del paciente.")

# Limpiar archivos antiguos
remove_files(7)



            

           


        
    


