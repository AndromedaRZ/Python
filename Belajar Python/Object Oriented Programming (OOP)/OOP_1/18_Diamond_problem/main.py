'''
Diamond problem
'''

class A: # urutan terakhir show yang akan dieksekusi
    def show(self):
        print("ini adalah show A")

class B(A): # urutan pertama show yang akan dieksekusi
    # def show(self):
    #     print("ini adalah show B")
    pass

class C(A): # urutan kedua show yang akan dieksekusi
    # def show(self):
    #     print("ini adalah show C")
    pass
    
class D(B,C):
    pass

objek = D()

objek.show()
help(objek)