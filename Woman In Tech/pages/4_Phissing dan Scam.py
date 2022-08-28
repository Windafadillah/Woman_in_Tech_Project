import streamlit as st
from PIL import Image


st.write("""# MENGHINDARI PHISSING AND SCAM""")
video1 = open("Menghindariphisingdanscam.mp4", "rb")
st.video(video1)

st.write("")
st.write("")
st.write("")

st.write("""# KEJAHATAN MENGENAI PHARMING""")
video2 = open("Kejahatanmengenaipharming.mp4", "rb")
st.video(video2)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

komentar4 = st.text_input("Barikan komentar anda:", "")

st.markdown(f"Komentar : {komentar4}")