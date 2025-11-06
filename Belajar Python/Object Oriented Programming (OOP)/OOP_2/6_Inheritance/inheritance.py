'''
Apa itu Inheritance? (Pewarisan)
- Inheritance adalah kemampuan untuk membuat class baru berdasarkan class yang sudah ada
- Class baru (child/subclass) mewarisi properties dan methods dari class lama (parent/superclass), dan bisa menambahkan atau mengubah functionality atau fungsinya

Analogi Dunia Nyata
- Kendaraan (parent) -> Mobil, Motor, Pesawat (children)
- Hewan (parent) -> Anjing, Kucing, Burung (children)
Karyawan (parent) -> Manager, Developer, Designer (children)

Keuntungan Inheritance
- Code Reuse - Tidak perlu menuliskan kode yang sama (property, methods)
- Constintency - Interface/blueprint yang sama antar class yang berelasi (terhubung)
- Maintainability - Mengubah parent class berefek ke semua children class
- Extensibility - Mudah menambah tipe baru tanpa ubah terlalu banyak kode
- Polymorphism - Memperlakukan object yang berbeda dengan interface/blueprint yang sama


Function super() - Akses Parent Class
- super() digunakan untuk mengakses methods dan attributes dari parent class
- super() biasanya sering digunakan untuk memanggil consctructor (__init__) di parent class

Method Overriding
- Method Overriding adalah mendefinisikan ulang method parent di child class dengan implementasi berbeda
- Saat kita melakukan method overriding, jika kita ingin memanggil method parent class yang sama, kita bisa memanfaatkan super()

'''

# class parent Kendaraan
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
        
    def info(self):
        return f"Merek: {self.merek}, Tahun: {self.tahun}, beroda {self.jumlah_roda}"
    
    def nyalakan(self):
        print(f'{self.merek} dinyalakan!')

# class child Mobil dengan mengambil parent Kendaraan
class Mobil(Kendaraan):
    
    
    def __init__(self, merek, tahun, jumlah_roda):
        # super() berfungsi untuk mengamibl attribute yang ada di class  parent
        super().__init__(merek, tahun)
        self.jumlah_roda = jumlah_roda
    
    def klakson(self):
        print(f'Mobil {self.info()} memiliki klakson')

# class child Motor dengan mengambil parent kendaraan

class Motor(Kendaraan):
    
    def klakson(self):
        print(f'Motor {self.info()} memiliki klakson')
    
    # override nama methods dari yang sudah dibuat parent class, 
    def nyalakan(self):
        print(f"Motor {self.merek} dinyalakan secara otomatis")
        
# membuat object dari subclass Mobil
avanza = Mobil('avanza', 2019, 4)
avanza.nyalakan()
avanza.klakson()

# membuat object dari subclass Motor
scoopy = Motor('scoopy', 2022)
scoopy.nyalakan()

'''
Multilevel Inheritance
- Class bisa inherit dari class yang juga sudah inherit (iheritance chain)
- Tidak ada batasan untuk inheritance
- Namun jangan terlalu banyak level pewarisannya karena akan sulit untuk di maintain dan sulit untuk dibaca kodenya
'''

# contoh multilevel inheritance
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        
        
# parent classnya Karyawan dengan child classnya KaryawanTetap
class KaryawanTetap(Karyawan): 
    pass

# parent classnya KaryawanTetap dengan child classnya Manager
class Manager(KaryawanTetap):
    pass

# parent classnya Manager dengan child classnya VicePresident
class VicePresident(Manager):
    pass

'''
Multiple Inheritance
- Di beberapa bahasa pemrograman, class tidak bisa melakukan pewarisan lebih dari satu class
- Namun di Python itu bisa dilakukan
- Perlu diingat bahwa pewarisan lebih dari satu kadang bisa berbahaya, apalagi jika terjad diamond problem
- Jadi sebisa mungkin jika memang tidak butuh melakukan pewarisan lebih dari satu class, jangan lakukan hal ini
'''

# contoh multiple inheritance

class BisaBerlari():
    def berlari(self):
        print(f"{self.name} bisa berlari")
        
class BisaBerenang():
    def berenang(self):
        print(f"{self.name} bisa berenang")
        
# sebuah child class bisa mengambil lebih dari satu parent class
class Atlit(BisaBerlari, BisaBerenang):
    def __init__(self, name):
        self.name = name
        
andi = Atlit("Andi")
andi.berlari()
andi.berenang()

'''
Multiple inheritance dapat menyebabkan diamond problem

Apa itu Diamond Problem?
- Misal kita punya class A
- Class B adalah child dari class A
- Class C adalah child dari class A
- Lalu ada class D child dari class B dan class C
- Maka bentuk relasi 4 class tersebut akan menjadi diamond problem
'''

#        A
#      /   \
#     B     C
#      \   /
#        D



# contoh diamond problem

class A:
    def method(self):
        print("Method from A")
        
class B(A):
    def method(self): # method ini akan mengoverride dari method class A
        print("Method from B") 
        
class C(A):
    def method(self): # method ini akan mengoverride dari method class B
        print("Method from C")
        
class D(B, C): # jika B yang dipanggil terlebih dahulu (dipasang di kiri) maka method B yang akan terpanggil, begitupun sebaliknya jika C yang dipanggil terlebih dahulu
    pass

d = D()
d.method()

'''
Type Checking

- isinstance(value, Type) - Cek tipe object
- Akan menghasilkan True jika Class-nya adalah Type tersebut atau Sub Class dari type tersebut
- Jika bukan Class atau Sub Class dengan Type tersebut, maka hasilnya adalah False
'''

budi = Karyawan("Budi", 4000000)
eka = KaryawanTetap("Eka", 5000000)
joko = Manager("Joko", 80000000)
fadli = VicePresident("Fadli", 12000000)

print(isinstance(budi, Karyawan)) 
print(isinstance(eka, Karyawan))
print(isinstance(joko, Karyawan))
print(isinstance(fadli, Karyawan))

# hasil keempat di atas adalah True karena masih termasuk hasil instance dari Karyawan walaupun sisanya adalah turunan atau pewarisannya

'''
Best Practice untuk inheritance

- Selalu panggil super().__init__() dalam child constructor
- Hanya override methods yang butuh behaviour berbeda
- Gunakan isinstance() untuk type checking
- Level inheritance tidak terlalu dalam (max 3-4 levels)
- Jangan override tanpa alasan yang jelas
- Jangan buat inheritance hierarchy yang terlalu kompleks
- Jangan multiple inheritance kecuali benar-benar diperlukan
'''

