import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from PIL import Image
import time
import glob

from gtts import gTTS
from googletrans import Translator

st.title("Interfaces Multimodales")
st.subheader("TRADUCTOR")

image = Image.open('traductor.jpg')
st.image(image)

st.write("Toca el Botón y habla lo que quieres traducir")

# Variable para realizar el seguimiento de si se ha realizado una transcripción previa
transcription_completed = False

if not transcription_completed:
    stt_button = Button(label=" Inicio ", width=200)
else:
    stt_button = Button(label="Grabar otro audio", width=200)

stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if ( value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
    """))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    if "GET_TEXT" in result:
        transcription_completed = True
        st.write(result.get("GET_TEXT"))
    try:
        os.mkdir("temp")
    except:
        pass

if transcription_completed:
    # Agrega un botón para eliminar la transcripción anterior y reiniciar el proceso de grabación
    if st.button("Eliminar transcripción"):
        transcription_completed = False

st.title("Texto a Audio")
translator = Translator()

text = st.text_area("Texto a traducir", ""


        
    


