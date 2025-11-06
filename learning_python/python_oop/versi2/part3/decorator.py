'''
Decorator

- Digunakan untuk 'membungkus' atau memodifikasi behavior (attribute) dari function atau method
- Decorator ditandai dengan simbol @ diikuti nama decorator, dan ditulis di atas function/method
- Python menyediakan beberapa build-in (fungsi bawaan) decorators untuk OOP:
1. @staticmethod: membuat method yang tidak perlu self atau class
2. @classicmethod: membuat method yang menerima class sebagai parameter
3. @property: membuat method yang bisa diakses seperti attribute
'''

'''Static Methods (Independent Functions)'''
# Static method adalah method yang berdiri sendiri secara independen
# untuk mengakses static method, kita tidak perlu menggunakan object, kita bisa langsung menggunakan class nya
# static method tidak bisa mengakses class attribute ataupun instance attribute
# untuk membuat static method, kita bisa menambahkan decorator @staticmethod pada method di dalam class

class Matematika:
    
    @staticmethod
    def tambah(a, b): # jadi, kita tidak perlu menggunakan 'self' jika tidak dibutuhkan seperti contoh ini
        return a + b
    
result = Matematika.tambah(10, 3)
print(result)


'''Class Method'''
# Class Method adalah method yang menerima class sebagai parameter pertama (biasanya dinamakan cls (class)), bukan instance
# berguna untuk factory methods atau operasi yang berhubungan dengan class itu sendiri
# Class method bisa mengakses class attribute, namun tidak bisa mengakses instance attribute

class BankAccount:
    no = ''
    balance = 0
    activate = True
    
    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance
        
    @classmethod
    def disabled(cls, no, balance=0):
        result = cls(no, balance)   # cls disini membuat object
        result.activate = False
        return result
        
    
akun1 = BankAccount('Rina', 10000)
print(f"{akun1.no}, {akun1.balance}, {akun1.activate}")

akun2 = BankAccount.disabled('Andi', 10000) # cara memanggil class method
print(f"{akun2.no}, {akun2.balance}, {akun2.activate}")


'''
Kapan menggunakan method-method tadi?

Instance method digunakan ketika butuh akses ke attribute atau data dari instance tersebut (object)

Class method digunakan untuk factory methods (method untuk pembuatan instance object), atau operasi yang terjadi pada Class level

Static method digunakan untuk utility function yang berhubungan dengan Class tersebut tapi tidak butuh attribute atau datanya
'''