class Mangga:
    # magic method
    # method yang sudah memiliki keyword bawaan python dan bisa kita gunakan kembali
    # contoh pertamanya adalah yang sering kita gunakan, yaitu __init__
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah
        
    # contoh yang kedua
    def __repr__(self):
        return f"Debug - Mangga {self.nama} dengan jumlah {self.jumlah}"
        # berguna ketika kita menggunakan fungsi 'print()' pada suatu object secara langsung
        # maka __repr__ ini akan tereksekusi
        # jika kita tidak menggunakan repr, maka outputnya berubah menjadi defult yang menampilkan sekumpulan kode acak
        
    # contoh yang ketiga
    def __str__(self):
        return f"Mangga {self.nama} dengan jumlah {self.jumlah}"
        # fungsinya hampir mirip seperti __repr__
        # hanya saja, __str__ biasa digunakan ketika kode yang kita program sudah jadi
        # sedngkan __repr__ biasa digunakan untuk tujuan debugging
    
    # contoh magic method terakhir yang bisa dikenalkan
    def __add__(self, objek):
        return self.jumlah + objek.jumlah
        # berfungsi untuk melakukan suatu operasi aritmatika
        # pada kasus ini kita menjumlahkan jumlah masing-masing setiap objek
        # tergantung apa yang kita inginkan untuk dijumlahkan
    
    
    @property
    def __dict__(self):
        return "Objek ini mempunyai nama dan jumlah"
        # pada kasus penggunaan keyword dari method bawaan __dict__ diatas
        # kita perlu menambahkan decorator, yaitu @property

belanja1 = Mangga('Arumanis', 10)
belanja2 = Mangga('Manalagi', 30)
belanja3 = Mangga('Apel', 20)

# pada saat kita menggunakan class Mangga, maka ia akan mengeksekusi __init__ yang ada di dalam class Mangga secara otomatis

print(belanja1) # output dari repr bisa dilihat di baris ini

print(belanja2) # output ini berasal dari __str__ yang akan menimpa output dari syntax __repr__
# lalu bagaimana cara menampilan __repr__nya lagi?

print(repr(belanja3)) # kita bisa menambahkan method 'repr()' pada objeknya

# sebenarnya masih banyak magic method yang tersedia yang bisa digunakan, akan tetapi tidak muat untuk menuliskan semuanya disini
# ciri-ciri dari magic method, ia menggunakan 2 underscore (garis bawah) seperti contoh di atas
# __init__
# __repr__
# __str__

print(belanja1 + belanja2)
print(belanja1.__dict__) # maka hasil dari method __dict__ akan sesuai dengan yang kita atur di atas