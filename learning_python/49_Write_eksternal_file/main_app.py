# 1. mode write

with open('data1.txt', 'w', encoding='utf-8') as file: # ketika melakukan 'write' file, kita perlu menambahkan encodingnya
    file.write("John si Johnny")
    
with open('data1.txt', 'w', encoding='utf-8') as file:
    file.write("Ucup Surucup")
    
# ketika kita menjalankan baris perintah write ke dalam file yang sama seperti contoh di atas
# maka isi dari file tersebut akan diisi oleh perubahan terbaru
# artinya data sebelumnya akan tertimpa dengan data yang baru (overwrite)

# sisi baiknya, ketika kita file tersebut hilang atau terhapus
# otomatis program akan membuat file baru dengan nama yang kita tulis dan isi terbaru seperti yang kita ketik

# 2. mode append
# dengan menggunakan 'append', kita bisa menambahkan isi ke dalam file yang sama dan hasilnya tidak akan tertimpa

with open('data2.txt', 'w', encoding='utf-8') as file:
    file.write("John si Johnny\n")
    # jangan lupa ketika pertama kali menambahkan data, kita perlu menggunakan 'write' terlebih dahulu
    # agar data yang ada di dalam file sebelumnya tidak menumpuk terus-menerus
    
with open('data2.txt', 'a', encoding='utf-8') as file: # mode yang tadinya ditulis 'w', kita ganti dengan 'a' yang berarti append
    file.write("Ucup Surucup\n")

with open('data2.txt', 'a', encoding='utf-8') as file:
    file.write("Otong Surotong\n")
    
# 3. mode r+
# mode r+ berguna untuk menimpa teks sesuai dengan panjang data
# memang hampir mirip dengan mode 'write'
# hanya saja pada r+ data yang ditimpa sesuai dengan data baru yang kita masukkan
# artinya data sebelumnya yang tidak terkena timpaan akan masih ada

with open('data3.txt', 'w', encoding='utf-8') as file:
    file.write('data ke-3\n')
    
with open('data3.txt', 'r+', encoding='utf-8') as file:
    file.write('baris ke-1\n')
    file.write('baris ke-2\n')
    file.write('baris ke-3\n')
    
with open('data3.txt', 'r+', encoding='utf-8') as file:
    data = file.read()
    print(data)
    
with open('data3.txt', 'r+', encoding='utf-8') as file:
    file.write('Otong Surotong\n') # menimpa isi teks sesuai dengan panjang data