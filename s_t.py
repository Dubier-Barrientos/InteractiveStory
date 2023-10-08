import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageDraw
import numpy as np

# Lista para almacenar las imágenes guardadas
historieta = []

# Configuración del área de dibujo
drawing_mode = st.checkbox("Modo de Dibujo", False)
if drawing_mode:
    st.write("Dibuja algo en el lienzo a continuación:")
    canvas = st.image(None, caption="Lienzo", use_column_width=True, channels="RGB")
    draw = ImageDraw.Draw(canvas.image)

# Botón para guardar el dibujo actual
if st.button("Guardar Dibujo"):
    if drawing_mode:
        # Crea una copia de la imagen actual y la agrega a la lista de historietas
        historieta.append(canvas.image.copy())

        # Borra el dibujo en el lienzo
        draw.rectangle(((0, 0), (canvas.image.width, canvas.image.height)), fill="white", outline="white")

# Botón para borrar el lienzo y las imágenes guardadas
if st.button("Borrar Historieta"):
    historieta.clear()

# Mostrar las imágenes guardadas como una historieta
if historieta:
    st.write("Historieta:")
    for i, imagen in enumerate(historieta, start=1):
        st.image(imagen, caption=f"Imagen {i}", use_column_width=True)





            

           


        
    


