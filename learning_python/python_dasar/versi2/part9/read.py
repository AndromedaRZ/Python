'''membaca dari file (read)'''
# untuk membaca dari file, kita bisa menggunakan function (read), function ini akan mengembalikkan seluruh isi file
# namun jika kita ingin membaca hanya sebaris atau sebagian datanya saja, kita bisa melakukan iterasi dengan menggunakan fungsi for

print("=== MENAMPILKAN DATA NILAI ===")

file = open("nilai_siswa.txt", 'r') # cara membaca file menggunakan mode 'r'

for line in file:   # iterasi menggunakan for untuk melihat isi dari filenya
    data = line.strip().split(',')
    print(data[0], ':', data[1])
    
file.close()    # jangan lupa untuk menutup filenya menggunakan fungsi 'close'
print("=== SELESAI ===")