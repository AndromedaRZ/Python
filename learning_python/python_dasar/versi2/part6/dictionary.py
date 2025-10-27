'''dictionary (kamus)'''
# dictionary menyimpan data dalam pasangan key-value (kunci-nilai). Dictionary ditulis dengan kurung kurawal {}
# kita perlu menentukan key dan value ketika membuat dictionary (berbeda dengan list yang menggunakan index)
# key bisa dibuat dengan berbagai macam tipe data, namun biasanya orang-orang menggunakan string untuk membuat key

siswa = {
    "nama": "Luna",     # nama adalah key-nya, sedangkan 'Luna' adalah value-nya
    "umur": 17,         # umur adalah key-nya, sedangkan 17 adalah value-nya
    "kelas": "12A"      # kelas adalah key-nya, sedangkan '12A' adalah value-nya
}

print(siswa)

# untuk mengaskes data dan mengubah value dictionary, kita bisa gunakan key dengan kurung kotak (seperti index pada list)

print(siswa['nama'])    # gunakan kurung siku dan masukkan nama key dari value yang ingin kita akses
print(siswa['umur']) 
print(siswa['kelas']) 

siswa['umur'] = 16      # gunakan kurung siku dan masukkan nama key dari value yang ingin kita ubah dan masukkan nilai yang baru
print(siswa)

# untuk menghapus value di dictionary, kita bisa menggunakan fungsi 'del'
del siswa['kelas']      # gunakan 'del' dan ketik nama dictionary beserta key yang ingin kita hapus menggunakan kurung siku
print(siswa)

# untuk mengetahui panjang data dictionary, kita bisa menggunakan fungsi len()
print(len(siswa))

# dictionary juga bisa di iterasi menggunakan perulangan for
for key in siswa:
    print(f"{key}: {siswa[key]}")
    
# mengiterasi key-value pairs
for key, value in siswa.items():
    print(key, '=', value)