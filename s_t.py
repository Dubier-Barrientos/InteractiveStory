import os
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import speech_recognition as sr

st.title("Conversión de Audio a Texto")

# Variable para almacenar la transcripción
transcripcion = ""

st.write("Habla y convierte tu discurso en texto:")

stt_button = Button(label=" Iniciar ", width=200)

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
        if (value !== "") {
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
        transcripcion = result.get("GET_TEXT")
        st.write(transcripcion)

# Botón para borrar la transcripción y grabar otro audio
if st.button("Borrar"):
    transcripcion = ""
    st.write("Transcripción borrada.")

# Mostrar la transcripción actual
if transcripcion:
    st.subheader("Texto convertido del audio:")
    st.write(transcripcion)





        
    


