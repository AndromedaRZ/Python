# Dokumentasi function pada python remake part 2

'''
3) FUNGSI DENGAN RETURN (KEMBALIAN)

fungsi juga dapat mengembalikan sebuah nilai dengan return
'''

def pangkat_bilangan(input_angka):
    '''fungsi kuadrat'''
    output = input_angka ** 2 # variabel untuk digunakan pada return
    return output # mengebalikan atau return nilai dari variabel yang kita buat

hasil = pangkat_bilangan(10) # memasukan fungsi ke dalam variabel sebelum diprint
print(f"hasil pangkat = {hasil}")

def tambah(angka_1, angka_2):
    '''fungsi penjumlahan dengan multi input'''
    return angka_1 + angka_2 # kita juga bisa langsung menggunakan return tanpa membuat sebuah variabel terlebih dahulu

hasil = tambah(10, 14)
print(f"hasil pemnjumlahan = {hasil}")

print(f"hasil penjumlahan = {tambah(9, 9)}") # kita juga bisa langsung print hasil fungsinya tanpa membuat sebuah variabel terlebih dahulu dengan cara ini

# kasus lebih rumit
z = 10 * tambah(3, 5)
print(f"hasil = {z}")

## fungsi dengan return yang banyak

def operasi_aritmatika(angka_1, angka_2):
    '''fungsi operasi aritmatika'''
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    
    return tambah, kurang, kali, bagi # kita bisa return semua variabel yang sudah kita buat

print("\nfungsi dengan return banyak")
a, b, c, d = operasi_aritmatika(10, 2)
print(f"hasil tambah = {a}") 
print(f"hasil kurang = {b}") 
print(f"hasil kali = {c}") 
print(f"hasil bagi = {d}")

'''
4) ARGUMEN DEFAULT FUNGSI

argumen default, adalah nilai default dari argumen dalam suatu fungsi
'''

# fungsi tanpa argumen default
print(f"\nfungsi tanpa argumen default")
def salam(nama):
    '''fungsi memberikan salam'''
    print(f"Halo {nama}, selamat pagi!")

salam("Otong")
# salam() # dalam fungsi tanpa argumen default, jika kita tidak memasukan apapun ke argumen saat memanggil fungsinya, maka fungsi tersebut akan mengalami error

# contoh 1, menggunakan argumen default
print(f"\nfungsi dengan argumen default")
def say_hello(nama = "kawan"): # <- cara menambahkan argumen default adalah dengan memasukan sama dengan (=) dan nilainya di sebelah kanan parameter
    '''fungsi dengan argumen default'''
    print(f"Hello, apa kabar {nama}")
    
say_hello("Rizky") # jika kita memasukan argumen saat pemanggilan fungsi, maka fungsi akan menggunakan nilai ini untuk dimasukan ke parameternya
say_hello() # jika kita tidak memasukan argumen apapun pada fungsinya, maka fungsi tidak akan error dan akan menggunakan nilai defaultnya, yaitu yang berada di sebelah kanan parameter saat kita membuat fungsinya tadi


# contoh 2, menggunakan dua argumen dengan satunya adalah argumen default dan satunya lagi argumen biasa
def salam(nama, sapa="selamat pagi!"):
    '''fungsi menyapa'''
    print(f"Hai {nama}, {sapa}")
    
salam("Doni") # argumen ke 2 tidak kita masukan karena parameter fungsinya memiliki argumen default, jadi secara otomatis akan mengambil argumen yang default
salam("Ucup", "selamat siang!") # argumen ke 2 kita masukan nilai baru, jadi argumen defaultnya akan tertimpa oleh argumen yang baru kita buat

# contoh 3
def hitung_pangkat(angka, pangkat):
    '''fungsi menghitung pangkat bilangan'''
    output = angka ** pangkat
    return output

print(hitung_pangkat(4,2))

# mengakses argumen fungsinya dengan memanggil argumennya, cara ini berguna jika fungsi yang kita buat punya banyak sekali argumennya
hasil = hitung_pangkat(angka = 3, pangkat = 3)
print(f'3 pangkat 3 = {hasil}')

def fungsi_tambah(input1=1, input2=2, input3=3, input4=4): # masing-masing setiap parameter sudah ada argumen defaultnya
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi_tambah())

# akses salah satu argumen dari suatu fungsi dan mengubah nilainya
print(fungsi_tambah(input2=4))

