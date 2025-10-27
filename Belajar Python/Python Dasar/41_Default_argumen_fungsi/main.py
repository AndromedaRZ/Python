# Default argumen fungsi

'''Default argumen, adalah nilai default dari argumen suatu function'''

# def fungsi(argumen):
# def fungsi(argumen = nilai defaultnya)

# di bawah ini adalah fungsi say_hello yang digunakan untuk menanyakan kabar seseorang menggunakan f-string
def say_hello(nama):
    '''fungsi dengan argumen default'''
    print(f"Apa kabar {nama}?")
    
say_hello("rizky") # jika kita isi argumennya, maka program akan berjalan normal
# say_hello() # tetapi jika kita tidak mengisi argumennya, maka program akan mengalami error dan tidak dapat dijalankan

# Contoh 1

# cara menambahkan default argumen adalah dengan memasukkan sama dengan (=) di sebelah kiri argumennya dan isi nilainya sesuai yang kita inginkan
def say_hello(nama = "kawan"):
    '''fungsi dengan argumen default'''
    print(f"Apa kabar {nama}?")
    
say_hello() # tidak akan error karena jika argumen ini tidak diisi, maka fungsi ini akan mengambil argumen default dari yang tadi kita buat di atas]

# Contoh 2

# menggunakan dua argumen yang dengan satunya ada argumen defaultnya
def greeting(nama, pesan = "selamat pagi"):
    '''fungsi dengan satu argumen biasa, dan satu argumen default'''
    print(f"Hai {nama}, {pesan}")
    
greeting("doni", "apa kabar?")
greeting("ucup")

# Contoh 3
def hitung_pangkat(angka, pangkat):
    '''fungsi menghitung pangkat bilangan'''
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(4,2))

# mengakses argumen fungsinya dengan memanggil argumennya, cara ini berguna jika fungsi yang kita buat punya banyak sekali argumennya
hasil = hitung_pangkat(angka = 3, pangkat = 3)
print(f'3 pangkat 3 = {hasil}')

def fungsi(input1=1, input2=2, input3=3, input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())

# akses salah satu argumen dari suatu fungsi
print(fungsi(input2=4))