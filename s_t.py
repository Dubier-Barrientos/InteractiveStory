import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageDraw
import numpy as np

try:
    os.mkdir("temp")
except:
    pass

historieta = []

st.set_page_config(
    page_title="Creación de Historieta",
    page_icon="✏️",
    layout="wide"
)

selected_page = st.sidebar.radio("Selecciona una opción:", ["Historia a audio", "Dibujemos una historia"])

if selected_page == "Historia a audio":
    
    # Título de la aplicación
    st.title("Transcripción y Generación de Audio")

elif selected_page == "Dibujemos una historia":

    #Título de la sección
    st.title("Historieta Interactiva")
    
    
    st.subheader("Lienzo de Dibujo")
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 0)",  # Color de fondo transparente
        stroke_width=5,  # Grosor de la línea
        stroke_color="#000",  # Color de línea (negro)
        background_color="#FFF",  # Color de fondo blanco
        drawing_mode="freedraw",  # Modo de dibujo libre
        key="canvas",
        height=300  # Altura del lienzo de dibujo
    )
    
    
    if st.button("Guardar Dibujo"):
        image_data = canvas_result.image_data
        if image_data is not None:
            image = Image.fromarray(np.uint8(image_data))
    
            new_size = (300, 300)
            image = image.resize(new_size)
            
            historieta.append(image)
    
            st.image(image, use_column_width=True, caption=f"Imagen {len(historieta)}")
    
            if st.button(f"Borrar Imagen {len(historieta)}"):
                del historieta[-1]
                st.success(f"Imagen {len(historieta) + 1} borrada.")
        else:
            st.warning("No hay dibujo para guardar.")
    
    if st.button("Borrar Todas las Imágenes"):
        historieta.clear()
        st.success("Todas las imágenes borradas.")








            

           


        
    


