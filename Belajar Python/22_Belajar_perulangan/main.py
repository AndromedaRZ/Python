# Latihan perulangan membuat segitiga

print("===Program perulangan membuat segitiga===")
sisi = int(input("Masukan tinggi segitiga: "))
count = 1 # dummy variable

# 1. Menggunakan for loop

print("\nMenggunakan for loop")
for i in range(sisi):
    print("*" * count)
    count += 1

# 2. Menggunakan while

print("\nMenggunakan while")
count = 1
while True:
    print("*" * count)
    count += 1

    if count > sisi:
        break
# 3. Hanya ganjil saja

print("\nsegitiga ganjil saja")
count = 1
while True:
    if count % 2: # akan print jika ganjil 
        print("*" * count)
        count += 1
        
    else: # akan mengskip perulangan jika genap
        count += 1
        continue

    if count > sisi: # akan menghentikan program jika nilai 'count' lebih besar dari nilai 'sisi'
        break 
