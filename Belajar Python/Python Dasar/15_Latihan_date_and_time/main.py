# Date and Time (latihan)

import datetime as dt

hari_ini = dt.date.today() # fungsi kode disamping adalah mengecek tanggal hari ini
print(f"Today is {hari_ini:%A}") # format string ':%A' berfungsi untuk mengecek hari pada tanggal yang telah ditentukan didalam variabel 'hari ini'
print(hari_ini,"\n")


tanggal = dt.date(2006, 9, 22) # kita juga bisa menentukan tahun, bulan, dan tanggal sesuai yang kita inginkan
print(f"I was born on {tanggal:%A}")
print(tanggal)

# meminta input dari user untuk menentukan hari dari tanggal lahir user

print("Silahkan masukan tanggal, bulan, dan tahun lahir adalah: ")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan\t: "))
tahun = int(input("Tahun\t: ")) 

tanggal_lahir = dt.date(tahun, bulan, tanggal) # mengambil nilai dari input variabel tanggal, bulan, dan tahun di atas
print(f"Tanggal lahir anda adalah {tanggal_lahir}")

# umur = hari_ini.year - tahun
print(f"Hari ini tanggal : {hari_ini}")
# print(f"Umur saat ini adalah {umur} tahun")

umur_hari_ini = hari_ini - tanggal_lahir
umur_tahun = umur_hari_ini.days // 365 # perintah di samping akan membagi total hari anda sejak lahir dan akan membulatkan hasil pembagiannya karena hasilnya akan menjadi koma
umur_bulan_sisa = (umur_hari_ini.days % 365) // 30

print(f"Harinya adalah hari {tanggal_lahir:%A}")
print(f"Umur anda saat ini adalah {umur_tahun} tahun, {umur_bulan_sisa} bulan")
print(f"Lama hidup anda saat ini adalah {umur_hari_ini}")