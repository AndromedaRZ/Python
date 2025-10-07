## Tutorial membaca file eskternal

# Kita bisa menggunakan file eksternal sebagai database pada proyek python yang kita kerjakan

print(3*"=","Membaca file txt",3*"=")

# memasukkan sebuah data yang berasal dari file ekternal ke dalam variabel
file = open("data.txt", mode='r')

# jika kita langsung print variabelnya, maka hasilnya tidak akan bisa terbaca
# kita harus menambahkan method .read() agar bisa membaca isinyaa
# print(file.read())

print(f"Status read = {file.readable()}") # untuk mengecek apakah isi dari file tersebut bisa dibaca atau tidak
print(f"Status write = {file.writable()}") # untuk mengecek apakah isi dari file tersebut bisa ditulis atau tidak
# hasil dari pengetesan read dan write akan bersifat boolean

# membaca isi dari file secara perbaris
# print(file.readline(), end="") # membaca baris pertama
# print(file.readline(), end="") # membaca baris kedua

# membaca semua baris sebagai list
# print(file.readlines())

# ketika kita membuka file, kita bisa menutup filenya setelah digunakan agar bisa kita buka kembali ketika ingin menggunakannya kembali
print(f"Apakah file sudah ditutup = {file.closed}")
file.close() # gunakan perintah .closed() untuk menutup file eksternal
print(f"Apakah file sudah ditutup = {file.closed}")

## teknik lain untuk membuka file di Python

print('\n',3*"=","Membaca file txt dengan with",3*"=")

# dengan menggunakan with, kita bisa membuka file lalu otomatis menutupnya ketika program di dalam with selesai dieksekusi
with open("data.txt", mode='r') as file:
    content = file.readline()
    print(content, end='')
    print(f"Apakah file sudah ditutup = {file.closed}") # program di dalam with, hasilnya akan False
    
print(f"Apakah file sudah ditutup = {file.closed}") # program di luar with, hasilnya akan otomatis menjadi True
