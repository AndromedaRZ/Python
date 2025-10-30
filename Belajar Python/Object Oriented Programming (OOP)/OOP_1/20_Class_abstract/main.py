'''
Class asbtract

class biasa --> instance-nya adalah objek
class abstract --> instance-nya adalah class
'''

# abc = abstract base class
from abc import ABC, abstractmethod

# membuat class abstract
class Button(ABC): # agar bisa menjadi class asbtract, super class ini harus mengheritance dari ABC
    
    @abstractmethod
    def click(self):
        pass
        
class PushButton(Button):
    
    def click(self):
        print("push button click")
    
        
tombol1 = PushButton()
tombol1.click()

help(tombol1)