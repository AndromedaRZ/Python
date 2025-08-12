# Contoh penggunaan operasi bitwise

# Mengecek apakah bit tertentu dalam suatu angka aktif atau tidak
# contoh:

# Soal 1
print("Soal ke-1:")
print("pada sebuah angka desimal dengan nilai 13, tentukan angka biner nya, dan cek apakah bit ke-5 aktif atau tidak (1 atau 0)")

angka = 13 # biner: 00001101
'''
penjelasan urutan angka biner
angka = 13
biner = 00001101

urutan bit dari kanan ke kiri:
bit ke-0: 1
bit ke-1: 0
bit ke-2: 1
bit ke-3: 1
bit ke-4: 0
bit ke-5: 0
bit ke-6: 0
bit ke-7: 0
'''

mask = 1 << 5 # menggeser angka 1 ke kiri sebanyak posisi bit yang mau dicek
print(f"bilangan desimal : {angka}")
print(f"bilangan biner   : {format(angka, '08b')}")
print(f"bilangan mask    : {format(mask, '08b')}")
if angka & mask: # membandingkan biner angka dan biner mask agar bisa mencocokan posisi bit yang ingin dicek
    print("bit ke-5 aktif") # kalau aktif (nilainya 1)
else:
    print("bit ke-5 tidak aktif") # kalau tidak aktif (nilainya 0)


