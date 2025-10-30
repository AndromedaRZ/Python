# hubungan antara abstractmethod dengan decorator dan method

from abc import ABC, abstractmethod

class Button(ABC):
    
    # di dalam satu class ini, kita bisa mencampur bagian abstractmethod dan method biasa
    
    def __init__(self, set_link):
        self.link = set_link
    
    @abstractmethod
    def click(self):
        pass
    
    
    # kita akan membuat agar self.ling terhubung dengan method link
    @property # urutannya: @property -> @abstractmethod -> method
    @abstractmethod
    def link(self):
        pass

class PushButton(Button):
    
    def click(self):
        print(f"Go to: {self.link}")
        
    @Button.link.setter
    def link(self, input):
        self.__link = input
        
    @link.getter
    def link(self):
        return self.__link
    
              
tombol1 = PushButton('www.kelasterbuka.id')

tombol1.click()