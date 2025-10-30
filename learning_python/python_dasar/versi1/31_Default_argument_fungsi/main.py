'''default argument'''
 
# def fungsi(argument):
# def fungsi(argument = nilai defaultnya)

# maksudnya default argument disini adalah ketika kita mengosongkan parameter atau argumentnya
# maka argument ataupun parameter terebut akan diisi oleh nilai default

# contoh 1
def say_hello(nama):
    '''fungsi dengan default argument'''
    print(f"Halo {nama}")
    
say_hello("ucup")

# say_hello() ketika argument-nya kita kosongkan seperti ini, maka output-nya akan error
# dan menampilkan kode error bahwa kekurangan 1 posisi yang dibutuhkan yaitu tidak ada yang mengisi argument nama

# alternatifnya, kita bisa sedikit mengubah parameter ketika membuat fungsinya
def say_hello_2(nama = "Ganteng"): # outputnya akan menjadi 'Ganteng' ketika kita mengosongkan aragument nama
    '''fungsi dengan default argument'''
    print(f"Halo {nama}")
    
say_hello_2("ucup")
say_hello_2()

# contoh 2
def sapa_dia(nama, pesan = 'Apa kabar?'):
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"Hai {nama}, {pesan}")
    
sapa_dia("Dudung", "Selamat pagi") # baris ini ketika kedua argument terisi
sapa_dia("Aldo") # pesan akan digantikan oleh default argument ketika dikosongkan, dan memprioritaskan argument paling depan yaitu nama yang akan menjadi outputnya

# contoh 3
def hitung_pangkat(angka, pangkat = 2):
    '''fungsi menghitung perpangkatan'''
    hasil = angka ** pangkat
    return hasil

print(hitung_pangkat(5,4))

print(hitung_pangkat(10, pangkat = 3)) # kita bisa mengakses argumentnya di luar fungsi dan mengubahnya sesuai kebutuhan kita

# contoh 4
def fungsi_banyak(input1 = 1, input2 = 2, input3 = 3, input4 = 4):
    '''fungsi dengan banyak input'''
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi_banyak())
print(fungsi_banyak(input3 = 10)) # pada beberapa studi kasus, kita juga bisa mengubah salah satu argument default sesuai yang kita inginkan ketika dihadapkan dengan banyak kemungkinan ataupun perhitungan