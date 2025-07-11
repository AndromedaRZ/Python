# Latihan komparasi dan logika 2

# Buatlah program yang meminta pengguna memasukkan angka dengan rentang seperti berikut:
# 1. -----0+++++5-----8+++++11-----
# 2. +++++0-----5+++++8-----11+++++

# Soal 1
'''
Buatlah program yang meminta pengguna memasukkan angka dengan rentang lebih dari 0, kurang dari 5, lebih dari 8, dan kurang dari 11.
'''

inputUser = float(input('Masukkan angka yang ditetapkan: '))

# Lebih dari 0
isLebihdari0 = inputUser > 0
print('Lebih dari 0:', isLebihdari0)

# Kurang dari 5
isKurangdari5 = inputUser < 5
print('Kurang dari 5:', isKurangdari5)
 
# Lebih dari 8
isLebihdari8 = inputUser > 8
print('Lebih dari 8:', isLebihdari8)

# Kurang dari 11
isKurangdari11 = inputUser < 11
print('Kurang dari 11:', isKurangdari11)

# Menggabungkan kondsi

isCorrect = (isLebihdari0 and isKurangdari5) or (isLebihdari8 and isKurangdari11)
print("data yang anda masukkan: ", isCorrect)

