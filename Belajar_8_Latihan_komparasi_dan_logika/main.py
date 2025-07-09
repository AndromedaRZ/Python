# Latihan Komparasi dan Logika

# Membuat gabungan area rentang dari angka

# kurang dari 3 dan lebih dari 10
# +++++3-----10+++++

inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih dari 10: "))

# +++++3------------
# Memeriksa apakah inputUser memasukkan angka kurang dari 3
isKurangDari = inputUser < 3
print("Kurang dar 3: ",isKurangDari)

# ---------10+++++
# Memeriksa apakah inputUser memasukkan angka lebih dari 10
isLebihDari = inputUser > 10
print("Lebih dari 10: ",isLebihDari)

# Menggabungkan kedua kondisi
# +++++3-----10+++++
# Kondisi akan True jika salah satu dari kondisi isKurangDari atau isLebihDari bernilai True
# Jika kedua kondisi bernilai False, maka isCorret akan bernilai False
isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan: ", isCorrect)

print("\n",15*"=","\n")
# -----3+++++10-----
# Memeriksa apakah inputUser memasukkan angka di antara 3 dan 10 atau kasus irisan

inputUser = float(input("Masukkan angka yang bernilai di antara 3 dan 10: "))

# -----3++++++++++
# Lebih dari angka 3

isLebihDari = inputUser > 3
print("Lebih dari 3: ", isLebihDari)

# +++++++++10-----
# Kurang dari angka 10

isKurangDari = inputUser < 10
print("Kurang dari 10: ", isKurangDari)

# Menggabungkan kedua kondisi
# -----3+++++10-----
# Kondisi akan True jika kedua kondisi isLebihDari dan isKurangDari bernilai True

isCorrect = isLebihDari and isKurangDari
print("Angka yang anda masukkan: ", isCorrect)

