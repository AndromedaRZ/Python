'''with statement (direkomendasikan)'''
# saat membaca/menulis filem kita harus berhati-hati karena misalnya terjadi error dan kita lupa atau belum menutup filenya menggunakan 'close()'
# maka aplikasi kita bisa terjadi 'Memory Leak' (kondisi dimana informasi file masih ada di memory aplikasi, padahal kita sudah tidak menggunakan file tersebut)
# Memory Leak sangat berbahaya karena penggunaan memori aplikasi kita akan semakin besar tanpa kita sadari
# with statement memastikan file otomatis tertutup, bahkan jika terjadi error
# dengan menggunakan 'with' statement, kita tidak perlu khawatir lupa untuk menutup file menggunakan 'close()'

print('=== MENAMPILKAN DATA NILAI ===')

with open('nilai_siswa.txt', 'r') as file:  # as <nama variabel>, jadi as digunakan untuk memasukkan data yang diambil ke variabel
    for line in file:
        data = line.strip().split(',')
        print(f"{data[0]}: {data[1]}")

# bisa dilhat di atas kita tidak menggunakan fungsi close untuk menutup filenya
# karena jika kita menggunakan 'with', maka kita tidak perlu menggunakan fungsi close karena ia akan menutup filenya secara otomatis

'''error handling untuk file'''
# walaupun file akan selalu tertutup dengan otomatis menggunakan with statement, tapi jika terjadi error, maka aplikasi akan tetap berhenti
# oleh karena itu, kita perlu menggunakan try-except
# tapi bagaimana jika file yang kita baca ternyata tidak ada?
# maka akan terjadi error, seperti FileNotFound Error

print('=== MENAMPILKAN DATA NILAI ===')
try:
    with open('nilai_siswa2.txt', 'r') as file:  # as <nama variabel>, jadi as digunakan untuk memasukkan data yang diambil ke variabel
        for line in file:
            data = line.strip().split(',')
            print(f"{data[0]}: {data[1]}")
except FileNotFoundError:
    print("File tidak ditemukan")
        
print("=== SELESAI ===")