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
    
    # Subir la imagen para el reconocimiento
    image_file_patient = st.file_uploader("Cargar imagen para el reconocimiento (formato compatible: PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])
    
    # Variable para almacenar el diagnóstico
    diagnosis_text = ""

    if image_file_patient is not None:
        # Mostrar la imagen cargada
        st.image(image_file_patient, caption="Imagen para el reconocimiento", use_column_width=True)

        # Botón para realizar el reconocimiento
        if st.button("Realizar reconocimiento"):
            # Leer la imagen
            image_patient = Image.open(image_file_patient)
            
            # Convertir la imagen a un formato que OpenCV pueda procesar (numpy array)
            img_cv = np.array(image_patient)
            
            # Cargar el modelo Haar Cascade para detección de rostros
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            
            # Convertir la imagen a escala de grises para la detección
            gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
            
            # Realizar la detección de rostros
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
            if len(faces) > 0:
                # Si se detecta al menos un rostro, mostrar el diagnóstico
                diagnosis_text = "Se ha detectado un rostro. Aquí está su diagnóstico: [Insertar texto del diagnóstico aquí]"
            else:
                diagnosis_text = "No se ha detectado ningún rostro en la imagen."   

# Limpiar archivos antiguos
remove_files(7)



            

           


        
    


