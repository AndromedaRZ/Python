'''
Method resolution order // multiple inheritance
'''

class A:
    
    def show(self):
        print("ini adalah show A")
        
class B:
    
    def show(self):
        print("ini adalah show B")

# si class C ini mengambil dua method yaitu dari A dan B 
class C(A,B): # siapapun yang dipanggil terlebih dahulu methodnya maka akan dieksekusi duluan
    pass

class D(B,A):
    pass

objek = C()
objek2 = D()

objek.show() # objek akan memanggil method a duluan 
objek2.show() # objek2 akan mengambil method b duluan

