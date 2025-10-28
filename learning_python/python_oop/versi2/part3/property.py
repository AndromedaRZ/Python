'''
Property method untuk mengontrol akses

- salah satu kekurangan menggunakan attribute adalah kita tidak bisa mengontrol nilai yang dimasukkan atau didapatkan 
- jika kita menggunakan function, maka hal ini bisa dilakukan karena kita bisa memvalidasi nilai terlebih dahulu di dalam function tersebut
- banyak yang menggunakan method yang namanya 'setter' untuk mengubah nilai/datanya dan 'getter' untuk mengambil nilai/datanya agar mudah untuk mengontrol akses attribute
'''

class Category:
    _name = ''
    # garis bawah di depan nama variabel
    # menandakan bahwa kita tidak boleh mengakses attribute terebut secara langsung, walaupun kita tetap bisa mengaksesnya
    # dalam hal ini perlu menggunakan yang namanya getter
    
    def set_name(self, name):
        if name == '':
            raise ValueError("Nama tidak boleh kosong!")
        self._name = name
        
    def get_name(self):
        return self._name
    

category1 = Category()
category2 = Category()

category1._name = 'Kulkas'  # kita masih bisa mengubah datanya dengan cara seperti ini, namun itu tidak diperbolehkan

# category1.set_name('') # jika namanya kosong seperti ini, maka hasilnya akan error seperti yang sudah kita atur di dalam setter tadi

category2.set_name('Laptop') # cara yang tepat dengan menggunakan method sebagai setter

print(category1._name)  # kita juga masih bisa melihat nilai atau data dari attributenya dengan cara seperti ini, namun itu tetap tidak diperbolehkan

print(category2.get_name()) # # cara yang tepat dengan menggunakan method sebagai getter


'''Property Decorator'''
# Jika kita menggunakan Python versi terbaru, akan tersedia fitur bernama property decorator
# dengan menggunakan decorator @property, kita bisa menandai function sebagai setter dan getter
# dan kita bisa menggunakan method terebut layaknya seperti menggunakan attribute

class Category:
    _name = ''
    
    @property   # cara menggunakan property
    def name(self): # nantinya function 'name' ini bisa kita gunakan sebagai setter atau getter
        return self._name
    
    @name.setter    # 'name' adalah method yang kita tambahkan decorator property tadi
    def name(self, name):
        if name == '':
            raise ValueError("Nama tidak boleh kosong")
        self._name = name
        

category1 = Category()
category1.name = 'Gadget'
print(category1.name)
