import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie



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

hacker = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_zdtukd5q.json")
st_lottie(hacker, key=None)

st.write("# ANCAMAN CYBERCRIME")


st.markdown(
    """
### Menurut Kementerian Komunikasi dan Informatika, setidaknya terdapat lima modus kejahatan yang sering kali dilakukan oleh para penjahat siber, di antaranya:
- Phishing, yakni aktivitas yang ditujukan untuk mendapatkan informasi rahasia pengguna dengan cara memakai surel dan situs web palsu yang menyerupai tampilan asli dari web sebenarnya.
- Phraming, ialah tindakan berupa perintah yang mengarahkan korban ke situs web palsu. Umumnya, pelaku memasang malware pada situs palsu tersebut. Dengan demikian, mereka dapat mengakses perangkat korbannya secara ilegal.
- Sniffing, yaitu tindak penyadapan yang bertujuan untuk mengumpulkan informasi di perangkat korban sekaligus mengakses aplikasi yang memuat data penting.
- Money Mule, ialah tindakan pelaku yang meminta korbannya menerima sejumlah uang di rekeningnya. Kemudian uang tersebut dikirimkan ke orang lain.
- Social Engineering, merupakan modus kejahatan siber dengan memanipulasi psikologis korban untuk mendapatkan informasi penting, seperti OTP atau One-Time Password.

"""
)


st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

komentar2 = st.text_input("Barikan komentar anda:", "")

st.markdown(f"Komentar : {komentar2}")


