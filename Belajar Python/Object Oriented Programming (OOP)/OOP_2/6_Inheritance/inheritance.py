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


'''

# class parent Kendaraan
class Kendaraan:
    def __init__(self, merek, tahun):
        self.merek = merek
        self.tahun = tahun
        
    def info(self):
        return f"Merek: {self.merek}, Tahun: {self.tahun}"
    
    def nyalakan(self):
        print(f'{self.merek} dinyalakan!')

# class child Mobil dengan mengambil parent Kendaraan
class Mobil(Kendaraan):
    
    def identifikasi(self):
        print(f'Mobil {self.info()} beroda empat')

# class child Motor dengan mengambil parent kendaraan

class Motor(Kendaraan):
    
    def identifikasi(self):
        print(f'Motor {self.info()} beroda dua')
        
# membuat object dari subclass Mobil
avanza = Mobil('avanza', 2019)
avanza.nyalakan()
avanza.identifikasi()

# membuat object dari subclass Motor
scoopy = Motor('scoopy', 2022)
scoopy.nyalakan()
scoopy.identifikasi()