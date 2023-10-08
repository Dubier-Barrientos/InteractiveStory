import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image

st.title("Drawable Canvas")
st.markdown("""
Draw on the canvas, get the image data back into Python!
* Doubleclick to remove the selected object when not in drawing mode
""")
st.sidebar.header("Configuration")

# Specify brush parameters and drawing mode
b_width = st.sidebar.slider("Brush width: ", 1, 100, 10)
b_color = st.sidebar.color_picker("Enter brush color hex: ")
bg_color = st.sidebar.color_picker("Enter background color hex: ", "#eee")
drawing_mode = st.sidebar.checkbox("Drawing mode ?", True)

# Create a canvas component
image_data = st_canvas(
    b_width, b_color, bg_color, height=150, drawing_mode=drawing_mode, key="canvas"
)

# Do something interesting with the image data
if image_data is not None:
    # Convert the numpy array to a PIL image
    pil_image = Image.fromarray(image_data)

    # Display the PIL image
    st.image(pil_image)








            

           


        
    


