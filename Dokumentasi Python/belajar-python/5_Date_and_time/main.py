# Date and Time (Latihan)

import datetime as dt# mengimport library datetime dan kita tambahkan 'as dt' untuk mempersingkat perintahnya menjadi dt

# untuk fungsi lebih banyak dari datetime ini bisa dilihat pada url di bawah ini:
# https://docs.python.org/3/library/datetime.html

# hari_ini = datetime.date.today() # jika kita tidak menambahkan 'as dt' saat mengimport library datetime, maka kodenya harus ditulis seperti baris ke 5 ini

hari_ini = dt.date.today() # akan menampilkan tanggal hari ini tergantung perintahnya

print(hari_ini)
print


tanggal = dt.date(2006,9,22)
print(tanggal)

###########################################################

print("Silahkan masukkan tanggal, \nbulan dan tahun lahir anda \n")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah: {tanggal_lahir}")
print(f"Harinya adalah: {tanggal_lahir:%A}") # tambahan simbol (:%A) untuk menampilkan hari berdasarkan tanggal, bulan, dan tahun lahir yang kita masukkan saat penginputan data dari user


hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari  = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30


print(f"Harinya adalah: {tanggal_lahir:%A}")
print(f"Umur anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} Bulan")

# Penjelasan singkat bagaimana cara menghitung umur dari kode program di atas
'''
1. baris ke 31 Program akan mencari tahu tanggal, bulan, dan tahun hari ini
2. baris ke 34 menghitung umur tahun dengan cara menjumlahkan banyaknya hari dari umur kita dan membagikannya dengan 365 hari (365 hari setara dengan 1 tahun)
3. baris ke 35 menghitung sisa harinya dan membagikannya dengan 30 hari (1 bulan) untuk mencari bulan sisa 

'''
