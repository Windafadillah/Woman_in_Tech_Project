from email.mime import image
from os import write
import json
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

lottie_service = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_ozaanmx6.json")
st_lottie(lottie_service, key=None)

def local_css(Penyedia_Layanan_CyberSecurity):
    with open(Penyedia_Layanan_CyberSecurity) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

st.markdown("# PENYEDIA LAYANAN CYBERSECURITY")
st.write(
    """Cyber security yaitu aktivitas perlindungan sistem, data, jaringan dan program-program dari ancaman digital (cyber attack).
    Cyber security didefinisikan juga sebagai upaya untuk melindungi informasi pribadi yang sensitif dari serangan digital yang dengan
    sengaja dilakukan untuk mengganggu integritas kerahasiaan dan ketersediaan informasi. Selain perusahaan, individu juga memerlukan
    pengetahuan tentang cyber security dengan tujuan untuk memastikan keamanan data agar tidak sampai bocor ke tangan orang lain.
    Berikut adalah beberapa peyedia layanan cyber security :
    """
)

st.write("""
### 1. PT Phintraco Technology / Phintraco Ekasarana""")
image1 = Image.open("1_phintraco.png")
st.image(image1)

st.write("""
Penyedia jasa IT dengan ruang lingkup yang luas, mulai dari jasa perancangan infrastruktur IT, jasa contact center solution¸
token & teknologi smart card, jaringan dan keamanan IT, Electronic Transacion Services, pengembangan aplikasi, jasa konsultasi IT,
hingga jasa business process outsourcing.
- Partner	: Belum ada informasi
- Sertifikasi	: Belum ada informasi
- Client	: BNI, BCA, Adira Finance,Telkomsel, KAI, Tokopedia, Grab, dan lain-lain
- Website	: https://aplikas.com/
- Telp.	: +6221 691 6619 (Call) / 0878 8344 1838 (Whatsapp)
- Email	: marketing@phintraco.com 
- Alamat	: The East Tower 12th - 17th Floor Jl. DR. Ide Anak Agung Gde Agung Kav. E.3.2 No.1, Kawasan Mega Kuningan Jakarta 12950, Indonesia.

### 2. Aplikas Servis Pesona""")

image2 = Image.open("2_servispesona.png")
st.image(image2)

st.write("""
Merupakan penyedia jasa teknologi informasi bagian dari Phintraco Group. Menyediakan solusi IT dengan cakupan beragam mulai dari jasa perancangan jaringan dan keamanan IT, jasa pengintegrasian platform untuk meningkatkan keamanan, jasa implementasi dan manajemen sistem IT, serta jasa perencanaan dan konsultasi IT
- Partner	: McAfee, SailPoint, Fortinet, Cyberark, Tripwire, Crowdstrike, Forgerock,  
                      Seclore, Tenable, dan Extrahop
- Sertifikasi	: Certified Professional Qualification oleh McAfee
- Client	: Belum ada informasi
- Website	: https://aplikas.com/
- Telp.	: +6221 2555 6118
- Email	: info.asp@aplikas.com / marketing@phintraco.com 
- Alamat	: The East Tower 17th Floor Jl. Dr. Ide Anak Agung Gde Agung Kav. E3.2 No.1, Kawasan Mega Kuningan Jakarta 12950 – Indonesia.


### 3. PT. Berlisensi Berkah Mandiri""")
image3 = Image.open("3_berlisensi.png")
st.image(image3)

st.write("""
Menyediakan jasa konsultasi IT, beragam solusi IT untuk bisnis, pengembangan aplikasi, jasa penyediaan data center, jasa perancangan jaringan IT, penyedia outsourcing IT & IT support, dan jasa maintenance IT. 
- Partner	: Belum ada informasi
- Sertifikasi	: Belum ada informasi
- Client	: Belum ada informasi
- Website	: https://berlisensi.business.site/
- Telp.	: (021) 83710514
- Email	: 
- Alamat	: Spinindo Building, Jalan K.H. Wahid Hasyim No.76 RT.4/RW.3, Kebon Sirih, Menteng Kota Jakarta Pusat Daerah Khusus Ibukota Jakarta 10340 Indonesia


### 4. Lintasarta Security """)
image4 = Image.open("4_lintasarta.png")
st.image(image4)

st.write("""
Menyediakan jasa IT security antara lain manajemen keamanan device, firewall, antivirus, antivirus untuk server, dan security operation. Memiliki kualifikasi dalam manajemen keamanan fiber optic & keamanan IT di bangunan-bangunan tinggi (high rise building). Berpengalaman menangani klien di industry keuangan, pemerintahan, transportasi, manufaktur,telekomunikasi, media, dan lain-lain
- Partner	: IBM, Cisco, VMWare, Microsoft, Veeam, Riverbed, Paloalto Networks, F5,            Oracle, HP, Dell EMC, Lintas Media Danawa, Kazee.
- Sertifikasi	: ISO 9001, ISO/IEC 27001, ISO/IEC 20000-1 Cisco Channel Partner Program, dan lain-lain
- Client	: Korea Telecom, Singtel, SITA Bureau Service, Indosat Singapore, Bloomberg, China Telecom
- Website	: https://www.lintasarta.net/
- Telp.	: +6221 230 2345 (Hunting) / +6221 230 3567 (Fax) / 14052 (Customer Service) / 021 230 2347 (Product Information)
- Email	: info@lintasarta.co.id
- Alamat	: Central Jakarta, Menara Thamrin 12th Floor Jl. M.H. Thamrin Kav.3 Jakarta 10250


### 5. Deloitte Enterprise Technology and Performance""")

image5 = Image.open("5_deloitte.png")
st.image(image5)

st.write("""
Merupakan perusahaan penyedia jasa asurans, audit, dan konsultasi multinasional. Memiliki klien dari beragam latar industri. Menyediakan jasa IT terkait konsultasi strategi & implementasi teknologi; konsultasi rantai pasok dan jaringan operasional; serta implementasi SAP, Oracle, dan ERP Solutions lainnya.  Karena nature perusahaan yang lebih fokus pada sisi bisnis dan manajemen, ruang lingkup jasa IT yang disediakan cenderung lebih terbatas dibanding perusahaan IT lainnya.
- Partner	: Belum ada informasi
- Sertifikasi	: Belum ada informasi
- Client	: Belum ada informasi
- Website	: https://www2.deloitte.com/
- Telp.	: +62 21 5081 8000 (Call) / +62 21 2992 8200 / 8300 (Fax)
- Email	: iddttl@deloitte.com
- Alamat	: The Plaza Office Tower, 32nd Floor, Jl. M.H. Thamrin Kav 28-30, RT.9/RW.5, Gondangdia, Kec. Menteng, Kota Jakarta Pusat, DKI Jakarta 10350

### 6. Datacomm Cloud Business""")

image6 = Image.open("6_datacomm.png")
st.image(image6)

st.write("""
Perusahaan IT penyedia jasa cloud business, security services, dan colocation yang lebih berfokus pada perusahaan-perusahaan mikro dan menengah. Didukung dengan sarana infrastrukur IT yang optimal. Menyediakan jasa virtualisasi, cloud computing, cyber security, dan software define network.
- Partner	: Belum ada informasi
- Sertifikasi	: ISO 9000, ISO 27001 and ISO 20000, dan lain-lain
- Client	: Belum ada informasi
- Website	: https://datacommcloud.co.id/
- Telp.	: 0877-0008-2888 (Whatsapp)
- Email	: sales@datacommcloud.co.id
- Alamat	: Grha Datacomm, Kapten P. Tendean No.18 A, RT.1/RW.4, Mampang Prpt., Kec. Mampang Prpt., Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12790


### 7. TataCyber / Tata Lestari Makmur""")

image7 = Image.open("7_tatacyber.png")
st.image(image7)

st.write("""
Merupakan perusahaan IT yang fokus dalam hal cybersecurity. Memiliki kantor cabang di kota-kota besar se-Indonesia (Medan, Semarang, Solo, Surabaya, Balikpapan, Makassar). Menyediakan jasa cybersecurity yang beragam, antara lain: PCI DSS Audit & certification, vulnerability assessment & ASV, penetration testing, advisory & forensic, pelatihan dan konsultasi, Group-IB threat, intel & secure bank, Checkmarx app sec testing, Reaqta AI threat response, cloud-based LMS, dan lain-lain

- Partner	: Nova Systems, Network Intelligence (NI), CyberAssembly, GroupIB, Checkmarx, Kondukto
- Sertifikasi	: ISO 9000, ISO 27001 and ISO 20000, dan lain-lain
- Client	: BCA, BPPT, KPSG, Blibli, Paninbank, Dana 
- Website	: https://tatacyber.com/
- Telp.	: (021) 5366 0660 / 536 1370 (Call)
- Email	: contact@tatacyber.com
- Alamat	: Komp. Graha Kencana Blok.BE Jl. Raya Pejuangan 88, Kebon Jeruk Jakarta Barat 11530

### 8. Cyber Army Indonesia""")

image8 = Image.open("8_cyberarmy.png")
st.image(image8)

st.write("""
Merupakan perusahaan cybersecurity dengan basis crowd-based. Cyber Army Indonesia menghubungkan pihak klien dengan para bughunter untuk bekerjasama dalam meningkatkan keamanan cyber. Cyber Army Indonesia melibatkan lebih dari 700 bughunter dan menawarkan biaya operasional yang relatif lebih terjangkau disbanding jasa penetration testing. Jasa yang disediakan berfokus pada manajemen kerentanan (Vulnerability Disclosure Program - VDP), selain itu Cyber Army Indonesia juga menawarkan program Bug Bounty Program, dan Cyberarmy Academy.
- Partner	: Telkom Indonesia, Indigo Creative Nation, Badan Siber dan Sandi Negara
- Sertifikasi	: Belum ada informasi
- Client	: Indihome, BPJS Kesehatan, Jabar Digital Service, Kitabisa, bobobox, dan lain-lain
- Website	: https://www.cyberarmy.id/
- Telp.	: +62 812 9393 1337
- Email	: business@cyberarmy.id (for business) / hello@cyberarmy.id (for bughunter)
- Alamat	: Jl. Naripan No.53, Kb. Pisang, Sumur Bandung, Kota Bandung, Jawa Barat 40152

### 9. PT Global Innovation Technology""")

image9 = Image.open("9_innovation.png")
st.image(image9)

st.write("""
Merupakan perusahaan penyedia jasa layanan IT yang meliputi jasa: security, infrastruktur, dan pengembangan mobile app. Adapun jasa cybersecurity yang ditawarkan antara lain: implementasi SSO/ESSO, identity management system, cloud access security broker, priviledged access management, mobile device management, serta security information & event management
- Partner	: Authorized reseller for Oracle, IBM, NetIQ, Splunk, and ObserveIT in Indonesia.
- Sertifikasi	: Belum ada informasi
- Client	: Telkomsel, Telkom Indonesia, Pertamina, Kalbe, UOB, Mandiri, Bank Indonesia, SKK Migas
- Website	: https://innovation.co.id/
- Telp.	: +62 821-1111-2705 / +62 813-6307-7176 (Whatsapp) / +62 21 5794 9000 (Call)
- Email	: marketing@innovation.co.id
- Alamat	: Rukan Permata Senayan Blok B-07 Jl. Tentara Pelajar, RT 01/RW 07 Kebayoran Lama – Jakarta Selatan 12210 Indonesia

### 10. Defender Nusa Semesta (DNS)""")
image10 = Image.open("10_devenxor.png")
st.image(image10)

st.write("""
Merupakan perusahaan penyedia jasa cybersecurity yang menawarkan pemantauan keamanan 24/7, respon & manajemen insiden, manajemen kerentanan (vulnerability), konsultasi melalui aplikasi mobile, pengoleksian dan manajemen log, mencatat data jaringan dan forensic. Menawarkan jasa cybersecurity dengan harga yang bersaing.
- Partner	: CTI Group 
- Sertifikasi	: CISSP, CISA, ISO 27001 LA, ISO 20000 LA, PCI QSA 
- Client	: Belum ada informasi
- Website	: https://www.defenxor.com/
- Telp.	: (+62 21) 2902 3055 
- Email	: info@defenxor.com
- Alamat	: Graha BIP 6th floor, Jalan Jenderal Gatot Subroto Kavling 23, RT.2/RW.2, Karet Semanggi, Kecamatan Setiabudi, Kota Jakarta Selatan, Daerah Khusus Ibukota Jakarta 12930

"""
)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")

komentar5 = st.text_input("Barikan komentar anda:", "")

st.markdown(f"Komentar : {komentar5}")