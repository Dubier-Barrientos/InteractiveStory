import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

# Lista para almacenar las imágenes guardadas
historieta = []

# Configuración del área de dibujo
drawing_mode = st.checkbox("Modo de Dibujo", False)
if drawing_mode:
    st.write("Dibuja algo en el lienzo a continuación:")
    fig, ax = plt.subplots()
    canvas = fig.canvas
    draw = False

    def toggle_draw(event):
        nonlocal draw
        if event.key == "d":
            draw = not draw

    canvas.mpl_connect("key_press_event", toggle_draw)

    x, y = [], []

    def on_mouse_move(event):
        if draw:
            x.append(event.xdata)
            y.append(event.ydata)
            ax.plot(x, y, color="black")
            canvas.draw()

    canvas.mpl_connect("motion_notify_event", on_mouse_move)

# Botón para guardar el dibujo actual
if st.button("Guardar Dibujo"):
    if drawing_mode:
        # Guarda la imagen actual en la lista de historietas
        buf = canvas.buffer_rgba()
        historieta.append(np.array(buf))

        # Borra el lienzo
        ax.clear()
        canvas.draw()

# Botón para borrar el lienzo y las imágenes guardadas
if st.button("Borrar Historieta"):
    historieta.clear()
    ax.clear()
    canvas.draw()

# Mostrar las imágenes guardadas como una historieta
if historieta:
    st.write("Historieta:")
    for i, imagen in enumerate(historieta, start=1):
        st.image(imagen, caption=f"Imagen {i}", use_column_width=True)






            

           


        
    


