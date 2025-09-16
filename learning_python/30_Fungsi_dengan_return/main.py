# fungsi dengan nilai kembalian (return value)

'''
Gambaran sederhana dari return value

y = f(x)

y = outputnya
f = nama fungsi
x = input atau argument atau parameternya

###

def fungsi(input):
    hasil = input**2 (maksudnya kuadrat)
    return hasil ----> hasil ini bisa kita analogikan sebagai 'y'
'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#     badan fungsi
#     return output

# fungsi kuadrat
                                        # fungsi kuadrat dimasukkan ke dalam variabel y sambil mengisi parameternya dengan angka 5
def kuadrat(input_angka):               # ketika angka 5 sudah masuk ke fungsinya, program akan menjalankan perintah di dalam fungsi
    '''fungsi kuadrat'''                # ketika perhitungan sudah selesai (angka yang dimasukkan menjadi hasil dari pangkat 2)
    output_kuadrat = input_angka ** 2   # dan return berfungsi untuk memunculkan hasil penjumlahan tadi
    return output_kuadrat               # saat kita nge-print variabel y, maka outputnya adalah hasil perpangkatan 2
                                        # dari angka yang dimasukkan ke dalam kuadrat()
y = kuadrat(5)                          
print(y)

# fungsi terebut juga masih bisa digunakan bahkan ketika memanipulasi operasinya
# bahkan fungsi juga bisa sangat membantu ketika kita membuat program yang kelihatan rumit menjadi lebih simpel

print(kuadrat(6))

z = 10 + kuadrat(3)
print(z)

# fungsi tambah

def fungsi_tambah(angka_1, angka_2):
    '''fungsi tambah/return dengan multi input'''
    return angka_1 + angka_2
    # ketika kita print, hasil penjumlahan akan menjadi 'None' jika kita tidak menambahkan 'return'
print(fungsi_tambah(10,30))


# fungsi dengan banyak return (banyak output)

def operasi_aritmatika(angka_1, angka_2):
    '''fungsi dengan banyak output'''
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    return kali, bagi, tambah, kurang

ka, ba, ta, ku = operasi_aritmatika(9,5)

single_v = operasi_aritmatika(9,5) # jika kita hanya menempatkan datanya di 1 variabel saja

print(single_v) # maka hasil data default-nya akan berupa tuple
print(type(single_v))

print(f"Hasil kali = {ka}")
print(f"Hasil bagi = {ba}")
print(f"Hasil tambah = {ta}")
print(f"Hasil kurang = {ku}")