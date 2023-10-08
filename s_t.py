import streamlit as st
import speech_recognition as sr
import tempfile
import os

# Título de la aplicación
st.title("Conversión de Audio MP3 a Texto")

# Subir archivo de audio en formato MP3
audio_file = st.file_uploader("Cargar archivo de audio (formato MP3)", type=["mp3"])

# Verificar si se ha cargado un archivo
if audio_file:
    st.write("Procesando archivo de audio...")

    # Crear un objeto Recognizer
    recognizer = sr.Recognizer()

    # Crear un archivo temporal para convertir el audio MP3 a WAV
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
        temp_wav_file.write(audio_file.read())

    # Iniciar la conversión de audio a texto
    with sr.AudioFile(temp_wav_file.name) as source:
        try:
            audio_text = recognizer.record(source)
            text = recognizer.recognize_google(audio_text)
            st.subheader("Texto convertido del audio:")
            st.write(text)
        except sr.UnknownValueError:
            st.warning("No se pudo reconocer el audio.")
        except sr.RequestError as e:
            st.error(f"Error en la solicitud de reconocimiento de voz: {e}")

    # Eliminar el archivo temporal
    os.remove(temp_wav_file.name)





        
    


