# module matematiika dengan import

# sedikit berbeda dengan tujuan dari mengimport file python eksternal yang biasa
# biasanya module digunakan untuk menyimpan sebuah tool atau eksekusi kode program yang lebih komples
# bisa dikatakan juga kalo sebuah module bisa menyimpan banyak fungsi yang bisa kita gunakan
# sehingga kita tidak perlu menulis fungsi yang sama di dalam file python utama kita
# kita tinggal menggunakan import statement dan memanggil fungsi tersebut

# import <nama module>

import matematika

hasil_tambah = matematika.tambah(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = matematika.kali(1,2,3,4,5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = matematika.pangkat(3) # argument dari fungsi di baris ini adalah jumlah pangkat yang diinginkan
print(f"Pangkat 3 = {pangkat_3(3)}") # dan argument dari fungsi di baris ini adalah angka yang ingin kita pangkatkan

