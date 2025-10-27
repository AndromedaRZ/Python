# fungsi dengan return

'''fungsi dengan kembalian'''

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#    badan fungsi
#    return output

# fungsi kuadrat
def kuadrat(input_angka):
    '''fungsi kuadrat'''
    output_kuadrat = input_angka ** 2
    return output_kuadrat

print('fungsi kuadrat')
y = kuadrat(5)
print(y)

print(kuadrat(7))

# dibuat lebih rumit
z = 10 + kuadrat(7)
print(z)

# modulus
def modulus(angka1, angka2):
    '''fungsi modulus'''
    hasil = angka1 % angka2
    return hasil

print("\nfungsi modulus")
x = modulus(10, 3)
print(x)

# fungsi tambah
# kita juga bisa langsung menambahkan return tanpa membuat variabel baru terlebih dahulu
def fungsi_tambah(angka_1, angka_2):
    '''fungsi return dengan multi input'''
    return angka_1 + angka_2

print('\nfungsi tambah')
a = fungsi_tambah(5, 25)
print(a)

# fungsi dengan return banyak
def operasi_matematika(angka_1, angka_2):
    tambah = angka_1 + angka_2 
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    return tambah, kurang, kali, bagi

print('\nfungsi dengan return banyak')

b, c, d, e = operasi_matematika(9, 5)
print(f'Hasil tambah = {b}')
print(f'Hasil kurang = {c}')
print(f'Hasil kali = {d}')
print(f'Hasil bagi = {e}')
    