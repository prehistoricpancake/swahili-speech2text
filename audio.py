import streamlit as st
from audiorecorder import audiorecorder
import requests
import os
import time


st.title("Kinasa Sauti (Speech To Text Recorder)")
st.write('I am a speech to text app well versed in English and Swahili. Try me and give me feedback. Shukran')
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    # To play audio in frontend:
    # st.audio(sample_rate=16000)
    st.audio(audio.export().read())  

    # To save audio to a file, use pydub export method:
    audio.export("audio.wav", format="wav")

    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")
    st.write('Storing audio file, fetching model in a bit')



if os.path.exists('audio.wav'):

    API_URL = "https://api-inference.huggingface.co/models/pplantinga/whisper-small-sw"

# do not do this, use dotenv, it's not loading well so I'll have to fix it.
    headers = {"Authorization": f"Bearer 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"}

    def query(filename):
        with open(filename, "rb") as f:
            data = f.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
    output = query("audio.wav")
    st.write('Model loading...')
    time.sleep(45)

    st.write(output)

    # clean up the file

    if os.path.isfile('audio.wav'):
        os.remove('audio.wav')
    







