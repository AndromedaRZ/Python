'''function'''
# function (fungsi) adalah baris kode yang bisa kita gunakan berkali-kali
# function membantu kita menulis kode yang lebih rapih, mudah dibaca, dan mudah dipelihara
# dengan function, kita tidak perlu menulis kode yang sama berulang kali

# sebenernya pada saat kita menggunakan 'print()' ataupun method-method seperti 'upper()' itu semua adalah function
# bawaan python yang bisa kita gunakan sesuka hati kita

# namun kali ini kita akan belajar cara membuat function sendiri
# 1. function dibuat dengan kata 'def' lalu diawali dengan nama function dan diakhiri dengan kurung buka dan tutup
# 2. biasanya nama function dibuat sama seperti membuat nama variabel dan ketentuannya pun hampir sama
# 3. isi function harus menggunakan indentasi (spasi di awal) untuk menandakan bahwa itu adalah sebuah function
# 4. untuk memanggil function, kita tinggal menulis nama function-nya dan diikuti dengan kurung buka dan tutup
# pada saat kita memanggil function, semua perintah yang ada di dalam function tersebut akan ikut tereksekusi

def nama_function():
    # baris kode yang akan dijalankan
    print("Hello dari function!")
    
# cara memanggil function
nama_function()     # otomatis semua perintah yang ada di dalam function tersebut akan tereksekusi
nama_function()
nama_function()


'''function dengan paramter'''
# parameter berguna agar kita bisa mengirim data ke function
# cara menambahkan parameter adalah dengan memberikan nama parameter di dalam kurung pada saat membuat function
# jika kita ingin membuat lebih dari satu parameter dalam 1 function, kita bisa memisahkan setiap nama parameter menggunakan koma
# pada saat kita memanggil function yang memiliki parameter tersebut, kita harus mengisi parameternya agar functionnya bisa berjalan


def sapa_nama(nama):    # 'nama' adalah sebuah parameter
    # lalu dalam function ini, kita bisa menggunakan data yang disimpan di parameter
    print(f"Halo {nama}!, senang berkenalan denganmu.")
    
    
sapa_nama('Luna')       # 'Luna' bisa kita analogikan sebagai input yang akan masuk menjadi parameter ke dalam functionnya
sapa_nama('Charles')    

# sapa_nama()       # jika parameternya kita kosongkan, maka hasilnya akan error


# kita juga bisa membuat fungsi untuk melakukan operasi
def hitung_luas(panjang, lebar):    # pisahkan dengan koma ketika membuat lebih dari 1 parameter
    luas = panjang * lebar
    print(f"Luas persegi panjang adalah: {luas}")
    

hitung_luas(10, 5)  # parameter yang dimasukkan kita pisahkan menggunakan koma
hitung_luas(3, 7)


'''function dengan return value'''
# saat membuat function, mungkin kita ingin membuat agar fungsi tersebut melalukan sebuah operasi ataupun kegiatan lain
# dan kita ingin mengambil data dari hasil perhitungan ataupun hasil kegiatan tersebut
# maka dari itu function juga bisa mengembalikan nilai dari kegiatan yang kita lakukan di dalam function
# dengan cara menggunakan 'return' kita bisa mendapatkan nilainya
# setelah kata kunci 'return', diikuti dengan nilai yang ingin kita kembalikan pada function tersebut

def hitung_luas_lingkaran(radius):
    pi = 3.14
    luas = pi * radius * radius
    return luas     # nantinya nilai 'luas' akan dikembalikan oleh function


luas1 = hitung_luas_lingkaran(4)
luas2 = hitung_luas_lingkaran(7)

print(f"Luas lingkaran radius 4: {luas1}")
print(f"Luas lingkaran radius 7: {luas2}")
print(f"Total luas: {luas1 + luas2}")


'''Default parameter'''
# ketika kita menambahkan parameter pada saat pembuatan function, maka ketika memanggil function tersebut parameter yang tersedia harud diisi
# namun kita juga bisa menambahkan 'default parameter', yaitu nilai awal untuk parameter tersebut
# hal ini menjadikan ketika kita tidak mengisi parameter tersebut pada saat memanggil fungsinya
# maka sebagai gantinya default parameterlah yang akan mengisi parameter tersebut
# posisi default parameter tidak boleh di depan parameter biasa, harus di belakang parameter biasa ketika membuat lebih dari 1 parameter
# untuk membuat default parameter, cukup gunakan '=' (sama dengan) diikuti dengan niali awalnya

def sapa(nama, sapaan='Halo'):  # 'sapaan="halo"' adalah default parameter
    print(sapaan, nama)         # sehingga kita 'tidak wajib' mengisi parameter sapaan (opsional)
                                # namun untuk parameter nama tetap wajib diisi

sapa('Luna')                # 'Luna' hanya mengisi parameter nama, sedangkan tidak ada input untuk parameter sapaan
                            # sehingga parameter sapaan akan diisi oleh nilai default yang sudah kita atur
sapa('Charles', 'Hai')      # 'Charles' akan mengisi parameter nama, dan 'Hai' akan mengisi parameter sapaan
sapa('Rina', 'Selamat pagi!') # 'Rina' akan mengisi parameter nama, dan 'Selamat pagi!' akan mengisi parameter sapaan



'''keyword argument (*kwargs)'''
# argument adalah nilai yang kita kirim ke parameter function pada saat pemanggilan function
# saat memanggil function, posisi argument harus sama dengan posisi parameter pada function
# namun, jika kita ingin mengubah posisi argument yang menyebabkan posisinya tidak sama dengan posisi parameter
# maka kita harus menyebutkan nama parameternya pada saat memanggil function
# fitur ini disebut keyword argument
# saat menggunakan keyword argument, kita juga bisa mengombinasikannya dengan argument biasa


def perkenalan(nama, umur, kota):
    print("Nama: ", nama)
    print("Umur: ", umur, "tahun")
    print("Kota: ", kota)
    print("----")
    
# positional argument (urutan argument harus sesuai dengan posisi parameter)
perkenalan("Luna", 18, "Tangerang")

# menggunakan keyword argument (urutan argument boleh bebas) dan harus disertai dengan nama parameternya
perkenalan(kota='Bekasi', nama='Charles', umur='21')
perkenalan(umur='18', kota='Jakarta', nama='Budi')


def buat_profil(nama, umur, kota='Jakarta', pekerjaan='Belum bekerja'):
    print(f"=== PROFIL {nama.upper()} ===")
    print(f"Umur : {umur} tahun")
    print(f"Kota : {kota}")
    print(f"Pekerjaan: {pekerjaan}")
    print("==========================")
    
    
buat_profil("Alice", 20)    # parameter 'kota' dan 'pekerjaan' tidak wajib diisi
buat_profil("Rina", 22, pekerjaan="Programmer")     # membuat nilai baru untuk parameter 'pekerjaan'
buat_profil("Zidane", 19, kota="Makassar")          # membuat nilai baru untuk parameter 'kota'


'''local variable'''
# ketika kita membuat variabel (assignment) di dalam sebuah funtion
# maka variabel tersebut bersifat local dan hanya bisa digunakan di dalam function terebut
# sehingga kita tidak bisa mengaksesnya dari luar function

def fungsi_tes():
    x = 10  # local variable
    print(f"Nilai x adalah: {x}")
    
fungsi_tes()
# print(x)  # ketika kita ingin mengakses variabel x, maka hasilnya akan error
            # karena variabel tersebut bersifat local variabel dan hanya bisa berfungsi di dalam function 'fungsi_tes'

'''global variable'''
# variabel yang biasanya kita buat di luar function bersifat global function dan bisa kita gunakan di dalam function
# namun kita tidak bisa mengubah nilai dari global variable di dalam function
# jika kita ingin mengubah nilanya, maka kita harus menggunakan kata kunci 'global' di dalam function-nya

nama_global = 'Luna'

def show_name():
    print(f"Halo, nama saya {nama_global}") # nama_global bisa kita akses di dalam function
                                            # namun, kita tidak bisa mengubah nilainya

def change_name():
    global nama_global  # jika kita tidak menggunakan keyword 'global', maka kita tidak bisa mengubah nilainya
    nama_global = 'Lucia'

show_name()     # 'Luna'
change_name()   # fungsi untuk mengganti nilai
show_name()     # 'Lucia'


'''parameter dinamis'''
# Python mendukung parameter dinamis, yang artinya jumlah argument yang kita masukkan bisa bebas semau kita
# kita bisa menambahkan 1 simbol bintang '*' sebelum nama parameter yang mengindikasikan bahwa ini adalah parameter dinamis berupa list
# atau menambahkan 2 simbol bintang '**' sebelum nama parameter yang mengindikasikan bahwa ini adalah parameter dinamis berupa dictionary
# jadi, semua data atau argument yang kita masukkan pada saat pemanggilan fungsi akan dikonversi menjadi list atau dictionary
# karena tipe data list dan dictionary bisa menyimpan banyak data, artinya kita bebas memasukkan data atau menuliskan argument sebanyak yang kita mau


def cetak_list(*list):
    print(list)  # jika kita ingin melihat isinya maka akan berupa list
    for item in list:
        print(item)
        
cetak_list(1,2,3,4,5)
cetak_list('Luna', 'Lucia', 'Zidane')


def cetak_dict(**dict):
    print(dict)  # jika kita ingin meilhat isinya maka akan berupa dictionary
    for key, value in dict.items():
        print(f"{key}: {value}")        

# karena tipe datanya berupa dictionary
# maka kita harus memasukkan sebuah 'key' untuk dijadikan key unik
cetak_dict(nama='Luna', umur='19', kota='Tangerang')
