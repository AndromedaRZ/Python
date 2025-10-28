'''
Encapsulation

- Encapsulation adalah prinsip OOP yang menggabungkan data dan method dalam satu unit (class) dan mengontrol akses ke data tersebut
- Bisa dibayangkan seperti kotak aman dan data penting disimpan di dalam, dan hanya bisa dikases melalui cara yang terkontrol (diperbolehkan)

Mengapa encapsulation penting?
- Data protection: mencegah data diubah sembarangan
- Data validation: memastikan data selalu dalam kondisi valid
- Interface control: menentukan bagaimana data boleh diakses
- Maintenance: mudah mengubah internal implementation
- Security: menyembunyikan detail sensitive

Access Modifiers dalam Python
Python menggunakan naming conventions untuk menandai level akses:
1. Public attributes (default) -> bisa diakses dari mana saja, tidak ada protection. Seperti kita membuat variabel pada biasanya
2. Protected attributes (menggunakan satu garis bawah di depan namanya '_') -> convention bahwa attribute ini untuk internal use class dan subclasses
3. Private attributes (menggunakan dua garis bawah di depan namanya '__') -> Python akan melakukan name mangling (pengubahan nama attribute dari luar) sehingga attribute sulit diakes dari luar

- Protected attributes tidak disarankan untuk diakses dari luar seperti menampilkan isinya
- Private attributes tidak akan bisa diakses dari luar seperti menampilkan isinya, kecuali menggunakan cara yang disarankan yaitu menggunakan getter
'''

class BankAccount:
    __no = ''
    __balance = 0
    # 'no' dan 'balance' sudah menjadi private attribute yang artinya kita tidak boleh mengaksesnya secara langsung
    
    def __init__(self, no):
        self.__no = no
    
    # tapi kita bisa menggunakan cara seperti di bawah ini untuk mendapatkan nilainya (disebut getter)
    def get_balance(self):
        return self.__balance
    
    # dan menggunakan 'setter' untuk mengubah nilai dari private attribute tadi
    def topup(self, amount):
        self.__balance += amount
    
    # cara membuat getter menggunakan property
    # lihat di bawah apa perbedaannya dengan yang tanpa property
    @property
    def show_no(self):
        return self.__no
        
    def cashout(self, amount):
        if amount > self.__balance:
            raise ValueError("Saldo tidak mencukupi")
        self.__balance -= amount
        

ucup_account = BankAccount('Ucup')

ucup_account.topup(100000)
print(ucup_account.get_balance())   # getter tanpa property
print(ucup_account.show_no)         # getter dengan property

ucup_account.cashout(50000)
print(ucup_account.get_balance())


'''
Getter dan Setter methods

@property decorator digunakan untuk membuat getter dan setter lebih elegan
dibanding cara manual menggunakan getter dan setter method

property decorator memungkinkan kita untuk menggunakan syntax seperti attribute biasa, tapi dengan control seperti method
'''