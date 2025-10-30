'''file I/O (input/output)'''
# file input/output adalah kemampuan program untuk membaca data dari file eksternal dan menulis data ke file eksternal
# dengan file I/O, kita bisa:
# - menyimpan data secara permanen
# - membaca data yang sudah tersimpan
# - membuat laporan dalam bentuk file
# - memroses data dari file eksternal
# - backup dan restore data aplikasi

'''membuka dan menutup file'''
# untuk membuka file, kita bisa menggunakan fungsi 'open(<file>, <mode>)'
# setelah kita membuka file, jangan lupa untuk menutupnya menggunakan function 'close()' pada variabelnya
# saat membuka file, kita harus menentukan modenya

# berikut adalah mode file
# r : read (baca) -> membaca file yang sudah ada
# w : write (tulis) -> menulis file baru atau menimpa file yang lama jika sudah ada
# a : append (tambah) -> menambah data di akhir file (maksudnya akhir itu seperti baris terakhir/index terakhir)
# x : create (buat) -> membuat file baru, dan akan menjadi error ketika file dengan nama yang sama sudah ada