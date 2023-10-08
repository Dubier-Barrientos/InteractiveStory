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

def text_to_speech(text, tld):
    #translation = translator.translate(text, src=input_language, dest=output_language)
    
    tts = gTTS(text, "es", tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text


display_output_text = st.checkbox("Muestra el  texto ")

if st.button("convert"):
    result, output_text = text_to_speech("es", "es", text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Your audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    if display_output_text:
        st.markdown(f"## Output text:")
        st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
            

           


        
    


