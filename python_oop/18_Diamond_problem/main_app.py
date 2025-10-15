# diamond problem
# merupakan salah satu masalah yang muncul jika kita menggunakan multiple inheritance

# kenapa disebut diamond?
# karena diagram untuk menggambarkan keterkaitan kodenya akan menjadi berbentuk seperti diamond

class A:
    
    def show(self):
        print("Ini adalah show A")
        
class B(A):
    
    def show(self):
        print("Ini adalah show B")
        
class C(A):
    
    def show(self):
        print("Ini adalah show C")
        
class D(B, C):
    pass


#    A
#   / \
#  /   \
# B     C
#  \   /
#   \ /
#    D

# penulisan kode tadi akan membuat diagramnya menjadi berbentuk diamond seperti contoh diatas

# jika sub class D inherit dari sub class B dan C, sedangkan sub class B dan C inherit dari super class A
# darimana sub class D mengambil method jika semua class mempunyai satu method dengan nama yang sama?

objek = D()
objek.show() # hasilnya ia akan memanggil method pada sub class B
# jika dilihat pada menu 'help()', sebenarnya objectnya akan mengambil method dari sub class D terlebih dahulu
# tapi karena di sub class D tidak ada methodnya, maka alternatifnya menggunakan method di sub class B
# dan jika method di sub class B tidak ada, ia akan menggunakan method pada sub class C
# yang terakhir jika method di sub class D, C, daN B tidak ada, maka ia akan menggunakan method pada super class A


help(objek)
# jika ingin mengetahui urutan eksekusi methodnya, kita bisa menggunakan 'help()' pada object yang menggunakan sub class D