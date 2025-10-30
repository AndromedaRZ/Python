# Program Hello Python (Hello, World!)

# pada permulaan belajar python, kita akan menggunakan sebuah terminal atau Python Interactive Shell
# buka terminal yang kita miliki lalu ketik `python` atau `python3` dan tekan enter
# maka otomatis kita berada di dalam Python Interactive Shell yang biasanya ditandai dengan simbol '>>>' pada kolom pengetikan terminal
# di sana kita bisa mengetik program pertama kita, yaitu 'print("Hello, Wordl!")' lalu tekan enter
# maka outputnya akan menampilkan kata yang kita masukkan di dalam kurung print()

# cara keluar dari Python Interactive Shell adalah dengan mengetik perintah 'exit()' atau 'quit()'

# berikutnya kita akan belajar tanpa menggunakan Python Interactive Shell, melainkan menggunakan file berformat python (ditandai dengan .py sebagai ekstensionnya)
# lalu menjalankan file python tersebut menggunakan terminal

# lalu buat program pertama kalian seperti di bawah ini
print("Hello, World!")

print("Apa kabar semuanya?")
# dan 'run' file python ini agar program di atas bisa berjalan

## Membuat komentar

# cara membuat komentar adalah dengan menambahkan simbol pagar '#' di awal baris kalimat yang ingin kita jadikan komentar
# komentar tidak akan tereksekusi oleh sistem

# contoh komentar, bahkan petunjuk yang dibuat di sini menggunakan komentar

'''Variabel dan Tipe Data'''

# Variabel adalah 'wadah' atau 'kotak' untuk menyimpan nilai atau suatu data
# dalam Python, variabel bersifat dinamis yang artinya nilainya bisa kita ubah sesuka hati kita

# pembuatan variabel dan nilanya biasa disebut assignment

# <nama_variabel> = <isi_variabel>

nama = 'Budi'   # wadah bernama 'nama' berisi teks 'Budi'
umur = 20       # wadah bernama 'umur' berisi angka 20
tinggi = 160.5  # wadah bernama 'tinggi' berisi angka desimal 170.5

# aturan penamaan variabel
# - Tidak boleh dimulai dengan angka (jika angkanya di tengah atau di belakang diperbolehkan)
# - Tidak boleh pakai simbol mines
# - Tidak boleh pakai keyword python (contoh: if, else, class, def)
# - Tidak boleh ada spasi (alternatifnya bisa menggunakan garis bawah (underscore) '_')


# variabel bersifat dinamis, yang artinya kita bisa mengubah nilainya sesuai kemauan kita
nilai_a = 10
print(nilai_a)

nilai_a = 20
print(nilai_a)

# walaupun di atas ada 2 variabel dengan nama yang sama, maka hasil print()-nya akan berbeda tergantung perubahan terbaru yang kita lakukan

'''tipe data dasar'''
# Integer (int) = bilangan bulat
# Float = bilangan desimal (bilangan yang memiliki tanda koma)
# String (str) = Teks
# Boolean (bool) = True/False

# bilangan bulat positif dan negatif (integer)
umur = 20
tahun_lahir = 2006
saldo = -50000
nol = 0

# bilangan besar (Python bisa menyimpan angka yang besar)
populasi_dunia = 8200000000
angka_besar = 1923811010931093198329812381120294248294282894928493

print(type(umur))           # <class 'int'>
print(type(angka_besar))    # <class 'int'>
# gunakan 'type()' untuk mencari tahu apa tipe data dari suatu variabel
print(type(nama))

# bilangan dengan koma (float)

berat = 40.5

pi = 3.14
suhu = -10.5

# notasi scientific
speed_of_light = 3e8    # 3 x 10^8 = 300000000
very_small = 1e-6       # 0.000001

print(type(tinggi)) # <class 'float'>
print(speed_of_light)

# tipe data string

# ada 3 cara untuk membuat string

# 1. menggunakan single quotes (petik satu)
nama = 'Budi Santoso'
kota = 'Jakarta'

# 2. menggunakan double quotes (petik dua)
alamat = "Jl. Merdeka No. 123"
pesan = "Selamat datang di Python!"

# 3. menggunakan triple quotes
# maksud dari triple quotes di sini adalah dengan menggunakan petik satu ataupun petik dua sebanyak 3 kali
puisi = '''
Ini adalah Puisi
yang terdiri dari
beberapa baris'''

# string kosong
empty_string = ""
another_empty = ''

print(type(nama)) # <class 'str'>

# tipe data boolean
# digunakan untuk menyatakan iya dan tidak, atau benar dan salah
is_student = True
is_married = False
has_licence = True

print(type(is_student)) # <class 'bool'>

# assigment dasar
nama = 'Luna'
umur = 23
tinggi = 156.0
is_married = False

# multiple assigment
x = y = z = 0           # semua variabel akan bernilai 0
a, b, c = 1, 2, 3       # a=1, b=2, c=3
name, age = 'Kyle', 21  # name='Kyle', age=21

# mengubah nilai variabel
skor = 80
print(skor) # 80
skor = 90   # mengubah nilai
print(skor, 'Nilainya sudah berubah') # 95


# untuk memunculkan isi dari variabel, kita bisa menggunakan perintah 'print()'
# di dalam kurung 'print()' kita isi dengan nama variabel yang ingin dipanggil
# kita bisa memunculkan banyak variabel sekaligus dalam satu perintah print

nama_depan = "Jade"
nama_belakang = "Watson"
nama_lengkap = nama_depan + ' ' + nama_belakang # tipe data string bisa kita gabungkan seperti ini

panjang = 10
lebar = 5
luas = panjang * lebar # jika isi variabel berupa angka, kita bisa melakukan operasi pada variabel tersebut

print("Nama lengkap:", nama_lengkap)
print("Luas persegi panjang:", luas)

'''input dari user (pengguna)'''

# gunakan perintah 'input()' untuk meminta input dari pengguna
# 'input()' akan selalu menghasilkan tipe data string

nama = input("Masukkan nama anda: ") # input dari user akan dimasukkan ke dalam variabel nama
print(nama)

# program akan berhenti di input dan akan dilanjut sampai kita memasukkan nilai dari user ke dalam input

umur_teks = input("Masukkan umur anda: ")
print("Umur anda:", umur_teks)
print("Tipe data umur:", type(umur_teks)) # <class 'str'>

'''Konversi tipe data'''
# mengubah tipe data lain menjadi tipe data yang kita inginkan
# int() -> mengubah string atau tipe data lain menjadi integer (bilangan bulat)
# float() -> mengubah integer atau string menjadi float (bilangan desimal)
# str() -> mengubah integer atau tipe data lain menjadi string (teks)
# bool() -> mengubah tipa data lain menjadi boolean (True/False)

umur_teks = input("Masukkan umur anda: ")
umur = int(umur_teks) # mengubah tipe data lain menjadi integer

print("Umur anda:", umur)
print("Tipe data umur:", type(umur)) # <class 'int'>