'''
ENCAPSULATION
- Encapsulation adalah prinsip OOP yang menggabungkan data dan methods dalam satu unit (class) dan mengontrol akses ke data tersebut
- Bayangkan encapsulation seperti kotak aman - data penting disimpan di dalam, dan hanya bisa diakses melalui cara yang terkontrol

Mengapa Encapsulation itu penting?
- Data Protection, mencegah data diubah sembarangan 
- Data Validation, memastikan data selalu dalam kondisi valid
- Interface kontrol, menentukan bagaimana data boleh diakses
- Maintenance, mudah mengubah internal implementation
- Security, menyembunyikan detail sensitif (rahasia)

Access Modifier dalam Python
- Python menggunakan naming conventions untuk manandai level akses:
- Public Attributes (default), bisa diakses dari mana saja - tidak ada protection
- Protected Attributes - Single Underscore _, convention bahwa attribut ini untuk internal use class dan subclass
- Private Attributes - Double Underscore __, python akan melakukan name mangling (pengubahan nama attribute dari luar) sehingga attribute sulit diakses dari luar
'''

class BankAccount:
    # private variabel
    __no = ""
    __balance = 0
    
    def __init__(self, no):
        self.__no = no
        
    @property
    def balance(self):
        return self.__balance
    
    @property
    def no(self):
        return self.__no
    
    def topup(self, topup_amount):
        self.__balance += topup_amount
        
    def cashout(self, cashout_amount):
        if cashout_amount > self.__balance:
            raise ValueError("Not enough balance")
        self.__balance -= cashout_amount 
        
account1 = BankAccount("Budi")
print(account1.no)
print(account1.balance)

account1.topup(5000)
print(account1.balance)


'''
Getter dan Setter Methods
- @property decorator untuk untuk membuat getter/setter yang lebih elegan dibanding manual menggunakan getter dan setter method
- Property decorator memungkinkan kita untuk menggunakan syntax seperti attribute biasa, tapi dengan control seperti method
'''

