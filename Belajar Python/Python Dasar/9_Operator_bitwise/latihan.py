# Contoh latihan operator bitwise

# a = 7
# b = 5
# c = a | b

# print(f"nilai a: {a}, biner: {format(a, '08b')} ")
# print(f"nilai b: {b}, biner: {format(b, '08b')} ")
# print("------------------------------(|)")
# print(f"nilai c: {c}, biner: {format(c, '08b')} ")


# Soal no 1
a = 14  # biner: 1110
b = 9   # biner: 1001
c = a & b # AND
d = a | b # OR
print("Jawaba soal no-1")
print("AND:", a & b)
print("OR :", a | b)

print(f"nilai a: {bin(a)}")
print(f"nilai b: {bin(b)}")
print(f"nilai c: {bin(c)}") # hasil dari a & b
print(f"nilai d: {bin(d)}") # hasil dari a | b
print()
# Soal no 2
x = 7  # biner: 0111
y = x << 2
z = x >> 1
print("Jawaba soal no-2")
print("Geser kiri 2:", x << 2)
print("Geser kanan 1:", x >> 1)
print(f'''x = angka: {x}
    biner: {bin(x)}''')
print(f'''x << 2 = angka: {y}
         biner: {bin(y)}''')
print(f'''x >> 1 = angka: {z}
         biner: {bin(z)}''')
print("Kedua hasil di atas bisa didapatkan karena adanya opeator shifting")
print()
# Soal no 3

angka = 18  # biner: 10010
mask = 1 << 4
print(f"angka: {angka}, biner: {bin(angka)}")
# memeriksa apakah bit ke-4 aktif
if angka & mask:
    print("bit ke-4 aktif")
else:
    print("bit ke-4 tidak aktif")
# menyalakan bit ke-1
mask2 = 1 << 1
angka_baru = angka | mask2
print(f'angka baru: {angka_baru}, biner: {bin(angka_baru)}')

# mematikan bit ke-4
mask3 = ~(1 << 4)
angka_baru2 = angka & mask3
print(f"angka baru: {angka_baru2}, biner: {bin(angka_baru2)}")


