from email.mime import image
from os import write
import json
from turtle import update
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

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

penetration = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_pjagkisd.json")
perbarui = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_md7jx0xq.json")
password = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_kwrygs18.json")
backup = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_YtsxhX.json")
hosting = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zfbyxadx.json")
firewall = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_1idqu1ac.json")
security = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jxdqwrvf.json")


with st.container():
        st.header("CARA MENCEGAH TERJADINYA CYBER ATTACK")
        st.write("##")
        image_column, text_column = st.columns((1,2))
        with image_column:
            st_lottie(penetration, height=250)
        with text_column:
            st.subheader(":one: Penetration testing")
            st.write(
                """
        Pada dasarnya, penetration testing adalah metode pengujian keamanan pada infrastruktur IT
        yang dilakukan dengan cara-cara yang sering digunakan oleh hackers. Artinya, para penguji 
        akan melakukan simulasi serangan cyber untuk mengetahui bagaimana
        tingkat keamanan pada sistem yang dikembangkan. Dari pengujian tersebut, dapat mengetahui kelemahan atau
        kerentanan apa saja yang ada pada sistem sehingga perbaikan dapat segera dilakukan.
        """
        )

st.write ("\n")
st.write ("\n")
st.write ("\n")

with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st_lottie(perbarui, height=250)
        with text_column:
            st.subheader(":two: Selalu memperbarui semua software yang digunakan")
            st.write(
                """
        Kegiatan memperbarui software bertujuan untuk meningkatan kualitas software baik dari sisi performa atau
        sistem keamanan di dalamnya. Jika hacker melihat Anda masih menggunakan software lama yang memiliki cacat kode di dalamnya,
        maka mereka dapat mengeksploitasi kerentanan tersebut untuk masuk dan mengakses data-data penting di dalamnya.
        Akibatnya, kasus kebocoran data dapat terjadi sehingga dapat merugikan diri sendiri bahkan orang lain."""
        )


st.write ("\n")
st.write ("\n")
st.write ("\n")

with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st_lottie(password, height=300)
        with text_column:
            st.subheader(":three: Gunakan kata sandi yang kuat")
            st.write(
                """Penggunaan password yang kuat merupakan salah satu cara mencegah cyber crime di perusahaan.
                Oleh karena itu, Anda perlu menerapkan penggunakan kata sandi yang kuat untuk semua sistem atau aplikasi yang dipergunakan.
                Antara satu aplikasi dengan aplikasi lain juga tidak boleh menggunakan kata sandi yang sama.
                Untuk menghasilkan kata sandi yang kuat, dapat mengikuti beberapa tips berikut :
                - Gunakan karakter yang panjang
                - Kombinasikan kata sandi menggunakan angka, simbol, huruf kapital, dan huruf kecil
                - Jangan menggunakan informasi pribadi sebagai password, seperti tanggal lahir."""
        )

st.write ("\n")
st.write ("\n")
st.write ("\n")

with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st_lottie(backup, height=300)
        with text_column:
            st.subheader(":four: Enkripsi dan backup data sensitif secara rutin")
            st.write(
                """Backup data yang dilakukan secara rutin akan membantu perusahaan untuk memulihkan data yang hilang
                ketika terjadi serangan cyber crime serta melindungi data-data ketika terjadi kerusakan pada sistem komputer. 
                Anda dapat melakukan backup data ke drive eksternal atau perangkat portabel lain seperti USB flash drive atau USB stick.
                Untuk backup yang lebih aman, Anda juga bisa menyimpannya ke dalam cloud yang menggunakan enkripsi
                ketika mentransfer dan menyimpan data-data Anda."""
        )

st.write ("\n")
st.write ("\n")
st.write ("\n")

with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st_lottie(hosting, height=300)
        with text_column:
            st.subheader(":five: Gunakan layanan hosting yang aman")
            st.write(
                """Jika Anda mengelola website, pastikan website tersebut menggunakan layanan hosting yang aman
                sehingga data-data akan terlindungi. Anda juga perlu memastikan bahwa layanan hosting yang digunakan
                dapat memberikan perlindungan terhadap serangan cyber crime seperti DDoS."""
        )

st.write ("\n")
st.write ("\n")
st.write ("\n")

with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st_lottie(firewall, height=300)
        with text_column:
            st.subheader(":six: Menggunakan Web Application Firewall (WAF)")
            st.write(
                """WAF berfungsi sebagai gatekeeper yang melindungi website atau web application perusahaan.
                Ketika menggunakan WAF , sistem akan memblokir dan menolak akses ketika menemukan lalu lintas
                yang mencurigakan atau lalu lintas yang memiliki indikasi sebagai ancaman untuk keamanan website perusahaan.
                Dengan demikian, website akan terhindari dari berbagai ancaman cyber seperti cross-site-scripting (XSS),
                cross-site forgery, SQL injection, DDoS, dan lain-lain."""
        )

st.write ("\n")
st.write ("\n")
st.write ("\n")

with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            st_lottie(security, height=300)
        with text_column:
            st.subheader(":seven: Gunakan security software")
            st.write(
                """Salah satu bentuk cyber crime yang banyak menyerang adalah infeksi malware baik itu dalam bentuk serangan ransomware,
                 worm, trojan, atau yang lain. Malware atau malicious software ini sengaja dirancang untuk  merusak perangkat,
                 mencuri data-data sensitif, dan berbagai tujuan jahat lainnya."""
        )

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

komentar3 = st.text_input("Barikan komentar anda:", "")

st.markdown(f"Komentar : {komentar3}")