# fungsi / function

# singkatnya, function digunakan untuk mempersingkat kode yang biasanya dibuat panjang
# atau sama seperti namanya 'fungsi' digunakan untuk menyimpan sebuah fungsi sehingga kita tidak perlu mengulangnya berkali-kali ketika membutuhkan fungsinya

# membuat fungsi

def hello_world(): # def bisa diartikan sebagai 'definision' atau mendefinisikan lalu dilanjut dengan nama fungsi yang kita inginkan
    # fungsi menampilkan hello world
    print("Hello, World!") # di dalam indentasinya kita masukkan perintah yang kita inginkan
    
# kita juga bisa mengeluarkan isi dari fungsi tersebut dengan mengetik nama fungsinya
hello_world() # nama fungsi dipanggil dengan menambahkan kurung buka dan tutup
# pemanggilan fungsi hanya berlaku setelah baris kode untuk fungsinya dibuat sebelumnya (lihat ke baris ke-8, jadi kita tidak bisa memanggil fungsi sebelum baris ke-8)

# kita juga bisa menempatkan banyak perintah atau program ke dalam satu fungsi
# sehingga akan sangat berguna ketika kita membutuhkan sebuah program khusus
# jadi kita tidak perlu mengulang-ulang kode program yang sama, hanya cukup gunakan fungsi yang sudah kita buat

# contoh satu fungsi dengan banyak perintah di dalamnya

def fungsi():
    nama = input("Masukkan nama anda: ")
    print(nama)
    if nama == '':
        print("Nama tidak boleh kosong")
    
fungsi() # cara memanggil fungsi dengan mengetik namanya