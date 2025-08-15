# program membuat bentuk piramida menggunakan bintang

tinggi = int(input("Masukkan tinggi piramida: ")) # meminta user memasukkan tinggi dari piramida 

for i in range(1, tinggi + 1): # membuat deretan angka mulai dari angka 1 sampai 'tinggi'
    spasi = " " * (tinggi - i) # variabel 'spasi' akan membuat spasi untuk menempatkan string yang membentuk piramidanya
    string = "+" * (2 * i - 1) # variabel 'string' akan menempatkan string yang akan membentuk piramidanya 
    print(spasi + string)
#   print(i)
