# belajar function

'''fungsi tanpa parameter (fungsi dasar)'''
def halo(): # fungsi tanpa argument dan parameter
    '''fungsi untuk menampilkan halo'''
    print("Halo semuanya! Selamat datang di dunia!")
    
halo() # kita bisa langsung memanggilnya tanpa mengisi argumentnya
# dan kita tidak perlu menggunakan print() untuk memanggil isinya ketika fungsi tersebut tidak memiliki parameter

'''fungsi dengan parameter'''
def tambah(angka1, angka2): # fungsi dengan 2 parameter
    return angka1 + angka2 # maka kita harus menambahkan return agar output dari fungsi ini bisa terlihat
    # tanpa 'return' maka output yang muncul akan menjadi none

print(tambah(10,5)) # lalu pada saat pemanggilan fungsinya, kita harus mengisi posisi parameter yang ada dengan nilai yang diinginkan

'''fungsi dengan default parameter'''
def sapa(nama="User"): # pada paramternya, kita tambahkan '=' dan nilai default yang kita inginkan
    # untuk apa nilai default itu? Nilai default akan muncul ketika kita mengosongkan parameter pada saat pemanggilan fungsinya
    print(f"Halo {nama}, bagaimana kabar anda?")
    
sapa() # mengosongkan parameter, yang artinya outputnya akan mengeksekusi parameter default
sapa("Dudung") # parameternya terisi, yang artinya outputnya akan menampilkan parameter yang kita masukkan

# fungsi sapa yang pertama akan menampilkan "Halo 'User'"" sebagai nilai defaultnya
# sedangkan fungsi sapa yang kedua akan menampilkan "Halo 'Dudung" karena Dudung kita jadikan untuk mengisi parameter yang kosong

'''fungsi dengan *args (jumlah argument tidak tetap)'''
def jumlahkan(*angka): # tambahkan satu simbol '*' di depan nama parameternya untuk menunjukkan bahwa itu adalah sebuah *args
    print(type(angka)) # hasil pengelompokkan data yang masuk ke dalam *args akan berupa tuple
    return sum(angka) # pada fungsi ini, kita bisa menjumlahkan semua angka yang masuk ke dalam parameter tersebut

print(jumlahkan(10,5,6,1,3)) # ketika memanggil fungsinya, kita bisa mengisi paramternya sebanyak yang kita mau

'''fungsi dengan key dan value (**kwargs = keyword args)'''
def info_produk(**kwargs): # tambahkan dua simbol '*' di depan nama parameternya untuk menunjukkan bahwa itu sebuah **kwargs
    print(type(kwargs)) # hampir mirip dengan *args, hasil pengelompokkan data yang masuk ke dalam **kwargs akan berupa dictionary
    print(kwargs)
    for key, value in kwargs.items(): # maka kita bisa melakukan operasi pada dictionary tersebut
        print(f"{key}: {value}")

hasil = info_produk(nama="Laptop", harga=7000000, stok=10) # ketika memanggil fungsinya, isi parameternya sebagai key dan value dari dictionarynya

'''fungsi dengan lambda (anonim)'''
angka = [1,3,6,2,8,4,9]
urut = sorted(angka, key=lambda x: x) # menyortir list berisi angka pada variabel 'angka' menggunakan lambda
print(urut)


# percobaan *args dan **kwargs

def belajar_args(*args):
    print(args, type(args))
    data_list = list(args)
    # print(data_list, type(args))
    return data_list
    
# nama = "ricky"
# tinggi = 160
# berat = 40

nama = input("Masukkan nama: ")
tinggi = input("Masukkan tinggi: ")
berat = input("Masukkan berat: ")
print(belajar_args(nama, tinggi, berat))

def belajar_kwargs(**kwargs):
    print(kwargs, type(kwargs))
 
print(belajar_kwargs(nama = nama, tinggi = tinggi, berat = berat))