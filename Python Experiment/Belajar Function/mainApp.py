# belajar function

def tambah(angka1, angka2, angka3, angka4):
    '''fungsi tambah'''
    hasil = angka1 + angka2 + angka3 + angka4
    return hasil
    
    
angka = int(input("Masukkan angka pertama: "))
hasil = tambah(angka, angka, angka, angka)
print(hasil)
