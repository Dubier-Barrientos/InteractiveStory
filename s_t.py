import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageDraw
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="Creación de Historieta",
    page_icon="✏️",
    layout="wide"
)

# Título de la aplicación
st.title("Historieta Interactiva")

# Crear un lienzo de dibujo
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

# Botón para guardar el dibujo
if st.button("Guardar Dibujo"):
    # Obtener el contenido del lienzo como una imagen
    image_data = canvas_result.image_data
    if image_data is not None:
        # Crear una imagen PIL a partir de los datos
        image = Image.fromarray(np.uint8(image_data))
        
        # Guardar la imagen
        image.save("dibujo.png")
        st.success("Dibujo guardado como 'dibujo.png'")

        # Mostrar la imagen guardada
        st.image(image, use_column_width=True)
    else:
        st.warning("No hay dibujo para guardar.")





            

           


        
    


