# method resolution order // multiple inheritance

'''
Kita akan membuat studi kasus seperti ini
buat super class A dan B dan isi kedua super class tersebut dengan 1 method yang namanya sama
ketika kita membuat multiple inheritance pada sub class C
pada saat kita menggunakan method dengan nama yang sama tersebut
hasilnya menunjukkan method dari super class yang lebih dulu dimasukkan ke parameter pada saat pembuatan sub class tersebut
urutan eksekusi tersebut bisa dikatakan sebagai method resolution order

akan tetapi ketika sub class tersebut juga memiliki nama method yang sama, maka ia akan lebih didahulukan


'''

class A:
    def show(self):
        print("Ini adalah show A")
    
    
class B:
    def show(self):
        print("Ini adalah show B")
    
class C(A, B):
    def show(self):
        print("Ini adalah show C")


tester = C()

tester.show()
help(tester)
# jika kita ingin melihat method resolution order atau urutannya
# kita bisa menggunakan help() lalu isi di dalam kurun tersebut dengan object-nya