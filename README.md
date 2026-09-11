
Nama    : Rasyad Fazri Mulyono NIM : 2225250023  Kelas : 3A
## Tujuan Repositori

Repositori ini berisi latihan dan tugas Pertemuan 2 mata kuliah Algoritma
dan Pemrograman, Program Studi S1 Pendidikan Matematika FKIP Untirta.
Isinya mencakup empat berkas latihan dasar Python (variabel, tipe data,
input-output, dan operator) serta satu tugas utama berupa program
kalkulator koordinat dua titik
## Daftar dan Fungsi Berkas

| Berkas | Fungsi |
|---|---|
| `latihan/01_biodata.py` | Menerima nama, NIM, kelas, dan tahun lahir, lalu menampilkan kartu biodata beserta perkiraan umur. |
| `latihan/02_persegi_panjang.py` | Menerima panjang dan lebar, lalu menghitung luas dan keliling persegi panjang. |
| `latihan/03_konversi_suhu.py` | Menerima suhu dalam Celsius, lalu mengonversinya ke Fahrenheit dan Kelvin. |
| `latihan/04_nilai_akhir.py` | Menerima nilai tugas, UTS, dan UAS, lalu menghitung nilai akhir berdasarkan bobot 20%, 30%, dan 50%. |
| `tugas/kalkulator_koordinat.py` | Menerima koordinat dua titik A dan B, lalu menghitung perubahan koordinat (dx, dy), jarak Euclidean, dan titik tengah antara keduanya. |
 Cara Menjalankan

Jalankan setiap berkas dari terminal VS Code menggunakan perintah berikut.
Pada macOS atau Linux, gunakan `python3` jika `python` tidak dikenali.

    python latihan/01_biodata.py
    python latihan/02_persegi_panjang.py
    python latihan/03_konversi_suhu.py
    python latihan/04_nilai_akhir.py
    python tugas/kalkulator_koordinat.py


## Hasil Pengujian Tugas Utama

| Kasus | Titik A | Titik B | dx | dy | Jarak | Titik Tengah | Sesuai Harapan |
|---|---|---|---|---|---|---|---|
| 1 | (0.00, 0.00) | (3.00, 4.00) | 3.00 | 4.00 | 5.00 | (1.50, 2.00) | Ya |
| 2 | (-2.00, 1.00) | (4.00, 1.00) | 6.00 | 0.00 | 6.00 | (1.00, 1.00) | Ya |
| 3 | (2.50, -1.00) | (2.50, 3.00) | 0.00 | 4.00 | 4.00 | (2.50, 1.00) | Ya |
## Refleksi

- Konsep yang paling saya pahami adalah **variabel dan tipe data (int, float, str)**
  karena saya bisa langsung membedakan tipe data yang dipakai di tiap latihan.

- Kesalahan yang saya temukan adalah **NameError karena salah ketik nama variabel**,
  dan saya memperbaikinya dengan memeriksa ulang ejaan nama variabel di kode.

- Pada pertemuan berikutnya saya ingin lebih memahami **alur kerja Git dan GitHub**,
  terutama urutan `add`, `commit`, dan `push`.
## Sumber

- Hendrayana, A. 2026. *Dasar Python di VS Code dan Pengumpulan melalui GitHub*.
  Bahan Ajar Pertemuan 2, Mata Kuliah Algoritma dan Pemrograman, Program Studi
  S1 Pendidikan Matematika FKIP Untirta.
