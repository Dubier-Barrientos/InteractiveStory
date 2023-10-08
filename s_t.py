import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageDraw

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
    image = Image.new("RGB", (canvas_result.shape[1], canvas_result.shape[0]), "#FFF")
    draw = ImageDraw.Draw(image)
    draw.bitmap((0, 0), canvas_result, fill="#000")  # Copiar el dibujo en la imagen
    st.image(image, use_column_width=True, caption="Dibujo Guardado")




            

           


        
    


