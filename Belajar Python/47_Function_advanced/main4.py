'''
6) *ARGS PADA FUNGSI

*args adalah singkatan dari arguments, digunakan jika kita ingin membuat sebuah fungsi dengan banyak parameter sekaligus, dan nilai yang masuk ke dalam args akan otomatis berubah menjadi tipe data tuple
'''
# dalam contoh di bawah ini, kita membuat parameter sebanyak 3 tetapi akan repot jika harus menambah parameter lagi karena itu kita bisa menggunakan *args untuk mempermudahnya
def fungsi(nama, tinggi, berat):
    '''fungsi data diri'''
    print(f"nama = {nama}, tinggi = {tinggi}, berat = {berat}")
    
fungsi("rizky", 160, 40)


# contoh penggunaan *args
def fungsi(*args): # cara menggunakan *args adalah dengan menambahkan simbol bintang (*) di depan parameter pada fungsi yang kita buat, namanya juga tidak harus args, kita bisa menggunakan nama lain karena args didefiniskan menggunakan simbol bintang di depan parameternya
    '''fungsi data diri menggunakan *args'''
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    hobi = args[3] # jika kita ingin menambahkan parameter lagi, kita bisa menyesuaikannya dengan membuat sebuah variabel yang mengambil nilai berdasarkan input user dan *argsnya
    print(f"nama = {nama}, tinggi = {tinggi}, berat = {berat}, hobi = {hobi}")
    
fungsi("rizky", 160, 40, "membaca")

# studi kasus *args

# kita akan mencoba membuat sebuah fungsi yang menjumlahkan semua angka
def tambah(*data):
    '''fungsi menjumlahkan seluruh bilangan menggunakan *args'''
    output = 0
    for angka in data:
        output += angka
    return output

print(f"hasil = {tambah(1, 2, 4, 5)}") # dengan ini kita tidak perlu membuat banyak parameter untuk menjumlahkan angka yang banyak
    
# kasus lebih sulit
def identitas(*data):
    for i, nilai in enumerate(data, 1):
        print(f"argumen ke-{i} = {nilai}")
        
identitas("Rizky", 18, "Membaca", 160, 40) # setiap kali kita menambahkan argumen baru, maka fungsi di atas akan secara otomatis menambah parameter baru untuk argumen yang kita tambahkan
 
# fungsi campuran argumen biasa dengan *args
def say_hi(sapa, *nama):
    '''fungsi menyapa setiap orang yang berbeda'''
    for orang in nama:
        print(f"{sapa}, {orang}")
        
say_hi("Halo", "Rizky", "Ricky", "Indra") # kita bisa menamabahkan argumen yang banyak untuk parameter *argsnya