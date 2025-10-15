'''
abstract class pada python

Singkatnya seperti ini:

ketika kita membuat class biasa -> instance-nya adalah sebuah object
sedangkan ketika kita membuat class abstract -> instance-nya adalah sebuah class

class biasa adalah sebuah blueprint dari object yang kita buat
dan class abstract adalah sebuah blueprint dari class yang kita buat

lalu, apa perbedaannya?
- class abstract akan memaksa class untuk mengimplementasikan method-nya
hampir mirip seperti inheritance pada super class
'''


# membuat class abstract
# jika kita ingin membuat class abstract, maka kita perlu mengimport module-nya terlebih dahulu

from abc import ABC, abstractmethod
# abc = absctract base class


class Button(ABC): # masukkan ABC sebagai parameter
    
    @abstractmethod
    def click(self): # dengan begitu, kita bisa memaksa fungsi 'click' ini untuk berjalan di sub class
        pass
        
class PushButton(Button):
    
    def click(self):
        print("push button click")
        
        
class RadioButton(Button):
    def click(self):
        print("radio buttom click")
        

# singkatnya, asbtract class berfungsi agar semua class bisa menggunakan method yang sama pada object        
        
tombol1 = PushButton()
tombol2 = RadioButton()

tombol1.click()
tombol2.click()

help(tombol1)