# Dokumentasi function pada python remake

'''
1) PENGENALAN FUNGSI

Function atau fungsi dalam python adalah sekumpulan kode yang dibuat untuk menjalankan tugas tertentu, dan bisa dipakai berulang-ulang tanpa perlu menulis ulang kodenya, jadi bisa kita manfaatkan untuk kode yang akan dijalankan berulang kali
'''

# cara membuat sebuah fungsi
def nama_fungsi(): # fungsi diawali dengan 'def' yang artinya definition atau definisi
    '''ini adalah fungsi untuk mencetak sebuah string''' # <- ini namanya doc tring, jika kita tambahkan doc string ini, maka saat kita ingin menjalankan sebuah fungsi atau saat kita arahkan kursor kita pada fungsi yang ingin kita panggil, string ini akan muncul, bisa digunakan sebagai catatan untuk fungsi yang kita buat
    print("Ini adalah fungsi") # <- ini adalah fungsi yang ingin kita jalankan

# cara memanggil sebuah fungsi
nama_fungsi()

'''
2) FUNGSI DENGAN PARAMETER/INPUT/ARGUMEN

untuk menambahkan parameter, kita bisa memasukannya di dalam kurung sebelah kanan fungsi yang kita buat
'''

# contoh menambahkan parameter
def fungsi_salam(nama): # <- kita bisa menambahkan parameter di dalam kurung saat membuat fungsi ini
    '''fungsi salam untuk nama yang dimasukan user'''
    print(f"Halo!, apa kabarmu {nama}?")
    
# saat kita memanggil fungsinya, kita bisa menambahkan sebuah string atau dalam kasus ini nama yang ingin kita input, saat pemanggilan nilai dalam tanda kurung disebut argumen, bukan parameter

# contoh menambahkan argumen
fungsi_salam("Rizky") # "Rizky" adalah argumen

# contoh kasus program penjumlahan

def tambah(angka_1, angka_2): # <- kita bisa memasukan dua parameter untuk diinput oleh user
    '''fungsi penjumlahan'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
    
tambah(10, 5) # <- kita bisa memasukan dua argumen pada fungsi yang dipanggil

# menggunakan list pada fungsi

def say_hi(list_peserta): # <- kita bisa memasukan sebuah list pada parameter ini
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")
        
peserta_lomba = ["Andi", "Budi", "Clara", "Deni"] # <- list yang ingin kita masukan pada fungsi kita harus kita siapkan terlebih dahulu

say_hi(peserta_lomba)

'''
parameter = adalah nama variabel yang kita masukan di dalam tanda kurung pada saat kita membuat atau mendefiniskan fungsi
argumen = adalah nilai atau value yang kita masukan saat memanggil fungsi, nilai argumen ini akan masuk ke variabel parameter yang belum ada nilainya
'''