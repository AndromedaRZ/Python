'''
7) **KWARGS PADA FUNGSI

**kwargs adalah singkatan dari keyword arguments, kalau *args menampung banyak nilai tanpa nama, maka **kwargs menampung banyak nilai dengan nama (keyword arguments), hampir sama seperti pasangan key-value pada dictionary. Nilai yang masuk ke dalam kwargs akan otomatis berubah menjadi diction
'''

# contoh fungsi biasa
def fungsi(nama, tinggi, berat):
    '''fungsi data tinggi dan berat'''
    print(f"Nama = {nama}, Tinggi = {tinggi}, Berat = {berat}")
    
fungsi("Rizky", 160, 40)

# contoh penggunaan **kwargs
def fungsi(**kwargs): # cara menggunakan **kwargs adalah dengan menggunakan dua simbol bintang (**) di depan parameter pada fungsi yang kita buat, namanya juga tidak harus kwargs, kita juga bisa menggunakan nama lain karena kwargs didefinisikan menggunakan dua simbol bintang di depan parameternya
    '''fungsi data tinggi dan berat menggunakan **kwargs'''
    print(type(kwargs))
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f'Nama = {nama}, Tinggi = {tinggi}, Berat = {berat}')
    
fungsi(nama = "Doni", tinggi = 165, berat = 55) # saat kita memanggil fungsinya, kita juga harus menentukan key dari value yang kita masukan seperti contoh ini, kita memasukan nilai "Doni" ke dalam key "nama" yang ada di dalam kwargs

# kita juga bisa menambahkan pasangan key-valuenya secara bersamaan di luar fungsinya
def keranjang(**buah):
    '''fungsi menyimpan buah berdasarkan warna buahnya'''
    print(buah)
    
keranjang(orange="orange", merah="apel", hijau="melon", kuning="pisang")

# kita juga bisa mengkses **kwargs menggunakan cara yang sama seperti mengakses dictionary seperti contoh membuat loop di bawah ini
def ibukota(**negara):
    '''fungsi menyimpan data berbagai negara'''
    for key, value in negara.items():
        print(f"{key} = {value}")
        
ibukota(indonesia="Ikn", malaysia="Kuala lumpur", amerika="Washington d.c.", russia="moscow")


# studi kasus penggunaan **kwargs

'''
note: saat memasukan parameter ke dalam fungsi, kita harus menyesuaikan urutannya agar tidak mengalami error, berikut urutan penulisan parameter dalam fungsi di mulai dari sebelah kiri:
1. parameter biasa
2. *args
3. **kwargs
'''

# membuat biodata mahasiswa singkat menggunakan **kwargs
def biodata(**data):
    '''fungsi membuat biodata singkat'''
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")

biodata(nama="Rizky", umur=18, jurusan="Informatika", hobi="Membaca")

# menggabungkan parameter biasa dengan **kwargs
def sapa(nama, **ucapan): # karena parameter biasa yang di sebelah kiri, maka saat pemanggilan fungsinya harus memasukan argumen ke parameter tersebut terlebih dahulu
    '''fungsi menyapa seseorang dengan menggunakan kalimat yang berbeda'''
    for key, value in ucapan.items():
        print(f"{value} {nama} -> ({key})") # 

sapa("Rizky",pagi="Selamat pagi!", siang="Selamat siang!", sore="Selamat sore!") # saat pemanggilan fungsinya, kita harus menyesuaikan posisi saat memasukan argumen dan pasangan key-value untuk **kwargsnya

# menggabungkan *args dan *kwargs

# sistem struk pembayaran di supermarket

def struk(*barang, **detail):
    '''fungsi membuat sebuah struk pembelian di supermarket'''
    print("\n=== Daftar Pembelian ===")
    for i, item in enumerate(barang):
        print(f"{i+1}. {item}")
        
    print("\n=== Detail Pembelian ===")
    for key, value in detail.items():
        print(f"{key.capitalize()} = {value}")

# saat fungsinya dipanggil, kita harus menyesuaikan urutan pemanggilan fungsi sesuai aturannya, seperti contoh di bawah ini kita memanggil *args terlebih dahulu, dilanjutkan dengan memanggil **kwargsnya
struk(
    "air mineral", "tisu", "minuman kaleng", "teh kotak",
    nama="Rizky",
    pembayaran="Gopay",
    status="dibayar"
)

# sistem aritmatika

def aritmatika(*kumpulan_angka, **operasi): # membuat sebuah data *args (kumpulan_angka) untuk menyimpan semua angka yang ingin dioperasikan dan membuat data **kwargs (operasi) untuk menyimpan semua jenis operasi aritmatika yang ingin digunakan
    output = 0 # output harus 0 karena sebagai nilai awal yang masih kosong
    if operasi["option"] == "tambah":
        for angka in kumpulan_angka:
            output += angka
    elif operasi["option"] == "kurang":
        for angka in kumpulan_angka:
            output -= angka
    elif operasi["option"] == "kali":
        output = 1
        for angka in kumpulan_angka:
            output *= angka
    elif operasi["option"] == "bagi":
        output = 1
        for angka in kumpulan_angka:
            output /= angka
            
    return output

hasil = aritmatika(10,2,9,option="tambah")
print(f"hasil pertambahan adalah = {hasil}")
hasil = aritmatika(10,2,9,option="kurang")
print(f"hasil pengurangan adalah = {hasil}")
hasil = aritmatika(10,2,9,option="kali")
print(f"hasil perkalian adalah = {hasil}")
hasil = aritmatika(10,2,9,option="bagi")
print(f"hasil pembagian adalah = {hasil}")    

# operasi aritmatika yang kita buat di atas bekerja dengan cara menghitung semua angka yang kita masukan, jadi tidak cocok jika ingin mendapatkan hasil hitungan tertentu misalkan ingin membagi angka pertama dan angka kedua      