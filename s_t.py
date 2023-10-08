import streamlit as st
import speech_recognition as sr

# Título de la aplicación
st.title("Conversión de Audio a Texto")

# Crear un botón para iniciar la grabación de audio
if st.button("Iniciar Grabación"):
    st.write("Habla ahora...")

    # Crear un objeto Recognizer
    recognizer = sr.Recognizer()

    # Abrir el micrófono
    with sr.Microphone() as source:
        try:
            # Escuchar el audio
            audio_data = recognizer.listen(source)
            st.write("Grabación completada. Procesando...")

            # Convertir el audio a texto utilizando el reconocimiento de Google
            text = recognizer.recognize_google(audio_data)

            # Mostrar el texto convertido
            st.subheader("Texto convertido del audio:")
            st.write(text)
        except sr.WaitTimeoutError:
            st.write("No se detectó ninguna entrada de audio.")
        except sr.RequestError as e:
            st.error(f"Error en la solicitud de reconocimiento de voz: {e}")




        
    


