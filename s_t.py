import streamlit as st
from PIL import Image
import pytesseract
from gtts import gTTS
import os

# Título de la aplicación
st.title("Aplicación de Diagnóstico Médico")

# Subir la imagen del diagnóstico
image_file = st.file_uploader("Cargar imagen del diagnóstico (formato compatible: PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

# Definir una función para extraer texto de la imagen y guardar en caché
@st.cache
def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

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
    if st.button("Generar audio"):
        # Recuperar el texto de la caché
        text = extract_text(image)

        # Generar audio con el texto
        tts = gTTS(text, lang="es")  # Puedes especificar el idioma que desees
        audio_file = "diagnóstico_audio.mp3"
        tts.save(audio_file)

        # Mostrar el enlace para descargar el audio
        st.markdown(f"## Audio del diagnóstico:")
        st.audio(audio_file, format="audio/mp3", start_time=0)
            

           


        
    


