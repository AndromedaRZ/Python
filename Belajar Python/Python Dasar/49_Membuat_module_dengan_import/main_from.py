# membuat module dengan import

'''
kita bisa memanggil sebuah fungsi yang kita buat di file python eksternal, pada contoh di bawah ini, kita akan mencoba mengambil (menggunakan) fungsi dari file python eksternal bernama matematika.py yang isinya adalah fungsi perhitungan aritmatika'''
# module matematika dengan import

# kita bisa mengambil beberapa fungsi dari suatu file eksternal menggunakan from seperti contoh berikut
# from (nama filenya) import (nama fungsi atau modul yang ada di dalam file eksternal tersebut), agar lebih jelas lagi, lihatlah contoh kasus di bawah ini

from matematika import tambah, kali # bisa kita pilih setiap fungsi yang ingin kita ambil
from matematika import * # bisa gunakan simbol bintang untuk mengambil semua fungsi yang ada di dalam file eksternal tersebut
from matematika import tambah as add # kita juga bisa menggunakan fungsi as untuk memperpendek nama fungsi yang kita gunakan
from matematika import kali as multi # mempersingkat nama fungsi kali
from matematika import pangkat as rank # mempersingkat nama fungsi pangkat
import matematika as math # mempersingkat nama filenya
 
hasil_tambah = add(2, 5, 6) # kita tidak perlu lagi menambahkan 'matematika' atau nama filenya lagi dikarenakan kita sudah mengimpor penuh fungsinya dari file tersebut menggunakan form dan import
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = multi(5, 2, 1, 2)
print(f"hasil kali = {hasil_kali}")

pangkat2 = rank(2)
print(f"hasil 5 pangkat 2 = {pangkat2(5)}")

hasil_tambah2 = math.tambah(5, 5)
print(f'hasil tambah 2 = {hasil_tambah2}')

