'''menulis ke file (write)'''
# untuk menulis ke file, kita bisa menggunakan fungsi write('string')
# perlu diperhatikan, file yang sudah ditutup (close) tidak bisa ditulis lagi
# jika ingin menulis lagi maka perlu membuka filenya lagi

print("=== SIMPAN DATA NILAI ===")

file = open('nilai_siswa.txt', 'w') # cara membuka filenya

while True:
    nama = input("Masukkan nama (enter untuk selesai): ")
    if nama == '':
        break
    
    nilai = input("Nilai: ")
    
    # tulis ke dalam file eksternal (file txt)
    file.write(f"{nama},{nilai}\n")    # cara menulis atau menyimpan datanya
    print(f"Data {nama} berhasil disimpan!")
    
file.close()    # jangan lupa kita tutup file yang dibuka tadi dengan menggunakan fungsi 'close'
# fungsi dari menutup file adalah agar file yang terbuka tadi bisa tertutup dan menyimpan data yang kita masukkan
# jika kita tidak menutup file-nya, maka filenya akan tetap terbuka dan menghabiskan resource
print('Semua data berhasil disimpan ke nilai_siswa.txt')
    