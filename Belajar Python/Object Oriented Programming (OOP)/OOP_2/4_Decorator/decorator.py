'''
Apa itu Decorator?
- Decorator adalah cara untuk 'membungkus' atau memodifikasi behavior dari function atau method
- Decorator ditandai dengan simbol @ diikuti nama decorator, dan ditulis di atas function/method
- Python menyediakan beberapa built-in decorators untuk OOP:
1. @staticmethod - membuat method yang tidak perlu self atau class
2. @classmethod - membuat method yang menerima class sebagai parameter pertamanya
3. @property - membuat method yang bisa diakses seperti attribute

1. STATIC METHODS - INDEPENDENT FUNCTIONS
- Static method adalah method yang berdiri sendiri secara independen
- Untuk mengakses static method, kita tidak perlu menggunakan object, kita bisa langsung menggunakan classnya
- Static method tidak bisa mengakses class attribute ataupun instance attribute
- Untuk membuat static method, kita bisa menambahkan decorator @staticmethod pada method di class
'''

print("static method:")
# staticmethod, method yang tidak memerlukan object 
class Matematika:

    @staticmethod # penggunaan static method
    def tambah(a, b):
        return a + b
    

print(Matematika.tambah(5, 5))

'''
2. CLASS METHOD
- Class method adalah method yang menerima class sebagai parameter pertama (biasanya dinamakan cls), bukan instance
- Berguna untuk factory methods atau operasi yang berhubungan dengan class itu sendiri
- Class method bisa mengakses class attribute, namun tidak bisa mengakses instance attribute
'''

print("\nclass method:")
# classmethod, kasusnya untuk membuat factory method
class BankAccount:
    
    no = ""
    balance = 0
    active = True
    
    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance
    
    @classmethod        
    def disabled(cls, no, balance=0):
        result = cls(no, balance)
        result.active = False
        return result
    
    
bank1 = BankAccount("123456", 800000)
print(f'{bank1.no}, {bank1.balance}, {bank1.active}')

bank2 = BankAccount.disabled("123456", 500000)
print(f'{bank2.no}, {bank2.balance}, {bank2.active}')

'''
Kapan menggunakan masing-masing?
- Instance method: ketika butuh akses ke instance (object) data
- Class method: untuk factory method (method untuk pembuatan instance object), atau operasi pada class level
- Static method: untuk utility functions yang berhubungan dengan class tapi tidak butuh instance/class data
'''

'''
3. PROPERTY METHOD untuk Mengontrol Akses
- Salah satu kekurangan menggunakan attribute adalah, kita tidak bisa mengontrol nilai yang dimasukan atau didapatkan
- Jika menggunakan function, maka hal ini bisa dilakukan, karena kita bisa memvalidasi nilai terlebih dahulu di function
- Banyak yang menggunakan method setter dan getter untuk mengontrol akses ke attribute 


PROPERTY DECORATOR
- Di python terbaru, terdapat fitur yang bernama property decorator, dimana kita bisa menandai function sebagai setter dan getter menggunakan decorator @property
- Selanjutnya, kita bisa menggunakan method tersebut layaknya seperti menggunakan attribute
'''

print("\nproperty method:")
# tanpa property method
class Category:
    _name = "" # underscore (_) di awal kalimat menandakan bahwa variabel ini tidak boleh diakses dari luar
    
    def set_name(self,name): # untuk mengubah nilai dari variabel _name
        if name == "":
            raise ValueError("Name cannot be empty")
        self._name = name
        
    def get_name(self): # untuk mengakses nilai dari variabel _name
        return self._name

category1 = Category()
category1.set_name("Laptop")
print(category1.get_name())


# dengan decorator property method
class Jenis:
    _name = ""
    
    @property # untuk menandakan sebagai property atau getternya (mengakses nilainya)
    def name(self):
        return self._name
    
    @name.setter # untuk mengubah nilai dari variabel _name atau disebut setternya
    def name(self, name):
        if name == "":
            raise ValueError("Nama tidak boleh kosong")
        self._name = name
        
jenis1 = Jenis()
jenis1.name = "Gadget"
print(jenis1.name)