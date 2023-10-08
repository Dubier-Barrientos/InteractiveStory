import streamlit as st
import speech_recognition as sr

# Título de la aplicación
st.title("Conversión de Audio a Texto")

# Subir archivo de audio
audio_file = st.file_uploader("Cargar archivo de audio (formato compatible: WAV, FLAC, etc.)", type=["wav", "flac"])

# Verificar si se ha cargado un archivo
if audio_file:
    st.write("Procesando archivo de audio...")

    # Crear un objeto Recognizer
    recognizer = sr.Recognizer()

    # Leer el archivo de audio
    audio_data = sr.AudioFile(audio_file)

    # Iniciar la conversión de audio a texto
    with audio_data as source:
        try:
            audio_text = recognizer.record(source)
            text = recognizer.recognize_google(audio_text)
            st.subheader("Texto convertido del audio:")
            st.write(text)
        except sr.UnknownValueError:
            st.warning("No se pudo reconocer el audio.")
        except sr.RequestError as e:
            st.error(f"Error en la solicitud de reconocimiento de voz: {e}")



        
    


