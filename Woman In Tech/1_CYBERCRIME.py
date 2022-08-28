import json
from sre_constants import CATEGORY_LINEBREAK
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from xml.etree.ElementTree import Comment
from streamlit_option_menu import option_menu

st.set_page_config(page_title="WOMAN IN TECH")
icon=("shield-check")

def load_lottofile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

cyber = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_nviqbm9p.json")
st_lottie(
    cyber, 
    height= 500,
    width= 500,
    key=None
)

st.write("# CYBER CRIME")


st.markdown(
    """
    Secara umum, arti dari cybercrime adalah suatu bentuk kejahatan virtual dengan memanfaatkan perangkat komputer yang terhubung dengan jaringan Internet.
    Tindakan tersebut tentunya melanggar hukum, sebab dapat menimbulkan kerugian bagi orang lain. Atau dalam pengertian lain Cyber crime adalah tindakan ilegal
    yang dilakukan pelaku kejahatan dengan menggunakan teknologi komputer dan jaringan internet untuk menyerang sistem informasi korban.
"""
)
st.write("")
st.write("")
st.write("")
komentar = st.text_input("Barikan komentar anda:", "")

st.markdown(f"Komentar : {komentar}")