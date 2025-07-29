# Operator Assignment: Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 10 # adalah assignment
print(f"nilai a = {a}")

# contoh penyingkatan yang umum digunakan yaitu pada operasi artimatika

# operasi penjumlahan 
a += 5 # artinya adalah a = a + 5
print(f"nilai a += 5, nilai a menjadi {a}\n")

# operasi pengurangan
a -= 5 # artinya adalah a = a - 5
print(f"nilai a -= 5, nilai a menjadi {a}\n")

# operasi perkalian
a *= 5 # artinya adalah a = a * 5
print(f"nilai a *= 5, nilai a menjadi {a}\n")

# operasi pembagian
a /= 5 # artinya adalah a = a / 5
print(f"nilai a /= 5, nilai a menjadi {a}\n")

b = 20
print(f"nilai b = {b}")

# operasi modulus
b %= 3 # artinya adalah b = b % 3
print(f"nilai b %= 3, nilai b menjadi {b}\n")

# operasi floor division
b = 10
print(f"nilai b = {b}")
b //= 3 # artinya adalah b = b // 3
print(f"nilai b //= 3, nilai b menjadi {b}\n")


# operasi eksponen
a = 5
print(f"nilai a = {a}")
a **= 3 # artinya adalah a = a ** 3
print(f"nilai a **= 3, nilai a menjadi {a}\n")


# operasi bitwise 
# OR
c = True
print(f"nilai c = {c}")
c |= False # artinya adalah c = c | False
print(f"nilai c |= False, nilai c menjadi {c}")

c = False
print(f"nilai c = {c}") 
c |= False # artinya adalah c = c | False
print(f"nilai c |= False, nilai c menjadi {c}\n")

# AND
c = True
print(f"nilai c = {c}")
c &= False # artinya adalah c = c & False
print(f"nilai c &= False, nilai c menjadi {c}")

c = True
print(f"nilai c = {c}")
c &= True # artinya adalah c = c & True
print(f"nilai c &= True, nilai c menjadi {c}\n") 

# XOR
c = True
print(f"nilai c = {c}")
c ^= False # artinya adalah c = c ^ False
print(f"nilai c ^= False, nilai c menjadi {c}")

c = True
print(f"nilai c = {c}")
c ^= True # artinya adalah c = c ^ True
print(f"nilai c ^= True, nilai c menjadi {c}\n")

# operasi bitwise shift
d = 0b0100
print(f"nilai d = {format(d, '04b')}")
d >>= 2 # artinya adalah d = d >> 2
print(f"nilai d >>= 2, nilai d menjadi {format(d, '04b')}\n")

print(f"nilai d = {format(d, '04b')}")
d <<= 1 # artinya adalah d = d << 1
print(f"nilai d <<= 1, nilai d menjadi {format(d, '04b')}\n")

