# Operasi Logika atau Boolean

# Operasi logika atau boolean adalah operasi yang menghasilkan nilai benar (True) atau salah (False).
# Atau sering disebut tabel kebenaran atau truth table.
# Operasi ini digunakan dalam berbagai aplikasi, seperti dalam pengambilan keputusan, pemrograman, dan logika matematika.

'''
Operasi logika yang umum digunakan adalah:
1. NOT (tidak)
2. OR (atau)
3. AND (dan)
4. XOR (eksklusif atau)
'''

# Operasi NOT
# Operasi NOT adalah operasi yang membalikkan nilai boolean.
print("\n==== NOT ====")
a = True
c = not a # Membalikkan nilai True menjadi False, begitu juga sebaliknya jika a adalah False
print(f"data a: {a}")
print("========== NOT")
print(f"data c: {c}")

# Operasi OR
# Operasi OR adalah operasi yang menghasilkan True jika salah satu nilainya atau keduanya True.
print("\n==== OR ====")
a = False
b = False
c = a or b  
print(f"{a} OR {b} = {c}")
a = False
b = True
c = a or b  
print(f"{a} OR {b}  = {c}")
a = True
b = False
c = a or b
print(f"{a}  OR {b} = {c}")
a = True
b = True
c = a or b  
print(f"{a}  OR {b}  = {c}")

# Operasi AND
# Operasi AND adalah operasi yang menghasilkan True jika kedua nilainya True.
print("\n==== AND ====")
a = False
b = False
c = a and b
print(f"{a} AND {b} = {c}")
a = False
b = True
c = a and b  
print(f"{a} AND {b}  = {c}")
a = True
b = False
c = a and b  
print(f"{a}  AND {b} = {c}")
a = True
b = True
c = a and b
print(f"{a}  AND {b}  = {c}")

# Operasi XOR
# Operasi XOR adalah operasi yang menghasilkan True jika salah satu nilainya True, sisanya False.
print("\n==== XOR ====")
a = False
b = False
c = a ^ b 
print(f"{a} XOR {b} = {c}")
a = False
b = True
c = a ^ b
print(f"{a} XOR {b}  = {c}")
a = True
b = False
c = a ^ b
print(f"{a}  XOR {b} = {c}")
a = True
b = True
c = a ^ b
print(f"{a}  XOR {b}  = {c}")
