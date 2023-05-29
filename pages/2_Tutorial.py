import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Tutorial",
    page_icon="📚",
)

st.title('Tutorial AuditWatch')

st.write("Selamat datang di Tutorial AuditWatch! AuditWatch adalah sebuah aplikasi yang digunakan untuk menganalisis data transaksi perbankan dan mengidentifikasi adanya aktivitas pencucian uang. Dalam tutorial ini, kami akan membantu Anda memahami langkah-langkah penggunaan AuditWatch.")

st.header('Prosedur Penggunaan')
st.subheader('1. Unggah Data Transaksi Perbankan')
st.write("Langkah pertama adalah mengunggah data transaksi perbankan dalam format CSV atau Excel. Pastikan ukuran file tidak melebihi 200 Mb untuk memastikan proses analisis berjalan dengan lancar. Anda dapat menggunakan tombol 'Browse Files' untuk memilih file yang akan diunggah.")
def load_sample_data():
    return pd.read_csv('assets/sample_data.csv')

sample_data = load_sample_data()
csv = sample_data.to_csv(index=False)
st.download_button(
    label="Unduh Sample Data.csv",
    data=csv,
    file_name='sample_data.csv',
    mime='text/csv'
)
st.write("Anda dapat mencoba AuditWatch dengan menggunakan berkas CSV sampel yang disediakan. Berkas sampel ini berisi data transaksi perbankan yang dapat digunakan untuk melakukan analisis.")
st.image('assets/unggah.png')

st.subheader('2. Pilih Kolom yang Sesuai')
st.write("Langkah selanjutnya adalah memilih kolom yang sesuai dari data transaksi perbankan. Anda perlu memastikan memilih kolom dengan benar untuk kolom Waktu, Akun, dan Jumlah. Anda dapat menggunakan dropdown untuk memilih kolom yang sesuai.")
st.image('assets/kolom.png')

st.subheader('3. Analisis Data')
st.write("Setelah Anda memilih kolom yang sesuai, Anda dapat melakukan analisis dengan mengklik tombol 'Analisis'. AuditWatch akan memproses data dan menghasilkan hasil analisis.")
st.image('assets/analisis.png')

st.subheader('4. Hasil Analisis')
st.write("Hasil analisis akan ditampilkan dalam bentuk tabel dan grafik batang. Tabel akan menampilkan akun-akun yang teridentifikasi sebagai pelaku pencucian uang, beserta tanggal transaksi. Grafik batang akan membandingkan jumlah pelaku dan non-pelaku pencucian uang.")
st.image('assets/grafik.png')

st.subheader('5. Unduh Hasil Analisis')
st.write("Anda dapat mengunduh hasil analisis dalam format CSV dengan mengklik tombol 'Unduh Hasil Analisis (CSV)'. File CSV akan berisi tabel hasil analisis yang dapat dibuka dan dianalisis lebih lanjut.")
st.image('assets/unduh.png')



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)