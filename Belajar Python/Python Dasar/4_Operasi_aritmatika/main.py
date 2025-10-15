# Operasi aritmatika

a = 10
b = 3

# Operasi penjumlahan (+)
hasil = a + b
print(a, "+", b, "=", hasil)

# Operasi pengurangan (-)
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi perkalian (*)
hasil = a * b
print(a, "*", b, "=", hasil)

# Operasi pembagian (/)
hasil = a / b
print(a, "/", b, "=", hasil)
# Hasil pembagian ini akan menghasilkan float

# Operasi eksponen/pangkat (**)
hasil = a ** b
print(a, "**", b, "=", hasil)

# Operasi modulus/sisa pembagian (%)
hasil = a % b
print(a, "%", b, "=", hasil)
# Cara kerja modulus adalah mencari sisa dari pembagian a dengan b, seperti 10 % 3 = 3, maka sisanya adalah 1

# Operasi floor division (//)
hasil = a // b
print(a, "//", b, "=", hasil)
# Operasi floor division akan membulatkan hasil pembagian ke bawah, seperti 10 // 3 = 3, karena 3 * 3 = 9, dan sisa pembagiannya adalah 1, sehingga hasilnya adalah 3

# Prioritas operasi, operational precedence

# Urutan proritas operasi aritmatika:
# 1. Eksponen (**)
# 2. Perkalian (*), pembagian (/), modulus (%), dan floor division (//)
# 3. Penjumlahan (+) dan pengurangan (-)

x = 3
y = 2
z = 4

hasil = x + y * z
print(x, "+", y, "*", z, "=", hasil)
# Hasilnya adalah 3 + (2 * 4) = 3 + 8 = 11, karena perkalian memiliki prioritas lebih tinggi daripada penjumlahan

hasil = (x + y) * z
print("(", x, "+", y, ")", "*", z, "=", hasil)
# Hasilnya adalah (3 + 2) * 4 = 5 * 4 = 20, karena tanda kurung memiliki prioritas lebih tinggi daripada perkalian

hasil = x + y * z - 5
print(x, "+", y, "*", z, "-", 5, "=", hasil)
# Hasilnya adalah 3 + (2 * 4) - 5 = 3 + 8 - 5 = 6, karena perkalian memiliki prioritas lebih tinggi daripada penjumlahan dan pengurangan

hasil = x ** y * (z + x)
print(x, "**", y, "*", "(", z, "+", x, ")", "=", hasil)
# Hasilnya adalah 3 ** 2 * (4 + 3) = 9 * 7 = 63, karena eksponen memiliki prioritas lebih tinggi daripada perkalian dan tanda kurung