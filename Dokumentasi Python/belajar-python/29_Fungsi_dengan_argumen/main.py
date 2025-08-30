'''
Fungsi dengan argument (input)

def -> berarti definition atau mendefinisikan
lalu dilanjut dengan nama dari fungsi yang kita buat
setelah itu ada tanda kurung buka dan tutup seperti ()
bagian dalam kurung tersebut bisa kita isi yang biasanya disebut sebagai argument atu parameter atau input juga
'''


# template untuk membuat fungsi
# def nama_fungsi():
#     badan fungsi -> akan berjalan ketika fungsi dipanggil
    


# contoh


# argument dari fungsi 'hello_world()' diisi dengan variabel nama
def hello_world(nama):
    '''fungsi hello world menerima input dengan variabel nama'''
    print(f"Selamat datang dunia wahai {nama}")
    

hello_world('ucup') # maka kita harus mengisi parameter ketika memanggil fungsinya agar fungsi tersebut bisa berjalan dengan baik

# selain itu, kita juga bisa menggunakan fungsi ini untuk menjalankan suatu program sederhana

# paramter dari fungsi tambah diisi dengan dua variabel yang bisa diatur di dalam program
def tambah(angka_1, angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2 # lalu program akan menjumlahkan kedua variabel yang telah berisi angka tersebut
    print(f"{angka_1} + {angka_2} = {hasil}")
    
tambah(10,5) # kita tinggal memasukkan 2 angka yang ingin dijumlahkan ketika memanggil fungsinyaa


# contoh function lain, kita bisa melakukan hal lain juga di dalam fungsi tersebut
def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    
    for i in data_peserta:
        print(f"Yang terhormat {i}")
        
  
# kita juga menambahkan for loop di dalam fungsi say hi, sehingga parameter yang kita masukkan akan menampilkan data setiap looping sesuai dengan program yang kita buat di dalam fungsi say hi      
# fungsi say hi akan menampilkan setiap data di dalam list dari variabel yang kita masukkan ke dalam parameter fungsinya ketika kita memanggil fungsi say hi        

boyband = ['ucup','joko','dudung']

say_hi(boyband)