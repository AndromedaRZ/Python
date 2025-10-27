# operator dalam bentuk methods

## merubah case dari string

# merubah semua huruf ke uppercase (huruf besar)

salam = "selamat siang, bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua huruf ke lowercase (huruf kecil)
ucapan = "seLamAt UlAng TaHun"
print("normal = " + ucapan)
ucapan = ucapan.lower()
print("lower = " + ucapan)

## pengecekan dengan isX method

# contoh pengecekan apakah string hanya berisi huruf kecil atau lowercase

salam = "selamat pagi"
# mengecek apakah string atau karakter dalam variabel 'salam' hanya berisi huruf kecil
check_lower = salam.islower() # method .islower() berfungsi untuk mengecek apakah semua karakter dalam variabel 'salam' adalah huruf kecil atau tidak, jika iya maka hasilnya adalah True, jika tidak maka hasilnya adalah False, keduanya merupaka tipe data boolean
print(f"'{salam}' is lower = {str(check_lower)}") # variabel 'check_lower' harus di casting ke string agar bisa diprint karena hasil sebelumnya adalah boolean

check_upper = salam.isupper() # method .isupper() berfungsi untuk mengecek apakah semua karakter dalam variabel 'salam' adalah huruf besar atau tidak, jika iya maka hasilnya adalah True, jika tidak maka hasilnya adalah False, keduanya merupaka tipe data boolean
print(f"'{salam}' is upper = {str(check_upper)}") # variabel 'check_upper' harus di casting ke string juga agar bisa diprint karena hasil sebelumnya adalah boolean

# contoh lainnya isX method

'''
isalpha() = untuk mengecek apakah string hanya berisi huruf
isalnum() = untuk mengecek apakah string hanya berisi angka dan huruf (alphanumeric)
isdecimal() = untuk mengecek apakah string hanya berisi angka
isspace() = untuk mengecek apakah ada string kosong seperti spasi, tab, atau newline (\n)
istitle() = untuk mengecek apakah setiap kata dalam string dimulai dengan huruf besar
'''

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # method .istitle() akan mengecek apakah setiap kata dalam string 'judul' dimulai dengan huruf besar, jika iya maka hasilnya True, jika tidak maka hasilnya False, hasilnya juga akan menjadi boolean

print(f"'{judul}' is title = {str(cek_judul)}")

## mengecek komponen .startwith() dan .endswith()

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim") # method .startswith() akan mengecek apakah string dalam variabel 'cek_start' dimulai dengan substring atau karakter yang ditetapkan atau tidak, jika iya maka hasilnya True, jika tidak maka hasilnya False
print("start =", str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak") # method .endswith() akan mengecek apakah string dalam variabel 'cek_end' diakhiri dengan substring atau karakter yang ditetapkan atau tidak, jika iya maka hasilnya True, jika tidak maka hasilnya False
print("end =", str(cek_end))

## penggabungan komponen .join() dan .split()
pisah = ['aku', 'sayang', 'kamu']
print(pisah)

gabung = ' '.join(pisah) # method .join() akan menggabungkan setiap isi di dalam list 'pisah' dengan pemisah yang ditentukan, dalam hal ini pemisahnya adalah tanda spasi (  )
print("gabungan =", gabung) #  hasil dari method .join() akan mengubah data list tadi menjadi string biasa


gabungan = "aku sayang kamu"
print(gabungan.split( )) # method .split() akan memisahkan string 'gabungan' menjadi list berdasarkan pemisah yang ditentukan, jika tidak ada pemisah yang ditentukan maka akan memisahkan meggunakan spasi secara default

# alokasi karakter
print(5*"=" + "data" + 5*"=") # mengulang karakter '=' sebanyak 5 kali, lalu menambahkan data, dan mengulang karakter '=' sebanyak 5 kali lagi

## alokasi karakter dengan .rjust(), .ljust(), dan .center()

kanan = "kanan".rjust(10) # angka '10' menunjukkan panjang total string yang diinginkan, jika panjang string 'kanan' kurang dari 10 karakter, maka sisanya akan diisi dengan spasi
print("'"+kanan+"'") # .rjust(10) akan menggeser string 'kanan' ke kanan sehingga panjang totalnya menjadi 10 karakter, sisanya diisi dengan spasi

kiri = "kiri".ljust(10) # .ljust(10) akan menggeser string 'kiri' ke kiri sehingga panjang totalnya menjadi 10 karakter, sisanya diisi dengan spasi
print("'"+kiri+"'") # .ljust(10) akan menggeser string 'kiri' ke kiri sehingga panjang totalnya menjadi 10 karakter, sisanya diisi dengan spasi

tengah = "tengah".center(10) # .center(10) akan menggeser string 'tengah' ke tengah sehingga panjang totalnya menjadi 10 karakter, sisanya diisi dengan spasi
print("'"+tengah+"'") # .center(10) akan menggeser string 'tengah' ke tengah sehingga panjang totalnya menjadi 10 karakter, sisanya diisi dengan spasi

# dalam ketiga perintah di atas, jika panjang string dalam variabel kurang dari angka yang ditentukan (dalam kasus ini 10), maka sisa karakternya secara otomatis akan diisi dengan spasi, tetapi jika panjang string lebih dari angka yang ditentukan, maka string tersebut tidak akan terpotong dan tetap utuh.

# kita juga bisa menggunakan karakter lain sebagai pengganti spasi
tengah = "tengah".center(10, '-') # menggunakan tanda '-' sebagai pengganti spasi
print(f"'{tengah}'") # hasilnya akan menggeser string 'tengah' ke tengah dengan panjang total 10 karakter, sisanya diisi dengan tanda '-'

# kebalikannya -> .strip()
tengah = tengah.strip("-") # .strip() akan menghapus karakter yang ditentukan dari awal dan akhir string, dalam hal ini karakter '-' dihapus dari awal dan akhir string 'tengah'
print(f"'{tengah}'") # hasilnya akan menjadi 'tengah' tanpa tanda '-' di awal dan akhir