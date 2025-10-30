class Mangga:
    
    # magic method
    def __init__(self, nama, jumlah):
        self.nama = nama
        self.jumlah = jumlah
    
    # digunakan saat debugging
    def __repr__(self):
        return "Debug - mangga {} dengan jumlah {}".format(self.nama, self.jumlah)
        
    # digunakan saat programnya sudah jadi  
    def __str__(self):
        return "mangga {} dengan jumlah {}".format(self.nama, self.jumlah)
    
    def __add__(self, objek): 
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self):
        return "objek ini mempunyai nama dan jumlah"
    
    
    
belanja1 = Mangga('arumanis', 10)
belanja2 = Mangga('manalagi', 5)
print(repr(belanja1))
print(belanja2)
print("belanja 1 + belanja 2 = ",belanja1 + belanja2)
print(belanja1.__dict__)
