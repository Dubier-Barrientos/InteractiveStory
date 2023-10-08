import streamlit as st
from PIL import Image
import pytesseract
from gtts import gTTS
import os
import face_recognition
import os

# Definir función para extraer texto de la imagen y guardar en caché
@st.cache
def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

# Definir función para reconocimiento facial
def facial_recognition(image_file):
    known_faces = []
    known_names = []
    known_faces_folder = "known_faces"

    for filename in os.listdir(known_faces_folder):
        if filename.endswith(".jpg"):
            image = face_recognition.load_image_file(os.path.join(known_faces_folder, filename))
            face_encoding = face_recognition.face_encodings(image)[0]
            known_faces.append(face_encoding)
            known_names.append(os.path.splitext(filename)[0])

    input_image = face_recognition.load_image_file(image_file)
    face_locations = face_recognition.face_locations(input_image)
    face_encodings = face_recognition.face_encodings(input_image, face_locations)

    recognized_person = None

    if len(face_encodings) > 0:
        for i, face_encoding in enumerate(face_encodings):
            results = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.5)
            if True in results:
                index = results.index(True)
                recognized_person = known_names[index]
                break

    return recognized_person

# Menú lateral
menu_option = st.sidebar.selectbox("Menú", ["Inicio", "Reconocimiento de Pacientes"])

# Cargar imagen del diagnóstico
if menu_option == "Inicio":
    st.title("Aplicación de Diagnóstico Médico")

    image_file = st.file_uploader("Cargar imagen del diagnóstico (formato compatible: PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

    if image_file is not None:
        # Mostrar la imagen cargada
        st.image(image_file, caption="Imagen del diagnóstico", use_column_width=True)

        # Botón para extraer el texto de la imagen
        if st.button("Extraer texto de la imagen"):
            # Leer la imagen y extraer el texto
            image = Image.open(image_file)
            text = extract_text(image)

            # Mostrar el texto extraído
            st.subheader("Texto extraído de la imagen:")
            st.write(text)

        # Botón para generar un audio con el texto
        if st.button("Generar audio"):
            # Generar audio con el texto
            tts = gTTS(text, lang="es")  # Puedes especificar el idioma que desees
            audio_file = "diagnostico_audio.mp3"
            tts.save(audio_file)

            # Mostrar el enlace para descargar el audio
            st.markdown(f"## Audio del diagnóstico:")
            st.audio(audio_file, format="audio/mp3", start_time=0)

# Reconocimiento de Pacientes
elif menu_option == "Reconocimiento de Pacientes":
    st.title("Reconocimiento de Pacientes")

    image_file_patient = st.file_uploader("Cargar imagen del paciente para reconocimiento", type=["png", "jpg", "jpeg"])

    if image_file_patient is not None:
        # Mostrar la imagen cargada
        st.image(image_file_patient, caption="Imagen del paciente", use_column_width=True)

        # Realizar el reconocimiento facial
        recognized_person = facial_recognition(image_file_patient)

        if recognized_person is not None:
            st.subheader("Paciente Reconocido:")
            st.write(recognized_person)
        else:
            st.warning("Paciente no reconocido.")


            

           


        
    


