# membuat module dengan import

'''
kita bisa memanggil sebuah fungsi yang kita buat di file python eksternal, pada contoh di bawah ini, kita akan mencoba mengambil (menggunakan) fungsi dari file python eksternal bernama matematika.py yang isinya adalah fungsi perhitungan aritmatika'''
# module matematika dengan import
 
import matematika

hasil_tambah = matematika.tambah(2, 5, 6)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = matematika.kali(5, 2, 1, 2)
print(f"hasil kali = {hasil_kali}")

pangkat2 = matematika.pangkat(2)
print(f"hasil 5 pangkat 2 = {pangkat2(5)}")

