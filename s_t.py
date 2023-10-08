import streamlit as st
import subprocess

# Título de la aplicación
st.title("Conversión de Audio a Texto")

# Crear un botón para iniciar la grabación de audio
if st.button("Iniciar Grabación"):
    st.write("Habla ahora...")

    # Utilizar el comando "arecord" para grabar audio en un archivo WAV
    audio_file = "audio.wav"
    record_command = f"arecord -d 5 -f S16_LE -r 16000 {audio_file}"
    subprocess.run(record_command, shell=True)
    st.write("Grabación completada. Procesando...")

    # Utilizar el comando "pocketsphinx_continuous" para convertir audio a texto
    speech_to_text_command = f"pocketsphinx_continuous -infile {audio_file} -hmm /usr/local/share/pocketsphinx/model/en-us/en-us -lm /usr/local/share/pocketsphinx/model/en-us/en-us.lm.bin -dict /usr/local/share/pocketsphinx/model/en-us/cmudict-en-us.dict"
    result = subprocess.run(speech_to_text_command, shell=True, capture_output=True, text=True)
    
    # Mostrar el texto convertido
    text = result.stdout.strip()
    st.subheader("Texto convertido del audio:")
    st.write(text)
           


        
    


