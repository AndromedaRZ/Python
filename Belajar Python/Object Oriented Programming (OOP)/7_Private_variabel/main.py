class Hero:
    
    # class variabel
    jumlah = 0
    
    def __init__(self,name,health):
        self.name = name
        self.health = health
        
        # variabel instance private
        self.__private = 'private'
        
        # variabel instance protected
        self._protected = 'protected'
                
mahou_shoujo = Hero("Mahou Shoujo", 100)
print(mahou_shoujo.__dict__)
