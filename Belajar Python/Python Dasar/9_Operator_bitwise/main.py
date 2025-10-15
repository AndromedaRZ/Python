# Operasi Bitwise > Operasi biner
# Operasi bitwise adalah operasi yang dilakukan pada level bit dari bilangan biner
# Python menyimpan angka dalam bentuk biner (basis 2 seperti 1 dan 0) bukan desimal (basis 10)

# Beberapa contoh operator bitwise diantaranya:
# 1. OR (|)
# 2. AND (&)
# 3. XOR (^)
# 4. NOT (~)
# 5. Shift Left (<<)
# 6. Shift Right (>>)

a = 9
b = 5

# Contoh penggunaan operator bitwise OR (|)
# Cara kerja OR: jika salah satu bit dari kedua perbandingan adalah 1, maka hasilnya 1
c = a | b 
print(f"\n==========OR==========")
print(f"nilai : {a} , biner : {format(a, '08b')}")
print(f"nilai : {b} , biner : {format(b, '08b')}")
print("-------------------------------- (|)")
print(f"hasil : {c} , biner : {format(c, '08b')}")

# Contoh penggunaan operator bitwise AND (&)
# Cara kerja AND: jika kedua bit dari kedua perbandingan adalah 1, maka hasilnya 1
c = a & b 
print(f"\n==========AND==========")
print(f"nilai : {a} , biner : {format(a, '08b')}")
print(f"nilai : {b} , biner : {format(b, '08b')}")
print("-------------------------------- (&)")
print(f"hasil : {c} , biner : {format(c, '08b')}")

# Contoh penggunaan operator bitwise XOR (^)
# Cara kerja XOR: jika salah satu bit dari kedua perbandingan adalah 1, tetapi tidak keduanya, maka hasilnya 1
c = a ^ b 
print(f"\n==========XOR==========")
print(f"nilai : {a} , biner : {format(a, '08b')}")
print(f"nilai : {b} , biner : {format(b, '08b')}")
print("-------------------------------- (^)")
print(f"hasil : {c} , biner : {format(c, '08b')}")

# Contoh penggunaan operator bitwise NOT (~)
# Cara kerja NOT: membalikkan setiap bit dari bilangan biner, 1 menjadi 0 dan 0 menjadi 1
c = ~a  
print(f"\n==========NOT==========")
print(f"nilai : {a} , biner : {format(a, '08b')}")
print("-------------------------------- (~)")
print(f"hasil : {c} , biner : {format(c, '08b')}")

# contohnya jika a = 9 (biner: 00001001)
# maka NOT a = ~9 (biner: 11110110) yang merupakan representasi dari -10 dalam bilangan desimal
# Operator Shifting, adalah operator yang menggeser bit ke kiri atau ke kanan

# Contoh penggunaan operator bitwise Shift right (>> )
# Cara kerja Shift right: menggeser bit ke kanan, menghilangkan bit paling kanan
c = a >> 2
print(f"\n==========Shift Right==========")
print(f"nilai : {a} , biner : {format(a, '08b')}")
print("-------------------------------- (>>)")
print(f"hasil : {c} , biner : {format(c, '08b')}")

# Contoh penggunaan operator bitwise Shift left (<< )
# Cara kerja Shift left: menggeser bit ke kiri, menambahkan bit 0 di sebelah kanan  
c = a << 2
print(f"\n==========Shift Left==========")
print(f"nilai : {a} , biner : {format(a, '08b')}")
print("-------------------------------- (<<)")
print(f"hasil : {c} , biner : {format(c, '08b')}") 


