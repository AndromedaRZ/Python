# Database sederhana

# program rilis buku

list_buku = []

while True:
    print("\nMasukkan data buku")
    judul = input("Masukkan judul buku\t: ")
    penulis = input("Masukkan nama penulis\t: ")

    buku_baru = [judul,penulis] # input yang didapat dari variabel judul dan penulis dimasukkan ke dalam variabel baru dalam bentuk list
    list_buku.append(buku_baru) # karena di atas terdapat While True, jadi setiap perulangan akan menambahkan isi yang terdapat di dalam variabel buku baru ke dalam list_buku menggunakan .append()
    
    print("\n")
    print("-"*35)
    print("No\t| Judul Buku\t| Penulis")
    print("-"*35)
    for index,buku in enumerate(list_buku): # enumerate berfungsi untuk memunculkan index setiap loopnya di dalam for loop
        print(f"{index+1}\t| {buku[0]}\t| {buku[1]}") # kita tinggal buat printnya seperti ini dan dengan menambahkan lokasi index untuk judul dan penulis karena kedua variabel tersebut berada di dalam list_buku
        
    isLanjut = input(f"\nApakah mau dilanjutkan? [y/n]: ")
    if isLanjut == "n":
        break

print("Program selesai")