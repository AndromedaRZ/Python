'''error'''
# Error adalah kesalahan yang terjadi saat program berjalan
# ketika error terjadi, maka program akan berhenti dan akan menampilkan pesan error

'''1. Syntax error'''
# kesalahan sintaks
# print("Hello, World!"     
# contoh syntax error di atas, kurangnya tanda kurung untuk melengkapi suatu fungsi

'''2. Name error'''
# variabel tidak ditemukan
# print(nama)
# variabel 'nama' belum didefiniskan atau dibuat, sehingga ketika kita ingin melihat isinya akan terjadi error

'''3. Type error'''
# kesalahan tipe data
# print("5" + 5)
# kita tidak bisa menambah string dengan integer (tipe data lain)

'''4. Value errror'''
# nilai tidak valid
# angka = int('abc')
# kita tidak bisa mengonversi tipe data string jika isinya huruf "abc" menjadi integer

'''5. Index error'''
# index tidak valid/tidak ditemukan
list_data = [1,2,3]
# print(list_data[4])
# index ke-4 tidak ditemukan karena jumlah index yang ada pada list hanya sampai index ke-2

'''6. Key error'''
# key tidak valid/tidak ditemukan
data = {'Nama': 'Luna'}
# print(data['umur'])   # hasinya akan key error
# karena key 'umur' tidak ada

'''7. Zero division error'''
# terjadi ketika kita melakukan operasi pembagian dengan angka 0
# print(10 / 0)
# jika kita belajar matematika, nilai yang dibagi dengan 0 akan menjadi tak terhingga
# namun untuk kasus komputer tidak ada jawaban tak terhingga, yang akan muncul adalah error