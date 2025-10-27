# string dan manipulasi string

# string adalah tipe data untuk menyimpan teks, dan ditulis menggunakan tanda kutip satu atau dua

# kita bisa menggabungkan variabel bertipe data string dengan variabel bertipe data string lainnya dengan menggunakan '+'
# namun, string tidak bisa digabung dengan tipe data lain seperti integer, float, dan boolean

nama = 'Kaizo'
umur = 20

# cara menggabungkan yang salah (akan error)
# pesan = "Nama saya " + nama + ", Umur " + umur
# print(pesan)

# karena pada saat kita menggabungkan variabel 'umur', variabel tersebut masih bertipe int (integer)

pesan = "Nama saya " + nama + ", Umur " + str(umur) # kita bisa menggunakan 'str()' untuk mengubah tipe variabel umur menjadi string
print(pesan)

# berikutnya panjang string, bisa dikatakan adalah total karakter pada string termasuk spasi
panjang = len(pesan)
print("Jumlah karakter atau panjang string pada variabel pesan:", panjang)
print("Variabel panjang bertipe:", type(panjang)) # hasil dari perhitungan 'len()' akan bertipe integer (int)

'''mengakses karakter dalam string'''
# setiap karakter di dalam string memiliki posisi (index) yang diawali dari 0

# kita akan coba mengambil karakternya menggunakan indexing dengan menggunakan simbol kurung siku
nama = "Python"
print(nama[0]) # P -> karakter pertama
print(nama[1]) # y -> karakter kedua
print(nama[2]) # t -> karakter ketiga

# kita juga bisa memasukkan index dari negatif yang artinya mengambil karakter dari index belakang terlebih dahulu
nama = "Python"
print(nama[-1]) # n -> karakter terakhir
print(nama[-2]) # o -> karakter kedua dari belakang
print(nama[-3]) # h -> karakter ketiga dari belakang

# string slicing
nama = "Python"
print(nama[0:3]) # Pyt -> index 0, 1, 2 (mengambil karakter dari index 0 sampai index ke 2 atau sampai urutan bukan index ke 3)
print(nama[2:5]) # tho -> index 2, 3, 4 ( ~ ~ dari index ke-2 sampai index ke-4 atau sampai urutan bukan index ke 4)
print(nama[1:4]) # yth -> index 1, 2, 3 ( ~ ~ dari index ke-1 sampai index ke-3 atau sampai urutan bukan index ke 3)

print(nama[:3]) # Pyt -> dari awal sampai index ke-2
print(nama[2:]) # thon -> dari index ke-3 sampai terakhir
print(nama[:])  # Python -> seluruh string

'''string method'''
# method adalah fungsi yang menempel pada suatu tipe data
# ada banyak method yang bisa digunakan, tapi kita tidak bisa memasukkan semua contohnya ke dalam file ini
# misalnya ada upper(), lower(), capitalize(), title(), replace(), dan sebagainya
nama = 'luna'
print(nama)
print(nama.upper()) # membuat seluruh karakter menjadi besar semua (uppercase)

nama = 'UCUP SURUCUP'
print(nama)
print(nama.lower()) # membuat seluruh karakter menjadi kecil semua (lowercase)
print(nama.capitalize()) # membuat karakter pertama menjadi kapital
print(nama.title()) # membuat karakter pertama setiap kata menjadi kapital
print(nama.replace(' ','_')) # mengganti karakter yang kita inginkan menjadi karakter yang lain

'''escape characters'''
# escape characters adalah karakter khusus yang bisa kita gunakan dalam string
# \n = untuk membuat newline
# \t = untuk menambahkan 'tab'
# \ = backslash
# ' dan " = (tanda kutip dalam string) perlu menambahkan \ di awal

kalimat = 'baris pertama\nbaris kedua'
print(kalimat)

data = 'Nama:\tLuna\nUmur:\t24'
print(data)

path = 'C:\\Users\\Luna\\Documents'
print(path)

kalimat1 = "Dia berkata \"Halo\" kepada saya"
print(kalimat1)

kalimat2 = 'I\'m learning python'
print(kalimat2)

# string interpolation
# f-string adalah cara paling direkomendasikan untuk melakukan string interpolation
# tambahkan huruf f pada saat membuat teks string
# lalu pada kalimat f-string tersebut kita bisa memasukkan variabel dengan menggunakan kurung kurawal
nama = 'Albert'
umur = 18
kota = 'Rajegpolis'

# menggunakan f-string
profil = f"Halo, nama saya {nama}, umur {umur} tahun, tinggal di kota {kota}"
print(profil)

# perbandingan ketika melakukan interpolation tanpa menggunakan f-string
profil = "Halo, nama saya " + nama + ", umur " + str(umur) + " tahun, tinggal di kota " + kota
print(profil)

# pada saat kita menggunakan f-string, kita bisa langsung memasukkan ekspression di dalamnya

harga = 10000
jumlah = 3

# operasi matematika dalam string
total = f"Total: Rp{harga * jumlah:,}"
print(total)

# menggunakan method dalam f-string
nama = 'Sam Altman'
salam = f"Halo {nama.upper()}!"
print(salam)