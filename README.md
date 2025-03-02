# simple-test-of-Isolation-Forest
penulis membuat contoh sederhana dalam melakukan anomaly detection menggunakan Isolation Forest
dengan beberapa point
1. data digunakan adalah data Iris
2. data dianggap bersih sehingga tidak dilakukan processing pada data

# apa itu Isolation Forest?
Isolation Forest adalah algoritma yang digunakan untuk mendeteksi suatu anomali atau outlier dalam suatu dataset. 
Algoritma ini bekerja dengan prinsip bahwa anomali lebih mudah diisolasi dibandingkan dengan data normal.
dimana hasil (terutama pada visualisasi) untuk nilai yang ditentukan (treshold) akan memiliki ruang sendiri seolah terisolasi atau terpisah dari data yang bukan anomali maupun outlier

# Cara Kerja Isolation Forest
berikut langkah kerja Isolation Forest dalam menentukan data anomaly ataupun outlier
1. Membangun Pohon Isolasi
Data dibagi secara rekursif dengan memilih fitur secara acak dan menentukan titik pemisahan secara acak di dalam rentang fitur tersebut.
Proses ini terus dilakukan hingga setiap sampel terisolasi dalam sebuah node.

2. Menghitung Kedalaman Isolasi
Semakin cepat suatu titik data terisolasi (semakin sedikit pemisahan yang dibutuhkan), semakin besar kemungkinan data tersebut merupakan anomali.
Data normal membutuhkan lebih banyak pemisahan sebelum akhirnya terisolasi.

3. Menentukan Skor Anomali
Skor dihitung berdasarkan kedalaman rata-rata isolasi suatu titik.
Jika skor tinggi, maka data kemungkinan besar adalah anomali.

sedehananya score ini bisa disebut anomaly score, kita dapat menentukan nilainya
sebagai contoh
Nilai Anomaly Score = 1 maka menunjukkan data tersebut adalah anomaly dan berarti path lengthnya pendek.
Nilai Anomaly Score < 0.5 maka menunjukkan  data tersebut normal dan berarti path lengthnya panjang.
Nilai Anoamly score disekita 0.5 menunjukkan bahwa dataset normal dan tidak ditemukan adanya anomaly.
