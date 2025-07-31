# operator dalam bentuk methods

## merubah case dari string

# merubah semua huruf ke uppercase (huruf besar)

salam = "selamat siang, bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua huruf ke lowercase (huruf kecil)
ucapan = "seLamAt UlAng TaHun"
print("normal = " + ucapan)
ucapan = ucapan.lower()
print("lower = " + ucapan)

## pengecekan dengan isX method

# contoh pengecekan apakah string hanya berisi huruf kecil atau lowercase

salam = "selamat pagi"
# mengecek apakah string atau karakter dalam variabel 'salam' hanya berisi huruf kecil
check_lower = salam.islower() # method .islower() berfungsi untuk mengecek apakah semua karakter dalam variabel 'salam' adalah huruf kecil atau tidak, jika iya maka hasilnya adalah True, jika tidak maka hasilnya adalah False, keduanya merupaka tipe data boolean
print(f"'{salam}' is lower = {str(check_lower)}") # variabel 'check_lower' harus di casting ke string agar bisa diprint karena hasil sebelumnya adalah boolean

check_upper = salam.isupper() # method .isupper() berfungsi untuk mengecek apakah semua karakter dalam variabel 'salam' adalah huruf besar atau tidak, jika iya maka hasilnya adalah True, jika tidak maka hasilnya adalah False, keduanya merupaka tipe data boolean
print(f"'{salam}' is upper = {str(check_upper)}") # variabel 'check_upper' harus di casting ke string juga agar bisa diprint karena hasil sebelumnya adalah boolean

# contoh lainnya isX method

'''
isalpha() = untuk mengecek apakah string hanya berisi huruf
isalnum() = untuk mengecek apakah string hanya berisi angka dan huruf (alphanumeric)
isdecimal() = untuk mengecek apakah string hanya berisi angka
isspace() = untuk mengecek apakah ada string kosong seperti spasi, tab, atau newline (\n)
istitle() = untuk mengecek apakah setiap kata dalam string dimulai dengan huruf besar
'''


