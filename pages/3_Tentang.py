import streamlit as st

st.set_page_config(
    page_title="Tentang",
    page_icon="ℹ️",
)

st.title('Tentang AuditWatch')

st.header('Latar Belakang')
col1, col2 = st.columns([1,3])
with col1:
        st.image("assets/logo_21.png")
with col2:
    st.write("AuditWatch adalah aplikasi yang dikembangkan sebagai proposal untuk kompetisi TrackAML Hackaton 2023 yang diselenggarakan oleh PPATK (Pusat Pelaporan dan Analisis Transaksi Keuangan). Aplikasi ini bertujuan untuk menganalisis data transaksi perbankan dan mengidentifikasi adanya aktivitas pencucian uang.")

st.header('Teori: Hukum Benford')
col1, col2 = st.columns(2)
with col1:
        st.image("https://raw.githubusercontent.com/danielmccarville/Benfords/main/assets/Demo%20Figure.png", width=300)
        st.write("Sumber: [Github](https://github.com/danielmccarville/Benfords)")
with col2:
        st.write("Salah satu teori yang digunakan dalam AuditWatch adalah Hukum Benford. Hukum Benford menyatakan bahwa dalam banyak kumpulan data numerik yang beragam, angka pertama yang signifikan pada banyak angka akan memiliki distribusi yang mengikuti pola tertentu. Anda dapat mempelajari lebih lanjut tentang Hukum Benford melalui tautan berikut: [Benford's law](https://en.wikipedia.org/wiki/Benford%27s_law)")

st.header('Metode')
st.write("AuditWatch mengimplementasikan metode ensemble learning menggunakan tiga algoritma klasifikasi, yaitu:")
st.subheader('Regresi Logistik')
st.write("Regresi Logistik adalah metode statistik yang digunakan untuk memprediksi probabilitas kejadian suatu peristiwa dengan menggunakan variabel independen. Anda dapat mempelajari lebih lanjut tentang Regresi Logistik melalui tautan berikut: [Regresi Logistik](https://en.wikipedia.org/wiki/Logistic_regression)")
st.subheader('Random Forest Classifier')
st.write("Random Forest Classifier adalah algoritma klasifikasi yang menggabungkan beberapa pohon keputusan (decision tree) untuk membuat prediksi. Anda dapat mempelajari lebih lanjut tentang Random Forest Classifier melalui tautan berikut: [Random Forest Classifier](https://en.wikipedia.org/wiki/Random_forest)")
st.subheader('XGBoost Classifier')
st.write("XGBoost Classifier adalah algoritma klasifikasi yang menggunakan pohon keputusan (decision tree) secara iteratif untuk meningkatkan performa prediksi. Anda dapat mempelajari lebih lanjut tentang XGBoost Classifier melalui tautan berikut: [XGBoost Classifier](https://en.wikipedia.org/wiki/XGBoost)")

st.divider()
    
st.header('Seiring Sehaluan')

col1, col2 = st.columns([2,1])
with col1:
    st.subheader('IPB University')
    st.write("- Muhammad Dzakwan Alifi (Statistika dan Sains Data 2022)")
    st.write("- Indra Mulya Ginting (Statistika dan Sains Data 2022)")
    st.write("- Kaylah Ziyadah Imana (Bisnis 2022)")
with col2:
    st.image('assets/logo_ipb.png')
    

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)