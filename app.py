import streamlit as st
from PIL import Image

st.set_page_config(page_title="Birthday Wishes 🎉", layout="centered")

st.header("🎉 Happy Birthday To You 🎉")

st.text("✨ play the audio and video to celebrate your special day")

name=st.text_input("🎂 What's your name, Birthday Star?")
if name:
    st.markdown(f"Sending smiles, hugs, and sparkles your way 🎁. 🎂 Happy Birthday {name} !")

vid_file=open("bday_video.mp4","rb")
vid_bytes=vid_file.read()
st.video(vid_bytes,width=700,start_time=0,format="video/mp4")

audio_file=open("happy-birthday-155461.mp3","rb").read()
st.audio(audio_file,start_time=0)

st.balloons()
