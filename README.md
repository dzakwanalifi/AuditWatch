# AuditWatch

AuditWatch adalah sebuah aplikasi untuk menganalisis data transaksi perbankan dan mengidentifikasi potensi aktivitas pencucian uang. Aplikasi ini dikembangkan sebagai proposal untuk kompetisi TrackAML Hackaton 2023 yang diselenggarakan oleh PPATK (Pusat Pelaporan dan Analisis Transaksi Keuangan).

## Deskripsi

Aplikasi ini menggunakan teori Hukum Benford dan teknik pembelajaran ensemble untuk mengidentifikasi potensi aktivitas pencucian uang dalam data transaksi perbankan. Hukum Benford adalah sebuah hukum empiris yang menjelaskan distribusi angka signifikan pertama dalam banyak jenis data nyata. Dalam aplikasi ini, hukum Benford digunakan untuk membandingkan distribusi digit pertama dalam transaksi dengan distribusi Benford yang diharapkan. Teknik pembelajaran ensemble menggabungkan hasil dari beberapa model pembelajaran mesin, seperti Logistic Regression, Random Forest Classifier, dan XGBoost Classifier, untuk meningkatkan akurasi dalam mengidentifikasi transaksi yang mencurigakan.

## Cara Menggunakan

1. Install dependencies:
`pip install -r requirements.txt`

2. Jalankan aplikasi:
`streamlit run app.py`

3. Unggah file data transaksi perbankan dalam format CSV atau Excel.

4. Pilih kolom yang sesuai untuk waktu transaksi, akun, dan jumlah.

5. Klik tombol "Analisis" untuk memulai analisis data.

6. Hasil analisis akan ditampilkan dalam tabel dan grafik. Transaksi yang dicurigai sebagai aktivitas pencucian uang akan ditandai sebagai "Pelaku".

7. Anda dapat mengunduh hasil analisis dalam format CSV.

## Tim Pengembang

- Muhammad Dzakwan Alifi (Statistika dan Sains Data 2022, IPB University)
- Indra Mulya Ginting (Statistika dan Sains Data 2022, IPB University)
- Kaylah Ziyadah Imana (Bisnis 2022, IPB University)
