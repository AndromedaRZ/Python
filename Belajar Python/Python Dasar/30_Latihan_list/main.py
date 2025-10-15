# Latihan list
# program list buku

list_buku = [] # setiap buku dan penulis yang ditambahkan user akan masuk ke dalam list_buku yang awalnya kosong ini

while True:
    print("Masukan data buku")
    judul = input("Judul buku\t: ")
    penulis = input('Nama penulis\t: ')

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru) # menambahkan data baru pada 'list_buku' berdasarkan variabel 'buku_baru'
    
    print("\n","="*10, "Data Buku", 10*"=")
    print("No.| Judul \t\t| Penulis")
    for index, buku in enumerate(list_buku): # dengan fungsi enumerate, kita dapat menampilkan index dari setiap list dari dalam 'list_buku'
        print(f'{index + 1}. | {buku[0]}\t\t| {buku[1]}')
        
    isLanjut = input('Apakah dilanjutkan? [y/n]: ')
    if isLanjut == "n":
        break
    
print('PROGRAM SELESAI')
    