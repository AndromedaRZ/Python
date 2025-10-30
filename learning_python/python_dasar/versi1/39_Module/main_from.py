# import matematika
# cara yang berbeda untuk menggunakan import

from matematika import tambah, kali, pangkat
# maksudnya adalah kita mengimport dengan langsung mengambil nama fungsi dari module tersebut
# dengan cara di atas, maka kita tidak perlu menghiraukan namespace-nya lagi ketika menggunakan fungsi dari module terebut
# jika tetap menggunakan namespace seperti sebelumnya maka hasilnya akan error

# ada juga cara untuk langsung mengimport semua fungsi yang ada di dalam sebuah module tanpa harus mengetik nama fungsinya satu per satu
from matematika import *
# dengan cara di atas kita bisa menggunakan semua fungsi di dalam module matematika tanpa perlu menambahkan namespace-nya
# hanya saja cara tersebut tidak direkomendasikan
# karena bisa menyebabkan kebingungan terhadap fungsi yang kita gunakan berasal dari mana

# dengan namespace.
# hasil_tambah = matematika.tambah(1,2,3,4,5)

# tanpa namespace.
hasil_tambah = tambah(1,2,3,4,5)
print(f"Hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"Hasil kali = {hasil_kali}")

pangkat_3 = pangkat(3)
print(f"Pangkat 3 = {pangkat_3(3)}")
