# Operasi Komparasi
# Setiap hasil dari operasi komparasi akan menghasilkan nilai boolean (True/False)

'''
Operasi komparasi yang tersedia:
1. Lebih besar dari (>)
2. Lebih kecil dari (<)
3. Sama dengan (==)
4. Tidak sama dengan (!=)
5. Lebih besar dari atau sama dengan
6. Lebih kecil dari atau sama dengan
'''

a = 4
b = 2

print("\nOperasi Komparasi\n")

# Lebih besar dari (>)
print("=========  Lebih besar dari ( > )  ==========")
hasil = a > 3
print(f"{a} > 3: {hasil}") # Hasilnya True karena angka 4 lebih besar dari angka 3
hasil = b > 3
print(f"{b} > 3: {hasil}") # Hasilnya False karena angka 2 tidak lebih besar dari angka 3
hasil = b > 2
print(f"{b} > 2: {hasil}") # Hasilnya False karena angka 2 tidak lebih besar dari angka 2, akan True jika menggunakan lebih besar sama dengan (>=)

# Lebih kecil dari (>)
print("=========  Lebih kecil dari ( < )  ==========")
hasil = a < 3
print(f"{a} < 3: {hasil}") # Hasilnya False karena angka 4 Tidak lebih kecil dari angka 3
hasil = b < 3
print(f"{b} < 3: {hasil}") # Hasilnya True karena angka 2 lebih kecil dari angka 3
hasil = b < 2
print(f"{b} < 2: {hasil}") # Hasilnya False karena angka 2 tidak lebih kecil dari angka 2, akan True jika menggunakan lebih kecil sama dengan (<=)

# Sama dengan (==)
print("===========  Sama dengan ( == )  ============")
hasil = a == 3
print(f"{a} == 3: {hasil}") # Hasilnya False karena angka 4 tidak sama dengan angka 3
hasil = b == 3
print(f"{b} == 3: {hasil}") # Hasilnya False karena angka 2 tidak sama dengan angka 3
hasil = b == 2
print(f"{b} == 2: {hasil}") # Hasilnya True karena angka 2 sama dengan angka 2

# Tidak sama dengan (!=)
print("========  Tidak sama dengan ( != )  =========")
hasil = a != 3
print(f"{a} != 3: {hasil}") # Hasilnya True karena angka 4 tidak sama dengan angka 3
hasil = b != 3
print(f"{b} != 3: {hasil}") # Hasilnya True karena angka 2 tidak sama dengan angka 3
hasil = b != 2
print(f"{b} != 2: {hasil}") # Hasilnya False karena angka 2 sama dengan angka 2

# Lebih besar sama dengan dari (>=)
print("====  Lebih besar sama dengan dari ( >= )  ====")
hasil = a > 3
print(f"{a} >= 3: {hasil}") # Hasilnya True karena angka 4 lebih besar dari angka 3
hasil = b >= 3
print(f"{b} >= 3: {hasil}") # Hasilnya False karena angka 2 tidak lebih besar dari ataupun sama dengan angka 3
hasil = b >= 2
print(f"{b} >= 2: {hasil}") # Hasilnya True karena angka 2 sama dengan angka 2

# Lebih kecil sama dengan dari (<=)
print("====  Lebih kecil sama dengan dari ( <= )  ====")
hasil = a <= 3
print(f"{a} <= 3: {hasil}") # Hasilnya False karena angka 4 tidak lebih kecil dari ataupun sama dengan angka 3
hasil = b <= 3
print(f"{b} <= 3: {hasil}") # Hasilnya True karena angka 2 lebih kecil dari angka 3
hasil = b <= 2
print(f"{b} <= 2: {hasil}") # Hasilnya True karena angka 2 sama dengan angka 2